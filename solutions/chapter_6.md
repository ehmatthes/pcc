---
layout: default
title: Solutions - Chapter 6
---

- [6-1: Person](#person)
- [6-2: Favorite Numbers](#favorite-numbers)
- [6-3: Glossary](#glossary)

Back to [solutions](#README.html).

6-1: Person
---

Use a dictionary to store information about a person you  know. Store their first name, last name, age, and the city in which they live. You should have keys such as `first_name`, `last_name`, `age`, and `city`. Print each piece of information stored in your dictionary.

```python
person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 43,
    'city': 'sitka',
    }

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])
```

Output:

```
eric
matthes
43
sitka
```

[top](#)

6-2: Favorite Numbers
---

Use a dictionary to store people's favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person's name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

```python
favorite_numbers = {
    'mandy': 42,
    'micah': 23,
    'gus': 7,
    'hank': 1000000,
    'maggie': 0,
    }

num = favorite_numbers['mandy']
print("Mandy's favorite number is " + str(num) + ".")

num = favorite_numbers['micah']
print("Micah's favorite number is " + str(num) + ".")

num = favorite_numbers['gus']
print("Gus's favorite number is " + str(num) + ".")

num = favorite_numbers['hank']
print("Hank's favorite number is " + str(num) + ".")

num = favorite_numbers['maggie']
print("Maggie's favorite number is " + str(num) + ".")
```

Output:

```
Mandy's favorite number is 42.
Micah's favorite number is 23.
Gus's favorite number is 7.
Hank's favorite number is 1000000.
Maggie's favorite number is 0.
```

[top](#)

6-3: Glossary
---

A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let's call it a glossary.

- Think of five programming words you've learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
- Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (`'\n'`) to insert a blank line between each word-meaning pair in your output.

```python
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }

word = 'string'
print("\n" + word.title() + ": " + glossary[word])

word = 'comment'
print("\n" + word.title() + ": " + glossary[word])

word = 'list'
print("\n" + word.title() + ": " + glossary[word])

word = 'loop'
print("\n" + word.title() + ": " + glossary[word])

word = 'dictionary'
print("\n" + word.title() + ": " + glossary[word])
```

Output:

```
String: A series of characters.

Comment: A note in a program that the Python interpreter ignores.

List: A collection of items in a particular order.

Loop: Work through a collection of items, one at a time.

Dictionary: A collection of key-value pairs.
```

[top](#)