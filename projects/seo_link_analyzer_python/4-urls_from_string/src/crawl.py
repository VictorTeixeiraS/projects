#!/usr/bin/python

from lxml import html

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

