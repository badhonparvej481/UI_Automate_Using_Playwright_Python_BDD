# 🎭 UI Automation Using Playwright + Python (BDD)

This repository contains UI automation tests built using **Playwright with Python**, following **BDD (Behavior Driven Development)** principles for clean and readable test cases.

---

## 📋 Prerequisites

Ensure you have the following installed on your system:

- **Python 3.9** or higher 🐍
- **Git** 🛠️
- **Visual Studio Code (VS Code)** 💻

---

## ⚙️ Setup & Installation (Windows)

Follow these steps inside your **VS Code Terminal** (`Ctrl + \``) to set up the project environment.

### 1. Create Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate Virtual Environment

Choose the command based on your terminal:

### PowerShell:

```bash
.venv\Scripts\activate
```

### Command Prompt: 
```bash
.venv\Scripts\activate.bat
```
### Git Bash: source 
```bash
.venv/Scripts/activate
```

Note: If PowerShell blocks execution, run:
```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
```
### 3. Verify Python & Pip

```bash
python --version
pip --version
```
### 4. Install Dependencies

```bash
# If requirements.txt exists:
pip install -r requirements.txt

# If setting up for the first time:
pip install pytest playwright pytest-playwright behave
pip freeze > requirements.txt
```
### 5. Install Playwright Browsers
```bash
python -m playwright install
```
# 🧪 Running Tests
You can run your tests using Pytest or Behave.

### ➤ Using Pytest
```bash
# Run all tests
pytest

# Run in quiet mode
pytest -q
```

### ➤ Using Behave (BDD)
```bash
# Run all features
behave

# Run a specific feature file
behave features/login.feature
```

# 🛑 Close Environment
  When you're done, simply run:

  ```bash
  deactivate
  ```