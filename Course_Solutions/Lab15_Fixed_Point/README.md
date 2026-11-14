# Lab 15 — Fixed-Point (Tier E-- · 1.1)

**Предпосылки:** Lab 12 (неточный скан).

## Цель

Включить гиперпрыжок: топливо ровно 1000.00, тяга ровно 3.25.

## Формат ввода

Только меню игры (номер действия). Режим Hardcore скрывает адреса.

## Сборка и запуск

```powershell
cmake --build build --config Release --target lab15_fixed_point
.\build\bin\Release\lab15_fixed_point.exe
```

## Как проверяется

* Флаг печатает программа (в нём подмешан ответ); в репо — только его sha256 (`check/expected.json`).
* Автопроверка (CTest): `lab15_build`, `lab15_solve_ok`, `lab15_wrong_fails` — эталонный ответ проходит, все неверные ответы из `solve/solve.py` (включая обходные) проваливаются.
* Подсказки — на карте (`docs/dojo-map.html`), `solve/solve.py` — спойлер.
