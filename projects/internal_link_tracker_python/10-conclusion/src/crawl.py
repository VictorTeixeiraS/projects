#!/usr/bin/python

from lxml import html
import requests
from urllib.parse import urlparse


def crawl_page(root_url, url, pages):
    normalized_url = normalize_url(url)

    # This is a new page, create an entry for it
    if normalized_url not in pages:
        pages[normalized_url] = 0

    # If this URL is offsite, skip it
    if urlparse(root_url).netloc != urlparse(url).netloc:
        pages[normalized_url] = None
        return pages

    # If this is a page we've already checked
    # and it is invalid skip it
    if pages[normalized_url] is None:
        return pages

    # If we've already validated this page
    # increase the count and skip
    if pages[normalized_url] > 0:
        pages[normalized_url] += 1
        return pages

    # Make a request to the URL
    resp = requests.get(url)

    # If the response isn't a a valid page, log
    # and skip it now and in the future
    try:
        validate_response(resp, url)
    except Exception as e:
        print(e)
        pages[normalized_url] = None
        return pages

    # Increment the count for this page
    pages[normalized_url] += 1

    # Scan the page and crawl each link found
    urls = get_urls_from_string(resp.content, root_url)
    for url in urls:
        crawl_page(root_url, url, pages)

    return pages


def validate_response(resp, url):
    if resp.status_code != 200:
        raise Exception(
            "{} didn't result in a 200 response code, got {}".format(
                url, resp.status_code
            )
        )

    # If the content type isn't HTML skip it
    if "text/html" not in resp.headers["content-type"].lower():
        raise Exception("{} didn't result in an HTML response".format(url))


# get_urls_from_string scans through a string,
# finds all the links, and returns the urls in a list
def get_urls_from_string(page_content, root_url):
    urls = []
    tree = html.fromstring(page_content)
    tree.make_links_absolute(base_url=root_url)
    for elem in tree.iter():
        if elem.tag == "a":
            url = elem.get("href")
            urls.append(url)
    return urls


# normalize_url returns a "normalized" URL that can be used to
# deduplicate URLs which resolve to the same web page
def normalize_url(url):
    parsed_url = urlparse(url)
    netloc_path = "{}{}".format(parsed_url.netloc, parsed_url.path)
    lowercased = netloc_path.lower()
    if len(lowercased) < 1:
        return lowercased
    last_slash_removed = lowercased if lowercased[-1] != "/" else lowercased[:-1]
    return last_slash_removed
