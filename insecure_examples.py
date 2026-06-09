"""INTENTIONALLY VULNERABLE CODE — TEST FIXTURE ONLY.

This module contains deliberate security anti-patterns used to validate
security scanners (SAST tools). DO NOT use any of this in real code, and
DO NOT deploy it. Every function below is flawed on purpose.
"""

import hashlib
import os
import pickle
import sqlite3
import subprocess

# --- Hardcoded secrets (CWE-798) -------------------------------------------
# NOTE: fake placeholder values — real provider key formats are avoided on
# purpose so GitHub push protection doesn't block this test fixture. A SAST
# tool's hardcoded-secret rule still fires on these assignments.
API_KEY = "FAKE_API_KEY_FOR_SAST_TESTING_0000000000"
DB_PASSWORD = "SuperSecret123!"
AWS_SECRET_ACCESS_KEY = "FAKE_AWS_SECRET_FOR_SAST_TESTING_00000000"


def sql_injection(username):
    """CWE-89: SQL injection via string formatting."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = '%s'" % username
    cursor.execute(query)
    return cursor.fetchall()


def command_injection(filename):
    """CWE-78: OS command injection via shell=True with user input."""
    return subprocess.check_output("cat " + filename, shell=True)


def os_command_injection(host):
    """CWE-78: OS command injection via os.system."""
    os.system("ping -c 1 " + host)


def code_injection(expression):
    """CWE-94: Arbitrary code execution via eval/exec."""
    result = eval(expression)
    exec("computed = " + expression)
    return result


def insecure_deserialization(data):
    """CWE-502: Untrusted deserialization via pickle."""
    return pickle.loads(data)


def weak_hash(password):
    """CWE-327: Weak hashing algorithm (MD5)."""
    return hashlib.md5(password.encode()).hexdigest()


def path_traversal(user_path):
    """CWE-22: Path traversal — no sanitization of user input."""
    with open("/var/data/" + user_path) as handle:
        return handle.read()
