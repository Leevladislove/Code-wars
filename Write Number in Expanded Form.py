"""
Write Number in Expanded Form
You will be given a number, and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
"""


def expanded_form(num):
    num_str = str(num)[::-1]
    expanded = []
    for i, digit in enumerate(num_str):
        if digit == '0':
            continue
        place_value = 10 ** i
        expanded.append(str(int(digit) * place_value))
    return ' + '.join(expanded[::-1])
