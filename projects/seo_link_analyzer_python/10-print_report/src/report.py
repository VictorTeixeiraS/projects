# print_report takes a dictionary of pages and prints them
# to the console in a human-friendly way
def print_report(pages):
    pages = remove_none_values(pages)
    pages_list = sort_pages(pages)
    for page in pages_list:
        url = page[0]
        count = page[1]
        print("Found {} internal links to {}".format(count, url))


# remove_none_values removes all keys from a dictionary
# where the value was None
def remove_none_values(dict):
    keys_to_delete = []
    for key, value in dict.items():
        if value is None:
            keys_to_delete.append(key)
    for key_to_delete in keys_to_delete:
        del dict[key_to_delete]
    return dict


def page_tuple_key(page_tuple):
    return page_tuple[1]


# sort_pages sorts a dictionary of pages
# into a list of tuples (url, count)
# with the highest counts first in the list
def sort_pages(pages):
    pages_list = []
    for url, count in pages.items():
        pages_list.append((url, count))
    pages_list.sort(key=page_tuple_key, reverse=True)
    return pages_list
