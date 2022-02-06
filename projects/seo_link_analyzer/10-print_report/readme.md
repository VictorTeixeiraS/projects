# Print a report

We're almost done, we've done all the hard parts! All we need to do now is clean up the output so that it's more human readable.

Let's add a `print_report(pages)` function to `report.py` and import it in `main`.

It should remove all the `None` values from the pages dictionary, sort the pages according to the counts, then iterate over each one and print something like:

```
Found {X} internal links to {URL}
```

for each remaining entry.
