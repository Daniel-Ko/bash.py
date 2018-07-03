import argparse
import re
from collections import Counter
from os.path import getsize
from sys import argv

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--bytes", help="print the byte counts", action="store_true")
    parser.add_argument("-w", "--words", help="print the word counts", action="store_true")
    parser.add_argument("-l", "--lines", help="print the newline count", action="store_true")
    parser.add_argument("-m", "--chars", help="print the character counts", action="store_true")
    parser.add_argument("-L", "--max_line_length", help="print the length of the longest line", action="store_true")
    parser.add_argument("FILE", nargs='*', help="file to analyze", default=['wc.py']) # No filenames analyses source code
    args = parser.parse_args()
    
    if (len(list(filter(lambda x: not x, vars(args).values()))) == 
        len(vars(args))-1): # Default case, print all three
        args.lines = True
        args.words = True
        args.bytes = True

    #TODO: write total line
    for filename in args.FILE:
        with open(filename, "r") as f:
            ftext = f.read()
        
            if args.lines:
                newlines = len(re.findall(r'\n', ftext))
                print("{} ".format(newlines), end="")
            if args.words:
                wordcount = sum(Counter(ftext.split()).values())
                print("{} ".format(wordcount), end="")
            if args.bytes:
                bytesize = getsize(filename)
                print("{} ".format(bytesize), end="")
            if args.chars:
                charsize = len(ftext)
                print("{} ".format(charsize), end="")
            if args.max_line_length:
                longest_line_size = len(max(ftext.split(), key=len))
                print("{} ".format(longest_line_size), end="")

            print(filename)

if __name__ == "__main__":
    main()