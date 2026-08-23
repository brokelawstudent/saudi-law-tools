"""Command-line interface for Saudi Law Tools."""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Sequence
from pathlib import Path
from typing import TextIO

from .document import parse_document
from .normalize import normalize_arabic_text


def _read_text(path: str, stdin: TextIO) -> str:
    if path == "-":
        return stdin.read()
    return Path(path).read_text(encoding="utf-8")


def _write_text(value: str, path: str | None, stdout: TextIO) -> None:
    if path is None or path == "-":
        stdout.write(value)
        if not value.endswith("\n"):
            stdout.write("\n")
        return
    Path(path).write_text(value, encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="saudi-law-tools",
        description="Parse and normalize Arabic Saudi legal text.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    parse_command = subparsers.add_parser(
        "parse", help="Parse a document and emit structured JSON."
    )
    parse_command.add_argument("input", nargs="?", default="-", help="UTF-8 file or -")
    parse_command.add_argument("-o", "--output", help="Output file; defaults to stdout")
    parse_command.add_argument(
        "--compact", action="store_true", help="Emit compact rather than indented JSON"
    )

    normalize_command = subparsers.add_parser(
        "normalize", help="Normalize Arabic legal text."
    )
    normalize_command.add_argument(
        "input", nargs="?", default="-", help="UTF-8 file or -"
    )
    normalize_command.add_argument(
        "-o", "--output", help="Output file; defaults to stdout"
    )
    normalize_command.add_argument(
        "--keep-digits",
        action="store_true",
        help="Preserve Arabic-Indic and Eastern Arabic digits",
    )
    normalize_command.add_argument(
        "--keep-tatweel", action="store_true", help="Preserve tatweel characters"
    )
    return parser


def main(
    argv: Sequence[str] | None = None,
    *,
    stdin: TextIO | None = None,
    stdout: TextIO | None = None,
) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    stdin = stdin or sys.stdin
    stdout = stdout or sys.stdout

    try:
        source = _read_text(args.input, stdin)
        if args.command == "parse":
            indent = None if args.compact else 2
            rendered = json.dumps(
                parse_document(source), ensure_ascii=False, indent=indent
            )
        else:
            rendered = normalize_arabic_text(
                source,
                normalize_numbers=not args.keep_digits,
                remove_tatweel=not args.keep_tatweel,
            )
        _write_text(rendered, args.output, stdout)
    except (OSError, UnicodeError) as exc:
        parser.exit(1, f"saudi-law-tools: {exc}\n")

    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
