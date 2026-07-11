#!/usr/bin/env python3
import subprocess
from pathlib import Path


# Source glyphs stay as codepoints; replacements below are visible output.
SETS = [
    ("+", "2714 2705"),
    ("x", "2717 2718"),
    (
        "*",
        "2728 1F50C 23F3 1F44D 1F600 1F680 1F642 1F44B 1F4BB 1F308 1F30D 1F31F 1F3F3 1F40D 1F468 1F469 1F4AB 1F4DD 1F60A 1F9EA",
    ),
    ("!", "26A0"),
    ("▪", "25E6"),
    ("■", "2022"),
    (">", "21B3"),
    ("~", "2301"),
    ("-", "2325"),
    ("v", "2304"),
    ("i", "24D8"),
    ("...", "22EE"),
    ("", "FE0F"),
    (" ", "3000 200A"),
    ("[", "3010"),
    ("]", "3011"),
    ("?", "3042 0939"),
]

TRANSLATE = {
    int(code, 16): replacement for replacement, codes in SETS for code in codes.split()
}
TEXT = {
    r"\u{200A}": " ",
}

SKIP = {
    "codex-rs/tui/src/bottom_pane/chat_composer.rs",
    "codex-rs/tui/src/diff_render.rs",
    "codex-rs/tui/src/live_wrap.rs",
    "codex-rs/tui/src/wrapping.rs",
    "codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__diff_gallery_120x40.snap",
    "codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__diff_gallery_80x24.snap",
    "codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__diff_gallery_94x35.snap",
}

PAD_BOX = {
    "codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__pnpm_update_available_history_cell_snapshot.snap",
    "codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__standalone_unix_update_available_history_cell_snapshot.snap",
    "codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__standalone_windows_update_available_history_cell_snapshot.snap",
}

HEADER_ONLY = {
    "codex-rs/tui/src/diff_render.rs",
    "codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__diff_gallery_120x40.snap",
    "codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__diff_gallery_80x24.snap",
    "codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__diff_gallery_94x35.snap",
}

RUSTFMT = set()


def pad_box(text):
    lines = text.splitlines(keepends=True)
    width = next(
        (
            len(line.removesuffix("\n"))
            for line in lines
            if line.startswith("┌") and line.removesuffix("\n").endswith("┐")
        ),
        None,
    )
    if width is None:
        return text

    padded = []
    for line in lines:
        body = line.removesuffix("\n")
        if body.startswith("│") and body.endswith("│") and len(body) < width:
            body = body[:-1] + (" " * (width - len(body))) + "│"
        padded.append(body + ("\n" if line.endswith("\n") else ""))
    return "".join(padded)


for path in Path("codex-rs/tui/src").rglob("*"):
    if path.suffix not in {".rs", ".snap"}:
        continue
    posix = path.as_posix()

    old = path.read_text(encoding="utf-8")
    if posix in HEADER_ONLY:
        new = old.replace('vec!["• ".dim()]', 'vec!["■ ".dim()]')
        new = new.replace("• Edited 6 files", "■ Edited 6 files")
    elif posix in SKIP:
        continue
    else:
        new = old.translate(TRANSLATE)
        for source, replacement in TEXT.items():
            new = new.replace(source, replacement)
        if posix in PAD_BOX:
            new = pad_box(new)
    if new != old:
        path.write_text(new, encoding="utf-8")
        if path.suffix == ".rs":
            RUSTFMT.add(posix)

if RUSTFMT:
    subprocess.run(["rustfmt", *sorted(RUSTFMT)], check=True)
