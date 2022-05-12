# Cell class

When you think of our maze, you can think of each little box in the grid as an individual "Cell" with 4 potential walls. We start in one cell, and we're allowed to move to an adjacent cell as long as there isn't a wall in the way.

Let's build a `Cell` class that holds all the data about an individual cell. It should know which walls it has, where it exists on the canvas in x/y coordinates, and access to the window so that it can draw itself.

Personally, I used the following data members:

* has_left_wall
* has_right_wall
* has_top_wall
* has_bottom_wall
* _x1
* _x2
* _y1
* _y2
* _win

Each wall should exist by default. It's a public data member though, so can be modified on each individual instance.

## draw() method

The `Cell` class needs to be able to draw itself to its canvas. It should take the x/y coordinates of its top-left corner, and its bottom-right corner as input.

If the cell has a left wall, draw it.

If the cell has a top wall, draw it, and so on and so forth for each wall.

## Update main to test your changes

Now, instead of drawing a couple lines, create a few cells and draw them! Draw some cells with different numbers of walls, etc. Make sure to test out all the various configurations you can think of.
