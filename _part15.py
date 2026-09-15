"""Part 15 — v0.38 commands."""


def is_armstrong(n: int) -> bool:
    if n < 0:
        raise ValueError("range")
    digits = str(n)
    p = len(digits)
    return n == sum(int(d) ** p for d in digits)


def next_prime(n: int) -> int:
    if n < 0 or n > 10_000_000:
        raise ValueError("range")
    cand = n + 1
    if cand < 2:
        cand = 2
    while True:
        if is_prime(cand):
            return cand
        cand += 1
        if cand > 10_000_037:
            raise ValueError("range")


def binary_gap(n: int) -> int:
    if n <= 0:
        raise ValueError("range")
    bits = bin(n)[2:].strip("0")
    if "0" not in bits:
        return 0
    return max(len(run) for run in bits.split("1") if run)


def harmonic_n(n: int) -> float:
    if n < 1 or n > 100_000:
        raise ValueError("range")
    return sum(1.0 / k for k in range(1, n + 1))


def is_twin_prime(n: int) -> bool:
    if n < 2:
        raise ValueError("range")
    return is_prime(n) and is_prime(n + 2)


def cmd_armstrong(args):
    n = int(_need(1, args, "n")[0])
    return "yes" if is_armstrong(n) else "no"


def cmd_nextprime(args):
    n = int(_need(1, args, "n")[0])
    return str(next_prime(n))


def cmd_binarygap(args):
    n = int(_need(1, args, "n")[0])
    return str(binary_gap(n))


def cmd_harmonic(args):
    n = int(_need(1, args, "n")[0])
    return str(harmonic_n(n))


def cmd_twins(args):
    n = int(_need(1, args, "n")[0])
    return "yes" if is_twin_prime(n) else "no"


COMMANDS.update({
    "armstrong": cmd_armstrong,
    "nextprime": cmd_nextprime,
    "binarygap": cmd_binarygap,
    "harmonic": cmd_harmonic,
    "twins": cmd_twins,
})
COMMAND_NAMES = list(COMMANDS)

_old_check = cmd_check


def cmd_check(args):
    out = _old_check(args)
    assert is_armstrong(153) is True
    assert is_armstrong(10) is False
    assert next_prime(14) == 17
    assert binary_gap(9) == 2
    assert abs(harmonic_n(1) - 1.0) < 1e-12
    assert is_twin_prime(5) is True
    assert is_twin_prime(7) is False
    return out


COMMANDS["check"] = cmd_check
