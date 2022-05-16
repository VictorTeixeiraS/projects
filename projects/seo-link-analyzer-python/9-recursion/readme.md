# Adding recursion

This is going to be the largest step so far, and will require the most "figuring it out own your own". If you get stuck, please reach out in the Discord!

We're going to update the `crawl_page` function to be [recursive](https://blog.boot.dev/javascript/how-to-recursively-traverse-objects/), which means its a function that will call itself. We do this because we want to continue to crawl each URL we find on a page until we've crawled every page on the site.

`crawl_page` will now take 3 arguments: `crawl_page(base_url, url, pages)`

The `current_url` parameter is the current URL we're crawling. In the first call to "crawl_page" this will just be a copy of the `base_url`, but as we go make requests to all the URLs we find on the `base_url`, this value will change.

Here's my pseudo code for the new function:

1. Get a normalized version of the current url
2. If the normalized url doesn't have an entry in the pages dictionary, create one and set it to `0`
3. Parse the base and current URLs. If they don't share a host (`.netloc`), then the current URL isn't on this site, and therefore isn't an internal link. Let's ignore it by setting it's entry in `pages` to `None`
4. If the entry in `pages` for the normalized url is `None` let's return early. Nothing more we should do as this url doesn't concern our users
5. By now, if the entry in `pages` for the normalized url is greater than `0`, it means we've already made a request to this url. If that's the case, let's just increment the count and return, no need to recrawl the page.
6. If we've gotten here, we haven't yet made a request to the current url yet, so let's do that.
7. Let's validate the response. If there are any issues, print the problem, set the value in `pages` for the normalized url to `None` to signify an error with this URL, and return early.
8. Now that we've gotten this far, we can increment the count in `pages` for the `normalized_url`
9. Get all the urls in the html response, and recursively crawl each one
10. Finally, return the updated `pages` dictionary

## Manually test

Give it a shot again! You should now be able to crawl a site and get a dictionary containing the counts of all the internal links!
