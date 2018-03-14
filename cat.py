import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--squeeze-blank", help="never more than one single blank line", action="store_true")
parser.add_argument("-T", "--show-tabs", help="display TAB characters as ^I", action="store_true")
parser.add_argument("-E", "--show-ends", help="display $ at the end of each line", action="store_true")
parser.add_argument("-FE", "--show-fends", help="display $ at the end of each line, aligned", action="store_true")
parser.add_argument("-n", "--number", help="number all output lines", action="store_true")
parser.add_argument("filename", nargs='*', help="file to concatenate", default=['cat.py']) # No filenames prints out source code!

args = parser.parse_args()

line_start_text = ''
line_end_text = ''
longest_line_len = 0

if args.show_fends: # -FE
    for filename in args.filename: # Find longest line of all files COMBINED
        with open(filename, "r") as f:
            longest_line_len = max( \
                len(max(f, key=len)), longest_line_len)

if args.number: # -n
    line_num = 1

# THE CONCATENATION    
for filename in args.filename:
    with open(filename, "r") as f:

        if args.squeeze_blank: # -s
            blank_space = False

        for line in f:
            line = line.rstrip('\n')

            if args.squeeze_blank: # -s
                if not line: # If line is empty
                    if blank_space:
                        continue
                    blank_space = True
                else:
                    blank_space = False

            if args.show_tabs: # -T
                line = line.replace('\t', '^I')

            if args.number: # -n
                line_start_text = '\t' + str(line_num) + '\t'
                line_num += 1
            
            if args.show_ends or args.show_fends: # -E and -FE
                line_end_text = '%{}s'.format(longest_line_len - len(line)) % ('$') # Make sure each line has all the same columns as every other
                
            print(line_start_text + line + line_end_text)


