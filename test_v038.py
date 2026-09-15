#!/usr/bin/env python3
"""v0.38 regression extras."""
from __future__ import annotations
import unittest
import grok

class V038Test(unittest.TestCase):
    def test_count_and_version(self) -> None:
        self.assertEqual(len(grok.COMMAND_NAMES), 155)
        self.assertEqual(grok.VERSION, "0.38.0")
        for name in ("armstrong", "nextprime", "binarygap", "harmonic", "twins"):
            self.assertIn(name, grok.COMMAND_NAMES)

    def test_helpers(self) -> None:
        self.assertTrue(grok.is_armstrong(153))
        self.assertTrue(grok.is_armstrong(9474))
        self.assertFalse(grok.is_armstrong(100))
        self.assertEqual(grok.next_prime(1), 2)
        self.assertEqual(grok.next_prime(13), 17)
        self.assertEqual(grok.binary_gap(9), 2)
        self.assertEqual(grok.binary_gap(8), 0)
        self.assertAlmostEqual(grok.harmonic_n(2), 1.5)
        self.assertTrue(grok.is_twin_prime(11))
        self.assertFalse(grok.is_twin_prime(13))
        with self.assertRaises(ValueError):
            grok.is_armstrong(-1)
        with self.assertRaises(ValueError):
            grok.binary_gap(0)

if __name__ == "__main__":
    unittest.main()
