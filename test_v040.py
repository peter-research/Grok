#!/usr/bin/env python3
"""v0.40 regression extras."""
from __future__ import annotations
import unittest
import grok

class V040Test(unittest.TestCase):
    def test_count_and_version(self) -> None:
        self.assertGreaterEqual(len(grok.COMMAND_NAMES), 160)
        self.assertGreaterEqual(tuple(int(x) for x in grok.VERSION.split(".")), (0, 40, 0))
        for name in ("hexagonal", "happy", "kaprekar", "catalan", "aliquot"):
            self.assertIn(name, grok.COMMAND_NAMES)

    def test_helpers(self) -> None:
        self.assertTrue(grok.is_hexagonal(1))
        self.assertTrue(grok.is_hexagonal(45))
        self.assertFalse(grok.is_hexagonal(8))
        self.assertTrue(grok.is_happy(19))
        self.assertTrue(grok.is_happy(1))
        self.assertFalse(grok.is_happy(4))
        self.assertTrue(grok.is_kaprekar(1))
        self.assertTrue(grok.is_kaprekar(9))
        self.assertTrue(grok.is_kaprekar(297))
        self.assertFalse(grok.is_kaprekar(11))
        self.assertEqual(grok.catalan_n(0), 1)
        self.assertEqual(grok.catalan_n(3), 5)
        self.assertEqual(grok.catalan_n(5), 42)
        self.assertEqual(grok.aliquot_sum(1), 0)
        self.assertEqual(grok.aliquot_sum(6), 6)
        self.assertEqual(grok.aliquot_sum(12), 16)
        with self.assertRaises(ValueError):
            grok.is_hexagonal(0)
        with self.assertRaises(ValueError):
            grok.is_happy(0)
        with self.assertRaises(ValueError):
            grok.catalan_n(31)

if __name__ == "__main__":
    unittest.main()
