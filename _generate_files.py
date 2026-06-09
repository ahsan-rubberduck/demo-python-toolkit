"""One-off generator for 100 demo modules (mix of clean + vulnerable).

Run once to populate generated/. Avoids real provider secret formats so
GitHub push protection won't block the fixtures.
"""

import os
import textwrap

OUT = os.path.join(os.path.dirname(__file__), "generated")
os.makedirs(OUT, exist_ok=True)

CLEAN_TEMPLATE = '''\
"""Auto-generated benign utility module #{n:03d}."""


def scale_{n}(value, factor={n}):
    """Multiply ``value`` by a fixed factor."""
    return value * factor


def clamp_{n}(value, low=0, high={hi}):
    """Clamp ``value`` into the inclusive range [low, high]."""
    return max(low, min(high, value))


def summarize_{n}(items):
    """Return basic stats for a list of numbers."""
    if not items:
        return {{"count": 0, "total": 0, "mean": 0}}
    total = sum(items)
    return {{"count": len(items), "total": total, "mean": total / len(items)}}
'''

VULN_TEMPLATES = [
    # SQL injection
    '''\
"""Auto-generated INTENTIONALLY VULNERABLE module #{n:03d} (CWE-89, test only)."""

import sqlite3


def lookup_{n}(user_id):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    # CWE-89: SQL injection via f-string
    cur.execute(f"SELECT * FROM accounts WHERE id = {{user_id}}")
    return cur.fetchall()
''',
    # Command injection
    '''\
"""Auto-generated INTENTIONALLY VULNERABLE module #{n:03d} (CWE-78, test only)."""

import os


def run_{n}(target):
    # CWE-78: command injection via os.system
    os.system("nslookup " + target)
''',
    # eval
    '''\
"""Auto-generated INTENTIONALLY VULNERABLE module #{n:03d} (CWE-94, test only)."""


def compute_{n}(expr):
    # CWE-94: arbitrary code execution
    return eval(expr)
''',
    # weak hash
    '''\
"""Auto-generated INTENTIONALLY VULNERABLE module #{n:03d} (CWE-327, test only)."""

import hashlib


def digest_{n}(data):
    # CWE-327: weak hashing algorithm
    return hashlib.md5(data.encode()).hexdigest()
''',
    # hardcoded secret (fake placeholder)
    '''\
"""Auto-generated INTENTIONALLY VULNERABLE module #{n:03d} (CWE-798, test only)."""

# CWE-798: hardcoded credential (fake placeholder for SAST testing)
TOKEN_{n} = "FAKE_TOKEN_FOR_SAST_TESTING_{n:03d}_000000"


def authenticate_{n}(supplied):
    return supplied == TOKEN_{n}
''',
]

manifest = []
for i in range(1, 101):
    if i % 4 == 0:  # ~25% vulnerable, spread across CWE types
        tmpl = VULN_TEMPLATES[(i // 4 - 1) % len(VULN_TEMPLATES)]
        kind = "vulnerable"
    else:
        tmpl = CLEAN_TEMPLATE
        kind = "clean"
    body = tmpl.format(n=i, hi=i * 10)
    name = f"module_{i:03d}.py"
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
        fh.write(body)
    manifest.append(f"{name}: {kind}")

with open(os.path.join(OUT, "MANIFEST.txt"), "w", encoding="utf-8") as fh:
    fh.write("Generated demo modules (clean vs intentionally vulnerable)\n")
    fh.write("=" * 58 + "\n")
    fh.write("\n".join(manifest) + "\n")

print(f"Wrote {len(manifest)} modules + MANIFEST.txt to {OUT}")
