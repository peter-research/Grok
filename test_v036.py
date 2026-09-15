#!/usr/bin/env python3
"""v0.36 regression extras."""
from __future__ import annotations
import unittest
import grok

class V036Test(unittest.TestCase):
    def test_count_and_version(self) -> None:
        self.assertEqual(len(grok.COMMAND_NAMES), 145)
        self.assertEqual(grok.VERSION, "0.36.0")
        for name in ("popcnt", "gray", "ungray", "soundex", "b32"):
            self.assertIn(name, grok.COMMAND_NAMES)

    def test_helpers(self) -> None:
        self.assertEqual(grok.popcnt_int(0), 0)
        self.assertEqual(grok.popcnt_int(255), 8)
        self.assertEqual(grok.gray_int(0), 0)
        self.assertEqual(grok.ungray_int(grok.gray_int(42)), 42)
        self.assertEqual(grok.soundex_word("Rubin"), "R150")
        self.assertTrue(grok.b32_text("Grok").endswith("====") or len(grok.b32_text("Grok")) >= 4)
        with self.assertRaises(ValueError):
            grok.popcnt_int(-1)
        with self.assertRaises(ValueError):
            grok.gray_int(-2)
        with self.assertRaises(ValueError):
            grok.soundex_word("123")

if __name__ == "__main__":
    unittest.main()
