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
        self.assertEqual(len(grok.COMMAND_NAMES), 47)
        self.assertIn("check", grok.COMMAND_NAMES)
        self.assertIn("commands", grok.COMMAND_NAMES)
        self.assertIn("wrap", grok.COMMAND_NAMES)
        self.assertIn("sample", grok.COMMAND_NAMES)
        self.assertIn("day", grok.COMMAND_NAMES)
        self.assertIn("echo", grok.COMMAND_NAMES)

    def test_version_looks_like_semver(self) -> None:
        parts = grok.VERSION.split(".")
        self.assertEqual(len(parts), 3)
        self.assertTrue(all(p.isdigit() for p in parts))


if __name__ == "__main__":
    unittest.main()
