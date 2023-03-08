import os


#Task 1
#Write a Python program to list only directories, files and all directories, files in a specified path.

path = "C:\\Users\\shohi\\OneDrive\\Документы\\uni\\sem2\\pp2"


print("Directories:")
for dir in os.listdir(path):
    if os.path.isdir(os.path.join(path, dir)):
        print(dir)


print("\nFiles:")
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        print(file)


#Task 2
#Write a Python program to check for access to a specified path. Test the existence, readability, 
#writability and executability of the specified path

import os

path = input("Enter the path to check: ")

if os.path.exists(path):
    print(f"{path} exists")
    if os.access(path, os.R_OK):
        print(f"{path} is readable")
    else:
        print(f"{path} is not readable")
    if os.access(path, os.W_OK):
        print(f"{path} is writable")
    else:
        print(f"{path} is not writable")
    if os.access(path, os.X_OK):
        print(f"{path} is executable")
    else:
        print(f"{path} is not executable")
else:
    print(f"{path} does not exist")

#Task 3
#Write a Python program to test whether a given path exists or not. 
#If the path exist find the filename and directory portion of the given path

import os

path = input("Enter a path: ")

if os.path.exists(path):
    print("Path exists.")
    filename = os.path.basename(path)
    directory = os.path.dirname(path)
    print(f"Filename: {filename}")
    print(f"Directory: {directory}")
else:
    print("Path does not exist.")

#Task 4
#Write a Python program to count the number of lines in a text file.    
file_path = input("Enter a path: ")

with open(file_path, 'r') as file:
    lines = file.readlines()
    num_lines = len(lines)
    print("The file contains", num_lines, "lines.")


#Task 5
# Write a Python program to write a list to a file.
file_path = input("Enter a path: ")
my_list = ["Hello", "world", "this", "is", "a", "list"]


with open(file_path, 'w') as file:
    for item in my_list:
        file.write("%s\n" % item)

#Task 6 
# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import string

letters = list(string.ascii_uppercase)

for letter in letters:
    filename = letter + ".txt"
    with open(filename, 'w') as file:
        file.write("Текст для проверки %s." % letter)
    print("Файлы созданы", filename)


#Task 7
#Write a Python program to copy the contents of a file to another file

source_file_path = input("Enter a path: ")
destination_file_path = input("Enter a path: ")


with open(source_file_path, 'r') as source_file:
    file_contents = source_file.read()

with open(destination_file_path, 'w') as destination_file:
    destination_file.write(file_contents)
print("File copied successfully!")


#Task 8
# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

file_path = input("Enter a path: ")

if os.path.exists(file_path) and os.access(file_path, os.R_OK) and os.access(file_path, os.W_OK):
    os.remove(file_path)
    print("File deleted successfully.")
else:
    print("Unable to delete the file. Please check if the file exists and has read/write access.")


