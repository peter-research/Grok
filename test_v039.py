#!/usr/bin/env python3
"""v0.39 regression extras."""
from __future__ import annotations
import unittest
import grok

class V039Test(unittest.TestCase):
    def test_count_and_version(self) -> None:
        self.assertEqual(len(grok.COMMAND_NAMES), 160)
        self.assertEqual(grok.VERSION, "0.39.0")
        for name in ("harshad", "pronic", "totient", "persist", "pentagonal"):
            self.assertIn(name, grok.COMMAND_NAMES)

    def test_helpers(self) -> None:
        self.assertTrue(grok.is_harshad(18))
        self.assertTrue(grok.is_harshad(1729))
        self.assertFalse(grok.is_harshad(11))
        self.assertTrue(grok.is_pronic(0))
        self.assertTrue(grok.is_pronic(12))
        self.assertFalse(grok.is_pronic(7))
        self.assertEqual(grok.euler_totient(1), 1)
        self.assertEqual(grok.euler_totient(10), 4)
        self.assertEqual(grok.euler_totient(9), 6)
        self.assertEqual(grok.multiplicative_persistence(9), 0)
        self.assertEqual(grok.multiplicative_persistence(39), 3)
        self.assertTrue(grok.is_pentagonal(1))
        self.assertTrue(grok.is_pentagonal(5))
        self.assertFalse(grok.is_pentagonal(8))
        with self.assertRaises(ValueError):
            grok.is_harshad(0)
        with self.assertRaises(ValueError):
            grok.euler_totient(0)
        with self.assertRaises(ValueError):
            grok.is_pentagonal(-1)

if __name__ == "__main__":
    unittest.main()
