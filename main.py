'''
Usage:
    main.py [options] [<input> [<output>]]

Options:
    -o <style>, --output-style <style>      Output style.
    -i --input-separator                    Input separator.
'''

from docopt import docopt

def output_style(string):
    print(string)

if __name__ == "__main__":
    args = docopt(__doc__, options_first=True)

    print(args)