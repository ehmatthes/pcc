Appendix A
===

Python has several different versions and a number of ways it can be set up on each operating system. This section will help you install Python if the simple approach in Chapter 1 didn't work, or if you want to install a different version of Python than the one that came with your system.

- [Python on Linux](#python-on-linux)
   - [Installing Python 3 on Linux](#installing-python-3-on-linux)
- [Python on OS X](#python-on-os-x)
   - [Installing Homebrew](#installing-homebrew)
   - [Instaling Python 3](#installing-python-3)
- [Python on Windows](#python-on-windows)

Python on Linux
---

Python is included by default on almost every Linux system, but you might want to use a different version than the default. If so, first find out which version of Python you already have installed:

    $ python --version
    Python 2.7.6

This shows that the default version is Python 2.7.6. However, you might have a version of Python 3 installed as well. To check, issue the following command:

    $ python3 --version
    Python 3.5.0

Python 3.5.0 is also installed. It's worth running both commands before you attempt to install a new version.

###Installing Python 3 on Linux

If you don't have Python 3 or if you want to install a newer version of Python 3, you can use a package called `deadsnakes`, which makes it easy to install multiple versions of Python:

    $ sudo add-apt-repository ppa:fkrull/deadsnakes
    $ sudo apt-get update
    $ sudo apt-get install python3.5

These commands will install Python 3.5 to your system. The following command will start a terminal session running Python 3.5:

    $ python3.5
    >>>

You'll also use this command when you configure your text editor to use Python 3, and when you run programs from a terminal.

[top](#)

Python on OS X
---

Python is already installed on most OS X systems, but you might want to use a different version than what's installed by default. First, find out which version of Python you already have installed:

    $ python --version
    Python 2.7.6

This shows that the default version is Python 2.7.6. However, you might have a version of Python 3 installed as well. To check, issue the command **python3 --version**. You'll probably get an error message, but it's worth checking to see if the version you want is already installed.

###Installing Homebrew

If you only have Python 2 installed, or if you have an older version of Python 3, you can install the latest version of Python 3 using a package called Homebrew.

Homebrew depends on Apple's Xcode package, so open a terminal and run the following command:

    $ xcode-select --install

Click through the confirmation dialogs that pop up. Next, install Homebrew with the following command:

    $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Make sure you include a space between `curl -fsSL` and the URL. The `-e` in this command tells Ruby (the programming language Homebrew is written in) to execute the code that's downloaded here. You should only run commands like this from sources you trust.

To confirm that Homebrew was installed correctly, run the following command:

    $ brew doctor
    Your system is ready to brew.

This output means you're ready to install Python packages through Homebrew.

###Installing Python 3

To install the latest version of Python 3, enter the following:

    $ brew install python3

You can check which version was installed:

    $ python3 --version
    Python 3.5.0
    $

Now you can start a Python 3 terminal session using the command `python3`, and you can ues the `python3` command to configure your text editor so it runs Python programs with Python 3 instead of Python 2.

[top](#)









