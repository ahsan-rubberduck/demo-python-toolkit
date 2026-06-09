"""Handy string helpers."""


def reverse(text):
    """Return the reversed string."""
    return text[::-1]


def is_palindrome(text):
    """Return True if ``text`` reads the same forwards and backwards."""
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


def count_vowels(text):
    """Return the number of vowels in ``text``."""
    return sum(1 for c in text.lower() if c in "aeiou")


def to_title_case(text):
    """Return ``text`` with each word capitalized."""
    return " ".join(word.capitalize() for word in text.split())


def truncate(text, length, suffix="..."):
    """Truncate ``text`` to ``length`` characters, adding ``suffix``."""
    if len(text) <= length:
        return text
    return text[: length - len(suffix)] + suffix
