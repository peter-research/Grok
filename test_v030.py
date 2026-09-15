#!/usr/bin/env python3
"""v0.30 regression extras."""
from __future__ import annotations
import unittest
import grok

class V030Test(unittest.TestCase):
    def test_count_and_version(self) -> None:
        self.assertEqual(len(grok.COMMAND_NAMES), 115)
        self.assertEqual(grok.VERSION, "0.30.0")
        for name in ("f2c", "deficient", "square", "cube", "mid"):
            self.assertIn(name, grok.COMMAND_NAMES)

    def test_helpers(self) -> None:
        self.assertAlmostEqual(grok.fahrenheit_to_c(212), 100.0)
        self.assertAlmostEqual(grok.fahrenheit_to_c(32), 0.0)
        self.assertTrue(grok.is_deficient(8))
        self.assertFalse(grok.is_deficient(12))
        self.assertTrue(grok.is_square(16))
        self.assertFalse(grok.is_square(12))
        self.assertEqual(grok.cube_int(3), 27)
        self.assertEqual(grok.cube_int(-2), -8)
        self.assertEqual(grok.mid_text("Grok"), "ro")
        self.assertEqual(grok.mid_text("odd"), "d")
        self.assertEqual(grok.mid_text(""), "")
        with self.assertRaises(ValueError):
            grok.is_deficient(0)
        with self.assertRaises(ValueError):
            grok.is_square(-1)
        with self.assertRaises(ValueError):
            grok.cube_int(100001)

if __name__ == "__main__":
    unittest.main()
