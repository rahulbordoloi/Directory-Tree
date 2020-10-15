# Importing Libraries
from pathlib import Path
import os
import platform


# Class Tree Path
class directory_path:

    """
    Python Utility Package that displays out the Tree Structure of a Particular Directory.
    @author : rahulbordoloi
    """

    # Constructor
    def __init__(self, path = None, parent_path = None, is_last = 0):

        # Class Variables [Directions]
        self.display_Node_Prefix_Middle = '├──'
        self.display_Node_Prefix_Last = '└──'
        self.display_Parent_Prefix_Middle = '    '
        self.display_Parent_Prefix_Last = '│   '
        
        # Class Variables [Status of Parent-Node Files]
        self.path = Path(str(path))
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
    def build_tree(cls, root, parent = None, is_last = False, criteria = None):

        ## Checking out for Root Directory for each Iteration
        root = Path(str(root))
        criteria = criteria or cls._default_criteria_

        # Yielding [Returning] Root Directory Name
        root_Directory_Display = cls(root, parent, is_last)
        yield root_Directory_Display

        ## Taking out the List of Children [Nodes] Files.
        children = sorted(list(path
                            for path in root.iterdir()
                            if criteria(path)),
                          key = lambda s: str(s).lower())
        
        ## Build the Tree
        countNodes = 1
        for path in children:
            is_last = countNodes == len(children)
            if path.is_dir():
                yield from cls.build_tree(path,
                                         parent = root_Directory_Display,
                                         is_last = is_last,
                                         criteria = criteria)
            else:
                yield cls(path, root_Directory_Display, is_last)
            countNodes += 1

    # Check Condition for Root Directory
    @classmethod
    def _default_criteria_(cls, path):
        return True

    # Displaying the Tree Path [Directories-Nodes]
    def displayPath(self):

        ## Check for Parent Directory Name
        if self.parent is None:
            return self.displayName

        filename_Prefix = (self.display_Node_Prefix_Last if self.is_last else self.display_Node_Prefix_Middle)

        ## Adding Prefixes to Beautify Output [List]
        parts = [f'{filename_Prefix} {self.displayName}']

        ## Adding Prefixes up for Parent-Node Directories
        parent = self.parent
        while parent and parent.parent is not None:
            parts.append(self.display_Parent_Prefix_Middle if parent.is_last else self.display_Parent_Prefix_Last)
            parent = parent.parent

        return ''.join(reversed(parts))


# Display Function to Print Directory Tree
def display_tree(dir_path = '', string_rep = False):

    # Check for Default Argument
    if dir_path:
        dir_path = Path(dir_path)
    else:
        dir_path = Path(os.getcwd())

    # Check for String Representation
    if string_rep:

        # String Representation [True]
        stringOutput = str()
        paths = directory_path.build_tree(dir_path)
        for path in paths:
            stringOutput += path.displayPath() + "\n"
        return stringOutput

    else:
        # Just Console Print
        print(f'''
$ Operating System : {platform.system()}
$ Path : {Path(dir_path)}

{"*" * 15} Directory Tree {"*" * 15}
''')

        paths = directory_path.build_tree(dir_path)
        for path in paths:
            print(path.displayPath())

