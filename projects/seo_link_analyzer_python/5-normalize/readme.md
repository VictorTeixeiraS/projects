# Normalize URLs

Often times you'll find URLs that link to the same page, but are actually different strings. For example, all of these URLs likely will resolve to the same page:

* https://Qvault.io
* http://qvault.io
* http://qvault.io/
* https://qvault.io#header
* https://qvault.io?via=lane

We want to count all these as the "same" URL for the purposes of our SEO tool.

## normalize_url(url)

Write a function that returns a normalized version of an input URL. You should use [urlparse](https://docs.python.org/3/library/urllib.parse.html#url-parsing) from the built-in [urllib.parse](https://docs.python.org/3/library/urllib.parse.html) library.

The way we'll create "normalized URLs" is by

1. Using `urlparse` to get a parsed URL object
2. Concatenating the `.netloc` and `.path` properties of the parsed URL
3. Converting the string to lower case
4. Removing the last character from the string if it's a `/` character

Be sure to write some great unit tests for this function, and feel free to put the function in `crawl.py`
