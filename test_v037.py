#!/usr/bin/env python3
"""v0.37 regression extras."""
from __future__ import annotations
import unittest
import grok

class V037Test(unittest.TestCase):
    def test_count_and_version(self) -> None:
        self.assertEqual(len(grok.COMMAND_NAMES), 150)
        self.assertEqual(grok.VERSION, "0.37.0")
        for name in ("isogram", "vowels", "cons", "rotl", "rotr"):
            self.assertIn(name, grok.COMMAND_NAMES)

    def test_helpers(self) -> None:
        self.assertTrue(grok.is_isogram("isogram"))
        self.assertFalse(grok.is_isogram("letter"))
        self.assertEqual(grok.count_vowels("AeIoU"), 5)
        self.assertEqual(grok.count_cons("rhythm"), 6)
        self.assertEqual(grok.rotate_left("abcd", 1), "bcda")
        self.assertEqual(grok.rotate_right("abcd", 1), "dabc")
        self.assertEqual(grok.rotate_left("ab", 2), "ab")
        with self.assertRaises(ValueError):
            grok.is_isogram("123")

if __name__ == "__main__":
    unittest.main()
