from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
VERSION_FILE = ROOT / "docs" / "i18n" / "version.txt"
FILES = [
    ROOT / "README.md",
    ROOT / "README.zh-CN.md",
    ROOT / "README.ja.md",
    ROOT / "README.ko.md",
    ROOT / "README.es.md",
]

expected = VERSION_FILE.read_text(encoding="utf-8").strip()
pattern = re.compile(r"<!--\s*i18n-version:\s*([^\s]+)\s*-->")
errors = []

for path in FILES:
    if not path.exists():
        errors.append(f"missing: {path.relative_to(ROOT)}")
        continue

    text = path.read_text(encoding="utf-8")
    match = pattern.search(text[:300])
    if not match:
        errors.append(f"missing i18n-version marker: {path.relative_to(ROOT)}")
        continue

    actual = match.group(1)
    if actual != expected:
        errors.append(
            f"version mismatch: {path.relative_to(ROOT)} has {actual}, expected {expected}"
        )

if errors:
    print("Timer OS multilingual documentation is out of sync:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"OK: all {len(FILES)} language files are at i18n version {expected}")
