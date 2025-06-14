import os
import django
import requests


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopetto.settings')


django.setup()


from product.models import Category 
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from urllib.parse import urlparse



class Command(BaseCommand):
    help = 'Your scraping command'

    def handle(self, *args, **options):
        parent_categories = Category.objects.filter(parent=None)
        #for category in parent_categories:
          #print(category)

        first_category = parent_categories[0]
        #print(first_category)

        childrens = Category.objects.filter(parent=first_category)
        for children_category in childrens:
            print(children_category)

        parent_category_url = str(parent_categories[0].name.lower().replace(" ", "-"))
        children_category_url = str(childrens[0].name.lower().replace(" ", "-"))
        url = f"https://www.bathroomsupastore.com/{parent_category_url}/{children_category_url}"
        print(f"Url: {url}")

        response = requests.get(url)
        final_url = response.url
        html_content = response.text
        #print(type(html_content))

        with open("bathroom-items.html", "w", encoding="utf-8") as f:
            f.write(html_content)

        soup = BeautifulSoup(html_content, 'html.parser')
        products = soup.find_all('a', class_='product-item-link')
        print(products)
       

        products_list = []
        for i, product in enumerate(products, 1):
            print(f"\nSpan element #{i}:")
            print(product)
            
            if hasattr(product, 'get_text'):  # Check if it's a BeautifulSoup Tag
                product_text = product.get_text(strip=True)
                print("Text content:", product_text)
                print("Attributes:", product.attrs)
                products_list.append(product_text)  # Append to products_list (not products!)
            else:
                print("Warning: Invalid product element (not a BeautifulSoup Tag)")

        products = list(dict.fromkeys(products_list))

        with open("spans.txt", "w", encoding="utf-8") as f:
          for product in products:
            f.write(f"{product}\n")

        srcs = []
        img_elements = soup.find_all('img', class_="product-image-photo")
        for img in img_elements:
            src=img.get('src')
            srcs.append(src)

        download_dir = "imgs"
        os.makedirs(download_dir, exist_ok=True)

        for src in srcs:
            response = requests.get(src, stream=True)
            response.raise_for_status()

            filename = os.path.basename(urlparse(src).path)
            filepath = os.path.join(download_dir, filename)

            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)

            print(f"Downloaded: {filename}")


        

   


        ##span_elements = soup.find_all('span')

        #spans = []