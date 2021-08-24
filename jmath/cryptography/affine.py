'''
    Affine cipher and Affine cipher relevant tools.
'''

# - Imports

from math import gcd
import string
from ..modular import extended_gcd, modular_inverse
from ..exceptions import OutOfRange
from typing import Tuple

# - Globals

ENGLISH_LOWER = string.ascii_lowercase
ENGLISH_UPPER = string.ascii_uppercase
ENGLISH_ALL = string.ascii_letters

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
        
        self.char_set = tuple(set(char_set)) # Convert to set first to remove duplicates
        self.a = a
        self.b = b

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

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
        
    def _char_to_num(self, char: str) -> int:
        """
            Converts a string character to a numeric value in alignment with the affine cipher.

            Parameters
            ----------

            char
                The string to find the numeric value of.
        """

        return self.char_set.index(char)

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

    def _affine_cipher(self, num: int) -> int:
        """
            Applies the affine cipher to a number

            Parameters
            ----------

            num
                The number to apply the affine cipher to
        """
        return (num*self.a + self.b) % len(self.char_set)

    def _affine_decipher(self, num: int) -> int:
        """
            Reverses the affine cipher on the number

            Parameters
            ----------

            num
                The number to decipher
        """

        return self.a_inverse*(num - self.b) % len(self.char_set)

    def _encrypt_char(self, char: str) -> int:
        """
            Encrypts a character as per the affine cipher.

            Parameters
            ----------

            char
                The character to encrypt
        """

        num = self._char_to_num(char[0])
        # Convert num per affine cipher
        return self._affine_cipher(num)

    def _decrypt_num(self, num: int) -> str:
        """
            Decrypts a number as per the reversed affine cipher.

            Parameters
            ----------

            num
                The number to decrypt
        """

        num = self._affine_decipher(int(num))
        # Convert num to char
        return self._num_to_char(num)

    def encrypt(self, string: str) -> str:
        """
            Encrypts a string of letters as per the affine cipher.

            Parameters
            ----------

            string
                The string to be encrypted by the affine cipher
        """
        output_list = []

        for char in string:
            # Automatic space filtering
            if char != " ":
                output_list.append(str(self._encrypt_char(char)))
        
        return " ".join(output_list)

    def decrypt(self, string: str) -> str:
        """
            Decrypts a string of numbers as per the affine cipher

            Parameters
            ----------

            string
                The string to be decrypted by the affine cipher, expects splits by spaces.
        """

        output_string = ""
        string = string.split(" ")

        for num in string:
            output_string += self._decrypt_num(num)

        return output_string