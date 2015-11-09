Appendix A
===

Python has several different versions and a number of ways it can be set up on each operating system. This section will help you install Python if the simple approach in Chapter 1 didn't work, or if you want to install a different version of Python than the one that came with your system.

- [Python on Linux](#python-on-linux)
    - [Installing Python 3 on Linux](#installing-python-3-on-linux)
- [Python on OS X](#python-on-os-x)
    - [Installing Homebrew](#installing-homebrew)
    - [Instaling Python 3](#installing-python-3)
- [Python on Windows](#python-on-windows)
    - [Installing Python 3 on Windows](#installing-python-3-on-windows)
    - [Finding the Python interpreter](#finding-the-python-interpreter)
    - [Adding Python to your Path variable](#adding-python-to-your-path-variable) 

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

Python on Windows
---

Python isn't usually included by default on Windows, but it's worth checking to see if it exists on your system. Open a command window and run the following command:

    > python --version
    Python 3.5.0

If you see output like this, Python is already installed, but you might want to install a newer version if your version is not up to date. If you see an error message, you'll need to download and install Python.

###Installing Python 3 on Windows

Go to [http://python.org/downloads/](http://python.org/downloads/) and click the version of Python you want. Download the installer, and when you run it make sure to check the *Add Python to PATH* option. This will let you use the `python` command instead of having to enter your system’s full path to python, and you won’t have to modify your system’s environment variables manually. After you’ve installed Python, issue the `python --version` command in a new terminal window. If it works, you’re done.

###Finding the Python interpreter

If you've installed Python and the simple command `python` doesn't work, you'll need to tell Windows where to find the Python interpreter. To find it, open your C drive and find the folder with a name starting with *Python* (you might need to enter the word `python` in the Windows Explorer search bar to find the right folder). Open the folder, and look for a file with the lowercase name *python*. Right-click this file and choose **Properties**; you'll see the path to this file under the heading *Location*.

In the terminal window, use the path to confirm the version you just installed:

    $ C:\\Python35\python --version
    Python 3.5.0

###Adding Python to your Path variable

It's annoying to type the full path each time you want to start a Python terminal session. If you add the path to the system you can just use the command `python`. (If you already check the *Add Python to PATH* box when installing, you can skip this step.)

Open your system's **Control Panel**, choose **System and Security**, and then choose **System**. Click **Advanced System Settings**. In the window that pops up, click **Environment Variables**. In the box labeled *System variables*, look for a variable called `Path`. click **Edit**. In the box that pops up, click in the box labeled *Variable value* and use the right arrow key to scroll all the way to the right. Be careful not to overwrite the existing variable; if you do, click Cancel and try again. Add a semicolon and the path to your *python.exe* file to the existing variable:

    %SystemRoot%\system32\...\System32\WindowsPowerShell\v1.0\;C:\Python35

Close your terminal window and open a new one. This will load the new `Path` variable into your terminal session. Now when you enter `python --version`, you should see the version of Python you just set in your `Path` variable. You can now start a Python terminal sesion by just entering `python` at a command prompt.

[top](#)




