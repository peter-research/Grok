"""Part 4 — stats, encodings, boxing."""


def median_nums(vals):
    s = sorted(vals)
    n = len(s)
    if n == 0:
        raise ValueError("empty")
    mid = n // 2
    if n % 2:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2


def reverse_words(text: str) -> str:
    return " ".join(reversed(text.split()))


def factor_list(n: int):
    if n < 1:
        raise ValueError("range")
    return [i for i in range(1, n + 1) if n % i == 0]


def mode_nums(vals):
    if not vals:
        raise ValueError("empty")
    counts = Counter(vals)
    best = max(counts.values())
    modes = [k for k, v in counts.items() if v == best]
    if len(modes) == 1:
        return modes[0]
    return modes


def stddev_nums(vals):
    if len(vals) < 2:
        raise ValueError("range")
    m = mean_nums(vals)
    var = sum((x - m) ** 2 for x in vals) / len(vals)
    return var ** 0.5


def pow_nums(a, b):
    if abs(b) > 32 and abs(a) > 1:
        raise ValueError("range")
    return a ** b


def unb64(text: str) -> str:
    raw = base64.b64decode(text.encode(), validate=True)
    return raw.decode()


def hamming(a: str, b: str) -> int:
    if len(a) != len(b):
        raise ValueError("length")
    return sum(x != y for x, y in zip(a, b))


def box_text(text: str) -> str:
    lines = text.splitlines() or [text]
    w = max(len(line) for line in lines)
    top = "+" + "-" * (w + 2) + "+"
    body = "\n".join("| " + line.ljust(w) + " |" for line in lines)
    return f"{top}\n{body}\n{top}"


def sum_nums(vals):
    return sum(vals)
