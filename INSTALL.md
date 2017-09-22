# Prerequisites for any OS
- [python 2.7][1]: required. 
- [pandas][5]: required. Can be installed with
```
$ python -m pip install pandas
```
- [jupyter][3]: optional: allows running the ipython notebooks under folder examples/. Can be installed with
```
$ python -m pip install jupyter
```

Alternatively, the [conda][2] python release comes with both python 2.7 and jupyter preinstalled.

# Prerequisites for Windows
- [Visual C++ Redistributable for Visual Studio 2015][4]

# Officially Supported OSes 
- Windows 7 or above, 64 bit
- Ubuntu 16.04 or above, 64 bit
For other OSes please contact me privately at 
`roberto.bruttomesso@gmail.com`.

# Install using pip
```
$ pip install git+https://github.com/formalmethods/intrepyd
```

# Install from a cloned/downloaded source
From the root directory of intrepid, execute
```
$ python setup.py install
```

# After install

## Linux
From the root directory of intrepid, execute
```
export LD_LIBRARY_PATH=`pwd`/libs/linux32
```
or
```
export LD_LIBRARY_PATH=`pwd`/libs/linux64
```
depending on your OS architecture.

## OSX
From the root directory of intrepid, execute
```
export DYLD_LIBRARY_PATH=`pwd`/libs/osx
```

# Unit test
From the root directory of intrepid, execute
```
python -m unittest discover
```
If the unit tests go through without any error,
then you should have a working version of
intrepid installed in your python environment.

# Bug reporting
Please report any bug you should experience [here](https://github.com/formalmethods/intrepyd/issues).

# Feedback
If you wish to drop a feedback you may write to
`roberto.bruttomesso@gmail.com`.


[1]: https://www.python.org/ "Python"
[2]: https://www.continuum.io/downloads "Anaconda"
[3]: http://jupyter.org/ "Jupyter"
[4]: https://www.microsoft.com/en-us/download/details.aspx?id=48145 "Visual C++ Redistributable for Visual Studio 2015"
[5]: http://pandas.pydata.org/ "Python Data Analysis Library"
