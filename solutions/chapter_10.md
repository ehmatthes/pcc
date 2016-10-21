---
layout: default
title: Solutions - Chapter 10
---

- [10-1: Learning Python](#learning-python)
- [10-2: Learning C](#learning-c)
- [10-3: Guest](#guest)
- [10-4: Guest Book](#guest-book)
- [10-5: Programming Poll](#programming-poll)
- [10-6: Addition](#addition)
- [10-7: Addition Calculator](#addition-calculator)
- [10-8: Cats and Dogs](#cats-and-dogs)
- [10-9: Silent Cats and Dogs](#silent-cats-and-dogs)

Back to [solutions](README.html).

10-1: Learning Python
---

Open a blank file in your text editor and write a few lines summarizing what you've learned about Python so far. Start each line with the phrase *In Python you can...* Save the file as *learning_python.txt* in the same directory as your exercises fro mthis chapter. Write a program that reads the file and prints what you wrote three times. Print the contents once by reading in the entire file, once by looping over the file object, and once by storing the lines in a list and then working with them outside the `with` block.

*learning_python.txt:*

```
In Python you can store as much information as you want.
In Python you can connect pieces of information.
In Python you can model real-world situations.
```

*learning_python.py:*

```python
filename = 'learning_python.txt'

print("--- Reading in the entire file:")
with open(filename) as f:
    contents = f.read()
print(contents)

print("\n--- Looping over the lines:")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n--- Storing the lines in a list:")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())
```

Output:

<pre>
--- Reading in the entire file:
In Python you can store as much information as you want.
In Python you can connect pieces of information.
In Python you can model real-world situations.

--- Looping over the lines:
In Python you can store as much information as you want.
In Python you can connect pieces of information.
In Python you can model real-world situations.

--- Storing the lines in a list:
In Python you can store as much information as you want.
In Python you can connect pieces of information.
In Python you can model real-world situations.
</pre>

[top](#)

10-2: Learning C
---

You can use the `replace()` method to replace any word in a string with a different word. Here's a quick example showing how to replace `'dog'` with `'cat'` in a sentence:

```python
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
```

Read in each line from the file you just created, *learning_python.txt*, and replace the word *Python* with the name of another language, such as *C*. Print each modified line to the screen.

```python
filename = 'learning_python.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    # Get rid of newline, then replace Python with C.
    line = line.rstrip()
    print(line.replace('Python', 'C'))
```

Output:

```
In C you can store as much information as you want.
In C you can connect pieces of information.
In C you can model real-world situations.
```

You can use `rstrip()` and `replace()` on the same line. This is called *chaining* methods. In the following code the newline is stripped from the end of the line and then *Python* is replaced by *C*. The output is identical to the code shown above.

```python
filename = 'learning_python.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    # Get rid of newline, then replace Python with C.
    print(line.rstrip().replace('Python', 'C'))
```

[top](#)

10-3: Guest
---

Write a program that prompts the user for their name. When they respond, write their name to a file called *guest.txt*.

```python
name = input("What's your name? ")

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(name)
```

Output:

<pre>
What's your name? <b>eric</b>
</pre>

*guest.txt:*

```
eric
```

[top](#)

10-4: Guest Book
---

Write a `while` loop that prompts users for their name. When they enter their name, print a greeting to the screen and add a line recording their visit in a file called *guest_book.txt*. Make sure each entry appears on a new line in the file.

```python
filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(name + "\n")
        print("Hi " + name + ", you've been added to the guest book.")
```

Output:

<pre>
Enter 'quit' when you are finished.

What's your name? <b>eric</b>
Hi eric, you've been added to the guest book.

What's your name? <b>willie</b>
Hi willie, you've been added to the guest book.

What's your name? <b>ever</b>
Hi ever, you've been added to the guest book.

What's your name? <b>erin</b>
Hi erin, you've been added to the guest book.

What's your name? <b>quit</b>
</pre>

*guest_book.txt:*

```
eric
willie
ever
erin
```

[top](#)

10-5: Programming Poll
---

Write a `while` loop that asks people why they like programming. Each time someone enters a reason, add their reason to a file that stores all the responses.

```python
filename = 'programming_poll.txt'

responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(response + "\n")
```

Output:

<pre>
Why do you like programming? <b>Programmers can build almost anything they can imagine.</b>
Would you like to let someone else respond? (y/n) <b>y</b>

Why do you like programming? <b>It's really fun, and really satisfying.</b>
Would you like to let someone else respond? (y/n) <b>y</b>

Why do you like programming? <b>It just never gets old.</b>
Would you like to let someone else respond? (y/n) <b>n</b>
</pre>

*programming_poll.txt:*

```
Programmers can build almost anything they can imagine.
It's really fun, and really satisfying.
It just never gets old.
```

[top](#)

10-6: Addition
---

One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an `int`, you'll get a `ValueError`. Write a program that prompts for two numbers. Add them together and print the result. Catch the `TypeError` if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.

```python
try:
    x = input("Give me a number: ")
    x = int(x)

    y = input("Give me another number: ")
    y = int(y)

except ValueError:
    print("Sorry, I really needed a number.")

else:
    sum = x + y
    print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")
```

Output with two integers:

<pre>
Give me a number: <b>23</b>
Give me another number: <b>47</b>
The sum of 23 and 47 is 70.
</pre>

Output with non-numerical input:

<pre>
Give me a number: <b>23</b>
Give me another number: <b>fred</b>
Sorry, I really needed a number.
</pre>

[top](#)

10-7: Addition Calculator
---

Wrap your code from Exercise 10-6 in a `while` loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number.

```python
print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("\nGive me a number: ")
        if x == 'q':
            break

        x = int(x)

        y = input("Give me another number: ")
        if y == 'q':
            break

        y = int(y)

    except ValueError:
        print("Sorry, I really needed a number.")

    else:
        sum = x + y
        print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")
```

Output:

<pre>
Enter 'q' at any time to quit.

Give me a number: <b>23</b>
Give me another number: <b>47</b>
The sum of 23 and 47 is 70.

Give me a number: <b>three</b>
Sorry, I really needed a number.

Give me a number: <b>3</b>
Give me another number: <b>five</b>
Sorry, I really needed a number.

Give me a number: <b>-12</b>
Give me another number: <b>20</b>
The sum of -12 and 20 is 8.

Give me a number: <b>q</b>
</pre>

[top](#)

10-8: Cats and Dogs
---

Make two files, `cats.txt` and `dogs.txt`. Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code ina `try-except` block to catch the `FileNotFound` error, and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the `except` block executes properly.

*cats.txt:*

```
henry
clarence
mildred
```

*dogs.txt:*

```
willie
annahootz
summit
```

```python
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print("\nReading file: " + filename)
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")
```

Output with both files:

```
Reading file: cats.txt
henry
clarence
mildred

Reading file: dogs.txt
willie
annahootz
summit
```

Output after moving *cats.txt:*

```
Reading file: cats.txt
  Sorry, I can't find that file.

Reading file: dogs.txt
willie
annahootz
summit
```

[top](#)

10-9: Silent Cats and Dogs
---

Modify your `except` block in Exercise 10-8 to fail silently if either file is missing.

```python
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    
    try:
        with open(filename) as f:
            contents = f.read()

    except FileNotFoundError:
        pass

    else:
        print("\nReading file: " + filename)
        print(contents)
```

Output when both files exist:

```
Reading file: cats.txt
henry
clarence
mildred

Reading file: dogs.txt
willie
annahootz
summit
```

Output when *cats.txt* has been moved:

```
Reading file: dogs.txt
willie
annahootz
summit
```

[top](#)