---
layout: default
title: Solutions - Chapter 3
---

- [3-1: Names](#names)
- [3-2: Greetings](#greetings)
- [3-4: Guest List](#guest-list)
- [3-5: Changing Guest List](#changing-guest-list)
- [3-6: More Guests](#more-guests)
- [3-7: Shrinking Guest List](#shrinking-guest-list)

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

3-4: Guest List
---

If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you'd like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

    guests = ['guido van rossum', 'jack turner', 'lynn hill']

    name = guests[0].title()
    print(name + ", please come to dinner.")

    name = guests[1].title()
    print(name + ", please come to dinner.")

    name = guests[2].title()
    print(name + ", please come to dinner.")

3-5: Changing Guest List
---

You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. You'll have to think of someone else to invite.

- Start with your program from Exercise 3-4. Add a `print` statement at the end of your program stating the name of the guest who can't make it.
- Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting.
- Print a second set of invitation messages, one for each person who is still in your list.

    # Invite some people to dinner.
    guests = ['guido van rossum', 'jack turner', 'lynn hill']

    name = guests[0].title()
    print(name + ", please come to dinner.")

    name = guests[1].title()
    print(name + ", please come to dinner.")

    name = guests[2].title()
    print(name + ", please come to dinner.")

    name = guests[1].title()
    print("\nSorry, " + name + " can't make it to dinner.")

    # Jack can't make it! Let's invite Gary instead.
    del(guests[1])
    guests.insert(1, 'gary snyder')

    # Print the invitations again.
    name = guests[0].title()
    print("\n" + name + ", please come to dinner.")

    name = guests[1].title()
    print(name + ", please come to dinner.")

    name = guests[2].title()
    print(name + ", please come to dinner.")

