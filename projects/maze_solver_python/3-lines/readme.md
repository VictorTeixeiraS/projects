# Drawing some lines

## Point class

Let's make a little `Point` class. It should simply store 2 public data members:

* x - the x-coordinate (horizontal) in pixels of the point
* y - the y-coordinate (vertical) in pixels of the point

`x=0` is the left of the screen.

`y=0` is the top of the screen.

## Line class

The line class has a bit more logic in it. It's constructor should take 2 points as input, and save them as data members.

### draw() method

The `Line` class needs a `draw()` method that takes a `Canvas` and a "fill color" as input. The `fill_color` will just be a string like `"black"` or `"red"`.

Next it should call the [Canvas's](https://tkdocs.com/pyref/canvas.html) `create_line` method.

```python
canvas.create_line(
    x1, y1, x2, y2, fill=fill_color, width=2
)
```

Finally, pack the canvas again, just like you did in the constructor.

## Window class draw_line() method

We need a `draw_line` method on our `Window` class. Tt should take an instance of a `Line` and a `fill_color` as inputs, then call the `Line`'s `draw()` method.

## Update you main function to test your changes

Draw a few lines using your new methods. You'll need to do the drawing after you've created an instance of a `Window`, but before you call `wait_for_close()`.
