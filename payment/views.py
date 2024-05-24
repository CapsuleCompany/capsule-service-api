import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from payment.models import Order
from payment.serializers import OrderSerializer, PaymentIntentSerializer, SubscriptionSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreatePaymentIntentView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PaymentIntentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                amount = serializer.validated_data['amount']
                description = serializer.validated_data['description']
                payment_method_id = serializer.validated_data['payment_method_id']

                order = Order.objects.create(
                    amount=amount,
                    description=description
                )

                intent = stripe.PaymentIntent.create(
                    amount=int(float(order.amount) * 100),  # amount in cents
                    currency='usd',
                    payment_method=payment_method_id,
                    confirmation_method='manual',
                    confirm=True,
                    metadata={'order_id': order.id},
                )

                return Response({'clientSecret': intent.client_secret, 'status': intent.status})
            except stripe.error.CardError as e:
                return Response({'error': str(e.user_message)}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateSubscriptionView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                email = serializer.validated_data['email']
                name = serializer.validated_data['name']
                payment_method_id = serializer.validated_data['payment_method_id']
                plan_id = serializer.validated_data['plan_id']

                customer = stripe.Customer.create(
                    email=email,
                    name=name,
                    payment_method=payment_method_id,
                    invoice_settings={
                        'default_payment_method': payment_method_id,
                    },
                )

                subscription = stripe.Subscription.create(
                    customer=customer.id,
                    items=[{'plan': plan_id}],
                    expand=['latest_invoice.payment_intent'],
                )

                order = Order.objects.create(
                    amount=0,  # or the subscription amount if needed
                    description='Subscription to your service',
                    is_subscription=True,
                    stripe_subscription_id=subscription.id
                )

                return Response({'subscriptionId': subscription.id, 'status': subscription.status})
            except stripe.error.CardError as e:
                return Response({'error': str(e.user_message)}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StripeWebhookView(APIView):
    def post(self, request, *args, **kwargs):
        payload = request.body
        sig_header = request.META['HTTP_STRIPE_SIGNATURE']
        endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except ValueError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except stripe.error.SignatureVerificationError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            order_id = payment_intent['metadata']['order_id']
            order = Order.objects.get(id=order_id)
            order.status = 'paid'
            order.save()

        if event['type'] == 'invoice.payment_succeeded':
            invoice = event['data']['object']
            subscription_id = invoice['subscription']
            order = Order.objects.filter(stripe_subscription_id=subscription_id).first()
            if order:
                order.status = 'paid'
                order.save()

        return Response(status=status.HTTP_200_OK)
