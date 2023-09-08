'''
Usage:
    main.py [options] [<input> [<output>]]

Options:
    -o <style>, --output-style <style>      Output style.
    -i --input-separator                    Input separator.
'''

from docopt import docopt
from os import path

# Dummy function
def output_style(string):
    print(string)

if __name__ == "__main__":
    # Getting parameters and options dictionary then print it (for understanding)
    args = docopt(__doc__, options_first=True)
    print(args)

    # Working with options and parameters using conditions
    if args['<input>'] and path.isfile(args['<input>']):
        with open(args['<input>'], 'r') as f:
            print(f.read())
            f.seek(0)
            input_text = f.read()
    elif args['<input>']:
        print(f'File \"{args["<input>"]}\" does not exist.')

    if args['<output>']:
        with open(args['<output>'], 'w+') as f:
            print(input_text)
            f.write(input_text) 
    