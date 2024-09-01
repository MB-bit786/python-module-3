#Write a Python program to read last n lines of a file.

with open("read.txt") as file:
 n = 3
 lines = file.readlines()
 lines = lines[-n:]
 for line in lines:
  print(line)