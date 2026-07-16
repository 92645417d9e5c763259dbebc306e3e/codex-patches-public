#!/usr/bin/env python3
from pathlib import Path
import unicodedata


TUI_SOURCE = Path("codex-rs/tui/src")


def codepoint(value: str) -> str:
    return chr(int(value, 16))


PRIMARY_HEAD_INPUT = codepoint("2022")
SECONDARY_HEAD_INPUT = codepoint("25E6")
SECONDARY_SEPARATOR_INPUT = codepoint("00B7")
VERTICAL_ELLIPSIS_INPUT = codepoint("22EE")
LEGACY_PRIMARY_HEAD_INPUT = codepoint("25A0")

# Replaced input glyphs use hexadecimal codepoints. Chosen output glyphs stay literal.
ROUNDED_BORDER_TRANSLATION = str.maketrans(
    {
        codepoint("256D"): "┌",
        codepoint("256E"): "┐",
        codepoint("2570"): "└",
        codepoint("256F"): "┘",
    }
)

NAMED_VISIBLE_REPLACEMENTS = {
    "success": (codepoint("2714"), "+"),
    "failure": (codepoint("2717"), "x"),
    "heavy_failure": (codepoint("2718"), "x"),
    "warning": (codepoint("26A0"), "!"),
    "primary_head": (PRIMARY_HEAD_INPUT, "▪"),
    "secondary_head": (SECONDARY_HEAD_INPUT, "▪"),
    "secondary_separator": (SECONDARY_SEPARATOR_INPUT, "▪"),
    "legacy_primary_head": (LEGACY_PRIMARY_HEAD_INPUT, "▪"),
    "continuation": (codepoint("21B3"), ">"),
    "cwd": (codepoint("2301"), "~"),
    "expanded": (codepoint("2304"), "v"),
    "info": (codepoint("24D8"), "i"),
    "powerline_branch": (codepoint("E0A0"), ">"),
}

VISIBLE_TRANSLATION = str.maketrans(
    {source: replacement for source, replacement in NAMED_VISIBLE_REPLACEMENTS.values()}
)

# These files own arbitrary input, grapheme, width, wrapping, or Unicode test
# semantics.  Their data is not product chrome and must remain byte-identical.
UNICODE_SEMANTICS_FILES = {
    "codex-rs/tui/src/bottom_pane/chat_composer.rs",
    "codex-rs/tui/src/bottom_pane/textarea.rs",
    "codex-rs/tui/src/live_wrap.rs",
    "codex-rs/tui/src/markdown.rs",
    "codex-rs/tui/src/markdown_stream.rs",
    "codex-rs/tui/src/mention_codec.rs",
    "codex-rs/tui/src/streaming/controller.rs",
    "codex-rs/tui/src/text_formatting.rs",
    "codex-rs/tui/src/wrapping.rs",
}

# Diff bodies are user payload.  Only the renderer-owned first header row is
# normalized in snapshots; the source owns the corresponding prefix.
DIFF_RENDER_SOURCE = "codex-rs/tui/src/diff_render.rs"
DIFF_RENDER_SNAPSHOT_PREFIX = (
    "codex-rs/tui/src/snapshots/codex_tui__diff_render__tests__"
)

BOX_SNAPSHOTS_REQUIRING_WIDTH_REPAIR = {
    "codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__pnpm_update_available_history_cell_snapshot.snap",
    "codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__standalone_unix_update_available_history_cell_snapshot.snap",
    "codex-rs/tui/src/history_cell/snapshots/codex_tui__history_cell__tests__standalone_windows_update_available_history_cell_snapshot.snap",
}

# Product glyphs outside the named Powerline set stay reviewable as Unicode
# codepoints.  Extra spacing preserves each replaced two-cell glyph's width.
ASTERISK_CODEPOINTS = (
    "2728",  # SPARKLES
    "1F50C",  # ELECTRIC PLUG
)
OWNED_WIDE_GLYPHS = {
    codepoint(value): "* " for value in ASTERISK_CODEPOINTS
}


def terminal_cell_width(text: str) -> int:
    """Return deterministic terminal-cell width for snapshot border repair."""
    width = 0
    for char in text:
        if char in {"\n", "\r"}:
            continue
        if unicodedata.combining(char) or unicodedata.category(char) in {"Cf", "Me", "Mn"}:
            continue
        width += 2 if unicodedata.east_asian_width(char) in {"F", "W"} else 1
    return width


def replace_owned_wide_glyphs(text: str) -> str:
    for source, replacement in OWNED_WIDE_GLYPHS.items():
        text = text.replace(source, replacement)
    return text


