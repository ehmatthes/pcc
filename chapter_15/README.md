Chapter 15
===

- [Installing matplotlib](#installing-matplotlib)
    - [Checking if matplotlib is already installed](#checking-if-matplotlib-is-already-installed)
    - [Installing matplotlib on Linux](#installing-matplotlib-on-linux)
    - [Installing matplotlib on OS X](#installing-matplotlib-on-os-x)
    - [Installing matplotlib on Windows](#installing-matplotlib-on-windows)
- [Installing Pygal](#installing-pygal)
- [Updates](#updates)

Installing matplotlib
---

There are many different ways to install matplotlib to your system. In this section, I'll recommend one method for each operating system. If you'd like to see the kinds of visualizations you can make with matplotlib, see the official matplotlib [sample gallery](http://matplotlib.org/gallery.html). When you click a visualization in the gallery, you can see the code used to generate the plot.

### Checking if matplotlib is already installed

First, check if matplotlib is already installed on your system:

    $ python
    >>> import matplotlib
    >>>

If you don't see an error message, then matplotlib is already installed on your system and you should be able to get started right away on this chapter's projects. If you get an error message, read the appropriate section below for help installing matplotlib on your operating system.

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

Installing Pygal
---
Pygal has been updated recently, which is a good thing; you're learning a library that's being steadily improved. This also means you have two choices about how to install Pygal. You can install version 1.7 which supports the code in the book exactly as it's written, or you can install the most recent version of Pygal and modify some of the code in the book. If you install the most recent version there are some slight changes you'll need to make for the code in the second half of chapters 15 and 16, and chapter 17.

### Running Pygal code exactly as it appears in the book

Pygal 1.7 allows the code to run exactly as it appears in the book. To do this, modify the command for installing pygal so pip will install version 1.7 (page 340):

    $ pip install --user pygal==1.7

On Windows, this would be:

    > python -m pip install --user pygal==1.7

If you've already installed Pygal you can see which version was installed by running the command `pip freeze`:

    $ pip freeze
    pygal==2.1.1

If you installed Pygal 2.0 or later and want to install 1.7 instead, uninstall Pygal first:

    $ pip uninstall pygal
    $ pip install --user pygal==1.7

### Using the latest version of Pygal

The latest version of Pygal is version 2.1.1. This is the version that will be installed if you don't specify a version for pip to install:

    $ pip install --user pygal

or

    $ python -m pip install --user pygal
    
If you use the latest version, you'll need to make some slight changes to the code in chapter 16 and chapter 17:

- [Updates to Chapter 16 Pygal code](../chapter_16/README.md#updates)
- [Updates to Chapter 17 Pygal code](../chapter_17/README.md#updates)

[top](#)

Updates
---

Pygal has been updated to version 2; make sure you've read the notes about [installing Pygal](#installing-pygal) above.

If you're using Pygal version 2.0 or higher you'll need to add one line to each file in order to render the charts correctly. Pygal has changed the way tooltips are displayed, so if you don't add this line you won't see any tooltips when you hover over the bars on a chart.

Each time you make a chart in Pygal, add a line that tells Pygal to make an SVG file that renders correctly in a browser. For example:

    hist = pygal.Bar()
    hist.force_uri_protocol = 'http'
    
This causes Pygal to configure the SVG rendering engine to work correctly for displaying the files in a browser.

Page by page updates
---

Code that appears in bold is new, or is modified from what appears in the book.

### p. 342, die_visual.py

<pre>
hist = pygal.Bar()
<b>hist.force_uri_protocol = 'http'</b>
</pre>
    
### p. 343-344, dice_visual.py

<pre>
hist = pygal.Bar()
<b>hist.force_uri_protocol = 'http'</b>
</pre>

### p. 345, different_dice.py

<pre>
hist = pygal.Bar()
<b>hist.force_uri_protocol = 'http'</b>
</pre>