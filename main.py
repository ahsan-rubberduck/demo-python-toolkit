"""CLI entry point that ties the demo modules together."""

import calculator
import string_utils
import temperature
import fibonacci


def main():
    print("=== Demo Python Toolkit ===\n")

    print("Calculator:")
    print(f"  2 + 3       = {calculator.add(2, 3)}")
    print(f"  10 / 4      = {calculator.divide(10, 4)}")
    print(f"  2 ** 8      = {calculator.power(2, 8)}\n")

    print("String utils:")
    print(f"  reverse('hello')          = {string_utils.reverse('hello')}")
    print(f"  is_palindrome('Racecar')  = {string_utils.is_palindrome('Racecar')}")
    print(f"  count_vowels('education') = {string_utils.count_vowels('education')}\n")

    print("Temperature:")
    print(f"  100C -> F = {temperature.celsius_to_fahrenheit(100)}")
    print(f"  32F  -> C = {temperature.fahrenheit_to_celsius(32)}\n")

    print("Fibonacci:")
    print(f"  first 10  = {fibonacci.fib_iterative(10)}")
    print(f"  10th      = {fibonacci.fib_nth(10)}")


if __name__ == "__main__":
    main()
