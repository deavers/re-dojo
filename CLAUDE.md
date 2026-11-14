# RE:DOJO — правила для агентов

План лаб: [`docs/lab_plan.md`](docs/lab_plan.md). Как делать и ревьюить лабы: [`docs/lab_authoring_guide.md`](docs/lab_authoring_guide.md)
(чеклист, типичные ошибки, решения и исключения, промпт ревьюера).

## Правила проекта

* Только свои бинарники; никакого обхода защит коммерческого ПО.
* Малварь — только в изолированной VM; сэмплов в репо нет.
* Никаких выдуманных адресов, смещений и версий: каждый литерал в подсказках должен быть в исходниках лабы.
* Новый C/C++ — в стиле Allman (фигурные скобки на отдельных строках); старые файлы не переформатировать.
* Python — только стандартная библиотека; в CTest раннер запускается как `python -I`. Исключение — лабы категории
  Z3 (`z3-solver`, метка `z3`).
* Пакеты и инструменты не ставить без слова автора: проверить наличие и сообщить, чего не хватает.
* `Game_Hacking/*.CT` и готовые подсказки не менять без просьбы автора.
* Ничего не пушить без слова автора. Историю не переписывать, `--fix-git` не запускать.
* PR #2 не мерджить и не закрывать. Merge — только локально: merge через веб-интерфейс GitHub создаёт коммит
  с именем из профиля, и opsec-проверка истории его ловит.
* Перед коммитом — `opsec_sanitizer.py --ci`: в файлах нет личных путей, почты и имён.

## Сборка и полная проверка

```powershell
# Windows, MSVC (CTest должен видеть Python с z3-solver)
cmake -S . -B build -A x64 -DPython3_EXECUTABLE="<python с z3-solver>"
cmake --build build --config Release --parallel
ctest --test-dir build -C Release --output-on-failure

# GCC в WSL, предупреждения = ошибки
wsl -e bash -lc "cd /mnt/<диск>/<путь к репо> && cmake -S . -B <dir> -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS='-Wall -Wextra -Werror' -DPython3_EXECUTABLE=<venv с z3>/bin/python && cmake --build <dir> && ctest --test-dir <dir>"

# Карта, данные, opsec
python -X utf8 Tools_and_Scripts/build_games_json.py; python -X utf8 Tools_and_Scripts/build_dojo_map.py
python -X utf8 Tools_and_Scripts/validate_games.py; python Tools_and_Scripts/tests/test_validator_fixtures.py
node Tools_and_Scripts/tests/e2e_dojo_map.mjs; python -X utf8 Tools_and_Scripts/opsec_sanitizer.py --ci
```

Лаба принята, только если её тесты `<id>_build`, `<id>_solve_ok`, `<id>_wrong_fails` зелёные на MSVC **и** GCC,
а полный прогон всего списка выше зелёный после каждого коммита.

## Ловушки WSL и окружения

* Внутри `wsl -e bash` — только пути `/mnt/<диск>/...`: Windows-путь с `C:/` превращается в относительную папку в репо.
* GCC ловит то, чего не видит MSVC (`-Wnarrowing` и т. п.) — смотреть все строки сборки, а не только тесты.
* CTest должен запускать Python с z3: `-DPython3_EXECUTABLE` при конфигурации (Windows — Python с z3-solver,
  WSL — venv).
* Корневой `README.md` хранится с CRLF — читать и писать байтами, сохраняя CRLF.
* Сложные правки строк — через файл или Edit, не через heredoc (экранирование `\v`, `\n` ломает текст).
