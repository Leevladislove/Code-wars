"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example:
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""


def solution(string):
    char = ''
    for letter in string:
        if letter.isupper():
            char += ' '
        char += letter

    return char
