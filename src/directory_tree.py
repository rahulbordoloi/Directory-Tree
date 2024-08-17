# Importing Libraries
from os import getcwd
from pathlib import Path
from platform import system
from typing import List, Union
from directory_path import DirectoryPath


# Display Function to Print Directory Tree
def display_tree(
        dir_path: str='',
        string_rep: bool=False,
        header: bool=False,
        max_depth: float=float('inf'),
        show_hidden: bool=False,
        ignore_list: List[str]=None
) -> Union[str, None]:

    """
    :param dir_path: Root Path of Operation. By Default, Refers to the Current Working Directory
    :param string_rep: Boolean Flag for Direct Console Output or a String Return of the Same. By Default, It Gives out Console Output
    :param header: Boolean Flag for Displaying [OS & Directory Path] Info in the Console. Not Applicable if `string_rep=True`
    :param max_depth: Max Depth of the Directory Tree. By Default, It goes upto the Deepest Directory/File
    :param show_hidden: Boolean Flag for Returning/Displaying Hidden Files/Directories if Value Set to `True`
    :param ignore_list: List of File and Directory Names or Patterns to Ignore
    :return: None if `string_rep=False` else (str)ing Representation of the Tree
    """

    try:

        # Check for Default Argument
        if dir_path:
            dir_path: Path = Path(dir_path)
        else:
            dir_path: Path = Path(getcwd())

        # Build Directory Tree
        paths: str = DirectoryPath.buildTree(
            root=dir_path,
            maxDepth=max_depth,
            showHidden=show_hidden,
            ignoreList=ignore_list
        )

        # Check for String Representation
        if string_rep:

            # String Representation
            stringOutput: str = str()
            for path in paths:
                stringOutput += path.displayPath() + '\n'
            return stringOutput

        else:
            # Just Console Print
            if header:
                print(f'''
$ Operating System : {system()}
$ Path : {Path(dir_path)}
    
{'*' * 15} Directory Tree {'*' * 15}
''')

            for path in paths:
                print(path.displayPath())

    except Exception as expMessage:
        print(f'Exception Occurred! Failed to Generate Tree:: {type(expMessage).__name__}: {expMessage}')

