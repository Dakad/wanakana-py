from .english import is_char_english_punctuation
from .japanese import is_char_japanese_punctuation
from ..constants import ROMAJI_RANGES


def is_empty(text: str) -> bool:
    return (not isinstance(text, str)) or (not len(text))


def is_char_in_range(char: str = "", start: int = 0, end: int = 0) -> bool:
    """Tests if a character is in a Unicode range."""
    if is_empty(char):
        return False
    code = ord(char[0])
    return start <= code <= end


def is_char_punctuation(char: str = "") -> bool:
    """Tests if a character is considered Japanese or English punctuation"""
    return is_char_english_punctuation(char) or is_char_japanese_punctuation(char)


def is_char_romaji(char: str = "") -> bool:
    """Tests if a character is Romaji (using Hepburn romanisation)."""
    return any(is_char_in_range(char, start, end) for start, end in ROMAJI_RANGES)
