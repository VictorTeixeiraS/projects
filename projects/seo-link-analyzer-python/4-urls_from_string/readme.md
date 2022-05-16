# Dependencies and URL extraction

Our link tracker will need to know how to read a page of [HTML](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics) text and extract links.

For example, the following HTML page has a single link to `https://blog.boot.dev`:

```html
<html>
    <body>
        <a href="https://blog.boot.dev"><span>Go to Boot.dev</span></a>
    </body>
</html>
```

We want to write a new function called `get_urls_from_string` in a new file called `crawl.py` that takes a string of HTML as input and returns a list of all the link URLs. To do so, we'll use a third-party HTML parsing library called [lxml](https://lxml.de/).

## Virtual environment

I highly recommend using a virtual environment for all your Python projects. It allows you to keep your installations of third party libraries like `lxml` separate for each project. Without `venv`, if you update a version `lxml` in one projet on your computer, it will update it for all your other projects, potentially breaking them!

* Create a new virtual environment in your project called `venv` by typing `python3 -m venv venv`
* Add `venv/` to your [gitignore](https://www.freecodecamp.org/news/gitignore-what-is-it-and-how-to-add-to-repo/) so it isn't saved as source code
* Activate your virtual environment by typing `source venv/bin/activate`
* You should see something like "(venv)" in your shell which means you activated successfully

## Installing lxml

Now that you're in a virtual environment, let's install lxml there. We want to track our dependencies in our source code, so create a new file called `requirements.txt`. This is the standard way to track dependencies in Python.
On the first line, type `lxml == 4.7.1`. Which means we are adding `lxml` version `4.7.1` as a dependency. Now install it by typing `pip3 install -r requirements.txt`.

## get_urls_from_string

Now that we have lxml, we can use it by adding `from lxml import html` to the top of our new `crawl.py` file.

`get_urls_from_string(page_content, base_url)` takes 2 arguments. The first is an HTML string like we discussed earlier, the second is the root URL of the website we're crawling. This will allow us to rewrite [relative URLs into absolute URLs](https://www.seoclarity.net/resources/knowledgebase/difference-relative-absolute-url-15325/).

## Some additional information

1. Use the [html.fromstring](https://lxml.de/apidoc/lxml.html.html#lxml.html.fromstring) method to get a document tree.
2. Use the tree's [make_links_absolute](https://lxml.de/apidoc/lxml.html.html#lxml.html.HtmlMixin.make_links_absolute) method to convert all the links in the tree to absolute URLs.
3. Use the tree's iter() method, `for elem in tree.iter():` to iterate over each HTML tag.
4. If an element is a link, which you can check by making sure it's `.tag` property is "a", append the URL to a list that you'll return at the end of the function. You can get the URL from the element using the `.get()` method: `elem.get("href")`.

## Tests

Here are some example tests for this function. Feel free to add more.

```python
def test_get_urls_from_string(self):
    self.assertEqual(
        ["https://blog.boot.dev"],
        get_urls_from_string(
            '<html><body><a href="https://blog.boot.dev"><span>Boot.dev></span></a></body></html>',
            "https://blog.boot.dev",
        ),
    )
    self.assertEqual(
        ["https://blog.boot.dev", "https://wagslane.dev"],
        get_urls_from_string(
            '<html><body><a href="https://blog.boot.dev"><span>Boot.dev></span></a><a href="https://wagslane.dev"><span>Boot.dev></span></a></body></html>',
            "https://blog.boot.dev",
        ),
    )
```
