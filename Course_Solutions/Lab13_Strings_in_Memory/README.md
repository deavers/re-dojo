# Lab 13 — Strings in Memory (Tier E-- · 0.8)

**Предпосылки:** Lab 12 (неточный скан).

## Цель

Попасть в Зал легенд: имя героя DRAGONSLAYER, тег гильдии DOJO.

## Формат ввода

Только меню игры: номер действия, при переименовании — текст (A-Z).

## Сборка и запуск

```powershell
cmake --build build --config Release --target lab13_strings
.\build\bin\Release\lab13_strings.exe
```

## Как проверяется

* Флаг печатает программа (в нём подмешан ответ); в репо — только его sha256 (`check/expected.json`).
* Автопроверка (CTest): `lab13_build`, `lab13_solve_ok`, `lab13_wrong_fails` — эталонный ответ проходит, все неверные ответы из `solve/solve.py` (включая обходные) проваливаются.
* Подсказки — на карте (`docs/dojo-map.html`), `solve/solve.py` — спойлер.
