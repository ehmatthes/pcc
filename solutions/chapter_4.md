---
layout: default
title: Solutions - Chapter 4
---

- [4-1: Pizzas](#pizzas)
- [4-3: Counting to Twenty](#counting-to-twenty)
- [4-5: Summing a Million](#summing-a-million)
- [4-7: Threes](#threes)
- [4-8: Cubes](#cubes)
- [4-9: Cube Comprehension](#cube-comprehension)

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

print("\n")

# Print a sentence about each pizza.
for pizza in favorite_pizzas:
    print("I really love " + pizza + " pizza!")

print("\nI really love pizza!")
```

Output:

```
pepperoni
hawaiian
veggie


I really love pepperoni pizza!
I really love hawaiian pizza!
I really love veggie pizza!

I really love pizza!
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

Output:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
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

Output:

```
1
1000000
500000500000
```

[top](#)

4-7: Threes
---

Make a list of the multiples of 3 from 3 to 0. Use a `for` loop to print the numbers in your list.

```python
threes = list(range(3, 31, 3))

for number in threes:
    print(number)
```

Output:

```
3
6
9
12
15
18
21
24
27
30
```

[top](#)

4-8: Cubes
---

A number raised to the third power is called a *cube*. For example, the cube of 2 is written as `2**3` in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a `for` loop to print out the value of each cube.

```python
cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)
```

Output:

```
1
8
27
64
125
216
343
512
729
1000
```

[top](#)

4-9: Cube Comprehension
---

Use a list comprehension to generate a list of the first 10 cubes.

```python
cubes = [number**3 for number in range(1,11)]

for cube in cubes:
    print(cube)
```

Output:

```
1
8
27
64
125
216
343
512
729
1000
```

[top](#)