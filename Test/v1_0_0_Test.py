# Importing Module(s)
from directory_tree import DisplayTree


# Main Method
if __name__ == '__main__':

    # 1. Test for String Representation
    stringRepresentation: str = DisplayTree(stringRep=True, sortBy=2)
    print(stringRepresentation)

    # 2. Test for Header in String Representation
    stringRepresentation: str = DisplayTree(stringRep=True, header=True)
    print(stringRepresentation)

    # 3. Test for Console-Print and Max Depth >> Actual Depth
    DisplayTree(maxDepth=1)

    # 4. Test for Console-Print, Header for [OS, Path] Info and Not Show Hidden Files/Directories
    DisplayTree(header=True, maxDepth=100, showHidden=False)

    # 5. Test for Console-Print, Header for [OS, Path] Info and Show Hidden Files/Directories
    DisplayTree(maxDepth=2, showHidden=True)

    # 6. Test for Ignore Files / Directories [Absolute Names]
    DisplayTree(maxDepth=4, showHidden=True, ignoreList=['Directory A', 'letseee.txt'])

    # 7. Test for Ignore Files / Directories [Absolute Names]
    DisplayTree(maxDepth=4, showHidden=True, ignoreList=['*.py'])

    # 8. Test for Only Files
    DisplayTree(showHidden=True, onlyFiles=True)

    # 9. Test for Only Directories
    DisplayTree(showHidden=True, onlyFiles=True, onlyDirs=True)

    # 10. Test for OnlyFiles and OnlyDirectories True Together [Raise Exception]
    DisplayTree(showHidden=True, onlyFiles=True, onlyDirs=True, raiseException=True)

    # 11. Test for OnlyFiles and OnlyDirectories True Together [Print Error Traceback]
    DisplayTree(showHidden=True, onlyFiles=True, onlyDirs=True, printErrorTraceback=True)

    # 12. Test for Sorting Order [Files First]
    DisplayTree(showHidden=True, sortBy=1)

