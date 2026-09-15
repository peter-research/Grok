"""Part 8 — v0.31 commands."""


def sign_int(n: int) -> int:
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0


def is_even(n: int) -> bool:
    return n % 2 == 0


def is_odd(n: int) -> bool:
    return n % 2 != 0


def abs_int(n: int) -> int:
    return -n if n < 0 else n


def rev_int(n: int) -> int:
    sign = -1 if n < 0 else 1
    return sign * int(str(abs_int(n))[::-1])


def cmd_sign(args):
    return str(sign_int(int(_need(1, args)[0])))


def cmd_even(args):
    return "yes" if is_even(int(_need(1, args)[0])) else "no"


def cmd_odd(args):
    return "yes" if is_odd(int(_need(1, args)[0])) else "no"


def cmd_abs(args):
    return str(abs_int(int(_need(1, args)[0])))


def cmd_revint(args):
    return str(rev_int(int(_need(1, args)[0])))


COMMANDS.update({
    "sign": cmd_sign,
    "even": cmd_even,
    "odd": cmd_odd,
    "abs": cmd_abs,
    "revint": cmd_revint,
})
COMMAND_NAMES = list(COMMANDS)

_old_check = cmd_check


def cmd_check(args):
    out = _old_check(args)
    assert sign_int(-7) == -1
    assert is_even(8)
    assert is_odd(9)
    assert abs_int(-12) == 12
    assert rev_int(120) == 21
    return out


COMMANDS["check"] = cmd_check
