# data/hints/ — hint batches for the RE:DOJO map

Hints live here, **not** in `data/games.json`. `Tools_and_Scripts/build_games_json.py` merges every
`*.json` file in this folder by node id, so rebuilding `games.json` never wipes hint work.

## File format (`batch_01.json`, `batch_02.json`, …)

```json
{
  "batch": 1,
  "entries": {
    "g019": {
      "status": "draft",
      "hints": [
        { "level": 1, "kind": "nudge",        "text": "…", "source": "my_notes",           "refs": ["Game_Hacking/README.md#1-plants-vs-zombies-goty-tier-e--21--10"] },
        { "level": 2, "kind": "concept",      "text": "…", "source": "repo_catalog",       "refs": [] },
        { "level": 3, "kind": "near_spoiler", "text": "…", "source": "needs_verification", "refs": [] }
      ]
    }
  }
}
```

| Field | Rule |
| :--- | :--- |
| node id | `gNNN` (Top 200 rank), `labNN` / `cmNN`, or a campaign quest id from `data/safety_overrides.json`. Each id may appear in only one batch file. |
| `status` | `draft` → `reviewed` once you checked it against the game yourself. |
| `hints` | Exactly 3, in order: `nudge` (намёк) → `concept` (концепт) → `near_spoiler` (почти спойлер). |
| `text` | Plain text, ≤ 400 chars, no HTML. |
| `source` | `my_notes` = **[из моих заметок]**: needs at least one ref to **this node's own notes** (`data/notes_index.json`; for a lab: its source). A lab source alone never makes a game hint "my notes". `repo_catalog` / `needs_verification` = **[нужна проверка]**. |

## Hard rules (enforced by `Tools_and_Scripts/validate_games.py`)

* **No invented literals.** Every concrete literal in `text` must appear (whole token, not a substring:
  `0x55` is not backed by `0x5560`) in this node's own text (title, engine, catalog / README / lab text)
  or in one of **this node's own notes** listed in `refs` (lab sources may be cited, but do not back literals). Checked literals:
  hex (`0x5560`, `+5560`, `+08`, `5560h`, `01005340`), `module.exe+offset`, `[rcx+08]`,
  AOB byte strings (`8B 45 08 ?? ??`), versions and builds (`v98`, `7.5`, `1.05`, `2019.4`, `build 98`).
  Citing `README.md` or the Top 200 catalog does **not** count as provenance for another game's literal.
* Plain numbers in prose (`8 байт`, `+20%`, `шаг 3`) are fine.
* Commercial protections (Arxan, Denuvo, SecuROM, VMProtect, anti-cheat, DRM …) may only be mentioned in
  hints of restricted nodes.
* Restricted nodes (`safety.restricted = true`, e.g. `g199`, `q_ss_legacy_drm`, `q_ssp_integrity_guard`):
  conceptual hints only, no concrete addresses / offsets / bytes at all, and the level-3 hint must reference
  one of the node's `redirect_labs` sources (your own binaries).
* **Known limits of the regex checks** (the `draft` → `reviewed` step is the real backstop):
  * still NOT detected: offsets without a prefix/suffix (`смещение 5560`, `1A4`) and versions glued to a word (`UE4.27`);
  * false alarms (fail closed, rephrase): decimals in prose (`999.0`), `+10 к урону`, `+100 EXP`, `C++20`, `Ctrl+F5`.

After editing (CI runs the same three checks with `--check`):

```
python Tools_and_Scripts/build_games_json.py
python Tools_and_Scripts/validate_games.py
python Tools_and_Scripts/build_dojo_map.py
```
