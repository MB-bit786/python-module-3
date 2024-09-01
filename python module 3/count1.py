#Write a Python program to count the frequency of words in a file.

with open("read.txt") as file:
    words = file.read().split()
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    print(count)