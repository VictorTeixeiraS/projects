#!/usr/bin/python

from lxml import html
from urllib.parse import urlparse


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
    netloc_path = f"{parsed_url.netloc}{parsed_url.path}"
    lowercased = netloc_path.lower()
    if len(lowercased) < 1:
        return lowercased
    last_slash_removed = lowercased if lowercased[-1] != "/" else lowercased[:-1]
    return last_slash_removed
