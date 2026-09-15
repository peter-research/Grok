#!/usr/bin/env python3
"""v0.32 regression extras."""
from __future__ import annotations
import unittest
import grok

class V032Test(unittest.TestCase):
    def test_count_and_version(self) -> None:
        self.assertEqual(len(grok.COMMAND_NAMES), 125)
        self.assertEqual(grok.VERSION, "0.32.0")
        for name in ("palnum", "digits", "prod", "minn", "maxn"):
            self.assertIn(name, grok.COMMAND_NAMES)

    def test_helpers(self) -> None:
        self.assertTrue(grok.is_palnum(121))
        self.assertTrue(grok.is_palnum(-1221))
        self.assertFalse(grok.is_palnum(123))
        self.assertEqual(grok.digit_count(0), 1)
        self.assertEqual(grok.digit_count(-120), 3)
        self.assertEqual(grok.prod_nums([2, 3, 4]), 24)
        self.assertEqual(grok.min_nums([3, 1, 8]), 1)
        self.assertEqual(grok.max_nums([3, 1, 8]), 8)

if __name__ == "__main__":
    unittest.main()
