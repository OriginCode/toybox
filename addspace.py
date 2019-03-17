#!/usr/bin/python3

__author__ = "OriginCode"

src = input('Input original text:\n> ')
out = ""
for x in range(len(src)):
    out = out + src[x] + " "
out = out[0:len(out) - 1]
print(out)
