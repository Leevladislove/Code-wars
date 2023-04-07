"""
Given a string s. You have to return another string such that even-indexed
and odd-indexed characters of s are grouped
and groups are space-separated
"""


def sort_my_string(s):
    return f'{s[::2]} {s[1::2]}'
