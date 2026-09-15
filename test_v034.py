#!/usr/bin/env python3
"""v0.34 regression extras."""
from __future__ import annotations
import unittest
import grok

class V034Test(unittest.TestCase):
    def test_count_and_version(self) -> None:
        self.assertEqual(len(grok.COMMAND_NAMES), 135)
        self.assertEqual(grok.VERSION, "0.34.0")
        for name in ("hypot", "lcm", "isqrt", "median", "powint"):
            self.assertIn(name, grok.COMMAND_NAMES)

    def test_helpers(self) -> None:
        self.assertEqual(grok.hypot_nums(5, 12), 13.0)
        self.assertEqual(grok.lcm_nums(0, 5), 0)
        self.assertEqual(grok.isqrt_num(0), 0)
        self.assertEqual(grok.median_nums([4, 1, 3, 2]), 2.5)
        self.assertEqual(grok.pow_int(3, 4), 81)
        with self.assertRaises(ValueError):
            grok.isqrt_num(-1)
        with self.assertRaises(ValueError):
            grok.pow_int(2, -1)

if __name__ == "__main__":
    unittest.main()
