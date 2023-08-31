# Directory Tree Package

[![Setup Automated](https://img.shields.io/badge/setup-automated-blue?logo=gitpod)](https://gitpod.io/from-referrer/)
![Test passing](https://img.shields.io/badge/Tests-passing-brightgreen.svg)
![Python Version](https://img.shields.io/badge/python-3.6+-brightgreen.svg)
[![PyPI version](https://badge.fury.io/py/directory-tree.svg)](https://badge.fury.io/py/directory-tree)
![Last Commit](https://img.shields.io/github/last-commit/rahulbordoloi/Directory-Tree?style=flat-square)
[![Open Source Love png2](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)


## About 

Want to Display your Project/Current Working Directory as a Neat Tree? No Worries!

`Directory Tree` is a simple python utility package that displays out the Tree Structure of a User Defined Directory.

<b><i> Currently Available for All Platforms.  </i></b>

## Installation

Run the Following Command on your Terminal to Install `directory_tree`: 

1 .  Installing the Package using `pip`:
```bash
pip install directory_tree
```
OR

```bash
pip3 install directory_tree
```

2 . Cloning the Repository:

```bash
git clone https://github.com/rahulbordoloi/Directory-Tree/
cd Directory-Tree
pip install -e .
```

## Usage

<h4> Function Signature </h4>

```python
display_tree(dir_path: str = '', string_rep: bool=False, header: bool=False, max_depth: float=float("inf"), show_hidden: bool=False, ignore_list: list=None)
```

<h4> Arguments Description </h4>

| __Parameters__ | __Description__                                                                                                 |
|    ---         |-----------------------------------------------------------------------------------------------------------------|
| __dir_path__ | Root Path of Operation. By Default, Refers to the Current Working Directory.                                    |
| __string_rep__ | Boolean Flag for Direct Console Output or a String Return of the Same. By Default, It Gives out Console Output. |
| __header__ | Boolean Flag for Displaying [OS & Directory Path] Info in the Console. Not Applicable if `string_rep=True`.     |
| __max_depth__ | Max Depth of the Directory Tree. By Default, It goes upto the Deepest Directory/File.                           |
| __show_hidden__ | Boolean Flag for Returning/Displaying Hidden Files/Directories if Value Set to `True`.                          |
| __ignore_list__ | List of File and Directory Names or Patterns to Ignore.                                                         |


Run this Script in Order to Print out the Tree Structure of a User-Defined Directory `DirectoryPath`!

```python
# Importing Libraries
from directory_tree import display_tree

# Main Method
if __name__ == '__main__':
    display_tree(DirectoryPath)
```

*   Here by default, the `DirectoryPath` is the current working directory (CWD) unless specified by the user.

## Output Examples

Sample Directory Tree -

![SampleDirectoryTree.png](https://github.com/rahulbordoloi/Directory-Tree/blob/main/images/SampleDirectoryTree.png?raw=true)

NOTE - Here, `letseee.txt` (File) and `Directory 4/` (Directory) are **HIDDEN** in Nature.

1. For <i>Current Working Directory</i> with Argument [Header Info = `False`]

```python
from directory_tree import display_tree
display_tree(header=True)
```

![CWDwithHeader.png](https://github.com/rahulbordoloi/Directory-Tree/blob/main/images/CWDwithHeader.png?raw=true)

2. For <i>User Specified Directory</i> with Arguments [String Representation = `True`, Show Hidden Entities = `True`]

```python
from directory_tree import display_tree
customPath = 'D:\Work\Python Packages Maintainence\Directory-Tree\Test\Main Directory'
stringRepresentation = display_tree(customPath, string_rep=True, show_hidden=True)
print(stringRepresentation)
```

![UserSpecifiedDirectoryStrRepShowHidden.png](https://github.com/rahulbordoloi/Directory-Tree/blob/main/images/UserSpecifiedDirectoryStrRepShowHidden.png?raw=true)

3. For <i>Current Working Directory</i> with Argument [Max Depth = `2`]

```python
from directory_tree import display_tree
display_tree(max_depth=2)
```

![UserSpecifiedDirectoryMaxDep.png](https://github.com/rahulbordoloi/Directory-Tree/blob/main/images/UserSpecifiedDirectoryMaxDep.png?raw=true)


## Developing `Directory Tree`

To install `directory_tree`, along with the tools you need to develop and run tests, and execute the following in your virtualenv:

```bash
$ pip install -e .[dev]
```

## Security & Probable Bugs

*   `Directory Tree` uses recursion. It will raise a `RecursionError` on really deep directory trees.
*   As the tree is lazily evaluated, it should behave well on really wide directory trees. Immediate children of a given directory are not lazily evaluated, though. It would be prompted to the last.
*   If you're a Windows user, it is always advised to use `\\` instead of `\` in the address as using `\` might catchup escape sequences and corrupt the address string.

## Contact Author

Name : __Rahul Bordoloi__ <br>
Website : https://rahulbordoloi.me <br>
Email : rahulbordoloi24@gmail.com <br>

Made with <span style="color: #e25555;">&#9829;</span> in Python!

