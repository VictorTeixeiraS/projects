#!/usr/bin/python

from lxml import html
import requests
from urllib.parse import urlparse


def crawl_page(base_url, pages):
    # Make a request to the URL
    resp = requests.get(base_url)

    # If the response isn't a a valid page, log
    # and skip it now and in the future
    try:
        validate_response(resp, base_url)
    except Exception as e:
        print(e)
        return pages

    # Scan the page and crawl each link found
    urls = get_urls_from_string(resp.content, base_url)
    for url in urls:
        pages[url] = 1

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
def get_urls_from_string(page_content, base_url):
    urls = []
    tree = html.fromstring(page_content)
    tree.make_links_absolute(base_url=base_url)
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
