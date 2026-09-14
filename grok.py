#!/usr/bin/env python3
"""Tiny original playground CLI for the Grok repository."""
from __future__ import annotations
import argparse, random, sys, uuid
from datetime import datetime, timezone
VERSION = "0.22.0"
LINES = ["Understand the universe. Then maybe have a snack.", "Curiosity is a feature, not a bug."]
FORTUNES = ["Today is a good day to read the source."]
JOKES = ["Why did the function cross the road? To get to the other side effect."]
WHYS = ["Because understanding beats guessing, most of the time."]
IDEAS = ["Document a command that does not exist yet, then invent it."]
TIPS = ["Ship the smallest useful change, then iterate."]
COMMAND_NAMES = ["greet","quote","fortune","joke","why","idea","tip","flip","dice","color","now","week","day","echo","version","about","check","rot13","slug","hash","uuid","palindrome","pick","sample","shuffle","reverse","count","wrap","b64","sum","title","upper","lower","words","lines","chars","sort","dedupe","join","split","anagram","initials","indent","percent","clamp","random","commands","repeat","morse","unique","yesno","leet","vowels","bin","hex","caesar","consonants","pig","ascii","snake","camel","nato","freq","entropy","lev","rle","box","roman","unroman","isogram","tap","fib","prime","gcd","lcm","unrle","fact","mean","median","revwords","factors"]
def pick(seq): return random.choice(seq)
def require(text, name):
    if text is None or text=="":
        print(f"{name}: pass some text", file=sys.stderr); sys.exit(1)
    return text
def items_required(items, name):
    if not any(x.strip() for x in items):
        print(f"{name}: pass at least one item", file=sys.stderr); sys.exit(1)
    return [x for x in items if x.strip()]
def rot13(text):
    return "".join(chr((ord(c)-97+13)%26+97) if 'a'<=c<='z' else chr((ord(c)-65+13)%26+65) if 'A'<=c<='Z' else c for c in text)
def slugify(text):
    out=[]; dash=False
    for c in text.lower():
        if c.isalnum(): out.append(c); dash=False
        elif out and not dash: out.append('-'); dash=True
    if out and out[-1]=='-': out.pop()
    return ''.join(out) or 'item'
def is_palindrome(t):
    c=[x.casefold() for x in t if x.isalnum()]; return bool(c) and c==c[::-1]
def count_text(t): return len(t), len(t.split()), t.count('\n')+(1 if t else 0)
def title_case(t):
    return ''.join(c.upper() if c.isalnum() and (i==0 or not t[i-1].isalnum()) else c.lower() if c.isalnum() else c for i,c in enumerate(t))
def wrap_text(text, width):
    if width<8: raise ValueError('width')
    words=text.split()
    if not words: return text
    lines=[]; current=words[0]
    for word in words[1:]:
        if len(current)+1+len(word)<=width: current=f"{current} {word}"
        else: lines.append(current); current=word
    lines.append(current); return '\n'.join(lines)
def nth_fib(n):
    if n < 0 or n > 92: raise ValueError('range')
    a, b = 0, 1
    for _ in range(n): a, b = b, a + b
    return a
def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False
    i = 3
    while i * i <= n:
        if n % i == 0: return False
        i += 2
    return True
def gcd_int(a, b):
    a, b = abs(a), abs(b)
    while b: a, b = b, a % b
    return a
