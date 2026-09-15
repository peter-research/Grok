"""Part 12 — v0.35 commands."""

from math import prod as math_prod


def ncr_nums(n: int, k: int) -> int:
    if n < 0 or k < 0:
        raise ValueError("range")
    if k > n:
        return 0
    k = min(k, n - k)
    out = 1
    for i in range(1, k + 1):
        out = out * (n - k + i) // i
    return out


def npr_nums(n: int, k: int) -> int:
    if n < 0 or k < 0:
        raise ValueError("range")
    if k > n:
        return 0
    out = 1
    for i in range(n - k + 1, n + 1):
        out *= i
    return out


def cbrt_int(n: int) -> int:
    if n < 0:
        raise ValueError("negative")
    lo, hi = 0, n
    best = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        cube = mid * mid * mid
        if cube == n:
            return mid
        if cube < n:
            best = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return best


def geomean_nums(vals):
    nums = [float(v) for v in vals]
    if not nums:
        raise ValueError("empty")
    if any(x < 0 for x in nums):
        raise ValueError("negative")
    if any(x == 0 for x in nums):
        return 0.0
    return math_prod(nums) ** (1.0 / len(nums))


def xor_str(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError("length")
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))


def cmd_ncr(args):
    n, k = _need(2, args)
    return str(ncr_nums(int(n), int(k)))


def cmd_npr(args):
    n, k = _need(2, args)
    return str(npr_nums(int(n), int(k)))


def cmd_cbrt(args):
    n = int(_need(1, args)[0])
    return str(cbrt_int(n))


def cmd_geomean(args):
    vals = _need(1, args, "numbers")
    out = geomean_nums(vals)
    if float(out).is_integer():
        return str(int(out))
    return str(out)


def cmd_xorstr(args):
    a, b = _need(2, args)
    raw = xor_str(a, b)
    return raw.encode("utf-8", "replace").hex()


COMMANDS.update({
    "ncr": cmd_ncr,
    "npr": cmd_npr,
    "cbrt": cmd_cbrt,
    "geomean": cmd_geomean,
    "xorstr": cmd_xorstr,
})
COMMAND_NAMES = list(COMMANDS)

_old_check = cmd_check


def cmd_check(args):
    out = _old_check(args)
    assert ncr_nums(5, 2) == 10
    assert npr_nums(5, 2) == 20
    assert cbrt_int(27) == 3
    assert abs(geomean_nums([1, 4, 16]) - 4.0) < 1e-9
    assert xor_str("ab", "cd") == "\x02\x06"
    return out


COMMANDS["check"] = cmd_check
