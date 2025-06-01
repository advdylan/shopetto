from django.contrib import admin
from product.models import *

class ProductAdmin(admin.ModelAdmin):
  list_display = ("name",
                 "category",
                 "price",
                 )
  
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
  list_display = ("id",
                  "name")

admin.site.register(Category, CategoryAdmin)
# Register your models here.
