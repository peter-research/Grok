"""Part 6 — command table and CLI entry."""


def _need(n, args, label="args"):
    if len(args) < n:
        raise SystemExit(f"need {label}")
    return args


def _ints(args):
    try:
        return [int(a) for a in args]
    except ValueError as e:
        raise SystemExit("bad number") from e


def _floats(args):
    try:
        return [float(a) for a in args]
    except ValueError as e:
        raise SystemExit("bad number") from e


def cmd_greet(args):
    name = args[0] if args else "friend"
    return f"hello {name}"


def cmd_quote(_args):
    return pick_one(QUOTES)


def cmd_fortune(_args):
    return pick_one(FORTUNES)


def cmd_joke(_args):
    return pick_one(JOKES)


def cmd_why(_args):
    return "because the playground said so"


def cmd_idea(_args):
    return pick_one(IDEAS)


def cmd_tip(_args):
    return pick_one(TIPS)


def cmd_flip(_args):
    return pick_one(["heads", "tails"])


def cmd_dice(args):
    sides = int(args[0]) if args else 6
    if sides < 2 or sides > 1000:
        raise SystemExit("range")
    return str(random.randint(1, sides))


def cmd_color(_args):
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


def cmd_now(_args):
    return datetime.now().isoformat(timespec="seconds")


def cmd_week(_args):
    return str(date.today().isocalendar()[1])


def cmd_day(_args):
    return date.today().isoformat()


def cmd_echo(args):
    return " ".join(args)


def cmd_version(_args):
    return VERSION


def cmd_about(_args):
    return f"Grok playground CLI {VERSION} — original stdlib-only sandbox."


def cmd_check(_args):
    assert rot13(rot13("Grok")) == "Grok"
    assert slugify("Hello, Grok!") == "hello-grok"
    assert to_roman(2026) == "MMXXVI"
    assert collatz_steps(6) == 8
    assert to_pascal("hello grok") == "HelloGrok"
    assert is_perfect(28)
    return "check ok"


def cmd_rot13(args):
    return rot13(" ".join(_need(1, args, "text")))


def cmd_slug(args):
    return slugify(" ".join(_need(1, args, "text")))


def cmd_hash(args):
    return hash_text(" ".join(_need(1, args, "text")))


def cmd_uuid(_args):
    return make_uuid()


def cmd_palindrome(args):
    return "yes" if is_palindrome(" ".join(_need(1, args, "text"))) else "no"


def cmd_pick(args):
    return pick_one(_need(1, args, "items"))


def cmd_sample(args):
    n = int(args[0]) if args else 1
    items = args[1:] or list("abcde")
    return " ".join(sample_n(items, n))


def cmd_shuffle(args):
    return shuffle_text(" ".join(_need(1, args, "text")))


def cmd_reverse(args):
    return reverse_text(" ".join(_need(1, args, "text")))


def cmd_count(args):
    chars, words, lines = count_text(" ".join(args))
    return f"{chars} {words} {lines}"


def cmd_wrap(args):
    width = int(args[0]) if args else 40
    text = " ".join(args[1:]) if len(args) > 1 else ""
    return wrap_text(text, width)


def cmd_b64(args):
    return base64.b64encode(" ".join(_need(1, args, "text")).encode()).decode()


def cmd_sum(args):
    return str(sum_nums(_floats(_need(1, args, "numbers"))))


def cmd_title(args):
    return title_case(" ".join(_need(1, args, "text")))


def cmd_upper(args):
    return to_upper(" ".join(_need(1, args, "text")))


def cmd_lower(args):
    return to_lower(" ".join(_need(1, args, "text")))


def cmd_words(args):
    return str(len(word_list(" ".join(args))))


def cmd_lines(args):
    return str(len(line_list("\n".join(args) if args else "")))


def cmd_chars(args):
    return str(len(" ".join(args)))


def cmd_sort(args):
    return sort_lines("\n".join(_need(1, args, "lines")))


def cmd_dedupe(args):
    return dedupe_lines("\n".join(_need(1, args, "lines")))


def cmd_join(args):
    sep = args[0] if args else ","
    rest = args[1:]
    return join_words(" ".join(rest), sep)


def cmd_split(args):
    sep = args[0] if args else ","
    rest = " ".join(args[1:])
    return split_sep(rest, sep)


def cmd_anagram(args):
    a, b = _need(2, args, "two texts")[0], " ".join(args[1:])
    return "yes" if is_anagram(a, b) else "no"


def cmd_initials(args):
    return initials(" ".join(_need(1, args, "text")))


def cmd_indent(args):
    n = int(args[0]) if args else 2
    text = " ".join(args[1:])
    return indent_text(text, n)


