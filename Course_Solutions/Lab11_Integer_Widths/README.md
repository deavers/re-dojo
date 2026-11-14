# Lab 11 — Integer Widths & Signedness (Tier F- · 0.3)

**Предпосылки:** Lab 01 (точный скан, заморозка).

## Цель

Открыть Проклятое хранилище. Оно открывается, когда одновременно:

* мораль ровно −100;
* стрел ровно 65535;
* золота ровно 5 000 000 000;
* зелий осталось не больше 3.

Ввод — только меню игры (номер действия). Режим Hardcore скрывает адреса.

## Сборка и запуск

```powershell
cmake --build build --config Release --target lab11_integer_widths
.\build\bin\Release\lab11_integer_widths.exe
```

## Как проверяется

* Флаг печатает программа; в репо — только его sha256 (`check/expected.json`).
* Автопроверка (CTest): `lab11_build`, `lab11_solve_ok`, `lab11_wrong_fails` — эталонный ответ проходит, все неверные
  ответы из `solve/solve.py` проваливаются.
* Подсказки — на карте (`docs/dojo-map.html`), `solve/solve.py` — спойлер.
