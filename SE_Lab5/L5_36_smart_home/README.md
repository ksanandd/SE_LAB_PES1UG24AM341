# Lab 5: Static Code Analysis — Smart Home Device Controller

## 1. Project Overview

This project focuses on improving the code quality, readability, maintainability, and security of a Python-based Smart Home Device Controller using static code analysis tools.

Three static analysis tools were used to identify potential issues in the original program:

- **Pylint** — identifies code quality issues, naming violations, missing docstrings, and potential programming errors.
- **Bandit** — detects common security issues in Python code.
- **Flake8** — checks Python code for style and formatting violations.

The identified issues were reviewed and corrected, and the tools were executed again to verify the improvements.

## 2. Objectives

- Analyze the original Python program using Pylint, Bandit, and Flake8.
- Identify code quality, security, and formatting issues.
- Fix the identified issues and improve the overall code structure.
- Compare the static analysis results before and after modifications.
- Document the issues, corrective actions, and lessons learned.
- Maintain Git commits documenting the project changes.

## 3. Technologies and Tools

| Tool | Purpose |
|---|---|
| Python | Programming language |
| Pylint | Code quality and error analysis |
| Bandit | Python security analysis |
| Flake8 | Coding style and formatting checks |
| Git and GitHub | Version control and project submission |
| Visual Studio Code | Development environment |

## 4. Project Structure

```text
L5_36_smart_home/
├── smart_home.py
├── README.md
├── issues.md
├── reflection.md
├── .gitignore
├── pylint_before.txt
├── pylint_after.txt
├── bandit_before.txt
├── bandit_after.txt
├── flake8_before.txt
└── flake8_after.txt
```

## 5. Implementation and Improvements

The original program was analyzed using all three tools. The following improvements were made:

- Added docstrings to improve code documentation.
- Corrected naming and formatting violations.
- Replaced a mutable default argument with a safer implementation.
- Corrected inconsistent return behavior.
- Specified file encoding when writing JSON data.
- Replaced a hardcoded network bind address with a loopback address.
- Removed hardcoded password usage in favor of environment-based configuration.
- Removed unsafe shell-command execution from the program.
- Improved device settings initialization and thermostat handling.

The modified program supports device registration, device toggling, thermostat temperature control, room-based device lookup, power usage calculation, hub address reporting, and JSON state persistence.

## 6. Static Code Analysis Results

The following results were obtained after modifying the program.

| Tool | Before | After |
|---|---|---|
| Pylint | 4.80/10 | 10.00/10 |
| Bandit | Security findings identified | No issues identified |
| Flake8 | Formatting violations identified | No violations |

The before-and-after reports are included in this repository for verification.

## 7. How to Run the Project

### Step 1: Install Python

Ensure Python is installed and available from your terminal.

### Step 2: Navigate to the project directory

```bash
cd L5_36_smart_home
```

### Step 3: Run the program

```bash
python smart_home.py
```

The program demonstrates smart home device operations and saves the device state to `home_state.json`.

### Step 4: Run static analysis tools

Install the tools if necessary:

```bash
python -m pip install pylint bandit flake8
```

Run Pylint:

```bash
python -m pylint smart_home.py
```

Run Bandit:

```bash
python -m bandit -r smart_home.py
```

Run Flake8:

```bash
python -m flake8 smart_home.py
```

## 8. Deliverables

The project contains the following deliverables:

- `smart_home.py` — corrected Python source code.
- `issues.md` — issue descriptions, severity or category, and corrective actions.
- `reflection.md` — reflections on static code analysis and the fixes performed.
- `pylint_before.txt` and `pylint_after.txt` — Pylint reports.
- `bandit_before.txt` and `bandit_after.txt` — Bandit reports.
- `flake8_before.txt` and `flake8_after.txt` — Flake8 reports.

## 9. Conclusion

This lab demonstrated how static code analysis can improve Python code quality, security, and consistency. Using Pylint, Bandit, and Flake8 helped identify different categories of issues in the original program. After applying corrective changes, the program achieved a Pylint score of 10.00/10, with no remaining Bandit findings or Flake8 violations.

The exercise also demonstrated the importance of documenting issues, verifying fixes through repeated analysis, and using Git for version control.

## 10. Repository

GitHub repository: [SE_LAB_PES1UG24AM341](https://github.com/ksanandd/SE_LAB_PES1UG24AM341)

Project directory: `SE_Lab5/L5_36_smart_home/`
