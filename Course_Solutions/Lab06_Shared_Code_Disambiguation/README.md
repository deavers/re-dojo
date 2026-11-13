# Lab 06 — Shared Code Disambiguation (Tier D · 3.0)

Исходник: [`lab06_shared_code.cpp`](./lab06_shared_code.cpp). Таблица Cheat Engine для лабы:
[`Game_Hacking/Dojo_Labs_Reference.CT`](../../Game_Hacking/Dojo_Labs_Reference.CT).

## Сборка

* CMake собирает лабу как `lab06_shared_code_filter.exe` — это имя модуля, которое ждёт
  `Dojo_Labs_Reference.CT` в `aobscanmodule` (цель CMake по-прежнему `lab06_shared_code`). `build_all.bat` даёт
  то же имя.
* Новые лабы (Lab 11 и дальше, CM 09 и дальше) собираются **только через CMake**; `build_all.bat` их не собирает:

```powershell
cmake -S . -B build -G "Visual Studio 17 2022" -A x64
cmake --build build --config Release --parallel
```

## Важно про таблицу `.CT`

* Адреса и байты в `.CT` **зависят от компилятора и сборки**. Скрипт этой лабы ищет инструкцию по AOB-сигнатуре,
  поэтому имя модуля важно; но если после пересборки сигнатура не находится или статический адрес не совпадает,
  место нужно найти заново («что пишет в этот адрес», затем новая сигнатура). Совпадение имени модуля этого не
  исправляет.
