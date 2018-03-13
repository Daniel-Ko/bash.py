import sys
#get command line arg (filename or more arguments). TODO: Use argparse 

# Check empty args passed, then print this source code itself
if len(sys.argv) == 1:
    with open('cat.py', "r") as catcode:
        for line in catcode:
            print(line.rstrip('\n'))
# If args are passed, then use the cat fn
else:
    for filename in sys.argv[1:]:
        with open(filename, "r") as f:
            for line in f:
                # catfile.write(line)
                print(line.rstrip('\n'))

