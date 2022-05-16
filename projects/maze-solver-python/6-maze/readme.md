# Maze class

To start, let's create a class that holds all the cells in the maze in a 2-dimensional grid, a list of lists.

I wrote my constructor to have the following signature:

```python
def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
```

It initializes data members fot all it's inputs, then calls its `_create_cells() method`

## _create_cells()

This method should fill a `self._cells` list with lists of cells. Each top-level list is a column of `Cell` objects. Once matrix is populated it should call its `_draw_cell()` method on each `Cell`.

## _draw_cell(self, i, j):

This method should calculate the x/y position of the `Cell` based on `i`, `j`, the `cell_size`, and the x/y position of the Maze itself. The x/y position of the maze represents how many pixels from the top and left the maze should start from the side of the window.

Once that's calculated, it should draw the cell and call the maze's `_animate()` method.

## _animate(self)

The animate method is what allows us to visualize what are algorithms are doing in real time. It should simply call the window's `redraw()` method, then sleep for a short amount of time so your eyes keep up with each render frame. I slept for `0.05` seconds.
