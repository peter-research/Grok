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

    def test_morse_encodes_letters(self) -> None:
        self.assertEqual(grok.to_morse("sos"), "... --- ...")
        self.assertEqual(grok.to_morse("Grok"), "--. .-. --- -.-")

    def test_unique_chars_preserves_order(self) -> None:
        self.assertEqual(grok.unique_chars("bookkeeper"), "bokepr")
        self.assertEqual(grok.unique_chars("aa"), "a")

    def test_leet_maps_common_letters(self) -> None:
        self.assertEqual(grok.to_leet("Grok"), "Gr0k")
        self.assertEqual(grok.to_leet("TEST"), "7357")

    def test_count_vowels(self) -> None:
        self.assertEqual(grok.count_vowels("Grok"), 1)
        self.assertEqual(grok.count_vowels("aeiou"), 5)

    def test_bin_and_hex(self) -> None:
        self.assertEqual(grok.to_bin("A"), "01000001")
        self.assertEqual(grok.to_hex("A"), "41")
        self.assertEqual(grok.to_hex("Grok"), "47726f6b")

    def test_base64_round_trip(self) -> None:
        text = "Grok — playground"
        encoded = base64.b64encode(text.encode("utf-8")).decode("ascii")
        self.assertEqual(base64.b64decode(encoded).decode("utf-8"), text)

    def test_hash_matches_stdlib(self) -> None:
        expected = hashlib.sha256(b"Hello, Grok!").hexdigest()
        self.assertEqual(
            hashlib.sha256("Hello, Grok!".encode("utf-8")).hexdigest(), expected
        )

    def test_command_names_are_unique(self) -> None:
        self.assertEqual(len(grok.COMMAND_NAMES), len(set(grok.COMMAND_NAMES)))
        self.assertEqual(len(grok.COMMAND_NAMES), 55)
        self.assertIn("check", grok.COMMAND_NAMES)
        self.assertIn("commands", grok.COMMAND_NAMES)
        self.assertIn("wrap", grok.COMMAND_NAMES)
        self.assertIn("sample", grok.COMMAND_NAMES)
        self.assertIn("repeat", grok.COMMAND_NAMES)
        self.assertIn("morse", grok.COMMAND_NAMES)
        self.assertIn("unique", grok.COMMAND_NAMES)
        self.assertIn("yesno", grok.COMMAND_NAMES)
        self.assertIn("leet", grok.COMMAND_NAMES)
        self.assertIn("vowels", grok.COMMAND_NAMES)
        self.assertIn("bin", grok.COMMAND_NAMES)
        self.assertIn("hex", grok.COMMAND_NAMES)

    def test_version_looks_like_semver(self) -> None:
        parts = grok.VERSION.split(".")
        self.assertEqual(len(parts), 3)
        self.assertTrue(all(p.isdigit() for p in parts))
        self.assertEqual(grok.VERSION, "0.15.0")


if __name__ == "__main__":
    unittest.main()
