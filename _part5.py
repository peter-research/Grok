"""Part 5 — extra numeric toys added in v0.25+."""


def variance_nums(vals):
    if len(vals) < 2:
        raise ValueError("range")
    m = mean_nums(vals)
    return sum((x - m) ** 2 for x in vals) / len(vals)


def nrange_nums(vals):
    if not vals:
        raise ValueError("empty")
    return max(vals) - min(vals)


def collatz_steps(n: int) -> int:
    if n < 1:
        raise ValueError("range")
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
        if steps > 10000:
            raise ValueError("range")
    return steps


def xor_text(text: str, key: int) -> str:
    key &= 0xFF
    return "".join(chr(ord(c) ^ key) for c in text)


def weekday_of(iso: str) -> str:
    names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    d = date.fromisoformat(iso)
    return names[d.weekday()]


def digit_sum(n: int) -> int:
    return sum(int(c) for c in str(abs(n)))


def triangular(n: int) -> int:
    if n < 0 or n > 10000:
        raise ValueError("range")
    return n * (n + 1) // 2


def isqrt_int(n: int) -> int:
    if n < 0:
        raise ValueError("range")
    if n < 2:
        return n
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def luhn_ok(text: str) -> bool:
    digits = [int(c) for c in text if c.isdigit()]
    if len(digits) < 2:
        return False
    total = 0
    for i, d in enumerate(reversed(digits)):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def to_kebab(text: str) -> str:
    return slugify(text)


def to_pascal(text: str) -> str:
    parts = [p for p in slugify(text).split("-") if p]
    return "".join(p[:1].upper() + p[1:] for p in parts)


def is_perfect(n: int) -> bool:
    if n < 2:
        return False
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            other = n // i
            if other != i and other != n:
                total += other
        i += 1
    return total == n


def julian_day(iso: str) -> int:
    return date.fromisoformat(iso).timetuple().tm_yday


def isbn10_ok(text: str) -> bool:
    chars = [c.upper() for c in text if c.isalnum()]
    if len(chars) != 10:
        return False
    total = 0
    for i, c in enumerate(chars):
        if i < 9:
            if not c.isdigit():
                return False
            total += int(c) * (10 - i)
        else:
            if c == "X":
                total += 10
            elif c.isdigit():
                total += int(c)
            else:
                return False
    return total % 11 == 0


def to_oct(n: int) -> str:
    return format(n, "o")


def is_pangram(text: str) -> bool:
    letters = {c.lower() for c in text if c.isalpha()}
    return set(string.ascii_lowercase) <= letters


def days_until(iso: str) -> int:
    return (date.fromisoformat(iso) - date.today()).days


def digital_root(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 0
    return 1 + (n - 1) % 9


def popcount(n: int) -> int:
    if n < 0:
        raise ValueError("range")
    return bin(n).count("1")


def isbn13_ok(text: str) -> bool:
    digits = [int(c) for c in text if c.isdigit()]
    if len(digits) != 13:
        return False
    total = sum(d if i % 2 == 0 else d * 3 for i, d in enumerate(digits))
    return total % 10 == 0


def is_leap(year: int) -> bool:
    if year <= 0:
        raise ValueError("range")
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def swap_case(text: str) -> str:
    return text.swapcase()


def celsius_to_f(c: float) -> float:
    return c * 9.0 / 5.0 + 32.0


def aliquot_sum(n: int) -> int:
    if n < 1:
        raise ValueError("range")
    if n == 1:
        return 0
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            other = n // i
            if other != i and other != n:
                total += other
        i += 1
    return total


def is_abundant(n: int) -> bool:
    if n < 1:
        raise ValueError("range")
    return aliquot_sum(n) > n


def fahrenheit_to_c(f: float) -> float:
    return (f - 32.0) * 5.0 / 9.0


def is_deficient(n: int) -> bool:
    if n < 1:
        raise ValueError("range")
    return aliquot_sum(n) < n


def is_square(n: int) -> bool:
    if n < 0:
        raise ValueError("range")
    r = isqrt_int(n)
    return r * r == n


def cube_int(n: int) -> int:
    if abs(n) > 100000:
        raise ValueError("range")
    return n * n * n


def mid_text(text: str) -> str:
    if not text:
        return ""
    n = len(text)
    if n % 2:
        return text[n // 2]
    return text[n // 2 - 1 : n // 2 + 1]
