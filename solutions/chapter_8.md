---
layout: default
title: Solutions - Chapter 8
---

- [8-1: Message](#message)
- [8-2: Favorite Book](#favorite-book)
- [8-3: T-Shirt](#t-shirt)
- [8-4: Large Shirts](#large-shirts)
- [8-5: Cities](#cities)

Back to [solutions](#README.html).

8-1: Message
---

Write a function called `display_message()` that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.

```python
def display_message():
    """Display a message about what I'm learning."""
    msg = "I'm learning to store code in functions."
    print(msg)

display_message()
```

Output:

```
I'm learning to store code in functions.
```

[top](#)

8-2: Favorite Book
---

Write a function called `favorite_book()` that accepts one parameter, `title`. The function should print a message, such as `One of my favorite books is Alice in Wonderland.` Call the function, making sure to include a book title as an argument in the function call.

```python
def favorite_book(title):
    """Display a message about someone's favorite book."""
    print(title + " is one of my favorite books.")

favorite_book('The Abstract Wild')
```

Output:

```
The Abstract Wild is one of my favorite books.
```

[top](#)

8-3: T-Shirt
---

Write a function called `make_shirt()` that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.

Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

```python
def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt('large', 'I love Python!')
make_shirt(message="Readability counts.", size='medium')
```

Output:

```
I'm going to make a large t-shirt.
It will say, "I love Python!"

I'm going to make a medium t-shirt.
It will say, "Readability counts."
```

[top](#)