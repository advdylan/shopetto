import json
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from product.models import Category, Product  # Adjust app/model names if needed
from djmoney.money import Money


class Command(BaseCommand):
    help = 'Import categories and products from a JSON file'

    def handle(self, *args, **kwargs):
      with open('/home/dylan/shopetto/backend/product/management/commands/data/categories_and_products.json') as f:
          data = json.load(f)
    

      cat_map = {}

      self.stdout.write("Creating categories...")

      # First pass: create top-level categories
      for cat in data['categories']:
          if not cat['parent']:
              obj, _ = Category.objects.get_or_create(
                  id=cat['id'],
                  defaults={
                      'name': cat['name'],
                      'slug': cat['slug'],
                      'parent': None
                  }
              )
              cat_map[cat['id']] = obj

      # Second pass: create subcategories
      for cat in data['categories']:
          if cat['parent']:
              parent_id = cat['parent']['id']
              parent = cat_map.get(parent_id)

              if not parent:
                  self.stderr.write(f"Parent with ID {parent_id} not found for category {cat['name']}")
                  continue

              obj, _ = Category.objects.get_or_create(
                  id=cat['id'],
                  defaults={
                      'name': cat['name'],
                      'slug': cat['slug'],
                      'parent': parent
                  }
              )
              cat_map[cat['id']] = obj

      self.stdout.write("Creating products...")

      for product in data['products']:
          category = cat_map.get(product['category'])
          if not category:
              self.stderr.write(f"Category with ID {product['category']} not found for product {product['name']}")
              continue

          Product.objects.get_or_create(
              name=product['name'],
              category=category,
              slug=slugify(product['name']),
              defaults={
                  'price': Money(product['price'], 'PLN')
              }
          )

      self.stdout.write(self.style.SUCCESS("Successfully imported all categories and products."))

