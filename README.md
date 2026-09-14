# python-basics-25BCON1288

A collection of beginner-level Python programs written as part of coursework.
Covers core fundamentals: loops, functions, conditionals, and classes/OOP.

**Student:** Dhruv
**Roll number:** 25BCON1288

## Programs

| File | What it does | Notes |
|---|---|---|
| `facrorial.py` | Computes the factorial of `n` using a `for` loop and prints the result. | The file reads `n` but never defines it, so it will raise a `NameError` as-is. Set `n` before running (e.g. add `n = 5` at the top). Filename is a typo of `factorial.py`. |
| `fibonacci.py` | Defines a `fibonacci(n)` function that returns the first `n` Fibonacci numbers as a list, and prints the first 10. | Runs standalone; no input needed. |
| `structure.py` | Demonstrates a class (`FactorialData`) by storing `n`, computing its factorial in a loop, and printing the result. | Runs standalone; uses `n = 5`. |
| `prime.py` | Prompts for an integer and reports whether it is prime (checks divisors up to √n). | Interactive — asks for input. |
| `palindrome.py` | Prompts for a word/phrase, strips non-alphanumeric characters, and checks whether it reads the same forwards and backwards. | Interactive — asks for input. |
| `student_class_OOP_Basics.py` | Defines a `Student` class with `name`, `roll`, and `marks`, creates one object, and prints its details. | Runs standalone; demonstrates basic OOP. |

## Getting started

1. Make sure Python 3 is installed (`python3 --version`).
2. Run any program from the repository root:

   ```bash
   python3 fibonacci.py
   python3 prime.py
   python3 palindrome.py
   python3 structure.py
   python3 student_class_OOP_Basics.py
   ```

3. For `facrorial.py`, define `n` first or add a line like `n = 5` before running:

   ```bash
   python3 facrorial.py
   ```

## Dependencies

None. Every program uses only the Python standard library. No `requirements.txt` is needed.

## Audit

See `AUDIT.md` for a claim-by-claim verification of the repository contents, a README benchmark, peer-review notes, and the HW-05 completion checklist.

## Maintainer

Dhruv — 25BCON1288
