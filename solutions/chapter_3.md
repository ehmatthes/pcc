---
layout: default
title: Solutions - Chapter 3
---

- [3-1: Names](#names)
- [3-2: Greetings](#greetings)

Back to [solutions](README.html).

3-1: Names
---

Store the names of a few of your friends in a list called `names`. Print each person's name by accessing each element in the list, one at a time.

    names = ['ron', 'tyler', 'dani']

    print(names[0])
    print(names[1])
    print(names[2])

[top](#)

3-2: Greetings
---

Start with the list you used in Exercise 3-1, but instead of just printing each person's name, print a message to them. The text of each message should be the same, but each message should be personalized with the person's name.

    names = ['ron', 'tyler', 'dani']

    msg = "Hello, " + names[0].title() + "!"
    print(msg)

    msg = "Hello, " + names[1].title() + "!"
    print(msg)

    msg = "Hello, " + names[2].title() + "!"
    print(msg)

[top](#)