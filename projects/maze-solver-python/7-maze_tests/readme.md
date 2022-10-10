# Maze tests

Unit tests are generally a great idea. Let's add a couple. In order to be able to test some of our `Maze` class's methods, we need to be able to run the logic without actually drawing anything graphically. We want to test the *logic*, not the *visuals* at this point.

First, make the `Window` parameter to the `Cell` and `Maze` class optional, and have it default to `None`.

## Writing tests in Python

First, create a `tests.py` file. We'll be using the [unittest](https://docs.python.org/3/library/unittest.html) package for our testing, so add the following to the top of `tests.py`:

```py
import unittest
```

Next, import your `Maze` code:

```py
from maze import Maze
```

Then create a simple test:

```py
class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
```

Add some code to make the tests run:

```py
if __name__ == "__main__":
    unittest.main()
```

Finally, run your tests:

```bash
python tests.py
```

If everything worked with that one test, great! Add a couple more tests to make sure your maze constructor works under different conditions. You can do so by adding new methods to the `Tests` class. Your new tests should create a new maze but use different numbers of rows and columns. Use the [assertEqual](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual) method again to check that everything worked.
