# Importing Necessary Libraries & Modules
from argparse import ArgumentParser
from directory_tree.tree_driver import DisplayTree
from .version import __version__


# CLI Function for Arguments Support for Directory Tree
def directoryTreeCli() -> None:
    """
    Function to Support Command Line Arguments for Directory Tree
    """

    # -------------------------------- Argument Parser -------------------------------- #
    parser: ArgumentParser = ArgumentParser(
        prog='directory-tree',
        description='Utility Package that Displays out the Tree Structure of a Particular Directory',
        epilog=('''
Utility Package that Displays out the Tree Structure of a Particular Directory. 
Also acts as a minimal implementation of `tree` for those who can pip install but don't have sudo privileges for `sudo apt install tree`.
'''),
    )

    # -------------------------------- Arguments -------------------------------- #

    parser.add_argument(
        '--version',
        '-v',
        action='store_true',
        help='Shows the version of the `directory_tree` package'
    )

    # `directory` Argument
    parser.add_argument(
        'directory',
        nargs='?',
        default=None,
        help='Root Path to Display. Uses Current Directory by Default'
    )

    # `header` Argument
    parser.add_argument(
        '--header',
        action='store_true',
        default=False,
        required=False,
        help='Display [OS & Directory Path] Info.'
    )

    # `max-depth` Argument
    parser.add_argument(
        '-L',
        '--max-depth',
        default=float('inf'),
        type=int,
        required=False,
        help='Max Depth of the Directory Tree. Defaults to Deepest Directory'
    )

    # `show-hidden` Argument
    parser.add_argument(
        '-a',
        '--show-hidden',
        action='store_true',
        default=False,
        required=False,
        help='Show Hidden Files and Directories'
    )

    # `ignore-list` Argument
    parser.add_argument(
        '-I',
        '--ignore-list',
        nargs='*',
        required=False,
        help='List of File and Directory Names or Patterns to Ignore'
    )

    # `only-files` Argument
    parser.add_argument(
        '-f',
        '--only-files',
        action='store_true',
        default=False,
        required=False,
        help='Display Only Files'
    )

    # `only-dirs` Argument
    parser.add_argument(
        '-d',
        '--only-dirs',
        action='store_true',
        default=False,
        required=False,
        help='Display Only Directories'
    )

    # `sort-by` Argument
    parser.add_argument(
        '--sort-by',
        choices=[0, 1, 2],
        default=0,
        nargs='?',
        required=False,
        type=int,
        help='Sorting Order. Possible Options: [0 - Default, 1 - Files First, 2 - Directories First]'
    )

    # `raise-exception` Argument
    parser.add_argument(
        '--raise-exception',
        action='store_true',
        default=False,
        required=False,
        help='Raise Exception if Any Error Occurs'
    )

    # `print-error-traceback` Argument
    parser.add_argument(
        '--print-error-traceback',
        action='store_true',
        default=False,
        required=False,
        help='Print Error Traceback if Any Error Occurs'
    )

    # -------------------------------- Parsing Arguments -------------------------------- #
    arguments: ArgumentParser.parse_args = parser.parse_args()

    # Displaying Version if Present
    if arguments.version:
        print(f'`directory_tree` Version: {__version__}')
        return

    # Displaying Directory Tree
    DisplayTree.display(
        dirPath=arguments.directory,
        header=arguments.header,
        maxDepth=arguments.max_depth,
        ignoreList=arguments.ignore_list,
        showHidden=arguments.show_hidden,
        onlyFiles=arguments.only_files,
        onlyDirs=arguments.only_dirs,
        sortBy=arguments.sort_by,
        raiseException=arguments.raise_exception,
        printErrorTraceback=arguments.print_error_traceback
    )
