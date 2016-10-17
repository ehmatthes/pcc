---
layout: default
title: Solutions - Chapter 7
---

- [7-1: Rental Car](#rental-car)
- [7-2: Restaurant Seating](#restaurant-seating)
- [7-3: Multiples of Ten](#multiples-of-ten)
- [7-4: Pizza Toppings](#pizza-toppings)
- [7-5: Movie Tickets](#movie-tickets)

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

7-4: Pizza Toppings
---

Write a loop that prompts the user to enter a series of pizza toppings until they enter a `quit` value. As they enter each topping, print a message saying you'll add that topping to their pizza.

```python
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break
```

Output:

<pre>
What topping would you like on your pizza?
Enter 'quit' when you are finished: <b>pepperoni</b>
  I'll add pepperoni to your pizza.

What topping would you like on your pizza?
Enter 'quit' when you are finished: <b>sausage</b>
  I'll add sausage to your pizza.

What topping would you like on your pizza?
Enter 'quit' when you are finished: <b>bacon</b>
  I'll add bacon to your pizza.

What topping would you like on your pizza?
Enter 'quit' when you are finished: <b>quit</b>
</pre>

[top](#)

7-5: Movie Tickets
---

A movie theater charges different ticket prices depending on a person's age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tel them the cost of their movie ticket.

```python
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")
```

Output:

<pre>
How old are you?
Enter 'quit' when you are finished. <b>2</b>
  You get in free!
How old are you?
Enter 'quit' when you are finished. <b>3</b>
  Your ticket is $10.
How old are you?
Enter 'quit' when you are finished. <b>12</b>
  Your ticket is $10.
How old are you?
Enter 'quit' when you are finished. <b>18</b>
  Your ticket is $15.
How old are you?
Enter 'quit' when you are finished. <b>quit</b>
</pre>

[top](#)