def lcm_int(a, b):
    if a == 0 or b == 0: return 0
    return abs(a // gcd_int(a, b) * b)
def undo_rle(text):
    out=[]; i=0; n=len(text)
    while i < n:
        if text[i].isdigit():
            j=i
            while j < n and text[j].isdigit(): j += 1
            if j == n: raise ValueError('bad')
            count=int(text[i:j])
            if count < 1 or count > 200: raise ValueError('bad')
            out.append(text[j]*count); i=j+1
        else:
            out.append(text[i]); i += 1
    return ''.join(out)
def factorial_int(n):
    if n < 0 or n > 20: raise ValueError('range')
    v = 1
    for i in range(2, n + 1):
        v *= i
    return v
def mean_nums(vals):
    return sum(vals) / len(vals)
def median_nums(vals):
    s = sorted(vals); n = len(s); mid = n // 2
    if n % 2: return s[mid]
    return (s[mid - 1] + s[mid]) / 2
def reverse_words(text):
    return ' '.join(text.split()[::-1])
def factor_list(n):
    if n < 1 or n > 1_000_000: raise ValueError('range')
    out = []; i = 1
    while i * i <= n:
        if n % i == 0:
            out.append(i)
            if i * i != n: out.append(n // i)
        i += 1
    return sorted(out)
def parse_int(raw, name, lo=None, hi=None):
    try: v = int(require(raw, name))
    except ValueError:
        print(f'{name}: need an integer', file=sys.stderr); sys.exit(1)
    if lo is not None and v < lo or hi is not None and v > hi:
        print(f'{name}: out of range', file=sys.stderr); sys.exit(1)
    return v
def cmd_greet(name):
    print(f"Hello, {name.strip() if name and name.strip() else 'friend'}. He does what he wants.")
def cmd_quote(): print(pick(LINES))
def cmd_version(): print(VERSION)
def cmd_about(): print(f"Grok playground CLI v{VERSION}\nOriginal code only. Stdlib only.\nRepo: https://github.com/peter-research/Grok")
def cmd_commands(): print('\n'.join(COMMAND_NAMES))
def cmd_fact(n):
    try: print(factorial_int(parse_int(n, 'fact')))
    except ValueError:
        print('fact: need an integer from 0 to 20', file=sys.stderr); sys.exit(1)
def cmd_mean(items):
    raw = items_required(items, 'mean')
    try: nums = [float(x) for x in raw]
    except ValueError:
        print('mean: not a number', file=sys.stderr); sys.exit(1)
    r = mean_nums(nums)
    print(str(int(r)) if float(r).is_integer() else format(r, 'g'))
def cmd_median(items):
    raw = items_required(items, 'median')
    try: nums = [float(x) for x in raw]
    except ValueError:
        print('median: not a number', file=sys.stderr); sys.exit(1)
    r = median_nums(nums)
    print(str(int(r)) if float(r).is_integer() else format(r, 'g'))
def cmd_revwords(t):
    print(reverse_words(require(t, 'revwords')))
def cmd_factors(n):
    try: print(' '.join(str(x) for x in factor_list(parse_int(n, 'factors'))))
    except ValueError:
        print('factors: need an integer from 1 to 1000000', file=sys.stderr); sys.exit(1)
def cmd_fib(n):
    try: print(nth_fib(parse_int(n, 'fib')))
    except ValueError:
        print('fib: need an integer from 0 to 92', file=sys.stderr); sys.exit(1)
def cmd_prime(n):
    v = parse_int(n, 'prime')
    print('yes' if is_prime(v) else 'no')
def cmd_gcd(items):
    raw = items_required(items, 'gcd')
    if len(raw) != 2:
        print('gcd: need two integers', file=sys.stderr); sys.exit(1)
    try: a, b = int(raw[0]), int(raw[1])
    except ValueError:
        print('gcd: need two integers', file=sys.stderr); sys.exit(1)
    print(gcd_int(a, b))
def cmd_lcm(items):
    raw = items_required(items, 'lcm')
    if len(raw) != 2:
        print('lcm: need two integers', file=sys.stderr); sys.exit(1)
    try: a, b = int(raw[0]), int(raw[1])
    except ValueError:
        print('lcm: need two integers', file=sys.stderr); sys.exit(1)
    print(lcm_int(a, b))
def cmd_rot13(t):
    print(rot13(require(t, 'rot13')))
def cmd_slug(t):
    print(slugify(require(t, 'slug')))
def cmd_check():
    assert len(COMMAND_NAMES)==len(set(COMMAND_NAMES))==81
    assert rot13(rot13('Hello, Grok!'))=='Hello, Grok!'
    assert slugify('Hello, Grok!')=='hello-grok'
    assert is_palindrome('Race car') and not is_palindrome('Grok')
    assert count_text('one two')==(7,2,1)
    assert title_case('hello grok')=='Hello Grok'
    assert wrap_text('one two three four',10)=='one two\nthree four'
    assert nth_fib(10)==55
    assert is_prime(13) and not is_prime(1)
    assert gcd_int(54,24)==6
    assert lcm_int(4,6)==12
    assert undo_rle('3a2bc')=='aaabbc'
    assert factorial_int(5)==120
    assert mean_nums([1,2,3])==2
    assert median_nums([1,3,2])==2
    assert reverse_words('hello grok')=='grok hello'
    assert factor_list(12)==[1,2,3,4,6,12]
    print('check ok')
def build_parser():
    p=argparse.ArgumentParser(prog='grok.py', description='Tiny original playground CLI for the Grok repository.')
    s=p.add_subparsers(dest='cmd')
    g=s.add_parser('greet'); g.add_argument('name', nargs='?')
    for n in ('quote','fortune','joke','why','idea','tip','flip','color','now','week','day','version','about','check','uuid','commands','yesno'): s.add_parser(n)
    for n in ('fact','revwords','factors','echo','fib','prime','rot13','slug'):
        q=s.add_parser(n); q.add_argument('text', nargs='?')
    for n in ('mean','median','gcd','lcm'):
        q=s.add_parser(n); q.add_argument('items', nargs='*')
    return p
def main(argv=None):
    a=build_parser().parse_args(argv)
    if a.cmd is None:
        cmd_greet(None); cmd_quote(); return 0
    h={
        'greet':lambda:cmd_greet(a.name),'quote':cmd_quote,'fortune':lambda:print(pick(FORTUNES)),
        'joke':lambda:print(pick(JOKES)),'why':lambda:print(pick(WHYS)),'idea':lambda:print(pick(IDEAS)),
        'tip':lambda:print(pick(TIPS)),'flip':lambda:print('heads' if random.random()<.5 else 'tails'),
        'color':lambda:print(f'#{random.randint(0,0xFFFFFF):06x}'),
        'now':lambda:print(datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')),
        'week':lambda:print('week'),'day':lambda:print(datetime.now(timezone.utc).strftime('%A')),
        'version':cmd_version,'about':cmd_about,'check':cmd_check,'uuid':lambda:print(uuid.uuid4()),
        'commands':cmd_commands,'yesno':lambda:print(pick(['yes','no'])),
        'fact':lambda:cmd_fact(a.text),'revwords':lambda:cmd_revwords(a.text),'factors':lambda:cmd_factors(a.text),
        'echo':lambda:print(require(a.text,'echo')),'mean':lambda:cmd_mean(a.items),'median':lambda:cmd_median(a.items),
        'fib':lambda:cmd_fib(a.text),'prime':lambda:cmd_prime(a.text),
        'gcd':lambda:cmd_gcd(a.items),'lcm':lambda:cmd_lcm(a.items),
        'rot13':lambda:cmd_rot13(a.text),'slug':lambda:cmd_slug(a.text),
    }
    if a.cmd not in h:
        print('command exists in name list; core implements a subset');
        return 0
    h[a.cmd](); return 0
if __name__=='__main__':
    raise SystemExit(main())
