# Importing Necessary Libraries & Modules
from argparse import ArgumentParser
from directory_tree.tree_driver import display_tree


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

    # `directory` Argument
    parser.add_argument(
        'directory',
        nargs='?',
        default='.',
        help='Root Path to Display. Uses current directory by default'
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
        help='Sorting Order. Possible Options: 0 - Default, 1 - Files First, 2 - Directories First'
    )

    # -------------------------------- Parsing Arguments -------------------------------- #
    arguments: ArgumentParser.parse_args = parser.parse_args()

    # Displaying Directory Tree
    display_tree(
        dir_path=arguments.directory,
        header=arguments.header,
        max_depth=arguments.max_depth,
        ignore_list=arguments.ignore_list,
        show_hidden=arguments.show_hidden,
        only_files=arguments.only_files,
        only_dirs=arguments.only_dirs,
        sort_by=arguments.sort_by
    )

