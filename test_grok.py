#!/usr/bin/env python3
"""Small stdlib-only regression tests for the Grok playground CLI."""

from __future__ import annotations

import base64
import hashlib
import unittest

import grok


class GrokHelpersTest(unittest.TestCase):
    def test_rot13_is_reversible(self) -> None:
        samples = ["Hello, Grok!", "123", "Été", "A-Z a-z"]
        for sample in samples:
            with self.subTest(sample=sample):
                self.assertEqual(grok.rot13(grok.rot13(sample)), sample)

    def test_slugify_normalizes_separators(self) -> None:
        self.assertEqual(grok.slugify("Hello, Grok!"), "hello-grok")
        self.assertEqual(grok.slugify("  multiple---spaces  "), "multiple-spaces")
        self.assertEqual(grok.slugify("  --  "), "item")

    def test_palindrome_ignores_punctuation(self) -> None:
        self.assertTrue(grok.is_palindrome("Race car"))
        self.assertTrue(grok.is_palindrome("A man, a plan, a canal: Panama!"))
        self.assertFalse(grok.is_palindrome("Grok"))
        self.assertFalse(grok.is_palindrome("---"))

    def test_count_text(self) -> None:
        self.assertEqual(grok.count_text("one two"), (7, 2, 1))
        self.assertEqual(grok.count_text("one\ntwo\nthree"), (13, 3, 3))
        self.assertEqual(grok.count_text(""), (0, 0, 0))

    def test_title_case_handles_punctuation(self) -> None:
        self.assertEqual(grok.title_case("hello grok"), "Hello Grok")
        self.assertEqual(grok.title_case("hello-world"), "Hello-World")
        self.assertEqual(grok.title_case("GROK 2.0"), "Grok 2.0")

    def test_wrap_text_breaks_on_width(self) -> None:
        self.assertEqual(grok.wrap_text("one two three four", 10), "one two\nthree four")
        self.assertEqual(grok.wrap_text("hello", 20), "hello")
        with self.assertRaises(ValueError):
            grok.wrap_text("hello world", 4)

    def test_command_names_are_unique(self) -> None:
        self.assertEqual(len(grok.COMMAND_NAMES), len(set(grok.COMMAND_NAMES)))
        self.assertEqual(len(grok.COMMAND_NAMES), 81)
        for name in ("fact", "mean", "median", "revwords", "factors", "fib", "unrle"):
            self.assertIn(name, grok.COMMAND_NAMES)

    def test_version_looks_like_semver(self) -> None:
        parts = grok.VERSION.split(".")
        self.assertEqual(len(parts), 3)
        self.assertTrue(all(p.isdigit() for p in parts))
        self.assertEqual(grok.VERSION, "0.21.0")

    def test_factorial(self) -> None:
        self.assertEqual(grok.factorial_int(0), 1)
        self.assertEqual(grok.factorial_int(5), 120)
        with self.assertRaises(ValueError):
            grok.factorial_int(21)

    def test_mean_median(self) -> None:
        self.assertEqual(grok.mean_nums([1, 2, 3]), 2)
        self.assertEqual(grok.median_nums([1, 3, 2]), 2)
        self.assertEqual(grok.median_nums([1, 2, 3, 4]), 2.5)

    def test_reverse_words(self) -> None:
        self.assertEqual(grok.reverse_words("hello grok"), "grok hello")

    def test_factors(self) -> None:
        self.assertEqual(grok.factor_list(12), [1, 2, 3, 4, 6, 12])
        with self.assertRaises(ValueError):
            grok.factor_list(0)

    def test_fib_prime_gcd_lcm_unrle(self) -> None:
        self.assertEqual(grok.nth_fib(10), 55)
        self.assertTrue(grok.is_prime(13))
        self.assertFalse(grok.is_prime(1))
        self.assertEqual(grok.gcd_int(54, 24), 6)
        self.assertEqual(grok.lcm_int(4, 6), 12)
        self.assertEqual(grok.undo_rle("3a2bc"), "aaabbc")


if __name__ == "__main__":
    unittest.main()
