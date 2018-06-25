""" discount module.
Contains AbstractDiscount, NoDiscount, BulkDiscount classes.
"""

from abc import ABCMeta, abstractmethod

__all__ = ['AbstractDiscount', 'NoDiscount', 'BulkDiscount']

class AbstractDiscount(object):
    """ Abstract class of discounts objects.

    Contains name of the discounted ingredient. Implements calculation
    of ingredient's final price.

    Attributes:
          ingredient: Discounted ingredient's name.
    """

    __metaclass__ = ABCMeta

    def __init__(self, ingredient_name):
        """ Class constructor.

        :param ingredient_name: Discounted ingredient's name.
        """
        self.ingredient = ingredient_name

    @abstractmethod
    def calculate_line_total(self, quantity, price):
        """ Abstract method for calculating price with discount.
        Must be reimplemented in inherited classes.

        :param quantity: Ingredient's quantity to calculate total price.
        :param price: Ingredient's price.
        :return: Ingredient's final price with discount.
        """
        pass


class NoDiscount(AbstractDiscount):
    """ NoDiscount class.
    """

    def calculate_line_total(self, quantity, price):
        """  AbstractDiscount.calculate_line_total() implementation.
        """
        return quantity * price


class BulkDiscount(AbstractDiscount):
    """ BulkDiscount class.

    Implementation of bulk discount (e.g. buy 3, get 1 free).

    Attributes:
        buy_num: Ingredient's quantity that customer have to buy to get discount.
        free_num: Quantity of discount's free ingredients.
    """

    buy_num = 0
    free_num = 0

    def __init__(self, ingredient_name, buy, free):
        """ Extend of base constructor.

        :param ingredient_name: Discounted ingredient's name.
        :param buy: Ingredient's quantity to buy.
        :param free: Ingredient's quantity for free.
        """
        super(BulkDiscount,self).__init__(ingredient_name)
        self.buy_num = buy
        self.free_num = free

    def calculate_line_total(self, quantity, price):
        """  AbstractDiscount.calculate_line_total() implementation.
        """
        bulks = quantity // (self.buy_num + self.free_num)
        remainder = quantity % (self.buy_num + self.free_num)

        return (bulks * self.buy_num * price) + (remainder * price)
