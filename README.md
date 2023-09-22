## tabular

Converting csv data into tabular view.

## Options

### -o \<string\>, --output-style \<string\>

The `--output-style` option specifies a style for table.

The argument encodes the column formatting style. The first letter in the line selects the characters used to frame the fields.

`a` for ASCII characters <br>
`u` for Unicode graphics

The following letters encode the drawing of different borders in the table.

`h` for the border between the header (if defined) and the content <br>
`c` for the border between the columns <br>
`b` for the external border of the table.

If Unicode characters are selected, lowercase letters encode a single line thickness, and uppercase letters encode a double line.

The default style is assumed to be `uhC`

Examples of formatting can be found in the Usage section.

## Usage

```
tabular [options] [<input> [<output>]]
```

Here's an example of how to use the program:

```
example
```

In this example, the program...

## Installation

To install the program, simply clone the repository and install the required dependencies:

```
$ git clone https://github.com/hjvcx/tabular.git
$ cd tabular
$ pip install -r requirements.txt
```

Once the dependencies are installed, you can run the program using the command `./tabular`.