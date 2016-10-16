---
layout: default
title: Solutions - Chapter 5
---

- [5-3: Alien Colors #1](#alien-colors-1)

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

5-4: Alien Colors #2
---