'''
Usage:
    main.py [options] [<input> [<output>]]

Options:
    -o <style>, --output-style <style>          Defines style for columns.
    -i <string>, --input-separator <string>     Defines characters being used as separators.
    -s, --sticky-separators                     Multiple separators as one.
    -t, --trim-empty                            Deletes empty fields at beginning and end of entries.
    -n <string>, --names <string>               Defines names of columns (first character of string stands as separator).
    -1, --first-line-header                     If enabled, makes first string perceived as header.
    -f <string>, --fields <string>              Defines specification of output.
    -L <number>, --lines-inspect <number>       Defines number of strings being counted before calculating field sizes.
    -h, --help                                  Open this message.
    -v, --version                               Version check and finish program execution.
'''

from docopt import docopt
from os import path
import pprint
import sys

# Pretty print function
def pretty_printer(data):
    pp = pprint.PrettyPrinter()
    pp.pprint(data)

if __name__ == "__main__":
    # Getting parameters and options dictionary then print it (for understanding)
    args = docopt(__doc__, options_first=True)
    pretty_printer(args)

    # Working with options and parameters using conditions   
    if args['--version']:
        print('tabular v0.0.1')
        sys.exit()
        
    if args['<input>'] and path.isfile(args['<input>']):
        with open(args['<input>'], 'r') as f:
            print(f.read())
            f.seek(0)
            input_text = f.read()
    elif args['<input>']:
        print(f'File \"{args["<input>"]}\" does not exist.')
    else:
        input_text = input()

    if args['<output>']:
        with open(args['<output>'], 'w+') as f:
            print(input_text)
            f.write(input_text) 
    else:
        print(input_text)
    