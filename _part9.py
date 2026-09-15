"""Part 9 — v0.32 commands."""


def is_palnum(n: int) -> bool:
    s = str(abs(n))
    return s == s[::-1]


def digit_count(n: int) -> int:
    return len(str(abs(n)))


def prod_nums(nums):
    acc = 1
    for n in nums:
        acc *= n
    return acc


def min_nums(nums):
    if not nums:
        raise ValueError("empty")
    return min(nums)


def max_nums(nums):
    if not nums:
        raise ValueError("empty")
    return max(nums)


def cmd_palnum(args):
    return "yes" if is_palnum(int(_need(1, args)[0])) else "no"


def cmd_digits(args):
    return str(digit_count(int(_need(1, args)[0])))


def cmd_prod(args):
    nums = [float(x) for x in _need(1, args, "numbers")]
    return str(prod_nums(nums))


def cmd_minn(args):
    nums = [float(x) for x in _need(1, args, "numbers")]
    return str(min_nums(nums))


def cmd_maxn(args):
    nums = [float(x) for x in _need(1, args, "numbers")]
    return str(max_nums(nums))


COMMANDS.update({
    "palnum": cmd_palnum,
    "digits": cmd_digits,
    "prod": cmd_prod,
    "minn": cmd_minn,
    "maxn": cmd_maxn,
})
COMMAND_NAMES = list(COMMANDS)

_old_check = cmd_check


def cmd_check(args):
    out = _old_check(args)
    assert is_palnum(121)
    assert not is_palnum(123)
    assert digit_count(120) == 3
    assert prod_nums([2, 3, 4]) == 24
    assert min_nums([3, 1, 8]) == 1
    assert max_nums([3, 1, 8]) == 8
    return out


COMMANDS["check"] = cmd_check
