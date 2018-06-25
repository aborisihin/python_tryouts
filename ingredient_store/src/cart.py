""" cart module.
Contains Cart class.
"""

from discount import AbstractDiscount

__all__ = [ 'Cart' ]

class Cart(object):
    """ Cart class.

    Stores ingredients in customer's cart. Implements adding ingredient to cart
    and calculating total cart's price.

    Attributes:
        store: Reference to IngredientStore.
        cart_dict: Cart's ingredients dictionary.
            Dictionary key - name of the ingredient, value - quantity of the ingredient.
    """

    def __init__(self, ingredient_store):
        """ Class constructor.

        :param i_store: reference to the related IngredientStore.
        """
        self.store = ingredient_store
        self.cart_dict = {}

    def add(self, ingredient_name, quantity=1):
        """ Adding ingredient to chart.

        :param ingredient_name: name of the ingredient.
        :param quantity: quantity of the ingredient.
        """
        if(self.cart_dict.has_key(ingredient_name)):
            self.cart_dict[ingredient_name] += quantity
        else:
            self.cart_dict[ingredient_name] = quantity

    def get_total(self, discounts=[]):
        """ Calculating total price of chart including discounts.

        :param discounts: List of discount objects. Elements in list must inherit
            AbstractDiscount class from discount module.
        :return: Total cart's price.
        """
        for discount in discounts: # discounts list check
            assert isinstance(discount,AbstractDiscount), 'Discount class must be instance of AbstractDiscount'

        totals = []
        for key, val in self.cart_dict.items():
            price_from_store = self.store.get_ingredient_price(key)
            check_discounts = [discount.calculate_line_total(quantity=val,price=price_from_store)
                               for discount in discounts
                               if discount.ingredient == key] # calculate all prices with discounts for ingredient
            check_discounts.append(val * price_from_store) # append no-discount price

            totals.append(min(check_discounts)) # choose best price and append to totals list

        return sum(totals)

    def __str__(self):
        return 'Cart: ' + str(self.cart_dict)