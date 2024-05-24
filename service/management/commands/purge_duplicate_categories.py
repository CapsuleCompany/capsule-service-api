# your_app/management/commands/purge_duplicates.py

from django.core.management.base import BaseCommand
from service.models import Category, Subcategory


class Command(BaseCommand):
    help = 'Purge and remove duplicate categories in subcategories'

    def handle(self, *args, **kwargs):
        # Fetch all categories
        categories = Category.objects.all()

        # Get a list of category IDs
        category_ids = set(categories.values_list('id', flat=True))

        # Identify subcategories that also exist as main categories
        duplicate_subcategories = Subcategory.objects.filter(category__in=category_ids)

        for subcategory in duplicate_subcategories:
            # Check if subcategory ID exists in main categories
            if subcategory.id in category_ids:
                # Delete the subcategory
                subcategory.delete()
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Deleted subcategory {subcategory.name} with ID {subcategory.id} '
                        f'from category {subcategory.category.name}'
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'Subcategory {subcategory.name} with ID {subcategory.id} '
                        f'is not a duplicate.'
                    )
                )

        self.stdout.write(self.style.SUCCESS('Duplicate categories purged successfully.'))