def cmd_percent(args):
    nums = _floats(_need(2, args, "part whole"))
    return str(percent_of(nums[0], nums[1]))


def cmd_clamp(args):
    nums = _floats(_need(3, args, "x lo hi"))
    return str(clamp_num(nums[0], nums[1], nums[2]))


def cmd_random(args):
    lo = int(args[0]) if args else 0
    hi = int(args[1]) if len(args) > 1 else 100
    return str(random.randint(lo, hi))


def cmd_commands(_args):
    return "\n".join(COMMAND_NAMES)


def cmd_repeat(args):
    n = int(_need(1, args)[0])
    return repeat_text(" ".join(args[1:]), n)


def cmd_morse(args):
    return to_morse(" ".join(_need(1, args, "text")))


def cmd_unique(args):
    return unique_chars(" ".join(args))


def cmd_yesno(args):
    return yes_no(" ".join(args) if args else "")


def cmd_leet(args):
    return to_leet(" ".join(_need(1, args, "text")))


def cmd_vowels(args):
    return str(count_vowels(" ".join(args)))


def cmd_bin(args):
    return to_bin(int(_need(1, args)[0]))


def cmd_hex(args):
    return to_hex(int(_need(1, args)[0]))


def cmd_caesar(args):
    if len(args) < 2:
        raise SystemExit("need text shift")
    shift = int(args[-1])
    text = " ".join(args[:-1])
    return caesar(text, shift)


def cmd_consonants(args):
    return str(count_consonants(" ".join(args)))


def cmd_pig(args):
    return " ".join(pig_latin(w) for w in _need(1, args, "text"))


def cmd_ascii(args):
    return ascii_codes(" ".join(_need(1, args, "text")))


def cmd_snake(args):
    return to_snake(" ".join(_need(1, args, "text")))


def cmd_camel(args):
    return to_camel(" ".join(_need(1, args, "text")))


def cmd_nato(args):
    return to_nato(" ".join(_need(1, args, "text")))


def cmd_freq(args):
    return char_freq(" ".join(args))


def cmd_entropy(args):
    return f"{entropy_text(' '.join(args)):.4f}"


def cmd_lev(args):
    a, b = _need(2, args, "two strings")[0], args[1]
    return str(lev_dist(a, b))


def cmd_rle(args):
    return run_rle(" ".join(_need(1, args, "text")))


def cmd_box(args):
    return box_text(" ".join(_need(1, args, "text")))


def cmd_roman(args):
    return to_roman(int(_need(1, args)[0]))


def cmd_unroman(args):
    return str(from_roman(_need(1, args)[0]))


def cmd_isogram(args):
    return "yes" if is_isogram(" ".join(args)) else "no"


def cmd_tap(args):
    return tap_code(" ".join(_need(1, args, "text")))


def cmd_fib(args):
    return str(nth_fib(int(_need(1, args)[0])))


def cmd_prime(args):
    return "yes" if is_prime(int(_need(1, args)[0])) else "no"


def cmd_gcd(args):
    nums = _ints(_need(2, args, "two ints"))
    return str(gcd_int(nums[0], nums[1]))


def cmd_lcm(args):
    nums = _ints(_need(2, args, "two ints"))
    return str(lcm_int(nums[0], nums[1]))


def cmd_unrle(args):
    return undo_rle(" ".join(_need(1, args, "text")))


def cmd_fact(args):
    return str(factorial_int(int(_need(1, args)[0])))


def cmd_mean(args):
    return str(mean_nums(_floats(_need(1, args, "numbers"))))


def cmd_median(args):
    return str(median_nums(_floats(_need(1, args, "numbers"))))


def cmd_revwords(args):
    return reverse_words(" ".join(_need(1, args, "text")))


def cmd_factors(args):
    return " ".join(str(x) for x in factor_list(int(_need(1, args)[0])))


def cmd_mode(args):
    m = mode_nums(_floats(_need(1, args, "numbers")))
    if isinstance(m, list):
        return " ".join(str(x) for x in m)
    return str(m)


def cmd_stddev(args):
    return str(stddev_nums(_floats(_need(1, args, "numbers"))))


def cmd_pow(args):
    nums = _floats(_need(2, args, "base exp"))
    return str(pow_nums(nums[0], nums[1]))


def cmd_unb64(args):
    return unb64(_need(1, args)[0])


def cmd_hamming(args):
    a, b = _need(2, args, "two strings")[0], args[1]
    return str(hamming(a, b))


def cmd_variance(args):
    return str(variance_nums(_floats(_need(1, args, "numbers"))))


def cmd_nrange(args):
    return str(nrange_nums(_floats(_need(1, args, "numbers"))))


