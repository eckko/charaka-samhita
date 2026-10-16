#!/usr/bin/env python3
"""List every unit whose data asks for a human look.

    python3 tools/pipeline/make_review_queue.py > docs/review-queue.md

A unit is listed when its `confidence` is not "high", when it has
`text_flags` (suspected typos in the SARIT text) or when `notes` is not
empty. Run it again after changing data/.
"""
import json
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent.parent / "data"


def main():
    print("# Review queue (generated; do not edit by hand)\n")
    print("Source: `data/sutrasthana*_verses.json`. Regenerate with "
          "`python3 tools/pipeline/make_review_queue.py`.\n")
    for path in sorted(DATA.glob("sutrasthana*_verses.json")):
        chapter = path.stem.replace("sutrasthana", "").split("_")[0]
        units = json.loads(path.read_text(encoding="utf-8"))
        low = [u for u in units if u.get("confidence") != "high"]
        flagged = [u for u in units if u.get("text_flags")]
        print(f"## Sutrasthana chapter {chapter}: {len(units)} units, "
              f"{len(low)} not 'high' confidence, {len(flagged)} with "
              "text flags\n")
        for unit in units:
            reasons = []
            if unit.get("confidence") != "high":
                reasons.append(f"confidence {unit.get('confidence')}")
            for flag in unit.get("text_flags") or []:
                reasons.append(f"text flag `{flag.get('src')}` -> "
                               f"`{flag.get('suggest')}`: {flag.get('why')}")
            if reasons:
                print(f"- **{chapter}.{unit['n']}**: " + "; ".join(reasons))
        print()


if __name__ == "__main__":
    main()
