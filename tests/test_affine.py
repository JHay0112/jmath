"""
    Tests affine cipher
"""

# - Imports

from ..jmath.cryptography.affine import Affine, ENGLISH_ALL, ENGLISH_NUMERIC

# - Tests

def test_encrypt_decrypt():
    """Tests the affine cipher by encrypting then decrypting the cipher text."""
    test_text = "mymilkshakebringsalltheboystotheyard"
    cipher = Affine(5, 3)
    encrypted_text = cipher.encrypt(test_text)
    decrypted_text = cipher.decrypt(encrypted_text)
    assert decrypted_text == test_text

def test_encrypt_decrypt_all_english():
    """Tests that affine cipher encrypts and decrypts with lower and upper cases."""
    test_text = "MyMilkShakeBringsAllTheBoysToTheYard"
    cipher = Affine(3, 7, ENGLISH_ALL)
    encrypted_text = cipher.encrypt(test_text)
    decrypted_text = cipher.decrypt(encrypted_text)
    assert decrypted_text == test_text

def test_encrypt_decrypt_english_numeric():
    """Tests that the affine cipher encrypts and decrypts english with numeric values."""
    test_text = "Thereare1,322.50dollarsinmybankaccount"
    cipher = Affine(3, 7, ENGLISH_NUMERIC)
    encrypted_text = cipher.encrypt(test_text)
    decrypted_text = cipher.decrypt(encrypted_text)
    assert decrypted_text == test_text

def test_duplicate_ciphers():
    """Tests that different instances produce the same cipher text."""
    cipher1 = Affine(3, 10)
    cipher2 = Affine(3, 10)
    text = "ohgodhelpmetherearethousandsofbeespleasehelp"
    assert cipher1.encrypt(text) == cipher2.encrypt(text)