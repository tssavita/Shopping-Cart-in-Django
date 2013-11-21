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

class Contained(models.Model):

    """
    This class is the relation between the products and carts.
    Since one cart contains many products and one product can be 
    contained in many classes, it is a Many - To - Many relation 
    between the products and carts. This results in a table for 
    the relation between the two entities. 
    """

    cart_number = models.ForeignKey(Cart, verbose_name=_('cart number'))
    code = models.CharField(primary_key=True, validators=[RegexValidator(
                                              regex='^[0-9]*$',
                                              message='Invalid characters in the code.'
                                              )]

    class Meta:
        verbose_name = _('contained')
        verbose_name_plural = _('')
