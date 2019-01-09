#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import re
import sys
from pprint import pprint
from collections import defaultdict


def mimic_dict(filename):
    """ deixei código comentado para demonstrar algumas tentativas antes de ver o video do HB
   o mais interessante foi que, usando o
   file = open(filename).read()
   depois
   (alt1) words = ''.join(re.sub(' +', ' ', file).splitlines()).split(' ')
    ( alt 2) words = ''.join(file.splitlines()).split(' ')
   dava erro
   Traceback (most recent call last):
     File "E:/trabalhos/Python/google-python-exercises/basic/mimic.py", line 101, in <module>
       main()
     File "E:/trabalhos/Python/google-python-exercises/basic/mimic.py", line 96, in main
       dict = mimic_dict(sys.argv[1])
     File "E:/trabalhos/Python/google-python-exercises/basic/mimic.py", line 77, in mimic_dict
       mimic_d[k].append(v)
   AttributeError: 'str' object has no attribute 'append'

   words_tuples = []
   i = 0
   while i < len(words) - 1:
       words_tuples.append((words[i], words[i + 1]))
       i += 1
       mimic_d = collections.defaultdict(list)
   for k, v in words_tuples:
     mimic_d[k].append(v)
     """
    # o exercicio foi feito depois da aula do HB. Tentei fazer um misto de "ajuda do video" X quebrar a cabaça
    # assim o aprendizado foi melhor que só copiar do HB, rss

    with open(filename) as f:
        words = f.read().split()

    pprint(words)
    first, last, empty = words[0], words[-1], ''

    # depois que achei o erro da lista, foi possivel manter o defaultdict
    mimic_d = defaultdict(list, {empty: [first], last: [empty]})

    for k, v in zip(words[:-1], words[1:]):
        mimic_d[k].append(v)

    return mimic_d


def print_mimic(mimic_d, word):

    frase = []

    for n in range(200):
        x = mimic_d.get(word, '')
        w = random.choice(x)
        frase.append(w)
        word = w

    print(' '.join(frase))

    return None


# Provided main(), calls mimic_dict() and mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py file-to-read')
        sys.exit(1)

    dict = mimic_dict(sys.argv[1])
    print_mimic(dict, '')


if __name__ == '__main__':
    main()
