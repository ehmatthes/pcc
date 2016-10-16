---
layout: default
title: Solutions - Chapter 5
---

- [5-3: Alien Colors #1](#alien-colors-1)
- [5-4: Alien Colors #2](#alien-colors-2)
- [5-5: Alien Colors #3](#alien-colors-3)
- [5-6: Stages of Life](#stages-of-life)
- [5-7: Favorite Fruit](#favorite-fruit)

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




