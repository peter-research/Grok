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
