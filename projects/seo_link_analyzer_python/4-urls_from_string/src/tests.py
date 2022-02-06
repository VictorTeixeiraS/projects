import unittest

from report import remove_none_values, sort_pages
from crawl import get_urls_from_string


class Tests(unittest.TestCase):
    def test_remove_none_values(self):
        self.assertEqual({}, remove_none_values({"1": None}))
        self.assertEqual({"1": "1"}, remove_none_values({"1": "1", "2": None}))
        self.assertEqual({}, remove_none_values({}))
        self.assertEqual({"1": "1"}, remove_none_values({"1": "1"}))

    def test_sort_pages(self):
        self.assertEqual(
            [("0", 45), ("1", 35), ("2", 25), ("3", 0)],
            sort_pages({"3": 0, "1": 35, "2": 25, "0": 45}),
        )
        self.assertEqual(
            [("0", 3), ("1", 2), ("2", 1), ("3", 0)],
            sort_pages({"3": 0, "1": 2, "2": 1, "0": 3}),
        )
        self.assertEqual(
            [],
            sort_pages({}),
        )

    def test_get_urls_from_string(self):
        self.assertEqual(
            ["https://qvault.io"],
            get_urls_from_string(
                '<html><body><a href="https://qvault.io"><span>Qvault></span></a></body></html>',
                "https://qvault.io",
            ),
        )
        self.assertEqual(
            ["https://qvault.io", "https://wagslane.dev"],
            get_urls_from_string(
                '<html><body><a href="https://qvault.io"><span>Qvault></span></a><a href="https://wagslane.dev"><span>Qvault></span></a></body></html>',
                "https://qvault.io",
            ),
        )


if __name__ == "__main__":
    unittest.main()
