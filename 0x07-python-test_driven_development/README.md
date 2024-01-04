![Test_meme](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/246/giphy-4.gif)
# Test Driven Development (TDD) in Python

## Introduction

Test Driven Development (TDD) is a software development methodology where tests are written before the actual code. In Python, TDD is a common practice to ensure code reliability, maintainability, and ease of collaboration.

## Benefits of TDD

1. **Early Detection of Issues:** TDD allows early identification of defects, making it easier to fix problems at the beginning of the development process.

2. **Improved Code Quality:** Writing tests first helps in designing modular and well-structured code.

3. **Documentation:** Test cases serve as executable documentation, making it easier for developers to understand the expected behavior of functions and modules.

## TDD Workflow

1. **Write a Test:** Create a test case that defines the expected behavior of the code.

    ```python
    def test_add_integer():
        assert add_integer(3, 5) == 8
        assert add_integer(2.5, 3.5) == 5
        # Add more test cases
    ```

2. **Run the Test:** Execute the test to ensure it fails, as the code being tested does not exist yet.

    ```bash
    $ pytest test_module.py
    ```

3. **Write Code:** Implement the code necessary to make the test pass.

    ```python
    def add_integer(a, b=98):
        """Return the integer addition of a and b."""
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer or float")
        if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer or float")
        return int(a) + int(b)
    ```

4. **Run Tests Again:** Execute the tests to ensure that the new code passes all test cases.

    ```bash
    $ pytest test_module.py
    ```

5. **Refactor (if needed):** Refactor the code to improve its structure without changing its behavior.

6. **Repeat:** Repeat the process for the next feature or functionality.

## Using Doctest

Doctest is a built-in module in Python that allows you to include test cases in your docstrings. This promotes self-testing documentation.

Example:

```python
def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.

    Examples:
        >>> add_integer(3, 5)
        8
        >>> add_integer(2.5, 3.5)
        5
        >>> add_integer('a', 5)
        Traceback (most recent call last):
            ...
        TypeError: a must be an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)

When running `doctest`:
```python3 -m doctest -v your_module.py
```
Doctest will execute the examples in your docstrings and report any discrepancies.
