# This file is a part of the shopping-cart application written by Savita Seetaraman.

from django.db import models

class Cart(models.Model):

    """
    Describes the features of the shopping cart.
    """
    created_date = models.DateTimeField()
    number_of_products = models.PositiveIntegerField()

    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('carts')
        ordering = ('-created_date')


class Product(models.Model):

    """ 
    Describes the features that a Product has.
    """

    name = models.CharField(max_length=80)
    cost = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='', blank = True)
    date = models.DateTimeField()
    url = models.URLField(max_length=200)
    product = models.ManyToManyField(Cart)

    class Meta:
        verbose_name = ('product')
        verbose_name_plural = ('products')

