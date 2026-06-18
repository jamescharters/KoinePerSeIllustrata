#!/usr/bin/env python3
"""
vocab_check.py — Vocabulary tracking tool for KoinePerSeIllustrata

Usage:
    python3 scripts/vocab_check.py [--chapter N] [--atrophy-threshold N]

Reports:
    - New lemmas introduced per chapter
    - Any lemma not seen for more than --atrophy-threshold chapters (default: 4)
    - Coverage against the NT-750 frequency list (nt750.txt if present)

The script uses a simple whitespace tokeniser and strips punctuation.
For proper lemmatisation, replace the token→lemma stub with a call to
a morphological analyser (e.g. greek-lemmatization or CLTK).
"""

import argparse
import glob
import os
import re
import sys
from collections import defaultdict

# ---------------------------------------------------------------------------
# Punctuation and token cleaning
# ---------------------------------------------------------------------------
_STRIP = str.maketrans("", "", ".,·;:!?—\"\'""''()[]{}*_")

def clean_token(tok: str) -> str:
    return tok.translate(_STRIP).strip()

def tokenise(text: str) -> list[str]:
    tokens = []
    for tok in text.split():
        ct = clean_token(tok)
        if ct:
            tokens.append(ct)
    return tokens

# ---------------------------------------------------------------------------
# Stub lemmatiser — returns the token lowercased.
# Replace with a real morphological analyser for production use.
# ---------------------------------------------------------------------------
def lemmatise(token: str) -> str:
    return token.lower()

# ---------------------------------------------------------------------------
# Chapter parsing
# ---------------------------------------------------------------------------
def load_chapters(src_dir: str) -> dict[int, list[str]]:
    """Return {chapter_number: [lemma, ...]} sorted by chapter."""
    chapters: dict[int, list[str]] = {}
    pattern = os.path.join(src_dir, "*.md")
    for path in sorted(glob.glob(pattern)):
        basename = os.path.basename(path)
        m = re.match(r"^(\d+)\.md$", basename)
        if not m:
            continue
        ch_num = int(m.group(1))
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        # Strip markdown headings and HTML comments
        text = re.sub(r"^#+.*$", "", text, flags=re.MULTILINE)
        text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
        lemmas = [lemmatise(t) for t in tokenise(text) if t]
        chapters[ch_num] = lemmas
    return chapters

# ---------------------------------------------------------------------------
# NT-750 reference list loader
# ---------------------------------------------------------------------------
def load_nt500(path: str) -> list[str]:
    """
    Load a newline-separated list of NT lemmas in frequency order.
    Lines starting with # are comments. Returns list of lowercase lemmas.
    """
    if not os.path.exists(path):
        return []
    lemmas = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith("#"):
                lemmas.append(line.lower())
    return lemmas

# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------
def analyse(
    chapters: dict[int, list[str]],
    atrophy_threshold: int,
    nt500: list[str],
    target_chapter: int | None,
) -> None:
    introduced: dict[str, int] = {}       # lemma → chapter first seen
    last_seen: dict[str, int] = {}        # lemma → chapter last seen
    chapter_new: dict[int, list[str]] = defaultdict(list)

    all_chapters = sorted(chapters.keys())

    for ch in all_chapters:
        lemmas = chapters[ch]
        seen_this_chapter: set[str] = set()
        for lemma in lemmas:
            if lemma not in introduced:
                introduced[lemma] = ch
                chapter_new[ch].append(lemma)
            last_seen[lemma] = ch
            seen_this_chapter.add(lemma)

    # --- Report ---
    report_chapters = [target_chapter] if target_chapter else all_chapters

    for ch in report_chapters:
        if ch not in chapters:
            print(f"Chapter {ch:03d}: not found in src/", file=sys.stderr)
            continue

        new = chapter_new.get(ch, [])
        print(f"\n{'='*60}")
        print(f"Chapter {ch:03d}  —  {len(new)} new lemmas introduced")
        print(f"{'='*60}")
        if new:
            for lemma in new:
                print(f"  + {lemma}")

        # Atrophy check: lemmas introduced before this chapter, last seen
        # more than atrophy_threshold chapters ago
        at_risk = [
            lemma for lemma, first in introduced.items()
            if first < ch and last_seen[lemma] < ch - atrophy_threshold
        ]
        if at_risk:
            print(f"\n  ⚠ ATROPHY RISK ({len(at_risk)} lemmas not seen for "
                  f">{atrophy_threshold} chapters):")
            for lemma in sorted(at_risk):
                gap = ch - last_seen[lemma]
                print(f"    {lemma}  (last ch {last_seen[lemma]:03d}, {gap} chs ago)")

    # --- NT-500 coverage ---
    if nt500:
        final_ch = all_chapters[-1] if all_chapters else 0
        covered = [l for l in nt500 if l in introduced]
        pct = 100 * len(covered) / len(nt500) if nt500 else 0
        print(f"\n{'='*60}")
        print(f"NT-750 coverage after ch {final_ch:03d}: "
              f"{len(covered)}/{len(nt500)} ({pct:.1f}%)")
        missing = [l for l in nt500 if l not in introduced]
        if missing:
            print(f"  Not yet introduced ({len(missing)}):")
            for lemma in missing[:20]:
                print(f"    - {lemma}")
            if len(missing) > 20:
                print(f"    ... and {len(missing) - 20} more")
        print(f"{'='*60}")

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Vocabulary tracking for KoinePerSeIllustrata"
    )
    parser.add_argument(
        "--chapter", type=int, default=None,
        help="Report only for this chapter number (default: all chapters)"
    )
    parser.add_argument(
        "--atrophy-threshold", type=int, default=4,
        help="Warn if a lemma has not appeared for this many chapters (default: 4)"
    )
    parser.add_argument(
        "--src", default="src",
        help="Directory containing chapter .md files (default: src)"
    )
    parser.add_argument(
        "--nt500", default="scripts/nt750.txt",
        help="Path to NT vocabulary frequency list (default: scripts/nt750.txt)"
    )
    args = parser.parse_args()

    chapters = load_chapters(args.src)
    if not chapters:
        print(f"No chapter files found in {args.src}/", file=sys.stderr)
        sys.exit(1)

    nt500 = load_nt500(args.nt500)
    if not nt500:
        print(f"Note: NT-750 list not found at {args.nt500} — coverage check skipped.",
              file=sys.stderr)

    analyse(chapters, args.atrophy_threshold, nt500, args.chapter)

if __name__ == "__main__":
    main()
