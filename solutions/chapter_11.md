---
layout: default
title: Solutions - Chapter 11
---

- [11-1: City, Country](#city-country)
- [11-2: Population](#population)
- [11-3: Employee](#employee)

Back to [solutions](README.html).

11-1: City, Country
---

Write a function that accepts two parameters: a city name and a country name. The function should return a single string of the form *City, Country*, such as `Santiago, Chile`. Store the function in a module called *city_functions.py*.

Create a file called *test_cities.py* that tests the function you just wrote (remember that you need to import `unittest` and the function you want to test). Write a method called `test_city_country()` to verify that calling your function with values such as `santiago` and `chile` results in the correct string. Run *test_cities.py*, and make sure `test_city_country()` passes.

*city_functions.py:*

```python
"""A collection of functions for working with cities."""

def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return(city.title() + ", " + country.title())
```

***Note:** This is the function we wrote in Exercise 8-6.*

*test_cities.py:*

```python
import unittest

from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Does a simple city and country pair work?"""
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')

unittest.main()
```

Output:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

[top](#)

11-2: Population
---

Modify your function so it requires a third parameter, `population`. It should now return a single string of the form `City, Country - population xxx`, such as `Santiago, Chile - population 5000000`. Run *test_cities.py* again. Make sure `test_city_country()` fails this time.

Modify the function so the `population` parameter is optional. Run *test_cities.py* again, and make sure `test_city_country()` passes again.

Write a second test called `test_city_country_population()` that verifies you can call your function with the values `'santiago'`, `'chile'`, and `'population=5000000'`. Run *test_cities.py* again, and make sure this new test passes.

Modified *city_functions.py*, with required `population` parameter:

```python
"""A collection of functions for working with cities."""

def city_country(city, country, population):
    """Return a string like 'Santiago, Chile - population 5000000'."""
    output_string = city.title() + ", " + country.title()
    output_string += ' - population ' + str(population)
    return output_string
```

Output from running *test_cities.py:*

```
E
======================================================================
ERROR: test_city_country (__main__.CitiesTestCase)
Does a simple city and country pair work?
----------------------------------------------------------------------
Traceback (most recent call last):
  File "pcc\solutions\test_cities.py", line 10, in test_city_country
    santiago_chile = city_country('santiago', 'chile')
TypeError: city_country() missing 1 required positional argument: 'population'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

Modified *city_functions.py*, with optional `population` parameter:

```python
"""A collection of functions for working with cities."""

def city_country(city, country, population=0):
    """Return a string representing a city-country pair."""

    output_string = city.title() + ", " + country.title()
    if population:
        output_string += ' - population ' + str(population)
    return output_string
```

Output of running *test_cities.py:*

```
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

Modified *test_cities.py:*

```python
import unittest

from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Does a simple city and country pair work?"""
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')

    def test_city_country_population(self):
        """Can I include a population argument?"""
        santiago_chile = city_country('santiago', 'chile', population=5000000)
        self.assertEqual(santiago_chile, 'Santiago, Chile - population 5000000')

unittest.main()
```

Output:

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

[top](#)

11-3: Employee
---

Write a class called `Employee`. The `__init__()` method should take in a first name, a last name, and an annual salary, and store each of these as attributes. Write a method called `give_raise()` that adds $5000 to the annual salary by default but also accepts a different raise amount.

Write a test case for `Employee`. Write two test methods, `test_give_default_raise()` and `test_give_custom_raise()`. Use the `setUp()` method so you don't have to create a new employee instance in each test method. Run your test case, and make sure both tests pass.

*employee.py:*

```python
class Employee():
    """A class to represent an employee."""

    def __init__(self, f_name, l_name, salary):
        """Initialize the employee."""
        self.first = f_name.title()
        self.last = l_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Give the employee a raise."""
        self.salary += amount
```

*test_employee.py:*

```python
import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the module employee."""

    def setUp(self):
        """Make an employee to use in tests."""
        self.eric = Employee('eric', 'matthes', 65000)

    def test_give_default_raise(self):
        """Test that a default raise works correctly."""
        self.eric.give_raise()
        self.assertEqual(self.eric.salary, 70000)

    def test_give_custom_raise(self):
        """Test that a custom raise works correctly."""
        self.eric.give_raise(10000)
        self.assertEqual(self.eric.salary, 75000)

unittest.main()
```

Output:

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

[top](#)