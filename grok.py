#!/usr/bin/env python3
"""Tiny original playground CLI for the Grok repository."""
from __future__ import annotations
import argparse, base64, hashlib, math, random, sys, uuid
from datetime import datetime, timezone
VERSION = "0.17.0"
LINES = ["Understand the universe. Then maybe have a snack.", "Curiosity is a feature, not a bug.", "If the repo is empty, fill it with something honest.", "Ask better questions. The answers follow.", "He does what he wants — within the rules of the playground.", "Small original tools beat giant copied ones.", "A sandbox is useful when you actually play in it.", "Code that stays readable is a kindness to future you.", "The best commit is the one that makes the next one easier.", "Silence is fine. A clear error message is better.", "Ship the small thing. The large thing can wait.", "A good name is half the design.", "The universe does not owe you a clean stack trace, but you can still write one.", "Play first. Polish second. Delete third if needed.", "A short function is easier to trust than a clever one.", "The next line you write is the only one that matters right now.", "Read the code before you change the code.", "A playground without play is just a directory.", "Clarity compounds faster than cleverness.", "Leave room for the next person — it might be you.", "A quiet tool that works beats a loud one that almost works.", "The best debug is the one you never need because the name was clear.", "Keep the surface small so the depth can breathe.", "An honest failure message is more useful than a polite silence.", "A small command that does one thing well is still a gift.", "A hash is just a fingerprint that does not argue.", "A week number is a calendar that learned to count.", "Reverse a string when you want to see it from the other end.", "Counting words is how a sentence learns its own size.", "Wrap a line when it starts to wander off the page.", "Morse is just a language that learned to blink.", "Leet is just a letter that learned to wear sunglasses.", "Pig Latin is a word that packed a suitcase and left the first letter behind.", "ASCII is just a letter that learned to give its house number."]
FORTUNES = ["Today is a good day to read the source.", "The next question is better than the last answer.", "Push something small. Then push something smaller.", "The universe is large. This CLI is not. That is fine.", "Leave the repo better than you found it.", "A clean diff is a quiet gift.", "If it runs without drama, keep it that way.", "Your future self will thank you for the comment you almost skipped.", "A one-line fix can still deserve a careful message.", "When in doubt, print the type and move on.", "One honest commit is worth ten half-finished branches.", "The best time to add a check is before you need it.", "Keep the interface small and the behaviour clear.", "A short commit message can still be kind.", "Delete the clever bit if the simple bit works.", "A colour that looks good in the dark is worth keeping.", "The next push does not have to be perfect. It has to be better.", "A slug that reads well is a name you can live with.", "A UUID is uniqueness without asking for a name first.", "A sum is a list that decided to stand together.", "A sample is a choice that still leaves the rest standing.", "Yes or no is still a decision, even when it is random.", "Binary is just text that decided to whisper in ones.", "A Caesar shift is rot13 that remembered it had other gears.", "NATO is a letter that learned to introduce itself slowly.", "Entropy is a word counting how surprised it is by itself."]
JOKES = ["Why did the function cross the road? To get to the other side effect.", "I told my code a joke about recursion. It laughed until the stack overflowed.", "There are only two hard things: cache invalidation, naming things, and off-by-one errors.", "A SQL query walks into a bar, approaches two tables, and asks: may I join you?", "Why do programmers prefer dark mode? Because light attracts bugs.", "Debugging is like being the detective in a crime movie where you are also the murderer.", "I would tell you a UDP joke, but you might not get it.", "How many programmers does it take to change a light bulb? None, that is a hardware problem.", "There is no place like 127.0.0.1.", "A programmer's favourite place? The foo bar.", "Why was the JavaScript developer sad? Because he didn't Node how to Express himself.", "Why do Python programmers wear glasses? Because they can't C.", "A byte walks into a bar and orders a pint. The bartender says: sorry, we don't serve doubles.", "ROT13 is just a Caesar salad with extra letters.", "I asked the palindrome if it was coming or going. It said racecar.", "Base64 walked into a party and said: just put me on the table, I'll wrap myself.", "Morse code asked for a drink. The bartender said: dash of tonic, two dots of lime.", "Leet spoke softly: h3ll0 w0rld.", "Pig Latin ordered ocolatechay. The waiter brought the first letter last."]
WHYS = ["Because understanding beats guessing, most of the time.", "Because a clear question is already half an answer.", "Because the universe is interesting and so is a well-named variable.", "Because small experiments teach faster than big plans.", "Because the playground only works if someone plays.", "Because original code is easier to own than borrowed complexity.", "Because curiosity compounds.", "Because a short loop is better than a long explanation.", "Because the next person who reads this might be you.", "Because a good name saves ten comments.", "Because shipping something small is still shipping.", "Because a quiet improvement is still an improvement.", "Because a title case line still wants to stand up straight.", "Because repeating a line is how a terminal learns patience.", "Because vowels keep a word from collapsing.", "Because consonants are the bones a vowel hangs its coat on."]
IDEAS = ["Add one more original line to the quotes list.", "Make the self-check a little stricter.", "Give the landing page a quieter colour accent.", "Document a command that does not exist yet, then invent it.", "Add a tiny test that the version string still looks like a version.", "Write a fortune that mentions the commit message.", "Make the dice command accept a word like 'coin' and still work.", "Add a one-line comment that future-you will actually thank.", "Trim a function that grew longer than it needed to be.", "Sync one list between the CLI and the HTML so they stay friends.", "Add a tip that is useful even if you ignore the rest.", "Make the version command print the date of the last meaningful change.", "Add a colour command that returns a random hex.", "Keep the HTML and the CLI lists within a few lines of each other.", "Give pick a fair shuffle so the last item is not special.", "Add a reverse command so text can look over its shoulder.", "Wrap long help text so a terminal can breathe.", "Teach the page to print Morse without using innerHTML.", "Give hex a twin called bin so bits can stand in two rows.", "Let Caesar pick a shift instead of always walking thirteen steps.", "Give snake and camel a way to trade coats without losing the word.", "Count letter frequencies before you call a text crowded."]
TIPS = ["Name the thing after what it does, not how it feels.", "Prefer a boring solution that works over a clever one that almost works.", "Write the check before you need the failure message.", "Delete the comment that just restates the code.", "A short public interface is a gift to everyone who uses it.", "If the test is hard to write, the design is telling you something.", "Ship the smallest useful change, then iterate.", "Read the error message twice before you change anything.", "Keep the happy path obvious and the edge cases explicit.", "A clean git history is optional. A clear intent is not.", "A random colour can still be intentional if you choose the palette carefully.", "A slug is just a name that travels well in a URL.", "Count before you claim the sentence is short.", "Sample instead of shuffle when you only need a few items.", "Unique letters tell you how crowded a word really is.", "Count the vowels before you claim the word can sing.", "Count the consonants before you claim the word can stand.", "A NATO word is just a letter wearing a nametag."]
COMMAND_NAMES = ["greet","quote","fortune","joke","why","idea","tip","flip","dice","color","now","week","day","echo","version","about","check","rot13","slug","hash","uuid","palindrome","pick","sample","shuffle","reverse","count","wrap","b64","sum","title","upper","lower","words","lines","chars","sort","dedupe","join","split","anagram","initials","indent","percent","clamp","random","commands","repeat","morse","unique","yesno","leet","vowels","bin","hex","caesar","consonants","pig","ascii","snake","camel","nato","freq","entropy"]
MORSE = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.- ".replace(" ",""), "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", " ": "/"}
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
def cmd_entropy(t):
    e=shannon_entropy(require(t,'entropy'))
    print(format(e,'g'))
