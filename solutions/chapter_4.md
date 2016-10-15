---
layout: default
title: Solutions - Chapter 4
---

- [4-1: Pizzas](#pizzas)
- [4-3: Counting to Twenty](#counting-to-twenty)
- [4-5: Summing a Million](#summing-a-million)

Back to [solutions](README.html).

4-1: Pizzas
---

Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a `for` loop to print the name of each pizza.

- Modify your `for` loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like *I like pepperoni pizza.*
- Add a line at the end of your program, outside the `for` loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as *I really love pizza!*

```python
favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']

# Print the names of all the pizzas.
for pizza in favorite_pizzas:
    print(pizza)

# Print a sentence about each pizza.
for pizza in favorite_pizzas:
    print("I really love " + pizza + " pizza!")

print("\nI really love pizza!")
```

[top](#)

4-3: Counting to Twenty
---

Use a `for` loop to print the numbers from 1 to 20, inclusive.

```python
numbers = list(range(1, 21))

for number in numbers:
    print(number)
```

[top](#)

4-5: Summing a Million
---

Make a list of the numbers from one to one million, and then use `min()` and `max()` to make sure your list actually starts at one and ends at one million. Also, use the `sum()` function to see how quickly Python can add a million numbers.

```python
numbers = list(range(1, 1000001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))
```

[top](#)