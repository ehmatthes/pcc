Chapter 12
===

Restore Points
---

As you work your way through the Alien Invasion project, you'll develop a number of files that work together to create a functioning game. If you make an error somewhere, it can be difficult to know exactly where things went wrong. There are several *restore points* available for this chapter. You can use these restore points in two ways:

- **Compare your code to code that works:** You should try this first. Look at the code you have, and compare it to the corresonding restore point. You might be able to spot where your code differs, and simply correct your own code.

- **Start over from a restore point:** If you want to just start with code that works, you can make a copy of the project using a restore point and pick up from there. For example if you want to start from a working version that fires bullets, you can copy the files and directories from [restore_point_2_fires_bullets](https://github.com/ehmatthes/pcc/tree/master/chapter_12/restore_points/restore_point_2_fires_bullets) and go from there. This might be helpful if you get lost later in the project, or if you've been adding your own features and you want to go back to the book's version of the game.

There are three [restore points](https://github.com/ehmatthes/pcc/tree/master/chapter_12/restore_points) available for Chapter 12:

- The ship moves, which corresponds to the state of the game on page 257. This is [restore_point_1_ship_moves](https://github.com/ehmatthes/pcc/tree/master/chapter_12/restore_points/restore_point_1_ship_moves).
- The ship fires bullets, which corresponds to the state of the game on page 261. This is [restore_point_2_fires_bullets](https://github.com/ehmatthes/pcc/tree/master/chapter_12/restore_points/restore_point_2_fires_bullets).
- The ship fires only three bullets at a time, and the code has been refactored with `fire_bullets()`. This is [restore_point_3_end_chapter_12](https://github.com/ehmatthes/pcc/tree/master/chapter_12/restore_points/restore_point_3_end_chapter_12).

Installing Pygame
---

Pygame is usually straightforward to install, but it can get tricky depending on your operating system and the version of Python you have installed. These instructions can help you get Pygame installed quickly, so you can focus on building games.

- [Pygame on Linux](#pygame-on-linux)
- [Pygame on OS X](#pygame-on-os-x)
- [Pygame on Windows](#pygame-on-windows)

Pygame on Linux
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

You'll need pip for the next step; if you haven't set up pip yet, see the [instructions for seting up pip](installing_pip.md). Enter the following to install Pygame:

    $ pip install --user hg+http://bitbucket.org/pygame/pygame

The output will pause for a moment, informing you which libraries were found. Press **Enter**, even if there are some libraries missing. You should see a message that Pygame installed successfully. To confirm the installation was successful, start a Python terminal session and try to import Pygame by entering the following:

    $ python3
    >>> import pygame
    >>>

If you see no error messages, you're ready to start working on Alien Invasion!

<a href='pygame_osx'></a>Pygame on OS X
---

You'll need [Homebrew](http://brew.sh) to install some packages that Pygame depends on.

To install the libraries that Pygame depends on, enter the following:

    $ brew install hg sdl sdl_image sdl_ttf

This installs the minimum number of packages needed to run Alien Invasion. If you want Pygame to have a little more functionality such as working with sound, you can install two additional libraries:

    $ brew install sdl_mixer portmidi

You'll need [pip](installing_pip.md) to install Pygame. Once you have pip set up correctly, issue the following command:

    $ pip3 install --user  hg+http://bitbucket.org/pygame/pygame

To confirm the installation, start a Python terminal session and try to import Pygame:

    $ python3
    >>> import pygame
    >>>

If this works, you're ready to start building Alien Invasion!

<a href='pygame_windows'></a>Pygame on Windows
---

To install Pygame on your version of Windows, find a Windows installer at [https://bitbucket.org/pygame/pygame/downloads/](https://bitbucket.org/pygame/pygame/downloads/) that matches the version of Python you're running. If you don't see an appropriate installer listed at Bitbucket, check [http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame).

Once you've downloaded the appropriate file, run the installer if it's a *.exe* file.

If you have a file ending in *.whl*, copy the file to your project directory. You'll need [pip](installing_pip.md) set up, so if you haven't done that yet do so now. Then open a command window, navigate to the folder that you copied the installer to, and use pip to run the installer:

    > python -m pip install --user pygame-1.9.2a0-cp35-none-win32.whl

You can test if the installation was successful by starting a new Python terminal session and trying to import Pygame:

    > python
    >>> import pygame
    >>>

If this works, you're ready to start building Alien Invasion!