def cmd_check():
    assert len(COMMAND_NAMES)==len(set(COMMAND_NAMES))==64
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
    assert all(x in COMMAND_NAMES for x in ('day','echo','wrap','sample','repeat','morse','unique','yesno','leet','vowels','bin','hex','caesar','consonants','pig','ascii','snake','camel','nato','freq','entropy'))
    assert to_snake('HelloGrok')=='hello_grok'
    assert to_camel('hello_grok')=='helloGrok'
    assert to_nato('Grok')=='Golf Romeo Oscar Kilo'
    assert letter_freq('Aab').startswith('a:2')
    assert abs(shannon_entropy('aa'))<1e-12
    print('check ok')
def build_parser():
    p=argparse.ArgumentParser(prog='grok.py', description='Tiny original playground CLI for the Grok repository.')
    s=p.add_subparsers(dest='cmd')
    g=s.add_parser('greet'); g.add_argument('name', nargs='?')
    for n in ('quote','fortune','joke','why','idea','tip','flip','color','now','week','day','version','about','check','uuid','commands','yesno'): s.add_parser(n)
    q=s.add_parser('dice'); q.add_argument('sides', nargs='?')
    for n in ('rot13','slug','hash','palindrome','reverse','count','title','upper','lower','words','lines','chars','initials','echo','morse','unique','leet','vowels','bin','hex','consonants','pig','ascii','snake','camel','nato','freq','entropy'):
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
    return p
