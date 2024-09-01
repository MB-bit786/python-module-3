#Write a Python program to count the number of lines in a text file.

with open("read.txt") as file:
    lines = file.readlines()
    print(len(lines))   
