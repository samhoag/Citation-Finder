"""
This program is designed to help out students and writers like me who, instead of creating citations as they go along
writing, just jot down a note in parenthesis vaguely referencing some article that they hopefully saved somewhere. When
it comes time to actually make citations, I hate going back through and meticulously going from parenthesis to
parenthesis trying to find all of those notes. So I wrote a script to do it for me!

It's far from perfect. I spent about five minutes writing it and did not concern myself with efficiency at all.

To use:
1. Save your word document as a .txt file (I'd recommend making a backup copy first).
2. Move the .txt file to the same directory as this script
3. Either name your .txt "test.txt", or change "test.txt" in the call to main on line 38 to the name of your .txt file
4. The results will be printed to the console. 
"""

import re


def get_txt_as_string(file):
    text = open(file, encoding="ISO-8859-1").read()
    return text


def parse_text(text, remove_duplicates):
    return re.findall(r'\((.*?)\)', text)


def pretty_print_parsed_text(text_arr):
    for t in text_arr:
        print(t)


def main(file):
    pretty_print_parsed_text(parse_text(get_txt_as_string(file)))


if __name__ == '__main__':
    main("test.txt")
