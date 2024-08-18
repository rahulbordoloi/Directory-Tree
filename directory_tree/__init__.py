# Importing Necessary Libraries & Modules
from typing import Callable, List, Union
from warnings import warn
from .tree_driver import DisplayTree
from .version import __version__

# Alias for `DisplayTree.display`
DisplayTree: Callable[..., Union[str, None]] = DisplayTree.display


# Deprecated `display_tree` Function [ Till v0.0.4 ]
def display_tree(
        dir_path: str='',
        string_rep: bool=False,
        header: bool=False,
        max_depth: float=float('inf'),
        show_hidden: bool=False,
        ignore_list: List[str]=None,
        only_files: bool=False,
        only_dirs: bool=False,
        sort_by: int=0,
        raise_exception: bool=False,
        print_error_traceback: bool=False
) -> Union[str, None]:

    warn(
        message='The `display_tree` Function is Deprecated and will be Removed in a Future Release. '
        'Please use `DirectoryTree` Instead. End of Life Date is "31st December 2024".',
        category=DeprecationWarning,
        stacklevel=2
    )

    return DisplayTree(
        dirPath=dir_path,
        stringRep=string_rep,
        header=header,
        maxDepth=max_depth,
        showHidden=show_hidden,
        ignoreList=ignore_list,
        onlyFiles=only_files,
        onlyDirs=only_dirs,
        sortBy=sort_by,
        raiseException=raise_exception,
        printErrorTraceback=print_error_traceback
    )
