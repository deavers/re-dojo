# Lab 16 — Array of Structs & Stride (Tier E- · 1.4)

**Предпосылки:** Lab 03 (структуры, двумерный массив).

## Цель

Вывести Железный отряд: у всех 8 бойцов ровно 500 HP, и все живы.

## Формат ввода

Только меню игры: номер действия, при лечении — номер бойца.

## Сборка и запуск

```powershell
cmake --build build --config Release --target lab16_array_of_structs
.\build\bin\Release\lab16_array_of_structs.exe
```

## Как проверяется

* Флаг печатает программа (в нём подмешан ответ); в репо — только его sha256 (`check/expected.json`).
* Автопроверка (CTest): `lab16_build`, `lab16_solve_ok`, `lab16_wrong_fails` — эталонный ответ проходит, все неверные ответы из `solve/solve.py` (включая обходные) проваливаются.
* Подсказки — на карте (`docs/dojo-map.html`), `solve/solve.py` — спойлер.
