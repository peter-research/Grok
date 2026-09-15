#!/usr/bin/env python3
"""Small stdlib-only regression tests for the Grok playground CLI."""

from __future__ import annotations

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
        self.assertEqual(len(grok.COMMAND_NAMES), 105)
        for name in ("roman", "snake", "camel", "caesar", "rle", "hash", "dice", "mode", "unb64", "hamming", "variance", "collatz", "xor", "weekday", "nrange", "digitsum", "tri", "isqrt", "luhn", "kebab", "pascal", "perfect", "julian", "isbn", "oct", "pangram", "until", "droot", "bits"):
            self.assertIn(name, grok.COMMAND_NAMES)

    def test_version_looks_like_semver(self) -> None:
        parts = grok.VERSION.split(".")
        self.assertEqual(len(parts), 3)
        self.assertTrue(all(p.isdigit() for p in parts))
        self.assertEqual(grok.VERSION, "0.28.0")

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
        self.assertEqual(grok.run_rle("aaabbc"), "3a2bc")

    def test_roman_roundtrip(self) -> None:
        self.assertEqual(grok.to_roman(2026), "MMXXVI")
        self.assertEqual(grok.from_roman("MMXXVI"), 2026)
        with self.assertRaises(ValueError):
            grok.from_roman("ABC")

    def test_case_converters(self) -> None:
        self.assertEqual(grok.to_snake("HelloGrok"), "hello_grok")
        self.assertEqual(grok.to_camel("hello grok"), "helloGrok")

    def test_caesar_and_lev(self) -> None:
        self.assertEqual(grok.caesar("abc", 1), "bcd")
        self.assertEqual(grok.caesar(grok.caesar("Grok", 5), -5), "Grok")
        self.assertEqual(grok.lev_dist("kitten", "sitting"), 3)

    def test_mode_stddev_pow(self) -> None:
        self.assertEqual(grok.mode_nums([1, 2, 2, 3]), 2)
        self.assertEqual(sorted(grok.mode_nums([1, 1, 2, 2])), [1, 2])
        self.assertAlmostEqual(grok.stddev_nums([2, 4, 4, 4, 5, 5, 7, 9]), 2.0)
        self.assertEqual(grok.pow_nums(2, 10), 1024)
        with self.assertRaises(ValueError):
            grok.stddev_nums([1])

    def test_unb64_and_hamming(self) -> None:
        import base64
        raw = base64.b64encode(b"Grok").decode()
        self.assertEqual(grok.unb64(raw), "Grok")
        self.assertEqual(grok.hamming("karolin", "kathrin"), 3)
        with self.assertRaises(ValueError):
            grok.hamming("ab", "abc")

    def test_pig_and_box(self) -> None:
        self.assertEqual(grok.pig_latin("hello"), "ellohay")
        self.assertEqual(grok.pig_latin("apple"), "appleway")
        boxed = grok.box_text("Grok")
        self.assertTrue(boxed.startswith("+"))
        self.assertIn("| Grok |", boxed)

    def test_variance_nrange_collatz_xor_weekday(self) -> None:
        self.assertAlmostEqual(grok.variance_nums([2, 4, 4, 4, 5, 5, 7, 9]), 4.0)
        self.assertEqual(grok.nrange_nums([3, 1, 8]), 7)
        self.assertEqual(grok.collatz_steps(6), 8)
        self.assertEqual(grok.xor_text("hi", 1), "ih")
        self.assertEqual(grok.xor_text(grok.xor_text("Grok", 42), 42), "Grok")
        self.assertEqual(grok.weekday_of("2026-09-15"), "Tuesday")
        with self.assertRaises(ValueError):
            grok.variance_nums([1])
        with self.assertRaises(ValueError):
            grok.collatz_steps(0)

    def test_digitsum_tri_isqrt_luhn(self) -> None:
        self.assertEqual(grok.digit_sum(2026), 10)
        self.assertEqual(grok.triangular(10), 55)
        self.assertEqual(grok.isqrt_int(144), 12)
        self.assertTrue(grok.luhn_ok("79927398713"))
        self.assertFalse(grok.luhn_ok("123"))

    def test_kebab_pascal_perfect_julian_isbn(self) -> None:
        self.assertEqual(grok.to_kebab("Hello, Grok!"), "hello-grok")
        self.assertEqual(grok.to_pascal("hello grok"), "HelloGrok")
        self.assertTrue(grok.is_perfect(6))
        self.assertTrue(grok.is_perfect(28))
        self.assertFalse(grok.is_perfect(12))
        self.assertEqual(grok.julian_day("2026-09-15"), 258)
        self.assertTrue(grok.isbn10_ok("0-306-40615-2"))
        self.assertFalse(grok.isbn10_ok("123"))

    def test_oct_pangram_until_droot_bits(self) -> None:
        self.assertEqual(grok.to_oct(64), "100")
        self.assertTrue(grok.is_pangram("The quick brown fox jumps over the lazy dog"))
        self.assertFalse(grok.is_pangram("hello"))
        self.assertEqual(grok.days_until("2026-09-15"), (grok.date.fromisoformat("2026-09-15") - grok.date.today()).days)
        self.assertEqual(grok.digital_root(38), 2)
        self.assertEqual(grok.digital_root(0), 0)
        self.assertEqual(grok.popcount(13), 3)
        with self.assertRaises(ValueError):
            grok.popcount(-1)


if __name__ == "__main__":
    unittest.main()
