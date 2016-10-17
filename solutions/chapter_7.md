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

```
What kind of car would you like? <b>Toyota Tacoma</b>
Let me see if I can find you a Toyota Tacoma.
```

[top](#)