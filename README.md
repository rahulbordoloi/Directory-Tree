# Directory Tree Package

[![Setup Automated](https://img.shields.io/badge/setup-automated-blue?logo=gitpod)](https://gitpod.io/from-referrer/)
![Test passing](https://img.shields.io/badge/Tests-passing-brightgreen.svg)
![Python Version](https://img.shields.io/badge/python-3.6+-brightgreen.svg)
[![PyPI version](https://badge.fury.io/py/directory-tree.svg)](https://badge.fury.io/py/directory-tree)
![Last Commit](https://img.shields.io/github/last-commit/rahulbordoloi/Directory-Tree?style=flat-square)


## About 

Want to Display your Project / Current Working Directory as a Neat Tree? No Worries!

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
You can use either of the above methods to install `directory_tree`.

## Usage

<h3> Function Signature </h3>

```python
DisplayTree(
    dirPath: str='',
    stringRep: bool=False,
    header: bool=False,
    maxDepth: float=float('inf'),
    showHidden: bool=False,
    ignoreList: List[str]=None,
    onlyFiles: bool=False,
    onlyDirs: bool=False,
    sortBy: int=0
) -> Union[str, None]:
```

<h3> Arguments Description </h3>

| __Parameters__ | __CLI Parameters__ | __Description__                                                                                                |
|----------------|--------------------|----------------------------------------------------------------------------------------------------------------|
| __dirPath__    | `directory`        | Root Path of Operation. By Default, Refers to the Current Working Directory.                                   |
| __stringRep__  | N/A                | Boolean Flag for Direct Console Output or a String Return of the Same. By Default, It Gives out Console Output. |
| __header__     | `--header`         | Boolean Flag for Displaying [OS & Directory Path] Info in the Console. Not Applicable if `stringRep=True`.     |
| __maxDepth__   | `-L`, `--max-depth`| Max Depth of the Directory Tree. By Default, It goes upto the Deepest Directory/File.                          |
| __showHidden__ | `-a`, `--show-hidden`| Boolean Flag for Returning/Displaying Hidden Files/Directories if Value Set to `True`.                         |
| __ignoreList__ | `-I`, `--ignore-list`| List of File and Directory Names or Patterns to Ignore.                                                        |
| __onlyFiles__  | `-f`, `--only-files`| Boolean Flag to Display Only Files                                                                             |
| __onlyDirs__   | `-d`, `--only-dirs` | Boolean Flag to Display Only Directories                                                                       |
| __sortBy__     | `--sort-by`        | Sorting order. Possible Options: 0 - Default, 1 - Files First, 2 - Directories First                           |
| __raiseException__     | `--raise-exception`        | Boolean Flag to Raise Exception. By Default, It Doesn't Raise Exception                          |
| __printErrorTraceback__     | `--print-error-traceback`        | Boolean Flag to Print Error Traceback. By Default, It Doesn't Print Error Traceback                           |


<h3> Command Line </h3>

1. **Treating the Cloned Directory as Executable**  - <br>
   (Works if you've cloning privileges but not of installation. You can clone the repo, go to its root and run the below)
```bash
python directory_tree
```

OR

```bash
python -m directory_tree
```

Use the inline help for command-line options:
```
python directory_tree --help
```

2. **Treating the Package as Module** - <br>
   (You would need to install (`pip`) the Python Package in your system for the below to work)
```bash
directory_tree
```

Use the inline help for command-line options:
```bash
directory_tree --help
```

<h3> In Code </h3>

Example Script to Print out the Tree Structure of a User-Defined Directory `directoryPath`!

```python
# Importing Libraries
from directory_tree import DisplayTree

# Main Method
if __name__ == '__main__':
    DisplayTree(directoryPath)
```

*   Here by default, the `directoryPath` is the current working directory (CWD) unless specified by the user.

## Output Examples

Sample Directory Tree -

![SampleDirectoryTree.png](https://github.com/rahulbordoloi/Directory-Tree/blob/main/images/SampleDirectoryTree.png?raw=true)

NOTE - Here, `letseee.txt` (File) and `Directory 4/` (Directory) are **HIDDEN** in Nature.

1. For <i>Current Working Directory</i> with Argument [Header Info = `False`]

```python
from directory_tree import DisplayTree

DisplayTree(header=True)
```

![CWDwithHeader.png](https://github.com/rahulbordoloi/Directory-Tree/blob/main/images/CWDwithHeader.png?raw=true)

2. For <i>User Specified Directory</i> with Arguments [String Representation = `True`, Show Hidden Entities = `True`]

```python
from directory_tree import DisplayTree

customPath: str = 'Users/rahulbordoloi/Work/Python Packages Maintainence/Directory-Tree/Test/Main Directory'
stringRepresentation: str = DisplayTree(customPath, stringRep=True, showHidden=True)
print(stringRepresentation)
```

![UserSpecifiedDirectoryStrRepShowHidden.png](https://github.com/rahulbordoloi/Directory-Tree/blob/main/images/UserSpecifiedDirectoryStrRepShowHidden.png?raw=true)

3. For <i>Current Working Directory</i> with Argument [Max Depth = `2`]

```python
from directory_tree import DisplayTree

DisplayTree(maxDepth=2)
```

![UserSpecifiedDirectoryMaxDep.png](https://github.com/rahulbordoloi/Directory-Tree/blob/main/images/UserSpecifiedDirectoryMaxDep.png?raw=true)


## Developing `Directory Tree`

To install `directory_tree`, along with the tools you need to develop and run tests, use any of the following commands in your virtualenv:

```bash
pip install -e .[dev]
```

OR

```bash
pip install -e ".[dev]"
```

## Deprecation Notice
The `display_tree` function is deprecated and will be removed in a future release. Please use `DisplayTree` instead. The end-of-life date for `display_tree` is **December 31, 2024**. <br>

**Parameters Mapping Table** -

| __New Parameters__ | __Deprecated Parameters__  |
|----------------|----------------------------|
| __dirPath__    | dir_path                   |
| __stringRep__  | string_rep                 |
| __maxDepth__   | max_depth                  |
| __showHidden__ | show_hidden                |
| __ignoreList__ | ignore_list                |
| __onlyFiles__  | only_files                 |
| __onlyDirs__   | only_dirs                  |
| __sortBy__     | sort_by                    |
| __raiseException__     | raise_exception                    |
| __printErrorTraceback__     | print_error_traceback                    |


## Security & Probable Bugs

*   `Directory Tree` uses recursion. It will raise a `RecursionError` on really deep directory trees.
*   As the tree is lazily evaluated, it should behave well on really wide directory trees. Immediate children of a given directory are not lazily evaluated, though. It would be prompted to the last.
*   If you're a Windows user, it is always advised to use `\\` instead of `\` in the address as using `\` might catchup escape sequences and corrupt the address string.

## Contact Author

Name : __Rahul Bordoloi__ <br>
Website : https://rahulbordoloi.me <br>
Email : rahulbordoloi24@gmail.com <br>

Made with <span style="color: #e25555;">&#9829;</span> in Python!
