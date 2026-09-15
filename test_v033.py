#!/usr/bin/env python3
"""v0.33 regression extras."""
from __future__ import annotations
import unittest
import grok

class V033Test(unittest.TestCase):
    def test_count_and_version(self) -> None:
        self.assertEqual(len(grok.COMMAND_NAMES), 130)
        self.assertEqual(grok.VERSION, "0.33.0")
        for name in ("floor", "ceil", "roundn", "mod", "coprime"):
            self.assertIn(name, grok.COMMAND_NAMES)

    def test_helpers(self) -> None:
        self.assertEqual(grok.floor_num(-1.2), -2)
        self.assertEqual(grok.ceil_num(-1.2), -1)
        self.assertEqual(grok.round_num(2.5, 0), 2)
        self.assertEqual(grok.mod_nums(-5, 3), 1)
        self.assertTrue(grok.is_coprime(9, 28))
        self.assertFalse(grok.is_coprime(21, 14))

if __name__ == "__main__":
    unittest.main()
