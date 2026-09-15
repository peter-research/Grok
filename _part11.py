"""Part 11 — v0.34 commands."""

from math import hypot as math_hypot, gcd as math_gcd, isqrt as math_isqrt


def hypot_nums(a: float, b: float) -> float:
    return math_hypot(a, b)


def lcm_nums(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a // math_gcd(a, b) * b)


def isqrt_num(n: int) -> int:
    if n < 0:
        raise ValueError("negative")
    return math_isqrt(n)


def median_nums(vals):
    nums = sorted(float(v) for v in vals)
    if not nums:
        raise ValueError("empty")
    mid = len(nums) // 2
    if len(nums) % 2:
        return nums[mid]
    return (nums[mid - 1] + nums[mid]) / 2.0


def pow_int(base: int, exp: int) -> int:
    if exp < 0:
        raise ValueError("negative exp")
    if exp > 64:
        raise ValueError("range")
    return pow(base, exp)


def cmd_hypot(args):
    a, b = _need(2, args)
    return str(hypot_nums(float(a), float(b)))


def cmd_lcm(args):
    a, b = _need(2, args)
    return str(lcm_nums(int(a), int(b)))


def cmd_isqrt(args):
    n = int(_need(1, args)[0])
    return str(isqrt_num(n))


def cmd_median(args):
    vals = _need(1, args, "numbers")
    out = median_nums(vals)
    if float(out).is_integer():
        return str(int(out))
    return str(out)


def cmd_powint(args):
    a, b = _need(2, args)
    return str(pow_int(int(a), int(b)))


COMMANDS.update({
    "hypot": cmd_hypot,
    "lcm": cmd_lcm,
    "isqrt": cmd_isqrt,
    "median": cmd_median,
    "powint": cmd_powint,
})
COMMAND_NAMES = list(COMMANDS)

_old_check = cmd_check


def cmd_check(args):
    out = _old_check(args)
    assert hypot_nums(3, 4) == 5.0
    assert lcm_nums(4, 6) == 12
    assert isqrt_num(16) == 4
    assert median_nums([1, 3, 2]) == 2.0
    assert pow_int(2, 10) == 1024
    return out


COMMANDS["check"] = cmd_check
