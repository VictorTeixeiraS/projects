# Breaking down walls in the maze

This next one we can easily write a unit test for as well.

## _break_entrance_and_exit

The entrance to the maze will always be at the top of the top-left cell, the exit always at the bottom of the bottom-right cell.

Add a `_break_entrance_and_exit()` method that removes the walls from those cells, and calls `_draw_cell()` after each removal.

Next, write another unit test to ensure it's working.

## Draw the removed walls

You may have noticed that if you run your code graphically, it doesn't *appear* to be removing the walls. That's because they were already drawn to the canvas, and removing the wall in memory doesn't update the canvas. My recommendation is to simply update the `draw()` method in your `Cell` class to draw a `"white"` line (same color as the background) for walls that don't exist instead of doing nothing.

Now when you run your code it should remove the entrance and exit walls visually.
