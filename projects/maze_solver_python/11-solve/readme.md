# Solve the maze

## solve() method

The `solve()` method on the `Maze` class simply calls the `_solve_r` method starting at `i=0` and `j=0`. It should return `True` if the maze was solved, `False` otherwise. This is the same return value as `_solve_r`.

## _solve_r method

I wrote a depth-first first solution to the maze, feel free to do something different if you want. Here were my steps.

The `_solve_r` method returns `True` if the current cell is an end cell, OR if it leads to the end cell. It returns `False` if the current cell is a loser cell.

1. Call the `_animate` method.
2. Mark the current cell as visited
3. If you are at the "end" cell (the goal) then return `True`.
4. For each direction:
   1. If there is a cell in that direction, there is no wall blocking you, and that cell hasn't been visited:
      1. Draw a move between the current cell and that cell
      2. Call `_solve_r` recursively to move to that cell. If that cell returns `True`, then just return `True` and don't worry about the other directions.
      3. Otherwise, draw an "undo" move between the current cell and the next cell
5. If none of the directions worked out, return `False`.

## Update the main function

Call `maze.solve()` in the main function and watch your algorithm do its work!
