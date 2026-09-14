#!/usr/bin/env python3
"""Tiny original playground CLI for the Grok repository."""
from __future__ import annotations
import argparse, base64, hashlib, math, random, sys, uuid
from datetime import datetime, timezone
VERSION = "0.19.0"
LINES = ["Understand the universe. Then maybe have a snack.", "Curiosity is a feature, not a bug."]
FORTUNES = ["Today is a good day to read the source.", "A box is just a sentence that asked for walls.", "Roman numerals are counting that learned to dress up."]
JOKES = ["Why did the function cross the road? To get to the other side effect."]
WHYS = ["Because understanding beats guessing, most of the time."]
IDEAS = ["Document a command that does not exist yet, then invent it."]
TIPS = ["Ship the smallest useful change, then iterate."]
COMMAND_NAMES = ["greet","quote","fortune","joke","why","idea","tip","flip","dice","color","now","week","day","echo","version","about","check","rot13","slug","hash","uuid","palindrome","pick","sample","shuffle","reverse","count","wrap","b64","sum","title","upper","lower","words","lines","chars","sort","dedupe","join","split","anagram","initials","indent","percent","clamp","random","commands","repeat","morse","unique","yesno","leet","vowels","bin","hex","caesar","consonants","pig","ascii","snake","camel","nato","freq","entropy","lev","rle","box","roman","unroman","isogram","tap"]
MORSE = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", " ": "/"}
LEET_MAP = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5", "t": "7", "A": "4", "E": "3", "I": "1", "O": "0", "S": "5", "T": "7"}
VOWELS = set("aeiouyAEIOUY")
def pick(seq): return random.choice(seq)
def cmd_greet(name):
    print(f"Hello, {name.strip() if name and name.strip() else 'friend'}. He does what he wants.")
def cmd_quote(): print(pick(LINES))
def cmd_fortune(): print(pick(FORTUNES))
def cmd_joke(): print(pick(JOKES))
def cmd_why(): print(pick(WHYS))
def cmd_idea(): print(pick(IDEAS))
def cmd_tip(): print(pick(TIPS))
def cmd_flip(): print("heads" if random.random()<.5 else "tails")
def cmd_dice(sides):
    if not sides: n=6
    elif sides.lower()=="coin": cmd_flip(); return
    else:
        try: n=int(sides)
        except ValueError:
            print(f"dice: need an integer or 'coin', got {sides!r}", file=sys.stderr); sys.exit(1)
        if n<2:
            print("dice: sides must be >= 2", file=sys.stderr); sys.exit(1)
    print(f"rolled {random.randint(1,n)} (d{n})")
