````markdown
# UI_Automate_Using_Playwright_Python_BDD

This repository contains Playwright-based UI automation using Python and BDD-style tests.

Windows (PowerShell) — Step by step

1. Open PowerShell in the project root (this repo folder).

2. Create a virtual environment named `.venv` (recommended):

```powershell
python -m venv .venv
```
````

3. Activate the virtual environment (dot-source the PowerShell script):

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
. .\venv\Scripts\Activate.ps1
```

Notes:

- `Set-ExecutionPolicy` above only changes policy for the current PowerShell process.
- If you prefer the repo-local name used previously, replace `.venv` with `venv` in the commands.

4. Confirm Python and pip are from the venv:

```powershell
python --version
pip --version
```

5. Install project dependencies. If a `requirements.txt` exists:

```powershell
pip install -r requirements.txt
```

If there is no `requirements.txt` yet, install needed packages and then freeze:

```powershell
pip install pytest-playwright playwright
pip freeze > requirements.txt
```

6. Install Playwright browsers and optional dependencies:

```powershell
python -m playwright install
python -m playwright install-deps    # optional for Linux; harmless on Windows
```

7. Running tests (examples — use whichever applies to your project):

- pytest-based tests:

```powershell
pytest -q
```

- behave (BDD) tests:

```powershell
behave
```

8. Deactivate the venv when finished:

```powershell
deactivate
```

Troubleshooting

- If activation fails because `Activate.ps1` is missing or locked, create a fresh venv:

```powershell
python -m venv .venv
```

- If files are locked by OneDrive or permission errors occur, try closing any processes using the folder, pause OneDrive syncing for the project folder, or create the venv in a non-synced local path.

- To temporarily run venv activation from cmd.exe instead of PowerShell:

```cmd
.venv\Scripts\activate.bat
```

Additional notes

- Keep `requirements.txt` up to date with `pip freeze > requirements.txt` after installing or upgrading packages.
- If you want me to add a `requirements.txt` or update CI/automation scripts, tell me what packages you need or I can export the current environment.

```

```
