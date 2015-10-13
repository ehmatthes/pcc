Chapter 12
===

- [Installing pip](installing_pip.md)

Installing Pygame
---

Pygame is usually straightforward to install, but it can get tricky depending on your operating system and the version of Python you have installed. These instructions can help you get Pygame installed quickly, so you can focus on building games.

- [Pygame on Linux](#pygame_linux)
- [Pygame on OS X](#pygame_osx)
- [Pygame on Windows](#pygame_windows)

<a href='pygame_linux'></a>Pygame on Linux
---

### Python 2.7

If you're using your system's default version of Python 2.7, you can install Pygame using the package manager:

    $ sudo apt-get install python-pygame

To make sure the installation worked correctly, start a Python terminal session and try to import Pygame:

    $ python
    >>> import pygame
    >>>

If you don't see an error message, you're ready to start building Alien Invasion.

### Python 3

Setting up Pygame for Python 3 is a two-step process; first you'll install some packages that Pygame depends on, then you'll download and install Pygame.

Run the following commands to install the packages required to run Alien Invasion. (If you use a command such as `python3.5` on your system, replace `python3-dev` with `python3.5-dev`):

    $ sudo apt-get install python3-dev mercurial
    $ sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev

If you want to enable some more advanced functionality in Pygame such as the ability to add sounds, you can also install the following libraries:

    $ sudo apt-get install libsdl-mixer1.2-dev libportmidi-dev
    $ sudo apt-get install libswscale-dev libsmpeg-dev libavformat-dev libavcode-dev
    $ sudo apt-get install python-numpy

You'll need pip for the next step; if you haven't set up pip yet, see the instructions for seting up pip. Enter the following to install Pygame:

    $ pip install --user hg+http://bitbucket.org/pygame/pygame

The output will pause for a moment, informing you which libraries were found. Press **Enter**, even if there are some libraries missing. You should see a message that Pygame installed successfully. To confirm the installation was successful, start a Python terminal session and try to import Pygame by entering the following:

    $ python3
    >>> import pygame
    >>>

If you see no error messages, you're ready to start working on Alien Invasion!

<a href='pygame_osx'></a>Pygame on OS X
---



<a href='pygame_windows'></a>Pygame on Windows
---
