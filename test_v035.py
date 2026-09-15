#!/usr/bin/env python3
"""v0.35 regression extras."""
from __future__ import annotations
import unittest
import grok

class V035Test(unittest.TestCase):
    def test_count_and_version(self) -> None:
        self.assertEqual(len(grok.COMMAND_NAMES), 140)
        self.assertEqual(grok.VERSION, "0.35.0")
        for name in ("ncr", "npr", "cbrt", "geomean", "xorstr"):
            self.assertIn(name, grok.COMMAND_NAMES)

    def test_helpers(self) -> None:
        self.assertEqual(grok.ncr_nums(0, 0), 1)
        self.assertEqual(grok.ncr_nums(6, 3), 20)
        self.assertEqual(grok.npr_nums(6, 1), 6)
        self.assertEqual(grok.cbrt_int(0), 0)
        self.assertEqual(grok.cbrt_int(26), 2)
        self.assertEqual(grok.geomean_nums([4, 4]), 4.0)
        self.assertEqual(grok.xor_str("AA", "AA"), "\x00\x00")
        with self.assertRaises(ValueError):
            grok.cbrt_int(-8)
        with self.assertRaises(ValueError):
            grok.ncr_nums(-1, 1)
        with self.assertRaises(ValueError):
            grok.xor_str("a", "ab")

if __name__ == "__main__":
    unittest.main()
