"""Part 7 — v0.30 commands."""


def cmd_f2c(args):
    return str(fahrenheit_to_c(float(_need(1, args)[0])))


def cmd_deficient(args):
    return "yes" if is_deficient(int(_need(1, args)[0])) else "no"


def cmd_square(args):
    return "yes" if is_square(int(_need(1, args)[0])) else "no"


def cmd_cube(args):
    return str(cube_int(int(_need(1, args)[0])))


def cmd_mid(args):
    return mid_text(" ".join(_need(1, args, "text")))


COMMANDS.update({
    "f2c": cmd_f2c,
    "deficient": cmd_deficient,
    "square": cmd_square,
    "cube": cmd_cube,
    "mid": cmd_mid,
})
COMMAND_NAMES = list(COMMANDS)

_old_check = cmd_check


def cmd_check(args):
    out = _old_check(args)
    assert abs(fahrenheit_to_c(212) - 100.0) < 1e-9
    assert is_deficient(8)
    assert is_square(16)
    assert cube_int(3) == 27
    assert mid_text("Grok") == "ro"
    return out


COMMANDS["check"] = cmd_check
