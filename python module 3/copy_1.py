# Write a Python program to copy the contents of a file to another file.

with open("read.txt") as file:
    with open("copy.txt", "w") as copy:
        copy.write(file.read())