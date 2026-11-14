# Lab 18 — Lazy Singleton (Tier E+ · 2.0)

**Предпосылки:** Lab 04 (цепочки указателей).

## Цель

Открыть сокровищницу, имея ровно 99999 самоцветов.

## Формат ввода

Только меню игры (номер действия). Режим Hardcore скрывает адреса.

## Сборка и запуск

```powershell
cmake --build build --config Release --target lab18_lazy_singleton
.\build\bin\Release\lab18_lazy_singleton.exe
```

## Как проверяется

* Флаг печатает программа (в нём подмешан ответ); в репо — только его sha256 (`check/expected.json`).
* Автопроверка (CTest): `lab18_build`, `lab18_solve_ok`, `lab18_wrong_fails` — эталонный ответ проходит, все неверные ответы из `solve/solve.py` (включая обходные) проваливаются.
* Подсказки — на карте (`docs/dojo-map.html`), `solve/solve.py` — спойлер.
