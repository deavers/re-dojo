# Как добавить лабу RE:DOJO — короткое руководство

План и шаблоны категорий: [`docs/lab_plan.md`](./lab_plan.md). Базовый шаблон: [`Tools_and_Scripts/lab_template/`](../Tools_and_Scripts/lab_template/README.md).
Правила проекта: только свои бинарники, никакого обхода защит коммерческого ПО, никаких выдуманных адресов /
смещений / версий, малварь — только в изолированной VM и без сэмплов в репо. Новый C++ — Allman (скобки на отдельных строках).

## 1. Выбери категорию и образец

| Категория | Образец | Проверка |
| :--- | :--- | :--- |
| Память: типы, структуры, указатели | Lab 11–19 | selftest (`poke` / `chain`) |
| VMT | Lab 32 | selftest (`vcopy` / `vset`) |
| Эмулятор | Lab 54 | selftest (`chain` через указатель на гостевую RAM), `runs: 3` |
| Чекер артефакта / мини-UE | Lab 45 | selftest-чекер сравнивает дамп со своей памятью |
| Встроенная Lua | Lab 52 | selftest `luado`, `LIBS lua54` |
| Крякми (stdin) | CM 09, CM 10 | бинарь сам, `FLAG{...}` |
| Крякми с VM | CM 17 | бинарь сам, байткод из ассемблера вне репо |
| .NET / C# | Lab 39 | `dojo_add_dotnet_lab`; `<id>_sources` всегда, dotnet-тесты локально (`ci: sources_only`) |
| Z3 / символьное | CM 16 | бинарь сам, `solve.py` решает в z3, `LABELS z3` |

## 2. Чеклист

1. Папка по образцу + копия `Tools_and_Scripts/lab_template/.clang-format`.
2. Флаг вычисляет бинарь (FNV-1a от «печати»); в `check/expected.json` — только sha256. Хэш считает **независимая**
   реализация (Python), а не вывод самого бинаря.
3. `solve/solve.py`: `answer()` и `WRONG` — каждый неверный ответ обязан давать код 1 или 2 (падение / таймаут = FAIL).
4. Коды выхода: 0 решено · 1 неверно · 2 формат / не разрешено · 3 выход / конец ввода.
5. `static_assert` на каждое смещение из эталонного ответа; только типы фиксированной ширины; `char16_t`, не `wchar_t`.
6. `CMakeLists.txt`: `dojo_add_lab(ID … TARGET … DIR … SOURCE … [SELFTEST …] [LIBS …] [LABELS windows])`.
7. `data/labs_index.json`: `status: "built"` (тир и сложность = строка README), `prereqs`, `trains`, `check`, `platform`, `ci`.
8. Строка в таблице Dojo в `README.md` (формат как у соседних строк; **README в CRLF — сохранить CRLF**).
9. `data/notes_index.json` → `labs.<id>`: `core.hpp` как `lab_source` (иначе литералы из него не подтверждены).
10. 3 подсказки в `data/hints/labs_01.json` (`draft`): `my_notes` только со ссылками на файлы этой лабы.
    **Каждый литерал** (hex, `+0x..`, AOB, версии вроде `0.999`, `16.16`) должен целым токеном встречаться в своих
    источниках или строке README. Названия коммерческих защит — только у restricted-узлов.
11. README лабы: цель, сборка, как проверяется, что проверяется вручную.

## 3. Команды

```powershell
# CTest должен видеть Python с z3: один раз при конфигурации (Windows: Python 3.12; WSL: venv с z3)
cmake -S . -B build -A x64 -DPython3_EXECUTABLE="<python с z3-solver>"   # .NET-тесты: нужен SDK, DOJO_DOTNET_TESTS=ON
python -X utf8 Tools_and_Scripts/build_games_json.py; python -X utf8 Tools_and_Scripts/build_dojo_map.py
cmake -S . -B build -A x64; cmake --build build --config Release --parallel
ctest --test-dir build -C Release -R "^<id>_" --output-on-failure
wsl -e bash -lc "cmake -S . -B <dir> -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS='-Wall -Wextra -Werror' && cmake --build <dir> && ctest --test-dir <dir> -R '^<id>_'"
python -X utf8 Tools_and_Scripts/validate_games.py; python Tools_and_Scripts/tests/test_validator_fixtures.py
node Tools_and_Scripts/tests/e2e_dojo_map.mjs; python -X utf8 Tools_and_Scripts/opsec_sanitizer.py --ci
```
Лаба принята, только если `<id>_build`, `<id>_solve_ok`, `<id>_wrong_fails` зелёные на MSVC **и** GCC. В отчёт — число
предупреждений MSVC и GCC при чистой пересборке целей лабы (`--clean-first`, grep по выводу), а не только тесты.

## 4. Типичные ошибки из прошлых партий

* **Устаревший `.pyc`:** кэш байткода по mtime-секундам + размеру давал старый `solve.py` → runner отключает кэш.
* **CRLF:** README в индексе с CRLF; запись через Python с LF превратила дифф в «весь файл» → читать и писать байтами.
* **Сужение типов:** `rng()` (unsigned long на Linux) в `{}`-инициализаторе `uint32_t` — `-Wnarrowing` только на GCC
  → явный `static_cast`; смотреть **все** строки сборки, не только тесты.
* **Литералы не из исходников:** `12.50` (значение на экране), `+0x0300` при `0x0300` в коде → валидатор отклоняет.
* **Девиртуализация:** вызовы через `volatile`-указатель, иначе правка vptr не влияет.
* **`__declspec` вне Windows:** `LUA_BUILD_AS_DLL` только для `WIN32`.
* **Не тот Python у CTest:** `find_package` взял 3.14 / системный python3 без z3 → `-DPython3_EXECUTABLE`, раннер с `-I`.
* **PDB с локальным путём:** `dotnet build` писал PDB с путём пользователя (opsec сканирует `build/`) → `DebugType=none`.
* **Windows-путь в WSL:** `C:/...` внутри `wsl -e bash` стал относительной папкой `C:` в репо → в WSL только `/mnt/c/...`.
* **Суффиксы литералов:** в коде `0xFFFFU` — в подсказке тоже `0xFFFFU`, иначе валидатор не найдёт токен.
* **Экранирование в heredoc:** `\v` в Python-строке стал управляющим символом в YAML → правки сложных строк через файл/Edit.

## 5. Промпт-шаблон для более простой модели

```text
Сделай лабу <id> из docs/lab_plan.md по шаблону категории «<категория>» (образец: <образец>, раздел
«Шаблоны категорий» в docs/lab_plan.md) и по docs/lab_authoring_guide.md. Ветка dojo-labs.
Правила: только свои бинарники; без выдуманных адресов/смещений/версий; Allman для нового C++;
флаг вычисляет бинарь, в expected.json только sha256 из независимой реализации; WRONG — минимум 5 случаев
с кодом 1 или 2. Пройди весь чеклист раздела 2. Прогони команды раздела 3 (MSVC и GCC -Werror, валидатор,
регрессионный тест, e2e, opsec). Закоммить лабу отдельным коммитом, не пушь.
Покажи таблицу: лаба | build/solve_ok/wrong_fails (MSVC, GCC) | предупреждения MSVC | предупреждения GCC |
≈ токены | итерации исправлений с причинами. Если чего-то нет в окружении — ничего не ставь, остановись и скажи.
```
