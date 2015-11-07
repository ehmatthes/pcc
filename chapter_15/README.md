Chapter 15
===

Installing matplotlib
---

There are many different ways to install matplotlib to your system. In this section, I'll recommend one method for each operating system.

Checking if matplotlib is already installed
---

First, check if matplotlib is already installed on your system:

    $ python
    >>> import matplotlib
    >>>

If you don't see an error message, then matplotlib is already installed on your system and you should be able to get started right away on this chapter's projects. If you get an error message, read the appropriate section below for help installing matplotlib on your operating system.

Installing matplotlib
---

- [Installing matplotlib on Linux](#installing-matplotlib-on-linux)
- [Installing matplotlib on OS X](#installing-matplotlib-on-os-x)
- [Installing matplotlib on Windows](#installing-matplotlib-on-windows)

Installing matplotlib on Linux
---

If you're using the version of Python that came with your system, you can use your system's package manager to install matplotlib in one line. For Python 3, this is:

    $ sudo apt-get install python3-matplotlib

If you're using Python 2.7, this is:

    $ sudo apt-get install python-matplotlib

If you installed a newer version of Python, you'll have to install several libraries that matplotlib depends on:

    $ sudo apt-get install python3.5-dev python3.5-tk tk-dev
    $ sudo apt-get install libfreetype6-dev g++

Then use pip to install matplotlib:

    $ pip install --user matplotlib

If you need help using pip, see the <a href="../chapter_12/installing_pip.md">instructions</a> in Chapter 12.

[top](#)

Installing matplotlib on OS X
---

Aple includes matplotlib with its standard Python installation, so make sure you <a href="#checking-if-matplotlib-is-already-installed">check if it's already installed</a> before installing it yourself.

If matplotlib is not already installed and you used Homebrew to install Python, install it like this:

    $ pip install --user matplotlib

If you need help using pip, see the <a href="../chapter_12/installing_pip.md">instructions</a> in Chapter 12. If you have trouble installing matplotlib using pip, try leaving off the `--user` flag.

[top](#)

Installing matplotlib on Windows
---

To install matplotlib on Windows you'll first need to install Visual Studio, which will help your system install the packages that matplotlib depends on. Go to [https://dev.windows.com/](https://dev.windows.com/), click [**Downloads**](https://dev.windows.com/downloads), and look for *Visual Studio Community*. This is a free set of developer tools for Windows. Download and run the installer.

Next you'll need an installer for matplotlib. Go to [https://pypi.python.org/pypi/matplotlib/](https://pypi.python.org/pypi/matplotlib/) and look for a wheel file (a file ending in *.whl*) that matches the version of Python you’re using. For example, if you’re using a 32-bit version of Python 3.5, you’ll need to download *matplotlib-1.4.3-cp35-none-win32.whl*.

If you don't see a file matching your installed version of Python, look at what’s available at [http://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib](http://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib). This site tends to release installers a little earlier than the official matplotlib site.

Copy the *.whl* file to your project folder, open a command window, and navigate to the project folder. Then use pip to install matplotlib:

    > cd python_work
    python_work> python -m pip install --user matplotlib-1.4.3-cp35-none-win32.whl

If you need help using pip, see the <a href="../chapter_12/installing_pip.md">instructions</a> in Chapter 12.

[top](#)