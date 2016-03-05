Setup Instructions: Linux
===

- [Checking your current version of Python](#current_version)
- [Installing Python 3.5](#python3.5)
- [Installing Geany](#installing_geany)
    - [Configuring Geany](#configuring_geany)

<a name='current_version'></a>Checking your current version of Python
---

Python is probably already installed on your system. Find out which version is your default by issuing the command `python --version`:

    $ python --version
    Python 2.7.6

If you see something like this, Python 2.7 is your default version. You should also see if you have Python 3 installed:

    $ python3 --version
    Python 3.4.0

If you have Python 3.4 or later, it's fine to start out by using the installed version. If you have Python 3.3 or earlier, it's probably worth installing Python 3.5.

[top](#)

<a name='python3.5'></a>Installing Python 3.5
---

The following instructions should work on Ubuntu, and most Debian-based systems that use the apt package manager.

Add the *deadsnakes* package, and then install Python 3.5:

    $ sudo add-apt-repository ppa:fkrull/deadsnakes
    $ sudo apt-get update
    $ sudo apt-get install python3.5

You can confirm that the installation was successful:

    $ python3.5 --version
    Python 3.5.0

Now to start a Python terminal session, you'll use the command `python3.5`:

    $ python3.5
    Python 3.5.0 (default, Sep 17 2015, 00:00:00) 
    [GCC 4.8.4] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

You'll use this command when you configure your text editor, and when you run programs from the terminal.

[top](#)

<a name='installing_geany'></a>Installing Geany
---

On Ubuntu and other systems that use the apt package manager, you can install Geany in one line:

    $ sudo apt-get install geany

If this doesn't work, you can see the instructions at [http://geany.org/Download/ThirdPartyPackages/](http://geany.org/Download/ThirdPartyPackages/).

[top](#)

<a name='configuring_geany'></a>
### Configuring Geany

If you use the simple command `python` to start a terminal session on your system, you shouldn't have to configure Geany at all. But if you use a command like `python3` or `python3.5`, you'll have to modify Geany slightly so it uses the correct version of Python to run your programs.

Open an empty file and save it as *hello_world.py*. The file should have one line in it:

    print("Hello Python world!")

Go to **Build>Set Build Commands**. You should see the word *Compile*, and a command next to the word *Compile*. Change this to

    python3 -m py_compile "%f"

If you use a command like `python3.5`, make sure you use that command instead.

Next to the word *Execute*, enter the following command:

    python3 "%f"

Again, if you use a command like `python3.5`, make sure you use that command.

Now you can run programs by selecting **Build>Execute**, clicking the Execute icon with a set of gears on it, or by pressing **F5**.

[top](#)



