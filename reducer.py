#!/usr/bin/python

import sys

current_word = ''
current_count = 0

for line in sys.stdin:
    word, count = line.split()

    count = int(count)

    #if it is our first word, set current_word and _count
    if not len(current_word):
        current_word = word
        current_count = count
    else:
        #else, if new word is the same as the current one, then increment count
        if current_word == word:
            current_count += count
        else: #else, if new word is different, print the last word and its count, and set new word to the current
            print(f'{current_word} {current_count}')

            current_word = word
            current_count = count

#At the end, print the last word and its count.
print(f'{current_word} {current_count}')