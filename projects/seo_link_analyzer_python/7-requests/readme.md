# Crawl the page

Let's start actually crawling real webpages! For these remaining steps, you'll need a website you can crawl. Preferably a small one with less than 100 pages so the crawling doesn't take all day. You can use my personal blog, `https://wagslane.dev` if you don't have another in mind.


## Add the "requests" library as a dependency

`requests == 2.27.1`

## crawl_page(base_url, url, pages)

Create a `crawl_page` function in `crawl.py`  that takes a base URL (the root of the site we're going to crawl), and a dictionary called `pages`. The `pages` dictionary will store the URLs we've found as keys, and the number of times we've seen them as values.

For now, your function should:

1. Use [requests.get](https://docs.python-requests.org/en/latest/) to fetch the webpage of the `base_url`
2. Use `get_urls_from_string` to get all the URLs in the page
3. Create an entry for each URL found in `pages` and set the count to `1`
4. Return the `pages`

## main.py

Import `crawl_page` into your main function, and call it with the `base_url` passed in and an empty dictionary. Save the new returned dictionary and print it. Give your program a shot! It should print a dictionary to the console with all the URLs found on the page you crawled.
