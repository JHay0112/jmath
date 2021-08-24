"""
    Tests affine cipher
"""

# - Imports

from ..jmath.cryptography.affine import  Affine

# - Tests

def test_encrypt_decrypt():
    """Tests the affine cipher by encrypting then decrypting the cipher text."""
    test_text = "mymilkshakebringsalltheboystotheyard"
    cipher = Affine(5, 3)
    encrypted_text = cipher.encrypt(test_text)
    decrypted_text = cipher.decrypt(encrypted_text)
    assert decrypted_text == test_text