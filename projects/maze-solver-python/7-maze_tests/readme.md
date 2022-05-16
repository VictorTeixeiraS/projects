# Maze tests

Unit tests are generally a great idea. Let's add a couple. In order to be able to test some of our `Maze` class's methods, we need to be able to run the logic without actually drawing anything graphically. We want to test the logic, not the visuals at this point.

First, make the `Window` parameter to the `Cell` and `Maze` class optional, and have it default to `None`.

Next, create a `tests.py` file with a unit test for the `create_cells` method. It should ensure that `self._cells` has the right number of cells after initialization. If you can't remember the syntax for tests, refer back to your code from the [SEO Link Analyzer project](https://boot.dev/project/59fbb2aa-7d67-4e88-bac8-42f49798a9f5/4a7010c1-e7d3-4cc5-9b1b-d1f4e9f9ce81).

Finally, run your tests.

```bash
python tests.py
```
