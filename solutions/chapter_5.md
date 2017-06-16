---
layout: default
title: Solutions - Chapter 5
---

- [5-3: Alien Colors #1](#5-3-alien-colors-1)
- [5-4: Alien Colors #2](#5-4-alien-colors-2)
- [5-5: Alien Colors #3](#5-5-alien-colors-3)
- [5-6: Stages of Life](#5-6-stages-of-life)
- [5-7: Favorite Fruit](#5-7-favorite-fruit)
- [5-8: Hello Admin](#5-8-hello-admin)
- [5-9: No Users](#5-9-no-users)
- [5-10: Checking Usernames](#5-10-checking-usernames)
- [5-11: Ordinal Numbers](#5-11-ordinal-numbers)

Back to [solutions](README.html).

5-3: Alien Colors #1
---

Imagine an alien was just shot down in a game. Create a variable called `alien_color` and assign it a value of `'green'`, `'yellow'`, or `'red'`.

- Write an `if` statement to test whether the alien's color is green. If it is, print a message that the player just earned 5 points.

- Write one version of this program that passes the if test and another tha fails. (The version that fails will have no output.)

Passing version:

```python
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
```

Output:

```
You just earned 5 points!
```

Failing version:

```python
alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
```

(no output)

[top](#)

5-4: Alien Colors #2
---

Choose a color for an alien as you did in Exercise 5-3, and write an `if-else` chain.

- If the alien's color is green, print a statement that the player just earned 5 points for shooting the alien.
- If the alien's coor isn't green, print a statement that the player just earned 10 points.
- Write one version of this program that runs the `if` block and another that runs the `else` block.

`if` block runs:

```python
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")
```

Output:

```
You just earned 5 points!
```

`else` block runs:

```python
alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")
```

Output:

```
You just earned 10 points!
```

[top](#)

5-5: Alien Colors #3
---

Turn your `if-else` chain from Exercise 5-4 into an `if-elif-else` cahin.

- If the alien is green, print a message that the player earned 5 points.
- If the alien is yellow, print a message that the player earned 10 points.
- If the alien is red, print a message that the player earned 15 points.
- Write three versions of this program, making sure each message is printed for the appropriate color alien.

```python
alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")
```

Output for `'red'` alien:

```
You just earned 15 points!
```

[top](#)

5-6: Stages of Life
---

Write an `if-elif-else` cahin that determines a person's stage of life. Set a value for the variable `age`, and then:

- If the person is less than 2 years old, print a message that the person is a baby.
- If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
- If the person is at least 4 years old but less than 13, print a message that the person is a toddler.
- If the person is at least 13 years old but less than 20, print a message that the person is a toddler.
- If the person is at least 20 years old but less than 65, print a message that the person is a toddler.
- If the person is age 65 or older, print a message that the person is an elder.

```python
age = 17

if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult!")
else:
    print("You're an elder!")
```

Output:

```
You're a teenager!
```

[top](#)

5-7: Favorite Fruit
---

Make a list of your favorite fruits, and then write a series of independent `if` statements that check for certain fruits in your list.

- Make a list of your three favorite fruits and call it `favorite_fruits`.
- Write five `if` statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the `if` block should print a statement, such as *You really like bananas!*

```python
favorite_fruits = ['blueberries', 'salmonberries', 'peaches']

if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'apples' in favorite_fruits:
    print("You really like apples!")
if 'blueberries' in favorite_fruits:
    print("You really like blueberries!")
if 'kiwis' in favorite_fruits:
    print("You really like kiwis!")
if 'peaches' in favorite_fruits:
    print("You really like peaches!")
```

Output:

```
You really like blueberries!
You really like peaches!
```

[top](#)

5-8: Hello Admin
---

Make a list of five or more usernnames, including the name `'admin'`. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user:

- If the username is `'admin'`, print a special greeting, such as *Hello admin, would you like to see a status report?*
- Otherwise, print a generic greeting, such as *Hello Eric, thank you for loggin in again.*

```python
usernames = ['eric', 'willie', 'admin', 'erin', 'ever']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again!")
```

Output:

```
Hello eric, thank you for logging in again!
Hello willie, thank you for logging in again!
Hello admin, would you like to see a status report?
Hello erin, thank you for logging in again!
Hello ever, thank you for logging in again!
```

[top](#)

5-9: No Users
---

Add an `if` test to *hello_admin.py* to make sure the list of users is not empty.

- If the list is emtpy, print the message *We need to find some users!*
- Remove all of the usernames from your list, and make sure the correct message is printed.

```python
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + username + ", thank you for logging in again!")
else:
    print("We need to find some users!")
```

Output:

```
We need to find some users!
```

[top](#)

5-10: Checking Usernames
---

Do the following to create a program that simulates how websites ensure that everyone has a unique username.

- Make a list of five or more usernames called `current_users`.
Make another list of five usernames called `new_users`. Make sure one or two of the new usernames are also in the `current_users` list.
- Loop through the `new_users` list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
- Make sure your comparison is case insensitive. If `'John'` has been used, `'JOHN'` should not be accepted.

```python
current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry " + new_user + ", that name is taken.")
    else:
        print("Great, " + new_user + " is still available.")
```

Output:

```
Great, sarah is still available.
Sorry Willie, that name is taken.
Great, PHIL is still available.
Sorry ever, that name is taken.
Great, Iona is still available.
```

Note: If you're not comfortable with list comprehensions yet, the list `current_users_lower` can be generated using a loop:

```python
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())
```

[top](#)

5-11: Ordinal Numbers
---

Ordinal numbers indicate their position in a list, such as *1st* or *2nd*. Most ordinal numbers end in *th*, except 1, 2, and 3.

- Store the numbers 1 through 9 in a list.
- Loop through the list.
- Use an `if-elif-else` chain inside the loop to print the proper ordinal ending for each number. Your output should read `"1st 2nd 3rd 4th 5th 6th 7th 8th 9th"`, and each result should be on a separate line.

```python
numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")
```

Output:

```
1st
2nd
3rd
4th
5th
6th
7th
8th
9th
```

[top](#)