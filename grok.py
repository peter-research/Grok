#!/usr/bin/env python3
"""Tiny original playground CLI for the Grok repository."""
from pathlib import Path

_src = "".join(Path(__file__).with_name(f"_part{i}.py").read_text() for i in range(1, 13))
exec(compile(_src, "grok.py", "exec"), globals())
