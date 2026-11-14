# Lab 17 — Nested Structs & Padding (Tier E · 1.6)

**Предпосылки:** Lab 16 (массив структур).

## Цель

Стать легендой: шанс крита ровно 1.00, прочность брони ровно 9999, цена добычи ровно 1000000.

## Формат ввода

Только меню игры (номер действия). Режим Hardcore скрывает адреса.

## Сборка и запуск

```powershell
cmake --build build --config Release --target lab17_nested_padding
.\build\bin\Release\lab17_nested_padding.exe
```

## Как проверяется

* Флаг печатает программа (в нём подмешан ответ); в репо — только его sha256 (`check/expected.json`).
* Автопроверка (CTest): `lab17_build`, `lab17_solve_ok`, `lab17_wrong_fails` — эталонный ответ проходит, все неверные ответы из `solve/solve.py` (включая обходные) проваливаются.
* Подсказки — на карте (`docs/dojo-map.html`), `solve/solve.py` — спойлер.
