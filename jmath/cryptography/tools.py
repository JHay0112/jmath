'''
    Tools for analysing cipher text
'''

# - Functions

def character_frequencies(cipher_text: str, split_char: str = ""):
    """
        Records the most commonly occuring frequencies in the cipher text.

        Paramaters
        ----------

        cipher_text
            The text to analyse
    """
    frequencies = {}

    if split_char != "":
        cipher_text = cipher_text.split(split_char)

    for char in cipher_text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 0

    return frequencies