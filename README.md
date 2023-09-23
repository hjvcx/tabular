# tabular

Converting csv data into tabular view.

## Options

### -o \<string\>, --output-style \<string\>

The argument encodes the column formatting style. The first letter in the line selects the characters used to frame the fields.

`a` for ASCII characters <br>
`u` for Unicode graphics

The following letters encode the drawing of different borders in the table.

`h` for the border between the header (if defined) and the content<br>
`c` for the border between the columns<br>
`b` for the external border of the table.

If Unicode characters are selected, lowercase letters encode a single line thickness, and uppercase letters encode a double line.

The default style is assumed to be `uhC`

Examples of formatting can be found in the Usage section.

### -i \<string\>, --input-separator \<string\>

The line specifies all the characters that can separate fields. For example, when specifying `;,` both comma and semicolon separate fields.

By default, space is assumed.

### -s, --sticky-separators

A flag, when set, treats multiple consecutive separators as a single separator.

By default, and if the `-i` option is not specified, the flag is enabled.

### -t, --trim-empty

Removes empty fields at the beginning and end of a row.

### -n \<string\>, --names \<string\>

The string should contain a list of field names. The first character is the delimiter for names in the specified list, followed by the names separated by that delimiter. For example, in the sequence `'^№^Name^Surname^Share, %'`, the delimiter is "^", and the resulting field names are "№", "Name", "Surname", and "Share, %" (percentage share).

By default, the field names are empty.

If the option is specified, the table should be displayed with specified headers. If the `-n` or `-1` options are not specified, the header is not displayed.

You can specify either `-n` or `-1`, but not both options together.

If the list of field names is shorter than the list of fields, the list of field names is extended with empty names.

### -1, --first-line-header

Flag indicating that field headers are taken from the first row. By default, it is set to false. You can specify either `-n` or `-1`, but not both options together.

### -f \<string\>, --fields \<string\>

The string contains a specification of fields for output. Each field in the input stream is numbered starting from 1. The string lists the order of output fields and the rules for their formatting separated by commas. A field is described by an alignment character and a field number. The alignment characters are as follows:

`r` for right alignment<br>
`l` for left alignment<br>
`c` for centering<br>
`j` for justification

For example, the sequence `l2r1`indicates that the second field from the input stream is output first, aligned to the left, followed by the first field aligned to the right.

Field names, if included, are always left aligned. If the field number is specified as 0, it means all fields not explicitly specified in the specification should be included. Thus, `r2l0r1` should output the second field first, followed by all except the first field, and finally the first field aligned to the right.

The default specification is `l0`, that is, all fields are output with left alignment.

### -L \<number\>, --lines-inspect \<number\>

This specifies how many lines to read before calculating the field sizes. By default, it is set to 0, which means all lines are included.

### -h, --help

Shows help message.

### -v, --version

Print the program version and terminate execution.

## Usage

```
tabular [options] [<input> [<output>]]
```

Here's an example of how to use the program:

```
$ cat input.csv
Name,Age,Country
Alice,30,USA
Bob,25,Canada
Charlie,40,UK

$ ./tabular -o uHCB -i ',' -f r1c3l2 -1 input.csv output.tab

$ cat output.tab
╔═════════╦═════════╦═════╗
║    Name ║ Country ║ Age ║
╠═════════╬═════════╬═════╣
║   Alice ║   USA   ║ 30  ║
║     Bob ║  Canada ║ 25  ║
║ Charlie ║    UK   ║ 40  ║
╚═════════╩═════════╩═════╝
```

## Installation

To install the program, simply clone the repository and install the required dependencies:

```
$ git clone https://github.com/hjvcx/tabular.git
$ cd tabular
$ pip install -r requirements.txt
```

Once the dependencies are installed, you can run the program using the command `./tabular`.