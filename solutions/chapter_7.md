---
layout: default
title: Solutions - Chapter 7
---

- [7-1: Rental Car](#rental-car)
- [7-2: Restaurant Seating](#restaurant-seating)
- [7-3: Multiples of Ten](#multiples-of-ten)

Back to [solutions](README.html).

***Note:** Sublime Text doesn't run programs that prompt the user for input. You can use Sublime Text to write programs that prompt for input, but you'll need to run these programs from a terminal. See "Running Python Programs from a Terminal" on page 16.*

7-1: Rental Car
---

Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as "Let me see if I can find you a Subaru".

```python
car = input("What kind of car would you like? ")

print("Let me see if I can find you a " + car.title() + ".")
```

Output:

<pre>
What kind of car would you like? <b>Toyota Tacoma</b>
Let me see if I can find you a Toyota Tacoma.
</pre>

[top](#)

7-2: Restaurant Seating
---

Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they'll have to wait for a table. Otherwise, report that their table is ready.

```python
party_size = input("How many people are in your dinner party tonight? ")
party_size = int(party_size)

if party_size > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")
```

Output:

<pre>
How many people are in your dinner party tonight? <b>12</b>
I'm sorry, you'll have to wait for a table.
</pre>

or:

<pre>
How many people are in your dinner party tonight? <b>6</b>
Your table is ready.
</pre>

[top](#)

7-3: Multiples of Ten
---

Ask the user for a number, and then report whether the number is a multiple of 10 or not.

```python
number = input("Give me a number, please: ")
number = int(number)

if number % 10 == 0:
    print(str(number) + " is a multiple of 10.")
else:
    print(str(number) + " is not a multiple of 10.")
```

Output:

<pre>
Give me a number, please: <b>23</b>
23 is not a multiple of 10.
</pre>

or:

<pre>
Give me a number, please: <b>90</b>
90 is a multiple of 10.
</pre>

[top](#)