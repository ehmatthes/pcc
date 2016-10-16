---
layout: default
title: Solutions - Chapter 5
---

- [5-3: Alien Colors #1](#alien-colors-1)
- [5-4: Alien Colors #2](#alien-colors-2)
- [5-5: Alien Colors #3](#alien-colors-3)

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