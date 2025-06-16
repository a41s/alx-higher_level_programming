#!/usr/bin/python3
for i in range(26):
    i = chr(i + 97)
    if (i != 'q' and i != 'e'):
        print("{:s}".format(i), end="")
