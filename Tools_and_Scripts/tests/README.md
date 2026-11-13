# Tools_and_Scripts/tests — RE:DOJO map tests

Both tests run from any directory and write only to a temporary folder (never to `data/` or `docs/`).
The hint texts they use are **test stubs**, not real hints.

| Test | Needs | In CI | What it checks |
| :--- | :--- | :---: | :--- |
| `test_validator_fixtures.py` | Python 3.10+ (stdlib only) | no (run locally) | 82 positive/negative cases for `validate_games.py`: invented hex / versions / AOB bytes / `[reg+off]`, substring & laundered provenance, `my_notes` without own notes, protection tiers (products, EAC/VAC, license bypass; keygen allowed in own crackmes), restricted-node rules (g176 / g177 / g199), offline-only hints for `online_note` games, ambiguous-engine rules, structural mutations, plus a table of engine strings for `derive_engine()` |
| `e2e_dojo_map.mjs` | Node 22+, Python 3.10+, **Google Chrome or Chromium** | **no** (needs a browser) | Builds a fixture page and drives `docs/dojo-map.html` in headless Chrome via CDP: tiles, rank / breakthrough rule, locks, hints revealed in order, EXP penalty, restricted banners (g176 / g199), offline-only banner (online_note), ambiguous-engine chip, filters & counters, deep links, localStorage persistence and sanitizing, export / import / reset, theme, edges, mobile layout, no console errors or CSP violations |

```powershell
python Tools_and_Scripts/tests/test_validator_fixtures.py
node   Tools_and_Scripts/tests/e2e_dojo_map.mjs
```

Chrome is auto-detected in the usual install locations (Windows, macOS, Linux). Otherwise:

```powershell
$env:CHROME_PATH = "D:\Apps\Chrome\chrome.exe"; node Tools_and_Scripts/tests/e2e_dojo_map.mjs
```

```bash
CHROME_PATH=/usr/bin/chromium PYTHON=python3 node Tools_and_Scripts/tests/e2e_dojo_map.mjs
```

The e2e test starts a throw-away Chrome profile on `127.0.0.1:9339`, prints `N/M checks passed` and the temp
folder with screenshots, then deletes the profile. Exit code 0 = all checks passed.