def cmd_collatz(args):
    return str(collatz_steps(int(_need(1, args)[0])))


def cmd_xor(args):
    if len(args) < 2:
        raise SystemExit("need text key")
    return xor_text(" ".join(args[:-1]), int(args[-1]))


def cmd_weekday(args):
    return weekday_of(_need(1, args)[0])


def cmd_digitsum(args):
    return str(digit_sum(int(_need(1, args)[0])))


def cmd_tri(args):
    return str(triangular(int(_need(1, args)[0])))


def cmd_isqrt(args):
    return str(isqrt_int(int(_need(1, args)[0])))


def cmd_luhn(args):
    return "yes" if luhn_ok(_need(1, args)[0]) else "no"


def cmd_kebab(args):
    return to_kebab(" ".join(_need(1, args, "text")))


def cmd_pascal(args):
    return to_pascal(" ".join(_need(1, args, "text")))


def cmd_perfect(args):
    return "yes" if is_perfect(int(_need(1, args)[0])) else "no"


def cmd_julian(args):
    return str(julian_day(_need(1, args)[0]))


def cmd_isbn(args):
    return "yes" if isbn10_ok(_need(1, args)[0]) else "no"


COMMANDS = {
    "greet": cmd_greet, "quote": cmd_quote, "fortune": cmd_fortune, "joke": cmd_joke,
    "why": cmd_why, "idea": cmd_idea, "tip": cmd_tip, "flip": cmd_flip, "dice": cmd_dice,
    "color": cmd_color, "now": cmd_now, "week": cmd_week, "day": cmd_day, "echo": cmd_echo,
    "version": cmd_version, "about": cmd_about, "check": cmd_check, "rot13": cmd_rot13,
    "slug": cmd_slug, "hash": cmd_hash, "uuid": cmd_uuid, "palindrome": cmd_palindrome,
    "pick": cmd_pick, "sample": cmd_sample, "shuffle": cmd_shuffle, "reverse": cmd_reverse,
    "count": cmd_count, "wrap": cmd_wrap, "b64": cmd_b64, "sum": cmd_sum, "title": cmd_title,
    "upper": cmd_upper, "lower": cmd_lower, "words": cmd_words, "lines": cmd_lines,
    "chars": cmd_chars, "sort": cmd_sort, "dedupe": cmd_dedupe, "join": cmd_join,
    "split": cmd_split, "anagram": cmd_anagram, "initials": cmd_initials, "indent": cmd_indent,
    "percent": cmd_percent, "clamp": cmd_clamp, "random": cmd_random, "commands": cmd_commands,
    "repeat": cmd_repeat, "morse": cmd_morse, "unique": cmd_unique, "yesno": cmd_yesno,
    "leet": cmd_leet, "vowels": cmd_vowels, "bin": cmd_bin, "hex": cmd_hex, "caesar": cmd_caesar,
    "consonants": cmd_consonants, "pig": cmd_pig, "ascii": cmd_ascii, "snake": cmd_snake,
    "camel": cmd_camel, "nato": cmd_nato, "freq": cmd_freq, "entropy": cmd_entropy,
    "lev": cmd_lev, "rle": cmd_rle, "box": cmd_box, "roman": cmd_roman, "unroman": cmd_unroman,
    "isogram": cmd_isogram, "tap": cmd_tap, "fib": cmd_fib, "prime": cmd_prime, "gcd": cmd_gcd,
    "lcm": cmd_lcm, "unrle": cmd_unrle, "fact": cmd_fact, "mean": cmd_mean, "median": cmd_median,
    "revwords": cmd_revwords, "factors": cmd_factors, "mode": cmd_mode, "stddev": cmd_stddev,
    "pow": cmd_pow, "unb64": cmd_unb64, "hamming": cmd_hamming, "variance": cmd_variance,
    "nrange": cmd_nrange, "collatz": cmd_collatz, "xor": cmd_xor, "weekday": cmd_weekday,
    "digitsum": cmd_digitsum, "tri": cmd_tri, "isqrt": cmd_isqrt, "luhn": cmd_luhn,
    "kebab": cmd_kebab, "pascal": cmd_pascal, "perfect": cmd_perfect, "julian": cmd_julian,
    "isbn": cmd_isbn,
}

COMMAND_NAMES = list(COMMANDS)


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        print(f"Grok {VERSION}. Try: python3 grok.py commands")
        return 0
    name = argv[0]
    fn = COMMANDS.get(name)
    if fn is None:
        print(f"unknown command: {name}", file=sys.stderr)
        return 2
    try:
        print(fn(argv[1:]))
        return 0
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
