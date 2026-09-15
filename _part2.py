def count_text(t):
    return len(t), len(t.split()), t.count("\n") + (1 if t else 0)


def title_case(t):
    return "".join(
        c.upper() if c.isalnum() and (i == 0 or not t[i - 1].isalnum())
        else c.lower() if c.isalnum() else c
        for i, c in enumerate(t)
    )


def wrap_text(text, width):
    if width < 8:
        raise ValueError("width")
    words = text.split()
    if not words:
        return text
    lines = []
    current = words[0]
    for word in words[1:]:
        if len(current) + 1 + len(word) <= width:
            current = f"{current} {word}"
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return "\n".join(lines)


def nth_fib(n):
    if n < 0 or n > 92:
        raise ValueError("range")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def gcd_int(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm_int(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd_int(a, b) * b)


def run_rle(text):
    if not text:
        return ""
    out = []
    n = 1
    for i in range(1, len(text) + 1):
        if i < len(text) and text[i] == text[i - 1]:
            n += 1
        else:
            out.append((str(n) if n > 1 else "") + text[i - 1])
            n = 1
    return "".join(out)


def undo_rle(text):
    out = []
    i = 0
    n = len(text)
    while i < n:
        if text[i].isdigit():
            j = i
            while j < n and text[j].isdigit():
                j += 1
            if j == n:
                raise ValueError("bad")
            count = int(text[i:j])
            if count < 1 or count > 200:
                raise ValueError("bad")
            out.append(text[j] * count)
            i = j + 1
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


def factorial_int(n):
    if n < 0 or n > 20:
        raise ValueError("range")
    v = 1
    for i in range(2, n + 1):
        v *= i
    return v


def mean_nums(vals):
    return sum(vals) / len(vals)
