#!/usr/bin/python3

src = input('Input original text:\n> ')
out = ""

for x in range(len(src)):
    w = src[len(src) - x - 1]
    out = out + w

print(out)