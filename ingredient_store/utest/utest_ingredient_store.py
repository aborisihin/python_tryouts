import unittest

from ingredient import IngredientsStore
from cart import Cart
from discount import NoDiscount, BulkDiscount

# test data
ingredients = ['tomatoes', 'rice', 'pepper', 'onions', 'chicken']
prices = [3.2, 2.8, 1.6, 1.25, 4.5]


class BaseTestCase(unittest.TestCase):
    """
    BaseTestCase class.

    Contains all tests. Must be inherited by class with setUpClass() method implemented.
    """

    def test_get_ingredient_price(self):
        """
        IngredientsStore.get_ingredient_price() test.
        """
        extended_ingredients = ingredients + ['salt', 'milk']
        for i in range(len(extended_ingredients)):
            for p in range(len(prices)):
                if(i == p):
                    self.assertEqual(self.istore.get_ingredient_price(extended_ingredients[i]), prices[p])
                else:
                    self.assertNotEqual(self.istore.get_ingredient_price(extended_ingredients[i]), prices[p])

    def test_get_total(self):
        """
        Cart.get_total() test.
        """
        self.cart.add('pepper')
        self.assertEqual(self.cart.get_total(),1.6)

        self.cart.add('pepper', 6)
        self.assertEqual(self.cart.get_total(), 7 * 1.6)

        self.cart.add('onions')
        self.cart.add('chicken', 4)
        self.assertEqual(self.cart.get_total(), (7 * 1.6) + (1 * 1.25) + (4 * 4.5))

    def test_get_total_with_discounts(self):
        """
        Cart.get_total() test with discounts.
        """
        total = self.cart.get_total([NoDiscount('pepper'),NoDiscount('onions')])
        self.assertEqual(total, (7 * 1.6) + (1 * 1.25) + (4 * 4.5))

        total = self.cart.get_total([NoDiscount('pepper'),BulkDiscount('onions',3,1)])
        self.assertEqual(total, (7 * 1.6) + (1 * 1.25) + (4 * 4.5))

        total = self.cart.get_total([NoDiscount('pepper'), BulkDiscount('pepper', 3, 1)])
        self.assertEqual(total, ((3 * 1.6) + (1 * 0.0) + (3 * 1.6)) + (1 * 1.25) + (4 * 4.5))

        total = self.cart.get_total([NoDiscount('pepper'), BulkDiscount('pepper', 3, 1), BulkDiscount('chicken', 2, 1)])
        self.assertEqual(total, ((3 * 1.6) + (1 * 0.0) + (3 * 1.6)) + (1 * 1.25) + ((2 * 4.5) + (1 * 0.0) + (1 * 4.5)))


class ListTestCase(BaseTestCase):
    """
    ListTestCase class.

    Implements setUpClass() method with IngredientsStore constructed by list.
    """

    @classmethod
    def setUpClass(self):
        ingr_list = [(ingredients[i],prices[i]) for i in range(len(ingredients))]
        self.istore = IngredientsStore(ingr_list)
        self.cart = Cart(self.istore)

class CSVTestCase(BaseTestCase):
    """
    CSVTestCase class.

    Implements setUpClass() method with IngredientsStore initialized by CSV file.
    """

    @classmethod
    def setUpClass(self):
        self.istore = IngredientsStore.init_from_filepath('store_test.csv')
        self.cart = Cart(self.istore)


# run tests
test_classes = [ListTestCase,
                CSVTestCase]

test_methods = ['test_get_ingredient_price',
                'test_get_total',
                'test_get_total_with_discounts']

test_suite = unittest.TestSuite( [c(m) for c in test_classes for m in test_methods] )

unittest.TextTestRunner(verbosity=2).run(test_suite)
