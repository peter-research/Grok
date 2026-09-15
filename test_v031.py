#!/usr/bin/env python3
"""v0.31 regression extras."""
from __future__ import annotations
import unittest
import grok

class V031Test(unittest.TestCase):
    def test_count_and_version(self) -> None:
        self.assertEqual(len(grok.COMMAND_NAMES), 120)
        self.assertEqual(grok.VERSION, "0.31.0")
        for name in ("sign", "even", "odd", "abs", "revint"):
            self.assertIn(name, grok.COMMAND_NAMES)

    def test_helpers(self) -> None:
        self.assertEqual(grok.sign_int(5), 1)
        self.assertEqual(grok.sign_int(0), 0)
        self.assertEqual(grok.sign_int(-3), -1)
        self.assertTrue(grok.is_even(0))
        self.assertFalse(grok.is_even(3))
        self.assertTrue(grok.is_odd(-3))
        self.assertFalse(grok.is_odd(4))
        self.assertEqual(grok.abs_int(-12), 12)
        self.assertEqual(grok.abs_int(7), 7)
        self.assertEqual(grok.rev_int(120), 21)
        self.assertEqual(grok.rev_int(-91), -19)

if __name__ == "__main__":
    unittest.main()
