"""Part 16 — v0.39 commands."""

from math import gcd, isqrt


def is_harshad(n: int) -> bool:
    if n <= 0:
        raise ValueError("range")
    s = digit_sum(n)
    return s != 0 and n % s == 0


def is_pronic(n: int) -> bool:
    if n < 0:
        raise ValueError("range")
    k = isqrt(n)
    return k * (k + 1) == n


def euler_totient(n: int) -> int:
    if n < 1 or n > 1_000_000:
        raise ValueError("range")
    result = n
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            result -= result // p
        p += 1 if p == 2 else 2
    if x > 1:
        result -= result // x
    return result


def multiplicative_persistence(n: int) -> int:
    if n < 0 or n > 10**18:
        raise ValueError("range")
    steps = 0
    while n >= 10:
        prod = 1
        while n:
            prod *= n % 10
            n //= 10
        n = prod
        steps += 1
        if steps > 40:
            raise ValueError("range")
    return steps


def is_pentagonal(n: int) -> bool:
    if n <= 0:
        raise ValueError("range")
    disc = 24 * n + 1
    r = isqrt(disc)
    if r * r != disc:
        return False
    return (1 + r) % 6 == 0


def cmd_harshad(args):
    n = int(_need(1, args, "n")[0])
    return "yes" if is_harshad(n) else "no"


def cmd_pronic(args):
    n = int(_need(1, args, "n")[0])
    return "yes" if is_pronic(n) else "no"


def cmd_totient(args):
    n = int(_need(1, args, "n")[0])
    return str(euler_totient(n))


def cmd_persist(args):
    n = int(_need(1, args, "n")[0])
    return str(multiplicative_persistence(n))


def cmd_pentagonal(args):
    n = int(_need(1, args, "n")[0])
    return "yes" if is_pentagonal(n) else "no"


COMMANDS.update({
    "harshad": cmd_harshad,
    "pronic": cmd_pronic,
    "totient": cmd_totient,
    "persist": cmd_persist,
    "pentagonal": cmd_pentagonal,
})
COMMAND_NAMES = list(COMMANDS)

_old_check = cmd_check


def cmd_check(args):
    out = _old_check(args)
    assert is_harshad(18) is True
    assert is_harshad(19) is False
    assert is_pronic(12) is True
    assert is_pronic(10) is False
    assert euler_totient(9) == 6
    assert multiplicative_persistence(39) == 3
    assert is_pentagonal(5) is True
    assert is_pentagonal(6) is False
    return out


COMMANDS["check"] = cmd_check
