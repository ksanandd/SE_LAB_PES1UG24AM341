# Lab 5: Static Code Analysis — Issues and Fixes

## Issue Documentation

| Issue | Type | Line(s) Before Fix | Description | Fix Approach |
|---|---|---|---|---|
| Hardcoded bind address | Security | 4 | `0.0.0.0` allows a service to listen on all network interfaces if used for binding. | Changed the configured host to `127.0.0.1` for local use. |
| Hardcoded password | Security | 7 | A password embedded in source code can be exposed through version control. | Read the optional password from the `SMART_HOME_PASSWORD` environment variable. |
| Shell command execution | Security | 51 | `subprocess.call(..., shell=True)` can expose the program to command injection. | Removed the unused scene-execution function and its subprocess dependency. |
| Mutable default argument | Bug | 10 | Using `settings={}` shares a mutable object between function calls. | Changed the default to `None` and initialized a new dictionary inside the function. |
| Inconsistent return statements | Code quality | 17–20 | `toggleDevice()` returned a Boolean for existing devices but implicitly returned `None` for missing devices. | Added an explicit `None` return for missing devices. |
| Non-standard naming | Style | Multiple | CamelCase function and argument names reduce consistency with Python conventions. | Renamed functions and arguments using `snake_case`. |
| Missing docstrings | Code quality | Multiple | Functions and the module lacked documentation. | Added module and function docstrings. |
| Unspecified file encoding | Code quality | 41 | The JSON state file was opened without explicitly specifying an encoding. | Added `encoding="utf-8"` to the file operation. |
| Incorrect device settings | Functional bug | Device initialization | Non-thermostat devices did not need thermostat-specific settings. | Added a default temperature setting for thermostats only. |
| Formatting violations | Style | Multiple | Flake8 identified whitespace, blank-line, inline-comment spacing, and line-length issues. | Corrected spacing and formatting. |

## Verification Results

- Initial Pylint score: 4.80/10
- Final Pylint score: 10.00/10
- Final Bandit report: No issues identified
- Final Flake8 report: No violations reported

The final program was executed successfully after the changes. The demonstration output was checked to confirm that device listing, temperature validation, power usage calculation, and state persistence continued to work.