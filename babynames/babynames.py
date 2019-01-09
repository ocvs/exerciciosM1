#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
from pprint import pprint
import re
from glob import glob
from collections import defaultdict

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    with open(filename) as f:
        html_text = f.read()

    if html_text:
        year = re.findall(r'Popularity in (\d{4})', html_text)
        data_list = re.findall(r'<td>(.*?)<\/td>', html_text)

    final_list = year
    dict_list = defaultdict(list)

    for name_m, name_f, rank in zip(data_list[1::3], data_list[2::3], data_list[0::3]):
        final_list.extend([name_m + " " + rank, name_f + " " + rank])
        dict_list[int(rank)].extend([name_m, name_f])

    return dict_list, final_list


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    sys.argv = ['--summaryfile', glob('*.html')]
    args = sys.argv

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        print(args[1])
        summary = True
        del args[0]

        # +++your code here+++
        # For each filename, get the names, then either print the text output
        # or write it to a summary file
    lists = []

    for file in args[0]:
        lists_extract = extract_names(file)
        lists.append(lists_extract)
        pprint(sorted(lists_extract[1]))
        pprint(lists_extract[0])

    for list_ in lists:
        sys.stdout = open(list_[1][0] + '.txt', 'w')
        print("Popularity in " + list_[1][0])
        pprint(sorted(list_[1]))
        pprint(list_[0])
        sys.stdout.close()


if __name__ == '__main__':
    main()
