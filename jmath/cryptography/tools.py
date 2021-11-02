'''
    Tools for analysing cipher text
'''

# - Imports

from typing import Dict

# - Functions

def character_frequencies(cipher_text: str, split_char: str = "") -> Dict[str, int]:
    """
        Records the most commonly occuring frequencies in the cipher text.

        Parameters
        ----------

        cipher_text
            The text to analyse
        split_char
            The character to split items around, defaults to none.
    """
    frequencies = {}

    if split_char != "":
        cipher_text = cipher_text.split(split_char)

    for char in cipher_text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1

    return frequencies