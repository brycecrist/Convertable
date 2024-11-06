# JS/TXT Converter
Written in Python 3

## The Problem:
Have you ever needed to modify stringified, escaped JS code? Perhaps while using the Template class within the [Python string module](https://docs.python.org/3/library/string.html#string.Template)?

I have! For example, it's a pain to update the following code by hand, especially for larger blocks of code:

    "function example() {\n"
    "\tconsole.log("Hello world!")\n"
    "\tif (true) {\n"
    "\t\tconsole.log("I'm true!")\n"
    "\t}\n"
    "}"

## The Solution:
I have built a simple tool that allows one to write the above code in Javascript, within a Javascript file, and then convert it to a properly escaped, stringified txt file.

This program also allows for the opposite. You could pass in the filename of the above example in a txt file and have it converted back to Javascript.

Example files are included: `example.js` which can be converted to `output.txt`, as well as `output.js` which is the result of converting `output.txt` back to Javascript.

## How to Use:
Example usage:

    > python main.py example.js -txt

The first argument must be the input filename  that is to be converted, either `.js` or `.txt`.

The following argument must be the conversion target file type, either `-txt` or `-js`. 

In the above example, we convert a Javascript file named `example.js` to a txt file.
