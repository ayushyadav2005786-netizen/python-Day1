# Write a python program to print the contents of a directory using the os module search online for the function which does that.

import os

# Option 1: List current directory contents
contents = os.listdir()
print("Current directory contents:")
for item in contents:
    print(item)

# Option 2: List a specific directory
path = "C:/Users/YourName/Documents"
try:
    contents = os.listdir(path)
    print(f"\nContents of {path}:")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("Error: Directory not found")
except PermissionError:
    print("Error: No permission to access this directory")
