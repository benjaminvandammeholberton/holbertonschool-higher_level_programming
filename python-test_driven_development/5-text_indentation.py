#!/usr/bin/python3
"""
function that prints a text with 2 new lines after\
 each of these characters: ., ? and :
Args: Text
Return: Text with 2 lines after
"""


def text_indentation(text):
    """
    Print a text with two lines after these characters(. ? :)
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
