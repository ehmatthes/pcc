Installing pip
===

Pip is a special program used to install Python packages to your system. Pip is sometimes included automatically when Python is installed to your system, and sometimes you have to install it yourself. These instructions will help you check if pip is on your system, and help you upgrade or install it if necessary.

- [Pip on Linux](#pip-onlLinux)
    - [Checking for pip](#checking-for-pip)
    - [Installing pip](#installing-pip)
    - [Upgrading pip](#upgrading-pip)
    - [Installing Python packages with pip](#installing-python-packages-with-pip)
    - [Uninstalling packages with pip](#uninstalling-packages-with-pip)
- [Pip on OS X](#pip-on-os-x)
- [Pip on Windows](#pip-on-windows)

Pip on Linux
---

### Checking for pip

First, check whether pip is installed on your system:

    $ pip --version
    pip 7.0.3 from /usr/local/lib/python3.5/dist-packages (python 3.5)

The output of `pip --version` tells you which version of pip is currently installed, and which version of Python it's set up to install packages for. This is especially helpful if you have more than one version of Python installed on your system.

If you have only one version of Python installed on your system, you can use pip to install packages. You might want to try upgrading pip first though.

If you have more than one version of Python installed on your system, you should also try the command pip3:

    $ pip3 --version
    pip 7.0.3 from /usr/local/lib/python3.5/dist-packages (python 3.5)


Here pip3 is set up to install to the same version of Python, but often times pip will install to Python 2. pip3, if you have it set up, should always install packages to the version of Python 3 you have installed.

### Installing pip

To install pip, go to [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py). Save the file if you're prompted to do so; if the code for *get-pip.py* appears in your browser, copy and paste the entire program into your text editor and save the file as *get-pip.py*.

Open a terminal and navigate to the folder containing *get-pip.py*, and run it with administrative privileges:

    $ cd Downloads
    Downloads$ sudo python get-pip.py
    Collecting pip
      Downloading pip-7.1.2-py2.py3-none-any.whl (1.1MB)
        100% |████████████████████████████████| 1.1MB 448kB/s 
    Collecting setuptools
      Downloading setuptools-18.4-py2.py3-none-any.whl (462kB)
        100% |████████████████████████████████| 462kB 676kB/s 
    Collecting wheel
      Downloading wheel-0.26.0-py2.py3-none-any.whl (63kB)
        100% |████████████████████████████████| 65kB 912kB/s 
    Installing collected packages: pip, setuptools, wheel
    Successfully installed pip-7.1.2 setuptools-18.4 wheel-0.26.0

After the program runs, use the command `pip --version` (or `pip3 --version`) to make sure pip was installed correctly.

### Upgrading pip

Once you have pip installed, it's good to upgrade it from time to time. Usually pip will prompt you with instructions for how to upgrade it when necessary, but you can try to upgrade manually any time. For example, here's sample output for upgrading an out-of-date version of pip:

    $ sudo pip install --upgrade pip
    You are using pip version 6.1.1, however version 7.1.2 is available.
    You should consider upgrading via the 'pip install --upgrade pip' command.
    Collecting pip
      Downloading pip-7.1.2-py2.py3-none-any.whl (1.1MB)
        100% |████████████████████████████████| 1.1MB 382kB/s 
    Installing collected packages: pip
      Found existing installation: pip 6.1.1
        Uninstalling pip-6.1.1:
           Successfully uninstalled pip-6.1.1
    Successfully installed pip-7.1.2

### Installing Python packages with pip

Once you have pip installed, most Python packages can be installed in one line. For example, here's how you can install [Requests](http://docs.python-requests.org/en/latest/), which is used to make API calls from Python programs:

    $ pip install --user requests
    Collecting requests
      Downloading requests-2.8.1-py2.py3-none-any.whl (497kB)
        100% |████████████████████████████████| 499kB 595kB/s 
    Installing collected packages: requests
    Successfully installed requests

Here pip has downloaded the files needed to install Requests, and then managed the installation for us. The `--user` flag means pip has made Requests available to us, but not to other users. This keeps each user's Python packages from conflicting with each other on systems with more than one user. It's a good idea to use this flag unless you have a specific reason not to.

Now you can start a Python terminal session, and import requests:

    $ python
    >>> import requests
    >>> url = "http://google.com"
    >>> r = requests.get(url)
    >>> r.status_code
    200

Here we've used requests to retrieve Google's home page, and the status code of 200 tells us that the request was successful.

### Uninstalling packages with pip

If you ever want to uninstall a package, you can use requests to do so as well:

    $ pip uninstall requests
    Uninstalling requests-2.8.1:
      /home/ehmatthes/.local/lib/python3.5/site-packages/requests-2.8.1.dist-info/DESCRIPTION.rst
    ...
    Proceed (y/n)? y
      Successfully uninstalled requests-2.8.1

Pip lists all the files that will be removed, prompts you about whether to proceed, and then uninstalls the package.



























