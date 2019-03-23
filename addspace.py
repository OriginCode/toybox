#!/usr/bin/python3

__author__ = "OriginCode"

import sys

src = sys.argv[1]
out = ""
for x in range(len(src)):
    out = out + src[x] + " "
out = out[0:len(out) - 1]
print(out)