def normalize_diff_chrome(path: str, text: str) -> str:
    if path == DIFF_RENDER_SOURCE:
        candidates = (
            f'let mut header_spans: Vec<RtSpan<\'static>> = vec!["{PRIMARY_HEAD_INPUT} ".dim()];',
            f'let mut header_spans: Vec<RtSpan<\'static>> = vec!["{LEGACY_PRIMARY_HEAD_INPUT} ".dim()];',
            'let mut header_spans: Vec<RtSpan<\'static>> = vec!["▪ ".dim()];',
        )
        matches = sum(text.count(candidate) for candidate in candidates)
        if matches != 1:
            raise ValueError(f"expected one diff header producer in {path}")
        for candidate in candidates[:-1]:
            text = text.replace(candidate, candidates[-1])
        return text.replace(f'"{VERTICAL_ELLIPSIS_INPUT}".dim()', '"...".dim()')

    if path.startswith(DIFF_RENDER_SNAPSHOT_PREFIX) and path.endswith(".snap"):
        lines = text.splitlines(keepends=True)
        for index, line in enumerate(lines):
            for prefix in (
                f'"{PRIMARY_HEAD_INPUT} ',
                f'"{LEGACY_PRIMARY_HEAD_INPUT} ',
                '"▪ ',
            ):
                if line.startswith(prefix):
                    lines[index] = '"▪ ' + line[len(prefix):]
                    return "".join(lines)
            for prefix in (
                f"{PRIMARY_HEAD_INPUT} ",
                f"{LEGACY_PRIMARY_HEAD_INPUT} ",
                "▪ ",
            ):
                if line.startswith(prefix):
                    lines[index] = "▪ " + line[len(prefix):]
                    return "".join(lines)
        return text

    return text


def normalize_secondary_separators(path: str, text: str) -> str:
    if path == "codex-rs/tui/src/history_cell/separators.rs":
        return text.replace(f'join(" {PRIMARY_HEAD_INPUT} ")', 'join(" ▪ ")')
    return text


def normalize_owned_chrome_in_semantics_files(path: str, text: str) -> str:
    if path == "codex-rs/tui/src/bottom_pane/chat_composer.rs":
        return text.replace(f" {SECONDARY_SEPARATOR_INPUT} ", " ▪ ")
    if path == "codex-rs/tui/src/streaming/controller.rs":
        return text.replace(
            f'vec!["{PRIMARY_HEAD_INPUT} ".dim(), "Proposed Plan".bold()]',
            'vec!["▪ ".dim(), "Proposed Plan".bold()]',
        ).replace(
            f'vec!["{LEGACY_PRIMARY_HEAD_INPUT} ".dim(), "Proposed Plan".bold()]',
            'vec!["▪ ".dim(), "Proposed Plan".bold()]',
        ).replace(
            f'vec!["{PRIMARY_HEAD_INPUT} tail without newline".to_string()]',
            'vec!["▪ tail without newline".to_string()]',
        ).replace(
            f'vec!["{LEGACY_PRIMARY_HEAD_INPUT} tail without newline".to_string()]',
            'vec!["▪ tail without newline".to_string()]',
        )
    return text


def repair_box_right_padding(text: str) -> str:
    lines = text.splitlines(keepends=True)
    target_width = next(
        (
            terminal_cell_width(line.removesuffix("\n"))
            for line in lines
            if line.startswith("┌") and line.removesuffix("\n").endswith("┐")
        ),
        None,
    )
    if target_width is None:
        return text

    repaired = []
    for line in lines:
        body = line.removesuffix("\n")
        if body.startswith("│") and body.endswith("│"):
            row_width = terminal_cell_width(body)
            if row_width > target_width:
                raise ValueError("boxed snapshot row exceeds its top border")
            body = body[:-1] + (" " * (target_width - row_width)) + "│"
        repaired.append(body + ("\n" if line.endswith("\n") else ""))
    return "".join(repaired)


for path in TUI_SOURCE.rglob("*"):
    if path.suffix not in {".rs", ".snap"}:
        continue
    posix = path.as_posix()

    old = path.read_text(encoding="utf-8")
    new = old.translate(ROUNDED_BORDER_TRANSLATION)
    new = new.replace("BorderType::Rounded", "BorderType::Plain")
    new = normalize_diff_chrome(posix, new)
    is_diff_snapshot = posix.startswith(DIFF_RENDER_SNAPSHOT_PREFIX)
    if not is_diff_snapshot and posix != DIFF_RENDER_SOURCE:
        new = normalize_secondary_separators(posix, new)
        if posix in UNICODE_SEMANTICS_FILES:
            new = normalize_owned_chrome_in_semantics_files(posix, new)
        else:
            new = new.translate(VISIBLE_TRANSLATION)
            new = replace_owned_wide_glyphs(new)
    if posix in BOX_SNAPSHOTS_REQUIRING_WIDTH_REPAIR:
        new = repair_box_right_padding(new)

    if new != old:
        path.write_text(new, encoding="utf-8")


primary_head_survivors = []
for path in TUI_SOURCE.rglob("*"):
    if path.suffix not in {".rs", ".snap"}:
        continue
    posix = path.as_posix()
    if posix in UNICODE_SEMANTICS_FILES:
        continue
    text = path.read_text(encoding="utf-8")
    if PRIMARY_HEAD_INPUT in text or LEGACY_PRIMARY_HEAD_INPUT in text:
        primary_head_survivors.append(posix)

if primary_head_survivors:
    raise ValueError(
        "primary product-chrome bullet survived normalization: "
        + ", ".join(primary_head_survivors)
    )
