"""Part 18 — v0.41 commands."""

from math import isqrt


def _digit_sum_abs(n: int) -> int:
    s = 0
    n = abs(n)
    while n:
        s += n % 10
        n //= 10
    return s


def is_smith(n: int) -> bool:
    if n < 4 or n > 1_000_000:
        raise ValueError("range")
    x = n
    factors = []
    while x % 2 == 0:
        factors.append(2)
        x //= 2
    f = 3
    while f * f <= x:
        while x % f == 0:
            factors.append(f)
            x //= f
        f += 2
    if x > 1:
        factors.append(x)
    if len(factors) < 2:
        return False
    return _digit_sum_abs(n) == sum(_digit_sum_abs(p) for p in factors)


def is_automorphic(n: int) -> bool:
    if n < 0 or n > 10**8:
        raise ValueError("range")
    return str(n * n).endswith(str(n))


def lucas_n(n: int) -> int:
    if n < 0 or n > 90:
        raise ValueError("range")
    a, b = 2, 1
    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def is_squarefree(n: int) -> bool:
    if n < 1 or n > 10**7:
        raise ValueError("range")
    if n % 4 == 0:
        return False
    f = 3
    while f * f <= n:
        if n % f == 0:
            n //= f
            if n % f == 0:
                return False
        f += 2
    return True


def is_duck(n: int) -> bool:
    if n < 0 or n > 10**12:
        raise ValueError("range")
    if n == 0:
        return False
    return "0" in str(n)


def cmd_smith(args):
    n = int(_need(1, args, "n")[0])
    return "yes" if is_smith(n) else "no"


def cmd_automorphic(args):
    n = int(_need(1, args, "n")[0])
    return "yes" if is_automorphic(n) else "no"


def cmd_lucas(args):
    n = int(_need(1, args, "n")[0])
    return str(lucas_n(n))


def cmd_squarefree(args):
    n = int(_need(1, args, "n")[0])
    return "yes" if is_squarefree(n) else "no"


def cmd_duck(args):
    n = int(_need(1, args, "n")[0])
    return "yes" if is_duck(n) else "no"


COMMANDS.update({
    "smith": cmd_smith,
    "automorphic": cmd_automorphic,
    "lucas": cmd_lucas,
    "squarefree": cmd_squarefree,
    "duck": cmd_duck,
})
COMMAND_NAMES = list(COMMANDS)

_old_check = cmd_check


def cmd_check(args):
    out = _old_check(args)
    assert is_smith(4) is True
    assert is_smith(5) is False
    assert is_automorphic(25) is True
    assert is_automorphic(26) is False
    assert lucas_n(0) == 2
    assert lucas_n(5) == 11
    assert is_squarefree(10) is True
    assert is_squarefree(12) is False
    assert is_duck(101) is True
    assert is_duck(111) is False
    return out


COMMANDS["check"] = cmd_check
