# Write a Python program to read first n lines of a file.

with open("read.txt") as file:
 n = 3
 for i in range(n):
  print(file.readline())
  