# Lab 52 — Embedded Lua 5.4 (Tier A- · 6.3)

**Предпосылки:** Lab 09 (внутренняя DLL), Lab 17 (раскладка структур).

## Цель

Попасть в Гильдию архимагов: у героя ровно 1 000 000 золота и титул Archmage.

## Формат ввода

Только меню игры (номер действия). Режим Hardcore скрывает адреса.

## Сборка и запуск

```powershell
cmake --build build --config Release --target lab52_embedded_lua
.\build\bin\Release\lab52_embedded_lua.exe
```

## Как проверяется

* Флаг печатает программа (в нём подмешан ответ); в репо — только его sha256 (`check/expected.json`).
* Автопроверка (CTest): `lab52_build`, `lab52_solve_ok`, `lab52_wrong_fails` (метка `windows`) — эталонный ответ проходит, все неверные ответы из `solve/solve.py` (включая обходные) проваливаются.
* Подсказки — на карте (`docs/dojo-map.html`), `solve/solve.py` — спойлер.
* Lua — `third_party/lua` (Lua 5.4.9, MIT, без изменений), собирается как `lua54.dll` рядом с exe. Практика требует Windows; сборка и автопроверка идут и на Linux.
