# Importing Libraries
from __future__ import annotations
from fnmatch import fnmatch
from os import stat
from pathlib import Path
from stat import FILE_ATTRIBUTE_HIDDEN
from typing import List, Union


# Class for Calculating Directory Tree Path
class DirectoryPath:
    """
    Python Utility Package that Displays out the Tree Structure of a Particular Directory.
    @author : rahulbordoloi
    """

    # Class Variables [Directions]
    displayNodePrefixMiddle: str = '├──'
    displayNodePrefixLast: str = '└──'
    displayParentPrefixMiddle: str = '    '
    displayParentPrefixLast: str = '│   '

    # Constructor
    def __init__(self, path: Path, parentPath: Union[DirectoryPath, None]=None, isLast: bool=False) -> None:

        # Instance Variables [Status of Parent-Node Files]
        self.path: Path = Path(path)
        self.parent: DirectoryPath = parentPath
        self.isLast: bool = isLast
        if self.parent:
            self.depth: int = self.parent.depth + 1
        else:
            self.depth: int = 0

    # Destructor
    def __del__(self) -> None:
        del self.path, self.parent, self.isLast, self.depth

    # Displaying Names of the Nodes [Parents / Inner Directories]
    @property
    def displayName(self) -> str:
        """
        Method to Display the Name of the Nodes [Parents / Inner Directories]
        """

        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name

    # Building the Tree [Directories - Nodes]
    @classmethod
    def buildTree(cls, root: Path, parent: Union[DirectoryPath, None]=None, isLast: bool=False,
                  maxDepth: float=float('inf'), showHidden: bool=False, ignoreList: List[str]=None,
                  onlyFiles: bool=False, onlyDirectories: bool=False, sortBy: int=0) -> str:
        """
        Method to Build the Tree Structure of the Directory
        :param root: Root Path of the Directory
        :param parent: Parent Directory Path
        :param isLast: Boolean Flag for Last Node
        :param maxDepth: Max Depth of the Tree
        :param showHidden: Boolean Flag for Displaying Hidden Files/Directories
        :param ignoreList: List of Files/Directories to Ignore
        :param onlyFiles: Boolean Flag for Displaying Only Files
        :param onlyDirectories: Boolean Flag for Displaying Only Directories
        :param sortBy: Sorting Order of the Files / Directory
        :return: String Representation of the Tree
        """

        # Resolving `Ignore List`
        if not ignoreList:
            ignoreList: List[str] = []

        # Generator Method to Generate Tree
        root: Path = Path(root)
        rootDirectoryDisplay: DirectoryPath = cls(
            path=root,
            parentPath=parent,
            isLast=isLast
        )
        yield rootDirectoryDisplay

        ## Taking out the List of Children [Nodes] Files/Directories
        children: List[Path] = sorted(
            list(entityPath for entityPath in root.iterdir()), key=lambda s: str(s).lower()
        )

        ## Checking for Hidden Entities Flag
        if not showHidden:
            children: List[Path] = [
                entityPath for entityPath in children if not cls._hiddenFilesFiltering_(entityPath)
            ]

        # Filter out Entities (Files and Directories) Specified in the `ignore_list`
        children: List[Path] = [
            entityPath for entityPath in children
            if not any(
                fnmatch(str(entityPath.relative_to(root)), entity) or fnmatch(entityPath.name, entity) for entity in ignoreList
            )
        ]

        # Filtering out based on `onlyFiles` and `onlyDirectories` Flags
        if onlyFiles:
            children: List[Path] = [
                entityPath for entityPath in children if entityPath.is_file()
            ]
        elif onlyDirectories:
            children: List[Path] = [
                entityPath for entityPath in children if entityPath.is_dir()
            ]
        if onlyFiles and onlyDirectories:
            raise AttributeError('Only One of `onlyFiles` and `onlyDirectories` Flags can be Set to `True`')

        # Sorting based on `sortBy` Flag [ 1 - Files First, 2 - Directories First ]
        if sortBy == 1:
            children.sort(key=lambda s: (s.is_dir(), str(s).lower()))
        elif sortBy == 2:
            children.sort(key=lambda s: (not s.is_dir(), str(s).lower()))
        else:
            children.sort(key=lambda s: str(s).lower())

        countNodes: int = 1
        for path in children:
            isLast: bool = countNodes == len(children)
            if path.is_dir() and rootDirectoryDisplay.depth + 1 < maxDepth:
                yield from cls.buildTree(
                    root=path,
                    parent=rootDirectoryDisplay,
                    isLast=isLast,
                    maxDepth=maxDepth,
                    showHidden=showHidden,
                    ignoreList=ignoreList,
                    onlyFiles=onlyFiles,
                    onlyDirectories=onlyDirectories,
                    sortBy=sortBy
                )
            else:
                yield cls(
                    path=path,
                    parentPath=rootDirectoryDisplay,
                    isLast=isLast
                )
            countNodes += 1

    # Check Condition for Hidden Entities [Files / Directories]
    @classmethod
    def _hiddenFilesFiltering_(cls, path: Path) -> bool:
        """
        Method to Check for Hidden Files / Directories
        :param path: Path of the File / Directory
        """

        try:
            return bool(stat(path).st_file_attributes & FILE_ATTRIBUTE_HIDDEN) or path.stem.startswith('.')
        except (OSError, AttributeError):
            return path.stem.startswith('.')

    # Displaying the Tree Path [Directories-Nodes]
    def displayPath(self) -> str:
        """
        Method to Display the Path of the Tree [Directories-Nodes]
        :return: String Representation of the Path
        """

        # Check for Parent Directory Name
        if self.parent is None:
            return self.displayName

        # Checking for File-Name Prefix in Tree
        filenamePrefix: str = (
            DirectoryPath.displayNodePrefixLast if self.isLast else DirectoryPath.displayNodePrefixMiddle
        )

        # Adding Prefixes to Beautify Output [List]
        parts: List[str] = [f'{filenamePrefix} {self.displayName}']

        # Adding Prefixes up for Parent-Node Directories
        parent: DirectoryPath = self.parent
        while parent and parent.parent is not None:
            parts.append(
                DirectoryPath.displayParentPrefixMiddle if parent.isLast else DirectoryPath.displayParentPrefixLast
            )
            parent: Path = parent.parent

        return ''.join(reversed(parts))

