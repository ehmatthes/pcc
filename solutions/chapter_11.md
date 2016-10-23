---
layout: default
title: Solutions - Chapter 11
---

- [11-1: City, Country](#city-country)

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

    def test_simple_pair(self):
        """Do pairs like 'Santiago, Chile' work?"""
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

