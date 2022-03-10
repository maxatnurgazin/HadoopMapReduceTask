#!/usr/bin/python

import sys
from re import sub

#read lines from stdin one by one, and for each line
for line in sys.stdin:
    #use regex to remove unnecessary characters: [^\w\s] chooses chars that are not alphanumeric and space.
    line = sub('[^\w\s]', '', line).strip()

    #split the line and print it as a (key value) pair.
    for word in line.split():
        print(f'{word} 1')