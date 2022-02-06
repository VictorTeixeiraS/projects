# Validate responses

We need to make our crawler a little more robust. Right now, if `crawl_page` makes a request to a URL that results in anything other than a successful HTML page, our program will crash or have unexpected behavior.

## validate_response(resp, url)

Write a function called `validate_response` that:

1. Checks the [status code](https://docs.python-requests.org/en/latest/user/quickstart/#response-status-codes) on the response. If it's not `200`, raise an Exception that explains what the problem was.
2. Checks the [content-type header](https://docs.python-requests.org/en/latest/user/quickstart/#response-headers) in the response. If it doesn't contain the string `text/html`, raise an [Exception](https://pythonbasics.org/try-except/) explaining the problem.
3. If niether of those things happen, do nothing

Call `validate_response` within a [try/except block](https://pythonbasics.org/try-except/) in `crawl_page`. If there is an Exception caught, print the exception and return the current `pages` variable.

## Test it manually

Test this out manually by calling your program with a page that isn't HTML, or that doesn't return a `200`. For example, `python3 main.py https://wagslane.dev/index.xml`