def cmd_color(): print(f"#{random.randint(0,0xFFFFFF):06x}")
def cmd_now(): print(datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"))
def cmd_week():
    x=datetime.now(timezone.utc).isocalendar(); print(f"{x.year}-W{x.week:02d}-{x.weekday} UTC")
def cmd_day(): print(datetime.now(timezone.utc).strftime("%A"))
def require(text, name):
    if text is None or text=="":
        print(f"{name}: pass some text", file=sys.stderr); sys.exit(1)
    return text
def cmd_echo(t): print(require(t,'echo'))
def cmd_version(): print(VERSION)
def cmd_about(): print(f"Grok playground CLI v{VERSION}\nOriginal code only. Stdlib only. No third-party packages.\nRepo: https://github.com/peter-research/Grok")
def rot13(text):
    return "".join(chr((ord(c)-97+13)%26+97) if 'a'<=c<='z' else chr((ord(c)-65+13)%26+65) if 'A'<=c<='Z' else c for c in text)
def caesar(text, shift):
    out=[]
    for c in text:
        if 'a'<=c<='z': out.append(chr((ord(c)-97+shift)%26+97))
        elif 'A'<=c<='Z': out.append(chr((ord(c)-65+shift)%26+65))
        else: out.append(c)
    return ''.join(out)
def slugify(text):
    out=[]; dash=False
    for c in text.lower():
        if c.isalnum(): out.append(c); dash=False
        elif out and not dash: out.append('-'); dash=True
    if out and out[-1]=='-': out.pop()
    return ''.join(out) or 'item'
def cmd_rot13(t): print(rot13(require(t,'rot13')))
def cmd_slug(t): print(slugify(require(t,'slug').strip()))
def cmd_hash(t): print(hashlib.sha256(require(t,'hash').encode()).hexdigest())
def cmd_uuid(): print(uuid.uuid4())
def is_palindrome(t):
    c=[x.casefold() for x in t if x.isalnum()]; return bool(c) and c==c[::-1]
def cmd_palindrome(t): print('yes' if is_palindrome(require(t,'palindrome')) else 'no')
def items_required(items, name):
    if not any(x.strip() for x in items):
        print(f"{name}: pass at least one item", file=sys.stderr); sys.exit(1)
    return [x for x in items if x.strip()]
def cmd_pick_one(i): print(random.choice(items_required(i,'pick')))
def cmd_sample(count, items):
    pool=items_required(items,'sample')
    try: n=int(count) if count is not None else 1
    except ValueError:
        print('sample: count must be an integer', file=sys.stderr); sys.exit(1)
    if n<1:
        print('sample: count must be >= 1', file=sys.stderr); sys.exit(1)
    if n>len(pool):
        print('sample: count cannot exceed the number of items', file=sys.stderr); sys.exit(1)
    print(' '.join(random.sample(pool,n)))
def cmd_shuffle(i):
    x=items_required(i,'shuffle'); random.shuffle(x); print(' '.join(x))
def cmd_reverse(t): print(require(t,'reverse')[::-1])
def count_text(t): return len(t), len(t.split()), t.count('\n')+(1 if t else 0)
def cmd_count(t):
    c,w,l=count_text(require(t,'count')); print(f"{c} chars · {w} words · {l} lines")
def wrap_text(text, width):
    if width<8: raise ValueError('width')
    words=text.split()
    if not words: return text
    lines=[]; current=words[0]
    for word in words[1:]:
        if len(current)+1+len(word)<=width: current=f"{current} {word}"
        else: lines.append(current); current=word
    lines.append(current); return '\n'.join(lines)
def cmd_wrap(width, text):
    raw=require(text,'wrap')
    try: n=int(width) if width is not None else 72
    except ValueError:
        print('wrap: width must be an integer', file=sys.stderr); sys.exit(1)
    try: print(wrap_text(raw,n))
    except ValueError:
        print('wrap: width must be >= 8', file=sys.stderr); sys.exit(1)
def cmd_b64(t,d):
    try:
        print(base64.b64decode(require(t,'b64').encode(),validate=True).decode() if d else base64.b64encode(t.encode()).decode())
    except Exception:
        print('b64: could not decode that text', file=sys.stderr); sys.exit(1)
def cmd_sum(i):
    try: x=sum(float(v) for v in items_required(i,'sum'))
    except ValueError:
        print('sum: not a number', file=sys.stderr); sys.exit(1)
    print(str(int(x)) if x.is_integer() else format(x,'g'))
def title_case(t):
    return ''.join(c.upper() if c.isalnum() and (i==0 or not t[i-1].isalnum()) else c.lower() if c.isalnum() else c for i,c in enumerate(t))
def cmd_title(t): print(title_case(require(t,'title')))
def cmd_upper(t): print(require(t,'upper').upper())
def cmd_lower(t): print(require(t,'lower').lower())
def cmd_words(t): print('\n'.join(require(t,'words').split()))
def cmd_lines(t): print(len(require(t,'lines').splitlines()))
def cmd_chars(t): print(len(require(t,'chars')))
def cmd_sort(i): print(' '.join(sorted(items_required(i,'sort'), key=str.casefold)))
def cmd_dedupe(i):
    seen=set(); out=[]
    for x in items_required(i,'dedupe'):
        if x not in seen: seen.add(x); out.append(x)
    print(' '.join(out))
def cmd_join(i,sep): print(sep.join(items_required(i,'join')))
def cmd_split(t,sep): print('\n'.join(require(t,'split').split(sep)))
def cmd_anagram(a,b):
    a=require(a,'anagram'); b=require(b,'anagram')
    f=lambda x: sorted(c.casefold() for c in x if c.isalnum())
    print('yes' if f(a)==f(b) and f(a) else 'no')
def cmd_initials(t): print(''.join(x[0].upper() for x in require(t,'initials').split()))
def cmd_indent(t,n):
    require(t,'indent')
    if n<0:
        print('indent: spaces must be >= 0', file=sys.stderr); sys.exit(1)
    print('\n'.join(' '*n+x for x in t.splitlines()))
def cmd_percent(a,b):
    try: p,w=float(a),float(b)
    except (TypeError,ValueError):
        print('percent: pass two numbers', file=sys.stderr); sys.exit(1)
    if w==0:
        print('percent: whole cannot be zero', file=sys.stderr); sys.exit(1)
    print(format(p/w*100,'g')+'%')
def cmd_clamp(v,lo,hi):
    try: v,lo,hi=map(float,(v,lo,hi))
    except (TypeError,ValueError):
        print('clamp: pass value low high', file=sys.stderr); sys.exit(1)
    if lo>hi:
        print('clamp: low must be <= high', file=sys.stderr); sys.exit(1)
    r=min(max(v,lo),hi); print(str(int(r)) if r.is_integer() else format(r,'g'))
def cmd_random(lo,hi):
    try: lo,hi=int(lo or 1), int(hi or 100)
    except ValueError:
        print('random: bounds must be integers', file=sys.stderr); sys.exit(1)
    if lo>hi:
        print('random: low must be <= high', file=sys.stderr); sys.exit(1)
    print(random.randint(lo,hi))
def to_morse(text):
    out=[]
    for c in text.casefold():
        if c in MORSE: out.append(MORSE[c])
        elif c.isspace(): out.append('/')
    return ' '.join(out) if out else '.'
def unique_chars(text):
    seen=[]; bag=set()
    for c in text:
        if c not in bag:
            bag.add(c); seen.append(c)
    return ''.join(seen)
def to_leet(text):
    return ''.join(LEET_MAP.get(c, c) for c in text)
def count_vowels(text):
    return sum(1 for c in text if c in VOWELS)
def count_consonants(text):
    return sum(1 for c in text if c.isalpha() and c not in VOWELS)
def to_bin(text):
    return ' '.join(f'{b:08b}' for b in text.encode())
def to_hex(text):
    return text.encode().hex()
def pig_word(word):
    if not word: return word
    letters=[c for c in word if c.isalpha()]
    if not letters: return word
    first=letters[0]
    rest=''.join(letters[1:])
    if first.casefold() in 'aeiouy':
        moved=''.join(letters)+'yay'
    else:
        moved=rest+first+'ay'
    if word[0].isupper():
        moved=moved[:1].upper()+moved[1:].lower()
    else:
        moved=moved.lower()
    return moved
def to_pig(text):
    return ' '.join(pig_word(w) for w in text.split())
def to_ascii(text):
    return ' '.join(str(ord(c)) for c in text)
def cmd_repeat(count, text):
    raw=require(text,'repeat')
    try: n=int(count) if count is not None else 2
    except ValueError:
        print('repeat: count must be an integer', file=sys.stderr); sys.exit(1)
    if n<1 or n>80:
        print('repeat: count must be between 1 and 80', file=sys.stderr); sys.exit(1)
    print('\n'.join([raw]*n))
def cmd_morse(t): print(to_morse(require(t,'morse')))
def cmd_unique(t): print(unique_chars(require(t,'unique')))
def cmd_leet(t): print(to_leet(require(t,'leet')))
def cmd_vowels(t): print(count_vowels(require(t,'vowels')))
def cmd_consonants(t): print(count_consonants(require(t,'consonants')))
def cmd_bin(t): print(to_bin(require(t,'bin')))
def cmd_hex(t): print(to_hex(require(t,'hex')))
def cmd_pig(t): print(to_pig(require(t,'pig')))
def cmd_ascii(t): print(to_ascii(require(t,'ascii')))
def cmd_caesar(shift, text):
    raw=require(text,'caesar')
    try: n=int(shift) if shift is not None else 13
    except ValueError:
        print('caesar: shift must be an integer', file=sys.stderr); sys.exit(1)
    print(caesar(raw, n))
def cmd_yesno(): print(pick(['yes','no']))
def cmd_commands(): print('\n'.join(COMMAND_NAMES))
NATO = {"a":"Alfa","b":"Bravo","c":"Charlie","d":"Delta","e":"Echo","f":"Foxtrot","g":"Golf","h":"Hotel","i":"India","j":"Juliett","k":"Kilo","l":"Lima","m":"Mike","n":"November","o":"Oscar","p":"Papa","q":"Quebec","r":"Romeo","s":"Sierra","t":"Tango","u":"Uniform","v":"Victor","w":"Whiskey","x":"X-ray","y":"Yankee","z":"Zulu","0":"Zero","1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine"}
def to_snake(text):
    out=[]; prev=False
    for c in text.strip():
        if c.isupper() and out and not prev:
            out.append('_'); out.append(c.lower()); prev=False
        elif c.isalnum():
            out.append(c.lower()); prev=False
        else:
            if out and out[-1] != '_':
                out.append('_')
            prev=True
    if out and out[-1]=='_': out.pop()
    return ''.join(out) or 'item'
def to_camel(text, upper_first=False):
    parts=[]; buf=[]
    for c in text:
        if c.isalnum(): buf.append(c)
        else:
            if buf: parts.append(''.join(buf)); buf=[]
    if buf: parts.append(''.join(buf))
    if not parts: return 'item'
    first=parts[0]
    rest=''.join(p[:1].upper()+p[1:].lower() for p in parts[1:])
    head = first[:1].upper()+first[1:].lower() if upper_first else first[:1].lower()+first[1:]
    return head+rest
def to_nato(text):
    out=[]
    for c in text:
        k=c.casefold()
        if k in NATO: out.append(NATO[k])
        elif c.isspace(): out.append('/')
    return ' '.join(out) if out else '.'
def letter_freq(text):
    bag={}
    for c in text.casefold():
        if c.isalpha(): bag[c]=bag.get(c,0)+1
    if not bag: return '(no letters)'
    total=sum(bag.values())
    parts=[f"{k}:{v}({v*100/total:.0f}%)" for k,v in sorted(bag.items())]
    return ' '.join(parts)
def shannon_entropy(text):
    if not text: return 0.0
    bag={}
    for c in text: bag[c]=bag.get(c,0)+1
    n=len(text)
    value=-sum((c/n)*math.log2(c/n) for c in bag.values())
    return 0.0 if abs(value)<1e-12 else value
def cmd_snake(t): print(to_snake(require(t,'snake')))
def cmd_camel(t): print(to_camel(require(t,'camel')))
def cmd_nato(t): print(to_nato(require(t,'nato')))
def cmd_freq(t): print(letter_freq(require(t,'freq')))
def levenshtein(a, b):
    if a == b: return 0
    if not a: return len(b)
    if not b: return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(cur[j-1] + 1, prev[j] + 1, prev[j-1] + (ca != cb)))
        prev = cur
    return prev[-1]
