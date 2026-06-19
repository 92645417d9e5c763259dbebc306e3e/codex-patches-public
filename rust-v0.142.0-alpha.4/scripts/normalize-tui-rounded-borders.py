#!/usr/bin/env python3
from pathlib import Path


# Source rounded corners stay as codepoints; replacements are visible output.
TRANSLATE = {
    0x256D: "┌",
    0x256E: "┐",
    0x2570: "└",
    0x256F: "┘",
}


for path in Path("codex-rs/tui/src").rglob("*"):
    if path.suffix not in {".rs", ".snap"}:
        continue

    old = path.read_text(encoding="utf-8")
    new = old.translate(TRANSLATE).replace("BorderType::Rounded", "BorderType::Plain")
    if new != old:
        path.write_text(new, encoding="utf-8")
