# py

Quick python for command-line pipe-fu

    pip install quickpy


# Basic usage

With no input or flags, `py` executes inline python expresions:

    $ py '1 + 2'
    3

    $ py 'base64.encodestring("Hello")'
    SGVsbG8=

Modules are imported automatically, including the current directory.


# Processing input

`py` has three input handling modes, selected automatically when special
variable names are used in the expression:


Variable | Input mode
-------- | -------------
  line   | Eval expression for each line of input, assigning each to 'line'
  lines  | Eval expression once, assigning a list of input lines to 'lines'
  input  | Eval expression once, assigning input as a string to 'input'


These enable idioms like:

    $ ... | py 'line.replace("foo", "bar")'         # word replace
    $ ... | py 'max(lines, key = lambda l: len(l))' # longest line
    $ ... | py 'binascii.hexlify(input)'            # encode in hex
