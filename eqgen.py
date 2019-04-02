#!/usr/bin/python3

__author__ = "OriginCode"

import random

l = []
for x in range(1, 21):
    for y in range(1, 21):
        if x + y <= 20:
            l.append(str(x) + ' + ' + str(y))

for i in range(20):
    print(l[random.randrange(len(l) - 1)])
