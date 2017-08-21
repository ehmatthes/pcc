---
layout: default
title: Chapter 10
---

Updates
---

Some of the text files from [Project Gutenberg](https://www.gutenberg.org/) are now encoded as utf-8. This can result in a `UnicodeDecodeError` when trying to open the file. This can be addressed by adding an argument when we call `open()`, which explictly tells Python which encoding to use when opening the file.  For example, in the program *alice.py* on pages 203-204, the first lines of the program should look like this:

    filename = 'alice_new.txt'

    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()

The `encoding` argument should be added to the `open()` calls in *word_count.py* as well.