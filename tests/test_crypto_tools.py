'''
    Tests the cryptography analysis tools
'''

# - Imports

from ..jmath.cryptography.tools import character_frequencies

# - Tests

def test_character_frequency():
    """Tests that character frequency analysis function."""
    # Known text with every english character, o appears most (4 times), all appear at least once
    sample_text = "A quick brown fox jumped over the lazy dog"
    sample_text = sample_text.replace(" ", "") # Strip out spaces
    char_freq = character_frequencies(sample_text)

    print(char_freq)

    for char, count in char_freq.items():
        print(char)
        assert count >= 1 # All appear at least once
        assert count <= 4 # 'o' appears 4 times