# CM 16 — The Constraint Lock (Tier A · 6.6)

**Предпосылки:** CM 10 (серийник по правилам), CM 03 (обратимые преобразования). По плану — CM 13, она ещё не собрана.

## Цель

Ввести ключ, который принимает замок. Решение единственное.

## Формат ввода

Четыре 64-битных числа в hex, по 16 цифр, через `-`:
`XXXXXXXXXXXXXXXX-XXXXXXXXXXXXXXXX-XXXXXXXXXXXXXXXX-XXXXXXXXXXXXXXXX`. Программа печатает `FLAG{<ключ>}`.

| Код выхода | Значение |
| :-: | :--- |
| 0 | принят, флаг напечатан |
| 1 | нарушено ограничение |
| 2 | неверный формат |
| 3 | конец ввода |

## Сборка и запуск

```powershell
cmake --build build --config Release --target crackme16_z3_lock
.\build\bin\Release\crackme16_z3_lock.exe
```

## Как проверяется

* В репо — только sha256 флага (`check/expected.json`); ключа нет ни в исходнике, ни в `solve/solve.py`.
* Автопроверка (CTest, метка `z3`; нужен `z3-solver` в том Python, который запускает CTest): `cm16_build`,
  `cm16_solve_ok`, `cm16_wrong_fails` — эталонный решатель проходит, все неверные ключи проваливаются.
* Подсказки — на карте, `solve/solve.py` — спойлер.
