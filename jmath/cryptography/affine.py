'''
    Affine cipher and Affine cipher relevant tools.
'''

# - Imports

import string
from ..modular import modular_inverse
from ..exceptions import OutOfRange
from typing import Tuple

# - Globals

ENGLISH_LOWER = string.ascii_lowercase
ENGLISH_UPPER = string.ascii_uppercase
ENGLISH_ALL = string.ascii_letters
ENGLISH_SPECIAL_CHAR = ENGLISH_ALL + "~!@#$%^&*()_+`1234567890-=[]{}|;':\\\",./<>?"
ENGLISH_NUMERIC = ENGLISH_ALL + "1234567890.,"

# - Classes

class Affine:
    '''
        Creates an affine cipher 
        
        (ax + b) % len(set_length)

        Parameters
        ----------

        a
            Value to multiply x by
        b
            Value to add to x
        char_set
            Ordered set (tuple) of valid characters

        Raises
        ------

        OutOfRange
            Given if a or b are outside of the range from 0 to the length of the character set minus one.
    '''

    def __init__(self, a: int, b: int, char_set: Tuple["str"] = ENGLISH_LOWER):
        
        self.char_set = char_set
        self.a = a
        self.b = b

    @property
    def a(self):
        '''Value that x is multiplied by in the encryption process.'''
        return self._a

    @property
    def b(self):
        '''Value that x is added to in the encryption process.'''
        return self._b

    @property
    def char_set(self):
        '''Ordered set of unique characters to used in the cipher.'''
        return self._char_set

    @a.setter
    def a(self, a: int):
        """Check a assignment"""
        # Checking input parameters
        if a < 0 or a > len(self.char_set) - 1:
            raise OutOfRange(a, 0, len(self.char_set) - 1)
        
        # No errors, assign
        self._a = a
        self.a_inverse = modular_inverse(a, len(self.char_set))
        
        if self.a_inverse == None:
            raise ValueError("Value of 'Affine.a' has no modular inverse and is thus unusable.")

    @b.setter
    def b(self, b: int):
        """Check b assignment"""
        # Checking input parameters
        if b < 0 or b > len(self.char_set) - 1:
            raise OutOfRange(b, 0, len(self.char_set) - 1)

        # No errors, assign
        self._b = b

    @char_set.setter
    def char_set(self, char_set: Tuple["str"]):
        """Check's charset assignment"""
        self._char_set = tuple(dict.fromkeys(char_set)) # Assigns char set retaining order and uniqueness
        
    def _char_to_num(self, char: str) -> int:
        """
            Converts a string character to a numeric value in alignment with the affine cipher.

            Parameters
            ----------

            char
                The string to find the numeric value of.
        """

        return self.char_set.index(str(char))

    def _num_to_char(self, number: int) -> str:
        """
            Converts a number to a number in alignment with the affine cipher.

            Parameters
            ----------

            number
                The number (an index) of the character in the character set.
                Can be outside of the index number range as modulo operation is applied.
        """

        return self.char_set[number % len(self.char_set)]

    def _encrypt_char(self, char: str) -> str:
        """
            Encrypts a character as per the affine cipher.

            Parameters
            ----------

            char
                The character to encrypt
        """

        num = self._char_to_num(char[0])
        # Convert num per affine cipher
        num = (num*self.a + self.b) % len(self.char_set)
        return self._num_to_char(num)

    def _decrypt_num(self, char: str) -> str:
        """
            Decrypts a number as per the reversed affine cipher.

            Parameters
            ----------

            char
                The string to decrypt
        """

        num = self._char_to_num(char)
        num = self.a_inverse*(num - self.b) % len(self.char_set)
        # Convert num to char
        return self._num_to_char(num)

    def encrypt(self, string: str, split_char: str = "") -> str:
        """
            Encrypts a string of letters as per the affine cipher.

            Parameters
            ----------

            string
                The string to be encrypted by the affine cipher
            split_char
                The value to insert between encrypted values.
        """
        output_list = []

        for char in string:
            # Automatic space filtering
            if char != " ":
                output_list.append(str(self._encrypt_char(char)))
        
        return split_char.join(output_list)

    def decrypt(self, string: str, split_char: str = "") -> str:
        """
            Decrypts a string of numbers as per the affine cipher

            Parameters
            ----------

            string
                The string to be decrypted by the affine cipher, expects splits by spaces.
            split_char
                The character between encrypted values.
        """

        output_string = ""

        if split_char != "":
            string = string.split(split_char)

        for num in string:
            output_string += self._decrypt_num(num)

        return output_string