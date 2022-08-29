# Break all the walls

Next we need to break down enough walls that the maze is fun and challenging while also ensuring that there is a correct path from the start to the end.

## Seed your randomness

We will be using random number generation to create our maze, that way it's fun and different each time.

However, it can be tough to debug your application if each time you run it, it behaves slightly differently. I recommend adding another optional parameter to the `Maze` class constructor called `seed` that defaults to `None`. Then, in your constructor, if the `seed` isn't `None` you call [`random.seed(seed)`](https://docs.python.org/3/library/random.html#random.seed).

The purpose of providing a fixed seed, say `0`, is that it will ensure you *always* get the same "random" numbers. Once you're done debugging and want randomness for your application, just can just leave the `seed` parameter blank in `main`.

## A Cell's visited data member

Add a new data member to the cell class called `visited` and initialize it to `False`. This is how we'll track which cells have had their walls broken.

## _break_walls_r(self, i, j)

The recursive `break_walls_r` method is a breadth-first traversal through the cells, breaking down walls as it goes. I'll describe the algorithm I used, but feel free to write your own from scratch if you're up to it!

1. Mark the current cell as visited
2. In a loop:
   1. Create a new empty list which will hold the `i` and `j` values you need to visit
   2. Check the cells that are directly adjacent to the current cell. If one isn't visited, keep track of it as a "possible direction" that you can move in.
   3. If there are no directions you can go from the current cell, then draw the current cell and `return` to break out of the loop
   4. Otherwise, pick a [random](https://docs.python.org/3/library/random.html#random.randrange) direction.
   5. Knock down the walls between the current cell and the chosen cell.
   6. Move to the chosen cell by recursively calling `_break_walls_r`
