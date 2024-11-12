# `show_tree.py`: Generating a Tree Format of Your Directory Structure

The `show_tree.py` script allows you to visualize the directory structure of the parent folder where this script is located. When you run the script, it will create a file named `directory_structure.txt` that contains a detailed, organized tree view of all files and subdirectories.

## What the Script Does

- **Explores the Directory**: It goes through each file and folder in the specified directory (by default, it will scan the current directory, `.`).

- **Excludes Unwanted Files/Folders**: The script ignores certain folders that you might not want in the output (like `.git` or `__pycache__`).

- **Creates a Tree Format**: It formats the directory listing into a tree-like structure, similar to what you’d see with a `tree` command in Unix-based systems.

- **Writes to a File**: The output is saved in `directory_structure.txt`, making it easy to view or share.

## How to Use `show_tree.py`

1. **Place the Script**: Save `show_tree.py` in the parent directory you want to explore.
   
2. **Run the Script**: Open a terminal in the directory and execute:

   ```bash
   python show_tree.py
