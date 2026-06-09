"""Auto-generated INTENTIONALLY VULNERABLE module #096 (CWE-327, test only)."""

import hashlib


def digest_96(data):
    # CWE-327: weak hashing algorithm
    return hashlib.md5(data.encode()).hexdigest()
