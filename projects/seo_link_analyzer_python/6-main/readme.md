# Main

We're finally going to having a running program by the end of this step!

Add a `main.py` file to your project. Our final program will be called on the command line in the following way:

```bash
python3 main.py BASE_URL
```

Where `BASE_URL` is the root URL of the website we want to crawl. For example, my personal blog, `https://wagslane.dev`.

Create a main function that will only execute if it's called as a main function:

```python
#!/usr/bin/python

def main():
    # ?


if __name__ == "__main__":
    main()
```

All your main function should do at this point is:

1. Check to make sure the length of [sys.argv](https://docs.python.org/3/library/sys.html#sys.argv) is `2`. If it isn't, [exit](https://docs.python.org/3/library/constants.html#exit) with code `1`.
2. Print whatever was passed in as a command line arguement to the program (`sys.argv[1]`)
