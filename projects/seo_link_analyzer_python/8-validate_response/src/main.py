#!/usr/bin/python

import sys

from crawl import crawl_page


def main():
    if len(sys.argv) != 2:
        print("no website provided")
        exit(1)
    base_url = sys.argv[1]

    pages = {}
    pages = crawl_page(base_url, pages)
    print(pages)


if __name__ == "__main__":
    main()
