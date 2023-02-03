# Bookbot - Read file

Now that you've got your machine all configured, let's build "bookbot"! Bookbot is a simple command-line program that reads text from a file and generates a report about the text.

## Download "Frankenstein" by Mary Shelley (it's public domain)

You can find the [full text here](https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt).

Create a directory in your `bookbot` project called `books` and then add `frankenstein.txt` to it.

## Use a .gitignore file to ignore the "books" directory

We don't want to save *entire* book in our source code. Imagine if Microsoft Word's source code included all the *documents* it could operate on. Generally speaking, Git is for *code*, not for *data*.

Create a `.gitignore` file in the root of your project and add this text to it:

```
books/
```

You should see the filename turn dark gray in your VS Code file explorer. Now, whenever you run `git add .` all the files in the `books` directory will be automatically ignored!

## Read the book

Change `main.py` so that instead of printing "hello world", it reads the contents of the "frankenstein.txt" and prints it *all* to the console.

## Hints

Use a [with](https://builtin.com/software-engineering-perspectives/what-is-with-statement-python) block to open a file:

```py
with open(path_to_file) as f:
    # ...
```

Keep in mind that `path_to_file` needs to be relative to wherever you're running the program from. If you're running the program from the root of your project, you would probably use `books/frankenstein.txt`.

Once you have an open file, read the contents into a string:

```py
file_contents = f.read()
```
