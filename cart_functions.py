# This file is a part of the Shopping cart application written by Savita Seetaraman.

from django.db import models
import datetime

class Shoppingcart:

    """
    This class is for functions of the shopping cart - add, remove 
    and display products.
    """

    def productExists(self, code, cart_number):

        """
        Checks if the product exists in the cart or not. 
        """

        for i in Contained.objects.all():
            if (i.code == self.code and i.cart == self.cart):
                return True
            else:
                return False


    def addProduct(self, cart_number, code, name, cost, quantity, description):

        """
        This function helps in adding products to the shopping cart. 
        It first retrieves all products that are already in the cart.
        Then it checks if the product to be newly inserted already 
        exists in the cart. If no, it gets inserted. Else if it already 
        exists in the cart, it updates the 
        """

        cart = Cart.objects.create()
        item = Product.objects.create()
        update_time = datetime.datetime.now()

            if (productExists() == False): # If the product does not exist
                item.code = code
                item.code = cost
                item.quantity = quantity
                item.description = description
                item.save()
            else:
                item.cost = cost
                item.quantity = item.quantity + self.quantity
                item.description = description
                item.save()


    def removeProduct(self, code, name, quantity, description):

        """
        Remove a particular product from the shopping cart.
        """
                
            if (productExists() == True): # Checking if the product exists in the cart.
                
                # If the product is present in the cart it is deleted.
                
                remove = Contained.objects.get(code = self.code)
                remove.delete()

            else:
                print "Product does not exist"

                # If the product is not present in the cart nothing is done. 
    
    '''            
    
    def displayProducts():

        """
        Displays all objects in the cart. 
        """

        for i in Contained.objects.all():
            <><>
                
    '''

    def clearCart(self):
        
        """
        Removes all products in the cart.
        """
        
        remove_all = Contained.objects.all()
        remove_all.delete()
    

    def no_of_Products(self):

        """
        Returns the number of Products in the shopping cart.
        """

        return Contained.objects.count()
