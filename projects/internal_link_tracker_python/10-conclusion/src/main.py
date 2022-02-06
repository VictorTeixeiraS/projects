#!/usr/bin/python

import sys

from crawl import crawl_page
from report import print_report


def main():
    if len(sys.argv) < 2:
        print("no website provided")
        exit(1)
    root_url = sys.argv[1]

    pages = {}
    pages = crawl_page(root_url, root_url, pages)
    print_report(pages)


if __name__ == "__main__":
    main()
