# Lab 04 — MultiLevel Pointers (Tier E · 1.8)

Исходник: [`lab04_pointer_chains.cpp`](./lab04_pointer_chains.cpp). Таблица Cheat Engine для лабы:
[`Game_Hacking/Dojo_Labs_Reference.CT`](../../Game_Hacking/Dojo_Labs_Reference.CT).

## Сборка

* CMake собирает лабу как `lab04_multilevel_pointers.exe` — это имя модуля, которое ждёт
  `Dojo_Labs_Reference.CT` (цель CMake по-прежнему `lab04_pointer_chains`). `build_all.bat` даёт то же имя.
* Новые лабы (Lab 11 и дальше, CM 09 и дальше) собираются **только через CMake**; `build_all.bat` их не собирает:

```powershell
cmake -S . -B build -G "Visual Studio 17 2022" -A x64
cmake --build build --config Release --parallel
```

## Важно про таблицу `.CT`

* Статический адрес в `.CT` (`"lab04_multilevel_pointers.exe"+00018000`) **зависит от компилятора и сборки**.
  После пересборки (другой компилятор, другие флаги, правка исходника) базу цепочки нужно найти заново:
  pointer scan от найденного значения, перезапуск, повторный скан (как в Lab 19). Совпадение имени модуля
  этого не исправляет.
