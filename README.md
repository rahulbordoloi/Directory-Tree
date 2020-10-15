# Directory Tree Package

[![Setup Automated](https://img.shields.io/badge/setup-automated-blue?logo=gitpod)](https://gitpod.io/from-referrer/)
![Test passing](https://img.shields.io/badge/Tests-passing-brightgreen.svg)
![Python Version](https://img.shields.io/badge/python-3.6+-brightgreen.svg)
[![PyPI version](https://badge.fury.io/py/directory-tree.svg)](https://badge.fury.io/py/directory-tree)
![Last Commit](https://img.shields.io/github/last-commit/rahulbordoloi/Directory-Tree?style=flat-square)
[![Open Source Love png2](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)


## About 

Want to display your project/current working directory as a neat tree? No Worries!

`Directory Tree` is a simple python utility package that displays out the Tree Structure of a user-defined directory.

<b><i> Currently Available for All Platforms.  </i></b>

## Installation

Run the following command on your terminal to install `directory_tree`: 

1 .  Installing the package using `pip`:
```python
pip install directory_tree
```
OR

```python
pip3 install directory_tree
```

2 . Cloning the repository:

```
git clone https://github.com/rahulbordoloi/Directory-Tree/
cd Directory-Tree
pip install -e .
```

## Usage

<h4> Arguments </h4>


| __Parameters__ | __Description__ |
|    ---         |       ---       |
| __dir_path__ | Refers to the Directory Path of Operation. By default, refers to the Current Working Directory. |
| __string_rep__ | Refers to whether you just want the direct output or a string representation of the same. |


Run this script in order to print out the tree structure of a user-defined directory!

```python
# Importing Libraries
from directory_tree import display_tree

# Main Method
if __name__ == '__main__':
    display_tree(directory_path)
```

*   Here by default, the `directory_path` is the current working directory (CWD) unless specified by the user.

## Output

1. For <i>Current Working Directory</i> [DEFAULT] [String Representation = `False`]

```python
>>> from directory_tree import display_tree
>>> display_tree()

$ Operating System : Windows
$ Path : C:\Personal\Work\Directory-Tree\Test\Main Directory

*************** Directory Tree ***************

Main Directory/
├── Directory 1/
│   └── Directory 2/
│       ├── Directory 3/
│       │   └── Directory 4/
│       │       └── Hello World.txt
│       └── Say World.txt
├── Directory A/
│   └── Hmm.txt
├── directory-tree-print.cpp
├── letseee.txt
└── printTree.exe

```

2. For <i>User Specified Directory</i> [Argument] [String Representation = `True`]

```python
>>> from directory_tree import display_tree
>>> stringRepresentation = display_tree('C:\Personal\Work\Directory-Tree\Test\Main Directory', string_rep = True)
>>> print(stringRepresentation)

$ Operating System : Windows
$ Path : C:\Personal\Work\Directory-Tree\Test\Main Directory

*************** Directory Tree ***************

Main Directory/
├── Directory 1/
│   └── Directory 2/
│       ├── Directory 3/
│       │   └── Directory 4/
│       │       └── Hello World.txt
│       └── Say World.txt
├── Directory A/
│   └── Hmm.txt
├── directory-tree-print.cpp
├── letseee.txt
└── printTree.exe

```

## Developing `Directory Tree`

To install `directory_tree`, along with the tools you need to develop and run tests, and execute the following in your virtualenv:

```bash
$ pip install -e .[dev]
```

## Security & Bugs

*   `Directory Tree` uses recursion. It will raise a `RecursionError` on really deep directory trees.
*   As the tree is lazily evaluated, it should behave well on really wide directory trees. Immediate children of a given directory are not lazily evaluated, though. It would be prompted to the last.
*   Currently `Directory Tree` doesn't support the functionality of ignoring files/directories in a particular path, so will print every files-directories present in the given path.
*   If you're a Windows user, it is always advised to use `\\` instead of `\` in the address as using `\` might catchup escape sequences and corrupt the address string.
## Contact Author

Name : __Rahul Bordoloi__ <br>
Website : https://rahulbordoloi.me <br>
Email : rahulbordoloi24@gmail.com <br>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/rahulbordoloi/)
