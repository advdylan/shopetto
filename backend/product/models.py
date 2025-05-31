from django.db import models
from djmoney.models.validators import MinMoneyValidator
from djmoney.models.fields import MoneyField

# Create your models here.

class Product(models.Model):
  name = models.CharField(max_length=20)
  category = models.ForeignKey('Category', on_delete=models.CASCADE)

  price = MoneyField(max_digits=15,
                      decimal_places=2,
                      default=0.00,
                      validators=[MinMoneyValidator(1)],
                      default_currency ='PLN')

class Category(models.Model):
  name = models.CharField(max_length=20)



