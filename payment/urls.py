from django.urls import path
from payment.views import CreatePaymentIntentView, CreateSubscriptionView, StripeWebhookView

urlpatterns = [
    path('create-payment-intent/', CreatePaymentIntentView.as_view(), name='create-payment-intent'),
    path('create-subscription/', CreateSubscriptionView.as_view(), name='create-subscription'),
    path('webhook/', StripeWebhookView.as_view(), name='stripe-webhook'),
]
