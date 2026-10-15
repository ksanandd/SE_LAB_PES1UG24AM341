# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without executing it. It helps developers identify potential bugs, security weaknesses, and coding-style violations early in development. It improves maintainability and reduces the effort required to identify problems manually.

## 2. What are the differences between Pylint, Bandit, and Flake8?

Pylint checks code quality, naming conventions, documentation, and potential programming mistakes. Bandit identifies potentially insecure coding patterns in Python applications. Flake8 checks Python code for style violations, whitespace problems, and other formatting issues. Using all three provides complementary checks.

## 3. What issues were identified and how were they fixed?

The original program received a Pylint score of 4.80/10. The findings included missing docstrings, non-standard naming, a mutable default argument, inconsistent return statements, hardcoded configuration values, and unsafe shell execution. The code was updated to address these issues, improve file handling, and correct device-specific settings. The unused subprocess-based scene runner was removed.

## 4. What did you learn from this lab?

This lab demonstrated that code can execute successfully while still containing quality and security weaknesses. Pylint helped improve code quality, Bandit helped identify security risks, and Flake8 helped enforce consistent formatting. After the changes, Pylint reached 10.00/10, Bandit reported no issues, and Flake8 reported no violations. Static analysis is valuable, but its results should be reviewed alongside functional testing because a clean report does not guarantee that a program is completely bug-free.