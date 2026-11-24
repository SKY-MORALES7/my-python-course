import os # os(operating-system) module, provides a way for python programs to interact with the operating system

# when filedetecttext.txt file is next to filedetect.py 


# file_path = "filedetecttext.txt"

# if os.path.exists(file_path):
#     print(f'the location \'{file_path}\' exists')

# else:
#     print(f"That location '{file_path}'doesn't exist")

# howeever when filedetecttext.txt file is moved to filedetectdir we do this
# Relative file paths
file_path = "filedetectdir/filedetecttext.txt"

if os.path.exists(file_path):
    print(f'the location \'{file_path}\' exists')

else:
    print(f"That location '{file_path}'doesn't exist")

