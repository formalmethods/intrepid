# Prerequisites for any OS
- python 2.7 [link1][1], [link2][2] (this one contains jupyter by default)
- jupyter package [link][3] (optional, allows using the notebooks under examples/)

# Prequisites for Windows
- 64bits version
- Visual C++ Redistributable for Visual Studio 2015 [link][4]

# Install
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

# Feedback
If you wish to drop a feedback you may write to
`roberto.bruttomesso@gmail.com`.


[1]: https://www.python.org/ "Python"
[2]: https://www.continuum.io/downloads "Anaconda"
[3]: http://jupyter.org/ "Jupyter"
[4]: https://www.microsoft.com/en-us/download/details.aspx?id=48145 "Visual C++ Redistributable for Visual Studio 2015"
