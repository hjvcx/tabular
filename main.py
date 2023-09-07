from docopt import docopt

usage = '''
Usage:
main.py (-o | --output-style) <string>
'''

def output_style(string):
    print(string)

if __name__ == "__main__":
    args = docopt(usage)

    if args['-o'] or args['--output-style']:
        output_style(args['<string>'])