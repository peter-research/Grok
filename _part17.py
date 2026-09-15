"""Part 17 — v0.40 commands."""

from math import isqrt


def is_hexagonal(n: int) -> bool:
    if n <= 0:
        raise ValueError("range")
    disc = 8 * n + 1
    r = isqrt(disc)
    if r * r != disc:
        return False
    return (1 + r) % 4 == 0


def is_happy(n: int) -> bool:
    if n < 1 or n > 10**12:
        raise ValueError("range")
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        s = 0
        while n:
            d = n % 10
            s += d * d
            n //= 10
        n = s
    return n == 1


def is_kaprekar(n: int) -> bool:
    if n < 1 or n > 10**6:
        raise ValueError("range")
    sq = n * n
    s = str(sq)
    for i in range(1, len(s)):
        left = int(s[:i]) if s[:i] else 0
        right = int(s[i:]) if s[i:] else 0
        if right and left + right == n:
            return True
    return n == 1


def catalan_n(n: int) -> int:
    if n < 0 or n > 30:
        raise ValueError("range")
    c = 1
    for k in range(n):
        c = c * (2 * n - k) // (k + 1)
    return c // (n + 1) if n else 1


def aliquot_sum(n: int) -> int:
    if n < 1 or n > 1_000_000:
        raise ValueError("range")
    if n == 1:
        return 0
    total = 1
    r = isqrt(n)
    for i in range(2, r + 1):
        if n % i == 0:
            total += i
            other = n // i
            if other != i and other != n:
                total += other
    return total


def cmd_hexagonal(args):
    n = int(_need(1, args, "n")[0])
    return "yes" if is_hexagonal(n) else "no"


def cmd_happy(args):
    n = int(_need(1, args, "n")[0])
    return "yes" if is_happy(n) else "no"


def cmd_kaprekar(args):
    n = int(_need(1, args, "n")[0])
    return "yes" if is_kaprekar(n) else "no"


def cmd_catalan(args):
    n = int(_need(1, args, "n")[0])
    return str(catalan_n(n))


def cmd_aliquot(args):
    n = int(_need(1, args, "n")[0])
    return str(aliquot_sum(n))


COMMANDS.update({
    "hexagonal": cmd_hexagonal,
    "happy": cmd_happy,
    "kaprekar": cmd_kaprekar,
    "catalan": cmd_catalan,
    "aliquot": cmd_aliquot,
})
COMMAND_NAMES = list(COMMANDS)

_old_check = cmd_check


def cmd_check(args):
    out = _old_check(args)
    assert is_hexagonal(1) is True
    assert is_hexagonal(6) is True
    assert is_hexagonal(7) is False
    assert is_happy(19) is True
    assert is_happy(2) is False
    assert is_kaprekar(297) is True
    assert is_kaprekar(10) is False
    assert catalan_n(5) == 42
    assert aliquot_sum(12) == 16
    return out


COMMANDS["check"] = cmd_check
