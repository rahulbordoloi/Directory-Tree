import os
from src.directory_tree import display_tree

os.makedirs("dummy_dir/sub_dir1", exist_ok=True)
os.makedirs("dummy_dir/venv/bin", exist_ok=True)
os.makedirs("dummy_dir/__pycache__", exist_ok=True)

with open("dummy_dir/sub_dir1/file1.txt", "w") as f:
    f.write("Hello World 1")
    
with open("dummy_dir/sub_dir1/file2.txt", "w") as f:
    f.write("Hello World 2")
    
with open("dummy_dir/__pycache__/file3.pyc", "w") as f:
    f.write("Hello World 3")

# Display the directory tree, ignoring 'venv' and '__pycache__' directories
display_tree(dir_path='dummy_dir', ignore_dirs=['venv', '__pycache__'])