#!/usr/bin/env python3
"""
apply_i18n.py

Simple helper to generate a language-specific `config.i18n.<lang>.yaml` by
replacing known strings in `config.yaml` with translations from
`i18n/translations.json`.

Usage: python scripts/apply_i18n.py en
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config.yaml"
TRANSLATIONS = ROOT / "i18n" / "translations.json"


def load_translations():
    with TRANSLATIONS.open(encoding="utf-8") as f:
        return json.load(f)


def apply(lang: str):
    if not CONFIG.exists():
        print("config.yaml not found in workspace root")
        return 1
    data = CONFIG.read_text(encoding="utf-8")
    translations = load_translations()
    for key, langs in translations.items():
        if lang not in langs:
            print(f"Language '{lang}' not available for key {key}")
            continue
        target = langs[lang]
        # Replace any existing translation (any language value) with target
        for other in langs.values():
            if other == target:
                continue
            data = data.replace(other, target)
    out = ROOT / f"config.i18n.{lang}.yaml"
    out.write_text(data, encoding="utf-8")
    print(f"Wrote {out}")
    return 0


def main():
    if len(sys.argv) < 2:
        print("Usage: apply_i18n.py <lang>")
        return 2
    lang = sys.argv[1]
    return apply(lang)


if __name__ == "__main__":
    raise SystemExit(main())
