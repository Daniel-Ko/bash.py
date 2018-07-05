import argparse
import re
from collections import Counter, defaultdict
from os.path import getsize
from sys import argv

PARSED_FLAGS = 6

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--bytes", help="print the byte counts", action="store_true")
    parser.add_argument("-w", "--words", help="print the word counts", action="store_true")
    parser.add_argument("-l", "--lines", help="print the newline count", action="store_true")
    parser.add_argument("-m", "--chars", help="print the character counts", action="store_true")
    parser.add_argument("-L", "--max_line_length", help="print the length of the longest line", action="store_true")
    parser.add_argument("-A", "--all", help="report all statistics", action="store_true")
    parser.add_argument("FILE", nargs='*', help="file to analyze", default=['wc.py']) # No filenames analyses source code
    args = parser.parse_args()
    
    # Collect the number of flags specified as arguments
    # As filename is required, we can count it out 
    num_flags_off = len(list(filter(lambda x: not x, vars(args).values()))) 

    # Default case, print all three
    if num_flags_off == PARSED_FLAGS:
        args.lines = True
        args.words = True
        args.bytes = True

    # If more than one file passed in, create a running total
    if len(args.FILE) > 1:
        count_total = True
        totals = defaultdict(lambda: 0)

    for filename in args.FILE:
        with open(filename, "r") as f:
            ftext = f.read()

            # To count newlines
            if args.lines or args.all:
                newlines = len(re.findall(r'\n', ftext))
                no_newline_print(newlines)
                collect_total(totals, count_total, "newlines", newlines)
            # To count words
            if args.words or args.all:
                wordcount = sum(Counter(ftext.split()).values())
                no_newline_print(wordcount)
                collect_total(totals, count_total, "words", wordcount)
            # To count bytes
            if args.bytes or args.all:
                bytesize = getsize(filename)
                no_newline_print(bytesize)
                collect_total(totals, count_total, "bytes", bytesize)
            # To count characters
            if args.chars or args.all:
                charsize = len(ftext)
                no_newline_print(charsize)
                collect_total(totals, count_total, "chars", charsize)
            # To find longest line 
            if args.max_line_length or args.all:
                longest_line_size = len(max(ftext.split(), key=len))
                no_newline_print(longest_line_size)
                collect_total(totals, count_total, "max_line", longest_line_size)
            # Print the filename for these statistics
            print(filename)

    # Print the collected multi-file statistics         
    if count_total:
        # Total count
        num_flags_on = 1 - num_flags_off
        len_divider = (25 
        if PARSED_FLAGS == num_flags_off 
        else 4*(PARSED_FLAGS-num_flags_on))
        print(len_divider)
        print("="*len_divider)

        for total in totals.values():
            no_newline_print(total)
        print("total")

def no_newline_print(var):
    print("{:<5d} ".format(var), end="")

def collect_total(totals, count_total, key, new_val):
    # All options keep a running sum except max_line, which finds the longest line
    if count_total: # Only necessary if more than one file specified
        if key != "max_line":
            totals[key] += new_val
        else:
            totals[key] = max(totals[key], new_val)

if __name__ == "__main__":
    main()