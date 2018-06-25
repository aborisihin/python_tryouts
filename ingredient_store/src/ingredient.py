""" ingredient module.
Contains IngredientStore class.
"""

import csv

__all__ = ['IngredientsStore']

class IngredientsStore(object):
    """IngredientStore class.

    Stores ingredients prices, implements price getter method and initialization
    from csv file.

    Attributes:
        ingredients_dict: Ingredients prices dictionary.
            Dictionary key - name of the ingredient, value - price of the ingredient.
    """

    def __init__(self, init_list):
        """ Class constructor

        :param init_list: list of tuples that contains names and prices for ingredients,
            e.g. [('apple', 2.1), ('egg', 3.2)].
        """
        self.ingredients_dict = {init_item[0]: float(init_item[1]) for init_item in init_list}

    @staticmethod
    def init_from_filepath(csv_filepath):
        """ Static method of creating instance initialized by csv file.

        :param csv_filepath: Path to csv file. File must contains 2 columns:
            ingredient's name and ingredient's price. Delimiter must be comma.
        :return: IngredientStore instance initialized by csv file data.
        """
        with open(csv_filepath, 'rb') as csv_file:
            filedata = csv.reader(csv_file, delimiter=',')
            instance = IngredientsStore(filedata)
        return instance

    def get_ingredient_price(self, ingredient_name):
        """ Ingredient price getter.

        :param ingredient_name: String with ingredient's name.
        :return: Ingredient's price or 0.0 (if ingredient is not in the store)
        """
        if(self.ingredients_dict.has_key(ingredient_name)):
            return self.ingredients_dict[ingredient_name]
        else:
            return 0.0

    def __str__(self):
        return 'IngredientsStore: ' + str(self.ingredients_dict)