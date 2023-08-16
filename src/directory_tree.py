# Importing Libraries
from pathlib import Path
import os
import platform
import stat

# Class for Directory Tree Path
class DirectoryPath:
    """
    Python Utility Package that Displays out the Tree Structure of a Particular Directory.
    """

    # Class Variables [Directions]
    display_Node_Prefix_Middle = '├──'
    display_Node_Prefix_Last = '└──'
    display_Parent_Prefix_Middle = '    '
    display_Parent_Prefix_Last = '│   '

    # Constructor
    def __init__(self, path, parent_path=None, is_last=0):
        # Instance Variables [Status of Parent-Node Files]
        self.path = Path(path)
        self.parent = parent_path
        self.is_last = is_last
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

    # Displaying Names of the Nodes [Parents/Inner Directories]
    @property
    def displayName(self):
        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name

    # Building the Tree [Directories-Nodes]
    @classmethod
    def build_tree(cls, root, parent=None, is_last=False, max_depth=float("inf"), show_hidden=False, ignore_list=[]):
        root = Path(root)
        rootDirectoryDisplay = cls(root, parent, is_last)
        yield rootDirectoryDisplay

        children = sorted(list(entityPath for entityPath in root.iterdir()), key=lambda s: str(s).lower())
        if not show_hidden:
            children = [entityPath for entityPath in children if not cls._hidden_files_filtering_(entityPath)]

        # Filter out entities (files and directories) specified in the ignore_list
        children = [entityPath for entityPath in children if not any(ign in str(entityPath) for ign in ignore_list)]

        countNodes = 1
        for path in children:
            is_last = countNodes == len(children)
            if path.is_dir() and rootDirectoryDisplay.depth + 1 < max_depth:
                yield from cls.build_tree(path, parent=rootDirectoryDisplay, is_last=is_last, max_depth=max_depth,
                                          show_hidden=show_hidden, ignore_list=ignore_list)
            else:
                yield cls(path, rootDirectoryDisplay, is_last)
            countNodes += 1

    # Check Condition for Hidden Entities [Files / Directories]
    @classmethod
    def _hidden_files_filtering_(cls, path) -> bool:
        try:
            return bool(os.stat(path).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)
        except:
            return path.stem.startswith(".")

    # Displaying the Tree Path [Directories-Nodes]
    def displayPath(self):
        # Check for Parent Directory Name
        if self.parent is None:
            return self.displayName

        # Checking for File-Name Prefix in Tree
        filenamePrefix = (
            DirectoryPath.display_Node_Prefix_Last if self.is_last else DirectoryPath.display_Node_Prefix_Middle)

        # Adding Prefixes to Beautify Output [List]
        parts = [f'{filenamePrefix} {self.displayName}']

        # Adding Prefixes up for Parent-Node Directories
        parent = self.parent
        while parent and parent.parent is not None:
            parts.append(
                DirectoryPath.display_Parent_Prefix_Middle if parent.is_last else DirectoryPath.display_Parent_Prefix_Last)
            parent = parent.parent

        return ''.join(reversed(parts))

# Display Function to Print Directory Tree
def display_tree(dir_path: str = '', string_rep: bool = False, header: bool = False, max_depth: float = float("inf"),
                 show_hidden: bool = False, ignore_list: list = []):
    """
    :param dir_path: Root Path of Operation. By Default, Refers to the Current Working Directory
    :param string_rep: Boolean Flag for Direct Console Output or a String Return of the Same. By Default, It Gives out Console Output
    :param header: Boolean Flag for Displaying [OS & Directory Path] Info in the Console. Not Applicable if `string_rep=True`
    :param max_depth: Max Depth of the Directory Tree. By Default, It goes upto the Deepest Directory/File
    :param show_hidden: Boolean Flag for Returning/Displaying Hidden Files/Directories if Value Set to `True`
    :param ignore_list: List of file and directory names or patterns to ignore
    :return: None if `string_rep=False` else (str)ing Representation of the Tree
    """

    try:
        # Check for Default Argument
        if dir_path:
            dir_path = Path(dir_path)
        else:
            dir_path = Path(os.getcwd())

        # Build Directory Tree
        paths = DirectoryPath.build_tree(dir_path, max_depth=max_depth, show_hidden=show_hidden, ignore_list=ignore_list)

        # Check for String Representation
        if string_rep:
            # String Representation
            stringOutput = str()
            for path in paths:
                stringOutput += path.displayPath() + "\n"
            return stringOutput

        else:
            # Just Console Print
            if header:
                print(f'''
$ Operating System : {platform.system()}
$ Path : {Path(dir_path)}
    
{"*" * 15} Directory Tree {"*" * 15}
''')

            for path in paths:
                print(path.displayPath())

    except Exception as expMessage:
        print(f"Exception Occurred! Failed to Generate Tree:: {expMessage}")
