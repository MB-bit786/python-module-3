#Write a Python program to append text to a file and display  the text.

with open("append.txt","a") as file:
 file.write("hello world\n")
with open("append.txt") as file:
 print(file.read())
