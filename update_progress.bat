@echo off
echo ============================================================================
echo   Syncing RPG Character Card, Checkboxes ^& Custom Targets in README.md...
echo ============================================================================
python "%~dp0Tools_and_Scripts\rpg_manager.py" %*
