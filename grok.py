#!/usr/bin/env python3
"""Tiny original playground CLI for the Grok repository."""
from pathlib import Path

_src = "".join(Path(__file__).with_name(f"_part{i}.py").read_text() for i in range(1, 19))
_real_name = __name__
__name__ = "_parts"
exec(compile(_src, "grok.py", "exec"), globals())
__name__ = _real_name

if __name__ == "__main__":
    raise SystemExit(main())
