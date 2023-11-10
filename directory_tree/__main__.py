import argparse

from directory_tree import display_tree


parser = argparse.ArgumentParser(
    prog='Directory-Tree',
    description='Python implementation of basic elements of `tree`',
    epilog=(
"""
A minimal implementation of `tree` for those who can pip install but don't
have sudo privileges for `sudo apt install tree`.
"""
    ),
)

parser.add_argument('directory', nargs='?', default='.',
                    help='Root path to display.  Uses current directory by default.')
parser.add_argument('--header', action='store_true',
                    help='Display [OS & Directory Path] Info.')
parser.add_argument('-L', '--max-depth', default=2, type=int,
                    help='Max depth of the directory tree.  Defaults to deepest directory.')
parser.add_argument('-a', '--show-hidden', action='store_true',
                    help='Show hidden files and directories.')
parser.add_argument('-I', '--ignore-list', nargs='*',
                    help='List of File and Directory Names or Patterns to Ignore')
args=parser.parse_args()

display_tree(
    dir_path=args.directory,
    header=args.header,
    max_depth=args.max_depth,
    ignore_list=args.ignore_list,
    show_hidden=args.show_hidden,
)
