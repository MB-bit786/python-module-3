# Write a python program to find the longest words.

with open("read.txt") as file:
    lines = file.readlines()
    longest_word = max(lines, key=len)
    print(longest_word)