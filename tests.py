"""Lightweight self-tests for the demo modules."""

import calculator
import string_utils
import temperature
import fibonacci


def run_tests():
    passed = 0
    failed = 0

    def check(label, actual, expected):
        nonlocal passed, failed
        if actual == expected:
            passed += 1
            print(f"  PASS: {label}")
        else:
            failed += 1
            print(f"  FAIL: {label} (got {actual!r}, expected {expected!r})")

    print("Calculator tests:")
    check("add", calculator.add(2, 3), 5)
    check("subtract", calculator.subtract(10, 4), 6)
    check("multiply", calculator.multiply(3, 4), 12)
    check("divide", calculator.divide(9, 3), 3)
    check("power", calculator.power(2, 10), 1024)

    print("String utils tests:")
    check("reverse", string_utils.reverse("abc"), "cba")
    check("is_palindrome", string_utils.is_palindrome("A man a plan a canal Panama"), True)
    check("count_vowels", string_utils.count_vowels("hello"), 2)
    check("to_title_case", string_utils.to_title_case("hello world"), "Hello World")

    print("Temperature tests:")
    check("c_to_f", temperature.celsius_to_fahrenheit(0), 32)
    check("f_to_c", temperature.fahrenheit_to_celsius(212), 100)

    print("Fibonacci tests:")
    check("fib_iterative", fibonacci.fib_iterative(5), [0, 1, 1, 2, 3])
    check("fib_nth", fibonacci.fib_nth(7), 13)

    print(f"\n{passed} passed, {failed} failed")
    return failed == 0


if __name__ == "__main__":
    success = run_tests()
    raise SystemExit(0 if success else 1)
