# Unittests and integration tests

---

A unit test is a type of software testing that focuses on verifying the correctness of individual units or components of a program. The goal of unit testing is to validate that each unit of the software performs as expected.

### Key Characteristics of Unit Tests:

1. *Isolation*: Unit tests are designed to test a single "unit" of code, usually a function or method, in isolation from the rest of the application. Dependencies are often mocked or stubbed out.

2. *Automation*: Unit tests are typically automated, allowing them to be run frequently to catch regressions early in the development process.

3. *Repeatability*: They can be run multiple times with the same input data to ensure consistent results, making it easier to track down issues.

4. *Fast Execution*: Unit tests should be quick to execute, providing immediate feedback to developers.

5. *Granularity*: They test the smallest possible units of code, often leading to a high level of granularity in testing.

6. *Coverage*: A well-designed suite of unit tests should cover a large percentage of the code base, helping to ensure that the software behaves as expected under various conditions.

### Benefits of Unit Testing:

- *Early Bug Detection*: Unit tests can help identify bugs and errors at an early stage of the development cycle.
  
- *Simplified Debugging*: Since tests are isolated, it is easier to pinpoint the source of a bug.

- *Facilitates Refactoring*: With a comprehensive set of unit tests, developers can confidently refactor code knowing that tests will catch any introduced errors.

- *Documentation*: Unit tests can serve as documentation for the intended behavior of the code.

### Example in Python:

This is a simple example using Python's `unittest` framework to test a function that adds two numbers this same function was used in some of my program.

```python
import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)
        
    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
```

### Tools and Frameworks:

There are numerous tools but to this repo we will settle for:

- *Python*: `unittest`, `pytest`

Unit testing is a fundamental part of the Test-Driven Development (TDD) process, where tests are written before the actual code. This practice helps ensure that the code is designed to meet its requirements from the outset.
