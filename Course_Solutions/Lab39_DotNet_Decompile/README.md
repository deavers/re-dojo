# Lab 39 — .NET: Decompile Your Own C# Game (Tier C+ · 4.7)

**Предпосылки:** Lab 07 (классы, таблицы методов).

## Цель

Сказать часовому торговцу его парольную фразу. Игра печатает флаг (в нём подмешана фраза).

## Формат ввода

Одна строка — парольная фраза.

| Код выхода | Значение |
| :-: | :--- |
| 0 | принято, флаг напечатан |
| 1 | неверная фраза |
| 2 | пустая строка или длиннее 64 символов |
| 3 | конец ввода |

## Сборка и запуск (нужен .NET SDK 8)

```powershell
dotnet build Course_Solutions/Lab39_DotNet_Decompile/game/Lab39.csproj -c Release -o build/dotnet/lab39/out
.\build\dotnet\lab39\out\Lab39.exe
```

## Как проверяется (`"ci": "sources_only"`)

* Флаг печатает игра; в репо — только его sha256 (`check/expected.json`).
* Локально с .NET SDK: `lab39_sources`, `lab39_build`, `lab39_solve_ok`, `lab39_wrong_fails`. В CI (без SDK-тестов) —
  только `lab39_sources` (проверка исходников).
* Подсказки — на карте (`docs/dojo-map.html`), `solve/solve.py` — спойлер.
