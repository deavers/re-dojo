# Lab 12 — Double & Fuzzy Scans (Tier F+ · 0.6)

**Предпосылки:** Lab 02 (float, int16, битовая маска).

## Цель

Образовать Философский камень: эссенции ровно 1 000 000, чистота катализатора ровно 100 %. Числа на экране округлены.

## Формат ввода

Только меню игры (номер действия). Режим Hardcore скрывает адреса.

## Сборка и запуск

```powershell
cmake --build build --config Release --target lab12_double_fuzzy
.\build\bin\Release\lab12_double_fuzzy.exe
```

## Как проверяется

* Флаг печатает программа (в нём подмешан ответ); в репо — только его sha256 (`check/expected.json`).
* Автопроверка (CTest): `lab12_build`, `lab12_solve_ok`, `lab12_wrong_fails` — эталонный ответ проходит, все неверные ответы из `solve/solve.py` (включая обходные) проваливаются.
* Подсказки — на карте (`docs/dojo-map.html`), `solve/solve.py` — спойлер.
