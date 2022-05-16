# Cell draw_move() method

Next we need a way to draw a path between 2 cells. It should draw a line from the *center* of one cell to another. The method definition should look something like this:

```python
def draw_move(self, to_cell, undo=False):
```

The `undo` flag is not set, the line you draw should be `"red"`. Otherwise make it `"gray"`. This is so that when we go to draw the path, whenever we backtrack we can show that in a different color to better visualize what's happening.

Use the x/y coordinates of the 2 cells in question to decide how to draw the line connecting the two cells.