def run_length(text):
    if not text: return ''
    out=[]; prev=text[0]; n=1
    for c in text[1:]:
        if c == prev: n += 1
        else:
            out.append(f'{n}{prev}' if n > 1 else prev)
            prev=c; n=1
    out.append(f'{n}{prev}' if n > 1 else prev)
    return ''.join(out)
def text_box(text):
    lines = text.splitlines() or ['']
    w = max(len(x) for x in lines)
    top = '+' + '-' * (w + 2) + '+'
    body = ['| ' + x.ljust(w) + ' |' for x in lines]
    return '\n'.join([top, *body, top])
def to_roman(n):
    if n < 1 or n > 3999:
        raise ValueError('range')
    pairs = ((1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I'))
    out=[]
    for v,s in pairs:
        while n >= v:
            out.append(s); n -= v
    return ''.join(out)
def cmd_lev(a,b):
    print(levenshtein(require(a,'lev'), require(b,'lev')))
def cmd_rle(t): print(run_length(require(t,'rle')))
def cmd_box(t): print(text_box(require(t,'box')))
def cmd_roman(n):
    raw = require(n,'roman')
    try: v = int(raw)
    except ValueError:
        print('roman: need an integer from 1 to 3999', file=sys.stderr); sys.exit(1)
    try: print(to_roman(v))
    except ValueError:
        print('roman: need an integer from 1 to 3999', file=sys.stderr); sys.exit(1)
def cmd_entropy(t):
    e=shannon_entropy(require(t,'entropy'))
    print(format(e,'g'))
def from_roman(text):
    raw = ''.join(c for c in text.upper() if c.isalpha())
    if not raw:
        raise ValueError('empty')
    values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total = 0
    prev = 0
    for c in reversed(raw):
        if c not in values:
            raise ValueError('bad')
        v = values[c]
        if v < prev:
            total -= v
        else:
            total += v
            prev = v
    if total < 1 or total > 3999 or to_roman(total) != raw:
        raise ValueError('bad')
    return total
def is_isogram(text):
    letters = [c.casefold() for c in text if c.isalpha()]
    return bool(letters) and len(letters) == len(set(letters))
TAP = 'abcdefghijklmnopqrstuvwxy'
def to_tap(text):
    out = []
    for c in text.casefold():
        if c == 'z':
            c = 'x'
        if c in TAP:
            i = TAP.index(c)
            out.append(f'{i//5+1}{i%5+1}')
        elif c.isspace():
            out.append('/')
    return ' '.join(out) if out else '.'
def cmd_unroman(t):
    raw = require(t,'unroman')
    try:
        print(from_roman(raw))
    except ValueError:
        print('unroman: need a valid Roman numeral from I to MMMCMXCIX', file=sys.stderr); sys.exit(1)
def cmd_isogram(t):
    print('yes' if is_isogram(require(t,'isogram')) else 'no')
def cmd_tap(t):
    print(to_tap(require(t,'tap')))
def cmd_check():
    assert len(COMMAND_NAMES)==len(set(COMMAND_NAMES))==71
    assert rot13(rot13('Hello, Grok!'))=='Hello, Grok!'
    assert slugify('Hello, Grok!')=='hello-grok'
    assert is_palindrome('Race car') and not is_palindrome('Grok')
    assert count_text('one two')==(7,2,1)
    assert title_case('hello grok')=='Hello Grok'
    assert wrap_text('one two three four',10)=='one two\nthree four'
    assert to_morse('sos')=='... --- ...'
    assert unique_chars('bookkeeper')=='bokepr'
    assert to_leet('Grok')=='Gr0k'
    assert count_vowels('Grok')==1
    assert count_consonants('Grok')==3
    assert to_bin('A')=='01000001'
    assert to_hex('A')=='41'
    assert caesar('Grok', 13)==rot13('Grok')
    assert caesar(caesar('Grok', 7), -7)=='Grok'
    assert to_pig('Grok')=='Rokgay'
    assert to_ascii('A')=='65'
    assert all(x in COMMAND_NAMES for x in ('day','echo','wrap','sample','repeat','morse','unique','yesno','leet','vowels','bin','hex','caesar','consonants','pig','ascii','snake','camel','nato','freq','entropy','lev','rle','box','roman','unroman','isogram','tap'))
    assert to_snake('HelloGrok')=='hello_grok'
    assert to_camel('hello_grok')=='helloGrok'
    assert to_nato('Grok')=='Golf Romeo Oscar Kilo'
    assert letter_freq('Aab').startswith('a:2')
    assert abs(shannon_entropy('aa'))<1e-12
    assert levenshtein('kitten','sitting')==3
    assert run_length('aaabbc')=='3a2bc'
    assert text_box('Grok').startswith('+')
    assert to_roman(2026)=='MMXXVI'
    assert from_roman('MMXXVI')==2026
    assert is_isogram('Grok') and not is_isogram('book')
    assert to_tap('sos')=='44 35 44'
    print('check ok')
def build_parser():
    p=argparse.ArgumentParser(prog='grok.py', description='Tiny original playground CLI for the Grok repository.')
    s=p.add_subparsers(dest='cmd')
    g=s.add_parser('greet'); g.add_argument('name', nargs='?')
    for n in ('quote','fortune','joke','why','idea','tip','flip','color','now','week','day','version','about','check','uuid','commands','yesno'): s.add_parser(n)
    q=s.add_parser('dice'); q.add_argument('sides', nargs='?')
    for n in ('rot13','slug','hash','palindrome','reverse','count','title','upper','lower','words','lines','chars','initials','echo','morse','unique','leet','vowels','bin','hex','consonants','pig','ascii','snake','camel','nato','freq','entropy','rle','box','roman','unroman','isogram','tap'):
        q=s.add_parser(n); q.add_argument('text', nargs='?')
    for n in ('pick','shuffle','sort','dedupe','sum'):
        q=s.add_parser(n); q.add_argument('items', nargs='*')
    q=s.add_parser('sample'); q.add_argument('count', nargs='?'); q.add_argument('items', nargs='*')
    q=s.add_parser('repeat'); q.add_argument('count', nargs='?'); q.add_argument('text', nargs='?')
    q=s.add_parser('wrap'); q.add_argument('width', nargs='?'); q.add_argument('text', nargs='?')
    q=s.add_parser('caesar'); q.add_argument('shift', nargs='?'); q.add_argument('text', nargs='?')
    q=s.add_parser('b64'); q.add_argument('text', nargs='?'); q.add_argument('--decode', action='store_true')
    q=s.add_parser('join'); q.add_argument('items', nargs='*'); q.add_argument('--sep', default=' ')
    q=s.add_parser('split'); q.add_argument('text', nargs='?'); q.add_argument('--sep', default=' ')
    q=s.add_parser('anagram'); q.add_argument('left', nargs='?'); q.add_argument('right', nargs='?')
    q=s.add_parser('indent'); q.add_argument('text', nargs='?'); q.add_argument('--spaces', type=int, default=2)
    q=s.add_parser('percent'); q.add_argument('part', nargs='?'); q.add_argument('whole', nargs='?')
    q=s.add_parser('clamp'); q.add_argument('value', nargs='?'); q.add_argument('low', nargs='?'); q.add_argument('high', nargs='?')
    q=s.add_parser('random'); q.add_argument('low', nargs='?'); q.add_argument('high', nargs='?')
    q=s.add_parser('lev'); q.add_argument('left', nargs='?'); q.add_argument('right', nargs='?')
    return p
def main(argv=None):
    a=build_parser().parse_args(argv)
    if a.cmd is None:
        cmd_greet(None); cmd_quote(); return 0
    h={'greet':lambda:cmd_greet(a.name),'quote':cmd_quote,'fortune':cmd_fortune,'joke':cmd_joke,'why':cmd_why,'idea':cmd_idea,'tip':cmd_tip,'flip':cmd_flip,'dice':lambda:cmd_dice(a.sides),'color':cmd_color,'now':cmd_now,'week':cmd_week,'day':cmd_day,'echo':lambda:cmd_echo(a.text),'version':cmd_version,'about':cmd_about,'check':cmd_check,'rot13':lambda:cmd_rot13(a.text),'slug':lambda:cmd_slug(a.text),'hash':lambda:cmd_hash(a.text),'uuid':cmd_uuid,'palindrome':lambda:cmd_palindrome(a.text),'pick':lambda:cmd_pick_one(a.items),'sample':lambda:cmd_sample(a.count,a.items),'shuffle':lambda:cmd_shuffle(a.items),'reverse':lambda:cmd_reverse(a.text),'count':lambda:cmd_count(a.text),'wrap':lambda:cmd_wrap(a.width,a.text),'b64':lambda:cmd_b64(a.text,a.decode),'sum':lambda:cmd_sum(a.items),'title':lambda:cmd_title(a.text),'upper':lambda:cmd_upper(a.text),'lower':lambda:cmd_lower(a.text),'words':lambda:cmd_words(a.text),'lines':lambda:cmd_lines(a.text),'chars':lambda:cmd_chars(a.text),'sort':lambda:cmd_sort(a.items),'dedupe':lambda:cmd_dedupe(a.items),'join':lambda:cmd_join(a.items,a.sep),'split':lambda:cmd_split(a.text,a.sep),'anagram':lambda:cmd_anagram(a.left,a.right),'initials':lambda:cmd_initials(a.text),'indent':lambda:cmd_indent(a.text,a.spaces),'percent':lambda:cmd_percent(a.part,a.whole),'clamp':lambda:cmd_clamp(a.value,a.low,a.high),'random':lambda:cmd_random(a.low,a.high),'commands':cmd_commands,'repeat':lambda:cmd_repeat(a.count,a.text),'morse':lambda:cmd_morse(a.text),'unique':lambda:cmd_unique(a.text),'yesno':cmd_yesno,'leet':lambda:cmd_leet(a.text),'vowels':lambda:cmd_vowels(a.text),'bin':lambda:cmd_bin(a.text),'hex':lambda:cmd_hex(a.text),'caesar':lambda:cmd_caesar(a.shift,a.text),'consonants':lambda:cmd_consonants(a.text),'pig':lambda:cmd_pig(a.text),'ascii':lambda:cmd_ascii(a.text),'snake':lambda:cmd_snake(a.text),'camel':lambda:cmd_camel(a.text),'nato':lambda:cmd_nato(a.text),'freq':lambda:cmd_freq(a.text),'entropy':lambda:cmd_entropy(a.text),'lev':lambda:cmd_lev(a.left,a.right),'rle':lambda:cmd_rle(a.text),'box':lambda:cmd_box(a.text),'roman':lambda:cmd_roman(a.text),'unroman':lambda:cmd_unroman(a.text),'isogram':lambda:cmd_isogram(a.text),'tap':lambda:cmd_tap(a.text)}
    h[a.cmd](); return 0
if __name__=='__main__':
    raise SystemExit(main())
