# Timer OS multilingual documentation maintenance

Timer OS maintains five public language versions:

- `README.md` — English, canonical public source
- `README.zh-CN.md` — Simplified Chinese
- `README.ja.md` — Japanese
- `README.ko.md` — Korean
- `README.es.md` — Spanish

## Synchronization rule

All five files must carry the same `i18n-version` marker as `docs/i18n/version.txt`.

When a public architecture concept changes:

1. update the English source first;
2. update all four localized versions for semantic equivalence;
3. bump `docs/i18n/version.txt`;
4. put the same version in the `<!-- i18n-version: ... -->` marker at the top of every language file;
5. run `python scripts/check_i18n.py` before merging.

Translations should preserve architecture terminology and system boundaries. They should not introduce implementation details that are absent from the English public source.

## Canonical terminology

Do not translate these project identifiers:

- Timer OS
- Body
- External Brain
- YIdui
- Timer Scheduler / Timer OS Scheduler
- Timer Event Stream
- DeepSeek

`时代系统` is the official Chinese name of Timer OS and may appear alongside the English project name in every language.

## Scope

The synchronization check validates documentation-version parity, not translation quality. Human or model-assisted review is still required to ensure semantic equivalence.
