#!/usr/bin/env python3
"""v0.41 regression extras."""
from __future__ import annotations
import unittest
import grok

class V041Test(unittest.TestCase):
    def test_count_and_version(self) -> None:
        self.assertEqual(len(grok.COMMAND_NAMES), 165)
        self.assertEqual(grok.VERSION, "0.41.0")
        for name in ("smith", "automorphic", "lucas", "squarefree", "duck"):
            self.assertIn(name, grok.COMMAND_NAMES)

    def test_helpers(self) -> None:
        self.assertTrue(grok.is_smith(4))
        self.assertTrue(grok.is_smith(22))
        self.assertFalse(grok.is_smith(7))
        self.assertTrue(grok.is_automorphic(0))
        self.assertTrue(grok.is_automorphic(1))
        self.assertTrue(grok.is_automorphic(5))
        self.assertTrue(grok.is_automorphic(25))
        self.assertTrue(grok.is_automorphic(76))
        self.assertFalse(grok.is_automorphic(26))
        self.assertEqual(grok.lucas_n(0), 2)
        self.assertEqual(grok.lucas_n(1), 1)
        self.assertEqual(grok.lucas_n(2), 3)
        self.assertEqual(grok.lucas_n(5), 11)
        self.assertTrue(grok.is_squarefree(1))
        self.assertTrue(grok.is_squarefree(10))
        self.assertFalse(grok.is_squarefree(12))
        self.assertFalse(grok.is_squarefree(18))
        self.assertFalse(grok.is_duck(0))
        self.assertTrue(grok.is_duck(10))
        self.assertTrue(grok.is_duck(101))
        self.assertFalse(grok.is_duck(123))
        with self.assertRaises(ValueError):
            grok.is_smith(3)
        with self.assertRaises(ValueError):
            grok.lucas_n(91)
        with self.assertRaises(ValueError):
            grok.is_squarefree(0)

if __name__ == "__main__":
    unittest.main()
