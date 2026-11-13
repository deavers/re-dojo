# Lab template (new labs from `docs/lab_plan.md`)

Every new lab or crackme follows this layout. Only your own binaries; no commercial protection is
bypassed anywhere. Existing labs (Lab 01–10, CM 01–08) keep their current layout and style.

```
Course_Solutions/LabNN_<Name>/            crackmes: Crackmes_and_CTF/NN_<Name>/
  .clang-format              copy of Tools_and_Scripts/lab_template/.clang-format (Allman braces)
  labNN_<name>.cpp           the target. Labs keep Apprentice / Hardcore modes.
  labNN_core.hpp             state + win check + flag, no I/O  (memory labs, shared with the selftest)
  check/labNN_selftest.cpp   CTest harness: applies the edits a solver would make, then checks the win
  check/expected.json        {"flag_sha256": "...", "runs": 1}  - only the hash, never the flag
  solve/solve.py             reference solution (spoiler): answer() and WRONG = [...]
  README.md                  goal, prerequisites, how it is checked, which map games it prepares for
```

Hints are not stored in the lab folder: they go to `data/hints/labs_NN.json` (one id = one batch file),
so `validate_games.py` checks them like every other hint (provenance, no invented literals).

## Exit-code contract (new labs)

| Code | Meaning |
| :-: | :--- |
| 0 | solved, prints exactly one `FLAG{...}` |
| 1 | wrong answer / win condition not met |
| 2 | usage error (bad input format) |
| 3 | quit from the menu |

## Autocheck (CTest, `cmake/DojoLab.cmake`)

| Test | Passes when |
| :--- | :--- |
| `labNN_build` | the lab (and its selftest) compile |
| `labNN_solve_ok` | `solve.answer()` fed to the binary gives exit 0 and `sha256(FLAG) == check/expected.json` (in `runs` fresh processes) |
| `labNN_wrong_fails` | every payload in `solve.WRONG` gives exit != 0 and no `FLAG` |

A lab is accepted only if all three are green. Memory labs are driven through their selftest binary
(same `labNN_core.hpp`, no Cheat Engine in CI): that verifies the lab and the reference answer, not the
learner's Cheat Engine work, which the flag in the real binary proves.

Register a lab in `CMakeLists.txt`:

```cmake
dojo_add_lab(ID lab11 TARGET lab11_integer_widths DIR Course_Solutions/Lab11_Integer_Widths
             SOURCE   Course_Solutions/Lab11_Integer_Widths/lab11_integer_widths.cpp
             SELFTEST Course_Solutions/Lab11_Integer_Widths/check/lab11_selftest.cpp)
```

Then add the README Dojo row, set `status: "built"` in `data/labs_index.json`, rebuild the map
(`build_games_json.py`, `build_dojo_map.py`) and run `ctest`.
