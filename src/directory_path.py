# Importing Libraries
from __future__ import annotations
from os import stat
from pathlib import Path
from stat import FILE_ATTRIBUTE_HIDDEN
from typing import Any, Dict, List, Union


# Class for Directory Tree Path
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

        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name

    # Building the Tree [Directories - Nodes]
    @classmethod
    def buildTree(cls, root: Path, parent: Union[DirectoryPath, None]=None, isLast: bool=False, 
                  maxDepth: float=float('inf'), showHidden: bool=False, ignoreList: List[str]=None,
                  onlyFiles: bool=False, onlyDirs: bool=False) -> str:

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
            if not any(entity == entityPath.name or entity == str(entityPath.relative_to(root)) for entity in ignoreList)
        ]

        # Filtering out based on `onlyFiles` and `onlyDirs` Flags
        if onlyFiles:
            children: List[Path] = [
                entityPath for entityPath in children if entityPath.is_file()
            ]
        elif onlyDirs:
            children: List[Path] = [
                entityPath for entityPath in children if entityPath.is_dir()
            ]

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
                    onlyDirs=onlyDirs
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

        try:
            return bool(stat(path).st_file_attributes & FILE_ATTRIBUTE_HIDDEN) or path.stem.startswith('.')
        except:
            return path.stem.startswith('.')

    # Displaying the Tree Path [Directories-Nodes]
    def displayPath(self) -> str:

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
            parent: str = parent.parent

        return ''.join(reversed(parts))

