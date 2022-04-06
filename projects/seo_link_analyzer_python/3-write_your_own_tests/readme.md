# Writing your own tests

In your coding career, you won't have a teacher or boss writing your tests for you, you'll be writing them yourself! In this step, you'll be writing a new function and the tests for it all on your own.

## sort_pages

Within the same `report.py` file, create a new function called `sort_pages`. It accepts a [dictionary](https://boot.dev/course/f9a25dfb-3e00-4727-ac78-36de82315355/3afd4fce-5c36-4fa2-837b-f71cb1249331)
as input, and returns a sort [list](https://boot.dev/course/f9a25dfb-3e00-4727-ac78-36de82315355/6de00b1c-27e5-4602-8f19-be081c6c49a0) of [tuples](https://www.w3schools.com/python/python_tuples.asp).

For example, the following dictionary:

```python
{
    "first": 45,
    "third": 15,
    "second": 25
}
```

Would become:

```python
[
    ("first", 45),
    ("second", 25),
    ("third", 15)
]
```

We are sorting by the values in the dictionary, where the highest values come first in the list.

## Sorting

Take a look at Python's built-in [sort method](https://www.w3schools.com/python/ref_list_sort.asp). Particularly the optional "key" and "reverse" parameters, I ended up using both of those options.

`list.sort(reverse=True|False, key=myFunc)`

* `reverse`: Optional. reverse=True will sort the list descending. Default is reverse=False
* `key`: Optional. A function to specify the sorting criteria(s)
