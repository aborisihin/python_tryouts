## Ingredients Shopping
Your task is to create a simple shopping cart to buy ingredients for our delicious recipes!

Ingredients are stored in a `IngredientsStore` object. This can either be created from a list of ingredient tuples or initialized from a CSV file.

```python
from decimal import Decimal
from ingredient import IngredientsStore

ingredients = [
    ('tomatoes', Decimal('0.15')),
    ('chicken', Decimal('3.49')),
    ('onions', Decimal('2.00')),
    ('rice', Decimal('0.70')),
]
ingredient_store = IngredientsStore(ingredients)

# or

import os

csv_filepath = os.path.abspath('ingredients.csv')
ingredient_store = IngredientsStore.init_from_filepath(csv_filepath)
```

The price for an ingredient can be retrieved with `get_ingredient_price()`.

```python
price = ingredient_store.get_ingredient_price('chicken')
```

## Cart

Carts should be created with an IngredientsStore instance.

```python
from cart import Cart

shopping_cart = Cart(ingredient_store)
```

Ingredients can be added to a cart by name, with an optional quantity parameter.

```python
shopping_cart.add('tomatoes')
shopping_cart.add('onions', 3)
```

The total for the cart can be calculated with `get_total()`. This method optionally takes a list of [Discount](#discount) objects that are applied to items in the cart when calculating the total.

```python
total = shopping_cart.get_total()

# with discount
total_after_discount = shopping_cart.get_total(discounts=[discount_one, discount_two])
```

## Discount

Discount classes inherit from `AbstractDiscount` and must implement the `calculate_line_total()` method.

Two discount classes are provided; `NoDiscount`, `BulkDiscount`.

### NoDiscount

No discount is applied and the price remains unaffected.

```python
tomatoes_nodiscount = NoDiscount('tomatoes')
```

### BulkDiscount

A discount that applies when you buy a specific quantity. For example, buy one get one free, or, buy two get a third free.

```python
# buy one get one free on tomatoes
buy_one_get_one_free_tomatoes = BulkDiscount('tomatoes', 1, 1)

# buy two get third free on onions
buy_two_get_third_free_onions = BulkDiscount('onions', 2, 1)
```

