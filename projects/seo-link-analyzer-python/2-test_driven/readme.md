# Test driven development

"Test driven development" is a popular method of writing software. The idea is that you write tests for your code *first*, then you write the code that gets the tests to pass. We're going to approach this project using TDD.

In this step, we'll be writing a function that removes all keys in a  [dictionary](https://boot.dev/course/f9a25dfb-3e00-4727-ac78-36de82315355/3afd4fce-5c36-4fa2-837b-f71cb1249331) that have `None` as their value.

## tests.py

You'll need a `tests.py` file and a `report.py` file in the root of your project directory to start. We'll be using the [unittest](https://docs.python.org/3/library/unittest.html) package for our testing, and you can copy these tests I've provided into your `tests.py` file.

```python
import unittest

from report import remove_none_values


class Tests(unittest.TestCase):
    def test_remove_none_values(self):
        self.assertEqual({}, remove_none_values({"1": None}))
        self.assertEqual({"1": "1"}, remove_none_values({"1": "1", "2": None}))
        self.assertEqual({}, remove_none_values({}))
        self.assertEqual({"1": "1"}, remove_none_values({"1": "1"}))


if __name__ == "__main__":
    unittest.main()
```

## report.py

This file will house our functions that will generate the internal linking report that we'll eventually be printing to the console for our users. For now, you just need to write a function called `remove_none_values` that passes the test cases.

`remove_none_values(dict)` takes a dictionary as input, and scans each key/value pair, removing any keys from the dictionary that have an associated `None` value.

## Run your tests

To run your tests, type `python3 test.py` into the console. You should get a message saying `OK` if your tests passsed.
