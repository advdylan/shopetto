from django.db import models
from djmoney.models.validators import MinMoneyValidator
from djmoney.models.fields import MoneyField
from django.core.exceptions import ValidationError
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
  name = models.CharField(max_length=20)
  category = models.ForeignKey('Category', on_delete=models.CASCADE)
  slug = models.SlugField(max_length=100, unique=True, blank=True)

  price = MoneyField(max_digits=15,
                      decimal_places=2,
                      default=0.00,
                      validators=[MinMoneyValidator(1)],
                      default_currency ='PLN')
  
  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.name)

    super().save(*args, **kwargs)

  def clean(self):
        if self.category.children.exists():
            raise ValidationError("Cannot assign product to a parent category.")
        
  
  def __str__(self):
        return self.name
class Category(models.Model):

  name = models.CharField(max_length=20)
  slug = models.SlugField(unique=True, null=True)
  
  parent = models.ForeignKey(
      'self',
      null=True,
      blank=True,
      related_name='children',
      on_delete=models.CASCADE
  )

  class Meta:
      verbose_name_plural = "categories"

  
  def clean(self):
        if self.parent == self:
            raise ValidationError("Category cannot be its own parent.")
        
  def __str__(self):
      return self.name



