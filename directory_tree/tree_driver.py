# Importing Necessary Libraries & Modules
from __future__ import annotations
from os import getcwd
from pathlib import Path
from platform import system
from traceback import format_exc
from typing import Any, List, Union
from directory_tree.tree_calculator import DirectoryPath


# Class for Displaying Directory Tree
class DisplayTree:

    # Constructor
    def __init__(
            self,
            dirPath: str='',
            stringRep: bool=False,
            header: bool=False,
            maxDepth: float=float('inf'),
            showHidden: bool=False,
            ignoreList: List[str]=None,
            onlyFiles: bool=False,
            onlyDirs: bool=False,
            sortBy: int=0,
            raiseException: bool=False,
            printErrorTraceback: bool=False
    ) -> None:
        """
        :param dirPath: Root Path of Operation. By Default, Refers to the Current Working Directory
        :param stringRep: Boolean Flag for Direct Console Output or a String Return of the Same. By Default, It Gives out Console Output
        :param header: Boolean Flag for Displaying [OS & Directory Path] Info in the Console. Not Applicable if `string_rep=True`
        :param maxDepth: Max Depth of the Directory Tree. By Default, It goes upto the Deepest Directory/File
        :param showHidden: Boolean Flag for Returning/Displaying Hidden Files/Directories if Value Set to `True`
        :param ignoreList: List of File and Directory Names or Patterns to Ignore
        :param onlyFiles: Boolean Flag to Display Only Files
        :param onlyDirs: Boolean Flag to Display Only Directories
        :param sortBy: Sorting order. Possible Options: [0 - Default, 1 - Files First, 2 - Directories First]
        :param raiseException: Boolean Flag to Raise Exception. By Default, It Doesn't Raise Exception
        :param printErrorTraceback: Boolean Flag to Print Error Traceback. By Default, It Doesn't Print Error Traceback
        :return: None if `string_rep=False` else (str)ing Representation of the Tree
        """

        # Instance Variables
        self.dirPath: str = dirPath
        self.stringRep: bool = stringRep
        self.header: bool = header
        self.maxDepth: float = maxDepth
        self.showHidden: bool = showHidden
        self.ignoreList: List[str] = ignoreList
        self.onlyFiles: bool = onlyFiles
        self.onlyDirs: bool = onlyDirs
        self.sortBy: int = sortBy
        self.raiseException: bool = raiseException
        self.printErrorTraceback: bool = printErrorTraceback

    # Destructor
    def __del__(self):

        del self.dirPath, self.stringRep, self.header, self.maxDepth, self.showHidden, self.ignoreList, \
            self.onlyFiles, self.onlyDirs, self.sortBy, self.raiseException, self.printErrorTraceback

    # Display Function to Print Directory Tree
    @classmethod
    def display(cls, *args: List[Any], **kwargs: dict[str, Any]) -> Union[str, None]:

        # Instance Creation and Display Tree
        instance: DisplayTree = cls(
            *args, **kwargs
        )

        return instance.displayTree()

    # `Display Tree` Method to Print Directory Tree
    def displayTree(self) -> Union[str, None]:

        try:

            # Check for Default Argument
            if self.dirPath:
                self.dirPath: Path = Path(self.dirPath)
            else:
                self.dirPath: Path = Path(getcwd())

            # Build Directory Tree
            paths: str = DirectoryPath.buildTree(
                root=self.dirPath,
                maxDepth=self.maxDepth,
                showHidden=self.showHidden,
                ignoreList=self.ignoreList,
                onlyFiles=self.onlyFiles,
                onlyDirectories=self.onlyDirs,
                sortBy=self.sortBy
            )

            # Check for String Representation
            if self.stringRep:

                # String Representation
                stringOutput: str = str()
                for path in paths:
                    stringOutput += path.displayPath() + '\n'
                return stringOutput

            else:
                # Just Console Print
                if self.header:
                    print(f'''
$ Operating System : {system()}
$ Path : {Path(self.dirPath)}

{'*' * 15} Directory Tree {'*' * 15}
''')

                for path in paths:
                    print(path.displayPath())

        except Exception as expMessage:

            # Exception Handling
            if self.printErrorTraceback:
                print(f'Traceback Details:: {format_exc()}')
            errorMsg: str = f'Exception Occurred! Failed to Generate Tree:: {type(expMessage).__name__}: {expMessage}'
            if self.raiseException:
                raise type(expMessage)(errorMsg)
            else:
                print(errorMsg)
