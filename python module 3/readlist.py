""" Write a Python program to read a file line by line and store it
into a list Write a Python program to read a file line by line
 store it into a variable."""

with open('read.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

