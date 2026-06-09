"""Auto-generated INTENTIONALLY VULNERABLE module #068 (CWE-78, test only)."""

import os


def run_68(target):
    # CWE-78: command injection via os.system
    os.system("nslookup " + target)
