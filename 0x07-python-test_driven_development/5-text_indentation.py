#!/usr/bin/python3
"""
module composed by function that prints 2 new lines after "?:" char
"""

def text_indentation(text):
    """function prints 2lines after "?:" char
    args:
        text: input string

    Returns: void

    Raises:
        TypeError: if the text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end = "")
