#!/usr/bin/python3

__author__ = "OriginCode"

import sys

src = sys.argv[1]
out = ""

for x in range(len(src)):
    w = src[len(src) - x - 1]
    out = out + w

print(out)