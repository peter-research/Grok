"""Part 3 — encodings, roman numerals, case converters."""

MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", " ": "/",
}

NATO = {
    "A": "Alfa", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo",
    "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliett",
    "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar",
    "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
    "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "Xray",
    "Y": "Yankee", "Z": "Zulu",
}

LEET = str.maketrans("AaEeIiOoSsTt", "443311005577")

ROMAN_MAP = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]


def to_morse(text: str) -> str:
    out = []
    for c in text.upper():
        if c in MORSE:
            out.append(MORSE[c])
    return " ".join(out)


def unique_chars(text: str) -> str:
    seen = []
    for c in text:
        if c not in seen:
            seen.append(c)
    return "".join(seen)


def yes_no(text: str) -> str:
    t = text.strip().lower()
    if t in {"y", "yes", "true", "1", "on"}:
        return "yes"
    if t in {"n", "no", "false", "0", "off"}:
        return "no"
    return "maybe"


def to_leet(text: str) -> str:
    return text.translate(LEET)


def count_vowels(text: str) -> int:
    return sum(1 for c in text.lower() if c in "aeiouy")


def count_consonants(text: str) -> int:
    return sum(1 for c in text.lower() if c.isalpha() and c not in "aeiouy")


def to_bin(n: int) -> str:
    return bin(n)


def to_hex(n: int) -> str:
    return hex(n)


def caesar(text: str, shift: int) -> str:
    shift %= 26
    out = []
    for c in text:
        if "A" <= c <= "Z":
            out.append(chr((ord(c) - 65 + shift) % 26 + 65))
        elif "a" <= c <= "z":
            out.append(chr((ord(c) - 97 + shift) % 26 + 97))
        else:
            out.append(c)
    return "".join(out)


def pig_latin(word: str) -> str:
    if not word:
        return word
    w = word
    vowels = "aeiouAEIOU"
    if w[0] in vowels:
        return w + "way"
    i = 0
    while i < len(w) and w[i] not in vowels:
        i += 1
    return w[i:] + w[:i] + "ay"


def ascii_codes(text: str) -> str:
    return " ".join(str(ord(c)) for c in text)


def to_snake(text: str) -> str:
    out = []
    for i, c in enumerate(text):
        if c.isupper() and i and (text[i - 1].islower() or (i + 1 < len(text) and text[i + 1].islower())):
            out.append("_")
        if c.isalnum():
            out.append(c.lower())
        elif out and out[-1] != "_":
            out.append("_")
    return "".join(out).strip("_")


def to_camel(text: str) -> str:
    parts = [p for p in slugify(text).split("-") if p]
    if not parts:
        return ""
    return parts[0].lower() + "".join(p.title() for p in parts[1:])


def to_nato(text: str) -> str:
    return " ".join(NATO[c] for c in text.upper() if c in NATO)


def char_freq(text: str) -> str:
    counts = Counter(text)
    return " ".join(f"{c}:{n}" for c, n in counts.most_common())


def entropy_text(text: str) -> float:
    if not text:
        return 0.0
    n = len(text)
    counts = Counter(text)
    return -sum((c / n) * log2(c / n) for c in counts.values())


def lev_dist(a: str, b: str) -> int:
    if len(a) < len(b):
        a, b = b, a
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            ins = cur[j - 1] + 1
            delete = prev[j] + 1
            sub = prev[j - 1] + (ca != cb)
            cur.append(min(ins, delete, sub))
        prev = cur
    return prev[-1]


def to_roman(n: int) -> str:
    if n < 1 or n > 3999:
        raise ValueError("range")
    out = []
    for val, sym in ROMAN_MAP:
        while n >= val:
            out.append(sym)
            n -= val
    return "".join(out)


def from_roman(text: str) -> int:
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    s = text.upper()
    if not s or any(c not in vals for c in s):
        raise ValueError("bad")
    total = 0
    prev = 0
    for c in reversed(s):
        v = vals[c]
        if v < prev:
            total -= v
        else:
            total += v
            prev = v
    if to_roman(total) != s:
        raise ValueError("bad")
    return total


def is_isogram(text: str) -> bool:
    letters = [c.lower() for c in text if c.isalpha()]
    return bool(letters) and len(letters) == len(set(letters))


def tap_code(text: str) -> str:
    alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    out = []
    for c in text.upper():
        if c == "J":
            c = "I"
        if c in alpha:
            i = alpha.index(c)
            out.append(f"{i // 5 + 1}{i % 5 + 1}")
    return " ".join(out)