def main(argv=None):
    a=build_parser().parse_args(argv)
    if a.cmd is None:
        cmd_greet(None); cmd_quote(); return 0
    h={'greet':lambda:cmd_greet(a.name),'quote':cmd_quote,'fortune':cmd_fortune,'joke':cmd_joke,'why':cmd_why,'idea':cmd_idea,'tip':cmd_tip,'flip':cmd_flip,'dice':lambda:cmd_dice(a.sides),'color':cmd_color,'now':cmd_now,'week':cmd_week,'day':cmd_day,'echo':lambda:cmd_echo(a.text),'version':cmd_version,'about':cmd_about,'check':cmd_check,'rot13':lambda:cmd_rot13(a.text),'slug':lambda:cmd_slug(a.text),'hash':lambda:cmd_hash(a.text),'uuid':cmd_uuid,'palindrome':lambda:cmd_palindrome(a.text),'pick':lambda:cmd_pick_one(a.items),'sample':lambda:cmd_sample(a.count,a.items),'shuffle':lambda:cmd_shuffle(a.items),'reverse':lambda:cmd_reverse(a.text),'count':lambda:cmd_count(a.text),'wrap':lambda:cmd_wrap(a.width,a.text),'b64':lambda:cmd_b64(a.text,a.decode),'sum':lambda:cmd_sum(a.items),'title':lambda:cmd_title(a.text),'upper':lambda:cmd_upper(a.text),'lower':lambda:cmd_lower(a.text),'words':lambda:cmd_words(a.text),'lines':lambda:cmd_lines(a.text),'chars':lambda:cmd_chars(a.text),'sort':lambda:cmd_sort(a.items),'dedupe':lambda:cmd_dedupe(a.items),'join':lambda:cmd_join(a.items,a.sep),'split':lambda:cmd_split(a.text,a.sep),'anagram':lambda:cmd_anagram(a.left,a.right),'initials':lambda:cmd_initials(a.text),'indent':lambda:cmd_indent(a.text,a.spaces),'percent':lambda:cmd_percent(a.part,a.whole),'clamp':lambda:cmd_clamp(a.value,a.low,a.high),'random':lambda:cmd_random(a.low,a.high),'commands':cmd_commands,'repeat':lambda:cmd_repeat(a.count,a.text),'morse':lambda:cmd_morse(a.text),'unique':lambda:cmd_unique(a.text),'yesno':cmd_yesno,'leet':lambda:cmd_leet(a.text),'vowels':lambda:cmd_vowels(a.text),'bin':lambda:cmd_bin(a.text),'hex':lambda:cmd_hex(a.text),'caesar':lambda:cmd_caesar(a.shift,a.text),'consonants':lambda:cmd_consonants(a.text),'pig':lambda:cmd_pig(a.text),'ascii':lambda:cmd_ascii(a.text),'snake':lambda:cmd_snake(a.text),'camel':lambda:cmd_camel(a.text),'nato':lambda:cmd_nato(a.text),'freq':lambda:cmd_freq(a.text),'entropy':lambda:cmd_entropy(a.text)}
    h[a.cmd](); return 0
if __name__=='__main__':
    raise SystemExit(main())
