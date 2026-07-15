#!/usr/bin/env python3
from pathlib import Path


TUI_SOURCE = Path("codex-rs/tui/src")

# Product chrome only: the codepoints remain explicit and reviewable.
ROUNDED_BORDER_TRANSLATION = str.maketrans(
    {
        "╭": "┌",
        "╮": "┐",
        "╰": "└",
        "╯": "┘",
    }
)


for path in TUI_SOURCE.rglob("*"):
    if path.suffix not in {".rs", ".snap"}:
        continue

    old = path.read_text(encoding="utf-8")
    new = old.translate(ROUNDED_BORDER_TRANSLATION)
    new = new.replace("BorderType::Rounded", "BorderType::Plain")
    if new != old:
        path.write_text(new, encoding="utf-8")
