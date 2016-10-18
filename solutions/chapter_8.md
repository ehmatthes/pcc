---
layout: default
title: Solutions - Chapter 8
---

- [8-1: Message](#message)
- [8-2: Favorite Book](#favorite-book)
- [8-3: T-Shirt](#t-shirt)
- [8-4: Large Shirts](#large-shirts)
- [8-5: Cities](#cities)
- [8-6: City Names](#city-names)
- [8-7: Album](#album)
- [8-8: User Albums](#user-albums)
- [8-9: Magicians](#magicians)
- [8-10: Great Magicians](#great-magicians)
- [8-11: Unchanged Magicians](#unchanged-magicians)

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

8-4: Large Shirts
---

Modify the `make_shirt()` function so that shirts are large by default with a message that reads *I love Python*. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

```python
def make_shirt(size='large', message='I love Python!'):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')
```

Output:

```
I'm going to make a large t-shirt.
It will say, "I love Python!"

I'm going to make a medium t-shirt.
It will say, "I love Python!"

I'm going to make a small t-shirt.
It will say, "Programmers are loopy."
```

[top](#)

8-5: Cities
---

Write a function called `describe_city()` that accepts the name of a city and its country. The function should print a simple sentence, such as `Reykjavik is in Iceland.` Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

```python
def describe_city(city, country='chile'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('santiago')
describe_city('reykjavik', 'iceland')
describe_city('punta arenas')
```

Output:

```
Santiago is in Chile.
Reykjavik is in Iceland.
Punta Arenas is in Chile.
```

[top](#)

8-6: City Names
---

Write a function called `city_country()` that takes in the name of a city and its country. The function should return a string formatted like this:

> "Santiago, Chile"

Call your function with at least three city-country pairs, and print the value that's returned.

```python
def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return(city.title() + ", " + country.title())

city = city_country('santiago', 'chile')
print(city)

city = city_country('ushuaia', 'argentina')
print(city)

city = city_country('longyearbyen', 'svalbard')
print(city)
```

Output:

```
Santiago, Chile
Ushuaia, Argentina
Longyearbyen, Svalbard
```

[top](#)

8-7: Album
---

Write a function called `make_album()` that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.

Add an optional parameter to `make_album()` that allows you to store the nubmer of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album's dictionary. Make at least one new function call that includes the nubmer of tracks on an album.

Simple version:

```python
def make_album(artist, title):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)
```

Output:

<pre>
{'title': 'Ride The Lightning', 'artist': 'Metallica'}
{'title': 'Ninth Symphony', 'artist': 'Beethoven'}
{'title': 'Red-Headed Stranger', 'artist': 'Willie Nelson'}
</pre>

With tracks:

```python
def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)

album = make_album('iron maiden', 'piece of mind', tracks=8)
print(album)
```

Output:

<pre>
{'artist': 'Metallica', 'title': 'Ride The Lightning'}
{'artist': 'Beethoven', 'title': 'Ninth Symphony'}
{'artist': 'Willie Nelson', 'title': 'Red-Headed Stranger'}
{'tracks': 8, 'artist': 'Iron Maiden', 'title': 'Piece Of Mind'}
</pre>

[top](#)

8-8: User Albums
---

Start with your program from Exercise 8-7. Write a `while` loop that allows users to enter an album's artist and title. Once you have that information, call `make_album()` with the user's input and print the dictionary that's created. Be sure to include a quit value in the `while` loop.

```python
def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

# Prepare the prompts.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    
    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")
```

Output:

<pre>
Enter 'quit' at any time to stop.

What album are you thinking of? <b>number of the beast</b>
Who's the artist? <b>iron maiden</b>
{'artist': 'Iron Maiden', 'title': 'Number Of The Beast'}

What album are you thinking of? <b>touch of class</b>
Who's the artist? <b>angel romero</b>
{'artist': 'Angel Romero', 'title': 'Touch Of Class'}

What album are you thinking of? <b>rust in peace</b>
Who's the artist? <b>megadeth</b>
{'artist': 'Megadeth', 'title': 'Rust In Peace'}

What album are you thinking of? <b>quit</b>

Thanks for responding!
</pre>

[top](#)

8-9: Magicians
---

Make a list of magician's names. Pass the list to a function called `show_magicians()`, wich prints the name of each magician in the list.

```python
def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician.title())

magicians = ['harry houdini', 'david blaine', 'teller']
show_magicians(magicians)
```

Output:

```
Harry Houdini
David Blaine
Teller
```

[top](#)

8-10: Great Magicians
---

Start with a copy of your program from Exercise 8-9. Write a function called `make_great()` that modifies the list of magicians by adding the phrase *the Great* to each magician's name. Call `show_magicians()` to see that the list has actually been modified.

```python
def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)
```

Output:

```
Harry Houdini
David Blaine
Teller

Teller the Great
David Blaine the Great
Harry Houdini the Great
```

[top](#)

8-11: Unchanged Magicians
---

Start with your work from Exercise 8-10. Call the function `make_great()` with a copy of the list of magicians' names. Because the original list will be unchanged, return the new list and store it in a separate list. Call `show_magicians()` with each list to show that you have one list of the original names and one list with *the Great* added to each magician's name.

```python
def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\nOriginal magicians:")
show_magicians(magicians)
```

Output:

```
Harry Houdini
David Blaine
Teller

Great magicians:
Teller the Great
David Blaine the Great
Harry Houdini the Great

Original magicians:
Harry Houdini
David Blaine
Teller
```

[top](#)