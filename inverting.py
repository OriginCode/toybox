#!/usr/bin/python3

__author__ = "OriginCode"

src = input('Input original text:\n> ')
out = ""

for x in range(len(src)):
    w = src[len(src) - x - 1]
    out = out + w

print(out)