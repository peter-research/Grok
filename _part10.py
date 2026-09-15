"""Part 10 — v0.33 commands."""

from math import floor as math_floor, ceil as math_ceil, gcd as math_gcd


def floor_num(x: float) -> int:
    return int(math_floor(x))


def ceil_num(x: float) -> int:
    return int(math_ceil(x))


def round_num(x: float, ndigits: int = 0) -> float:
    return round(x, ndigits)


def mod_nums(a: int, b: int) -> int:
    if b == 0:
        raise ValueError("zero")
    return a % b


def is_coprime(a: int, b: int) -> bool:
    return math_gcd(abs(a), abs(b)) == 1


def cmd_floor(args):
    return str(floor_num(float(_need(1, args)[0])))


def cmd_ceil(args):
    return str(ceil_num(float(_need(1, args)[0])))


def cmd_roundn(args):
    vals = _need(1, args, "number [digits]")
    x = float(vals[0])
    nd = int(vals[1]) if len(vals) > 1 else 0
    return str(round_num(x, nd))


def cmd_mod(args):
    a, b = _need(2, args)
    return str(mod_nums(int(a), int(b)))


def cmd_coprime(args):
    a, b = _need(2, args)
    return "yes" if is_coprime(int(a), int(b)) else "no"


COMMANDS.update({
    "floor": cmd_floor,
    "ceil": cmd_ceil,
    "roundn": cmd_roundn,
    "mod": cmd_mod,
    "coprime": cmd_coprime,
})
COMMAND_NAMES = list(COMMANDS)

_old_check = cmd_check


def cmd_check(args):
    out = _old_check(args)
    assert floor_num(3.7) == 3
    assert ceil_num(3.2) == 4
    assert round_num(3.14159, 2) == 3.14
    assert mod_nums(10, 3) == 1
    assert is_coprime(8, 15)
    assert not is_coprime(8, 12)
    return out


COMMANDS["check"] = cmd_check
