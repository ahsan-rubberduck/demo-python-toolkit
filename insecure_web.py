"""INTENTIONALLY VULNERABLE CODE — TEST FIXTURE ONLY.

Web-flavored security anti-patterns for exercising a security scanner.
DO NOT use in real code. Every example is flawed on purpose.
"""

import random
import ssl
import urllib.request
from xml.etree import ElementTree

import yaml


def unsafe_yaml_load(raw):
    """CWE-20: yaml.load without SafeLoader allows arbitrary object construction."""
    return yaml.load(raw, Loader=yaml.Loader)


def xxe_parse(xml_string):
    """CWE-611: XML parsed without disabling external entity resolution."""
    return ElementTree.fromstring(xml_string)


def disabled_tls_verification(url):
    """CWE-295: TLS certificate verification disabled."""
    context = ssl._create_unverified_context()
    return urllib.request.urlopen(url, context=context).read()


def insecure_random_token():
    """CWE-330: Using a non-cryptographic RNG for a security token."""
    return "".join(random.choice("0123456789abcdef") for _ in range(32))


def reflected_xss(name):
    """CWE-79: Unescaped user input rendered into HTML."""
    return "<html><body>Hello, " + name + "!</body></html>"


def open_redirect(target):
    """CWE-601: Redirect to an unvalidated, user-controlled URL."""
    return {"status": 302, "Location": target}


def ssrf_fetch(user_url):
    """CWE-918: Server-side request to a fully user-controlled URL."""
    return urllib.request.urlopen(user_url).read()
