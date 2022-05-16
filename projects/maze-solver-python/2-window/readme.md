# Create a "Window" class using Tkinter

Our first step will simply be to get a graphical window up and running. When we run our program, it should open a new window with a blank canvas that the program will then draw on. We will be using Python 3's built-in [Tkinter](https://docs.python.org/3/library/tkinter.html) library for this.

First, create a `Window` class. You'll need to import a few things from `tkinter`.

```python
from tkinter import Tk, BOTH, Canvas
```

## Window class's constructor

1. The constructor should take a `width` and `height`. This will be the size of the new window we create in pixels.
2. It should create a new root widget using `Tk()` and save it as a data member
3. Set the `title` property of the root widget
4. Create a [`Canvas`](https://tkinter-docs.readthedocs.io/en/latest/widgets/canvas.html#) and save it as a data member.
5. [Pack](https://docs.python.org/3/library/tkinter.html#the-packer) the canvas so that it's ready to be drawn
6. Create a data member to represent that the window is "running", and set it to `False`

## redraw() method

We need a method we can call that will redraw all the graphics in the window. Tkinter is *not* a reactive framework like React or Vue - we need to tell the window when it should render to visuals.

The `redraw()` method on the window class should simply call the root widget's [`update_idletasks()` and `update()`](https://tkdocs.com/pyref/tk.html) methods. Each time this is called, the window will redraw itself.

## wait_for_close() method

This method should set the data member we created to track the "running" state of the window to `True`. Next, it should call `self.redraw()` over and over as long as the running state remains `True`.

## The close() method

Lastly, the `close()` method should simply set the running state to `False`. You'll also need to add another line to constructor to call the `protocol` method on the root widget, to connect your `close` method to the "delete window" action. This will stop your program from running when you close the graphical window.

```python
self.__root = Tk()
...
self.__root.protocol("WM_DELETE_WINDOW", self.close)
```

## Main

In your main function, create a window and wait for it to close.

```python
win = Window(800, 600)
win.wait_for_close()
```
