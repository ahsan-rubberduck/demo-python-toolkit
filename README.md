# Demo Python Toolkit

A small demo Python project showcasing a few self-contained utility modules.

## Modules

| File | Purpose |
|------|---------|
| `main.py` | CLI entry point that ties the modules together |
| `calculator.py` | Basic arithmetic operations |
| `string_utils.py` | Handy string helpers |
| `temperature.py` | Temperature unit conversions |
| `fibonacci.py` | Fibonacci sequence generators |
| `tests.py` | Lightweight self-tests for the modules |
| `insecure_examples.py` | ⚠️ **Intentionally vulnerable** test fixtures (SQLi, command/code injection, hardcoded secrets, weak hashing, path traversal) |
| `insecure_web.py` | ⚠️ **Intentionally vulnerable** web-flavored fixtures (unsafe YAML, XXE, disabled TLS, SSRF, XSS, open redirect) |

> ⚠️ **Security note:** `insecure_examples.py` and `insecure_web.py` contain
> deliberate vulnerabilities used only to test security scanners (SAST tools).
> They are not imported by the app, are not safe, and must never be deployed.

## Usage

```bash
python main.py
```

Run the tests:

```bash
python tests.py
```
