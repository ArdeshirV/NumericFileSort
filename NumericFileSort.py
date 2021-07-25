#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  NumericFileSort.py - Sort input file by numeric prefix per each line of file.
#  Copyright 2021 ArdeshirV@protonmail.com, Licensed under GPLv3+
import sys
import os.path
import colors as c


def main(args):
    # Read source file contents from a file or stdin into lines list
    lines = []
    if len(args) <= 1:
        for line in sys.stdin:
            lines.append(line)
    else:
        source_file = 0
        try:
            if not os.path.isfile(args[1]):
                error(-2, "Source file dosen't exists!")
            source_file = open(args[1])
            lines = source_file.readlines()
        except:
            error(-1, "Failed to open source file!")
        finally:
            if source_file:
                source_file.close()

    # Retrieve numeric prefixes per lines into a list and then sort it
    data = []
    for line in lines:
        try:
            data.append([float(RetrieveNumericPrefix(line.lstrip())), line])
        except: continue
    data.sort()

    # Create sorted output and present on standard output
    new_data = ''
    for i in range(0, len(data)):
        new_data += data[i][1]
    print(new_data, end='')

    return 0


def RetrieveNumericPrefix(string):
    domain = 0
    for i in range(1, len(string)):
        if string[0:i].replace('.', '', 1).isdigit():
            domain = i
        else: break
    return string[0:domain]


def error(error_code, error_messsage):
    print(f'{c.BoldRed}Error:{c.Red} {error_messsage}{c.Normal}', file=sys.stderr)
    if error_code != 0:
        exit(error_code)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
