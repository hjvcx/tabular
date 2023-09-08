from docopt import docopt

usage = '''
Usage:
    main.py [options] [input [output]]

Options:
    -o <style>, --output-style <style>      Output style.
    -i --input-separator                    Input separator.
'''


def output_style(string):
    print(string)

if __name__ == "__main__":
    args = docopt(usage, options_first=True)

    print(args)