# Importing Module(s)
from src.directory_tree import display_tree


# Main Method
if __name__ == '__main__':

    # 1. Test for String Representation
    stringRepresentation = display_tree(string_rep=True)
    print(stringRepresentation)

    # 2. Test for Header in String Representation
    stringRepresentation = display_tree(string_rep=True, header=True)
    print(stringRepresentation)

    # 3. Test for Console-Print and Max Depth >> Actual Depth
    display_tree(max_depth=100)

    # 4. Test for Console-Print and Max Depth << Actual Depth
    display_tree(max_depth=-100)

    # 5. Test for Console-Print, Header for [OS, Path] Info and Not Show Hidden Files/Directories
    display_tree(header=True, max_depth=100, show_hidden=False)

    # 6. Test for Console-Print, Header for [OS, Path] Info and Show Hidden Files/Directories
    display_tree(max_depth=2, show_hidden=True)

