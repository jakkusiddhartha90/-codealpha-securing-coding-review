# Secure Coding Review — Task 3

**Student:** JAKKU SIDDHARTHA
**Internship:** CodeAlpha  
**Application:** Python / Flask local training application  
**Environment:** Windows/Kali 

## 1. Scope and method
Reviewed the training source in `app/insecure_app.py`, compared it with `app/secure_app.py`, ran Bandit static analysis, and executed automated tests. Testing was limited to a local application.

## 2. Findings

| ID | Issue | Risk | Evidence in training sample | Remediation |
|---|---|---|---|---|
| SCR-01 | SQL injection | High | SQL query is assembled by concatenating the `id` parameter | Use parameterized SQL (`?`) and validate the expected data type |
| SCR-02 | Cross-site scripting (XSS) | High | User-controlled `name` is concatenated into an HTML response | Use context-aware output encoding / auto-escaping templates |
| SCR-03 | Debug mode enabled | Medium | Flask starts with `debug=True` | Disable debug mode outside local development; use a production WSGI server |
| SCR-04 | Missing input validation | Medium | Identifier is not validated as an integer | Validate type, range, length, and allowed values before processing |

Severity is a qualitative training assessment, not a formal CVSS score.

## 3. Fixes implemented
- SQL uses a parameterized query.
- `id` is parsed as a positive integer; invalid values return HTTP 400.
- Jinja template auto-escaping is used for user-controlled text.
- Debug mode is disabled.
- Automated tests cover normal input, HTML escaping, valid IDs, and invalid IDs.

## 4. Verification



| Check | Command | Actual result |
|---|---|---|
| Python version | `python --version` | python 3.15.2 |
| Unit tests | `python -m pytest -q` | 6 passed in 0.45 sec |
| Static analysis | `python -m bandit -c bandit.yaml -r app` | Completed successfully. Found 2 security issues in insecure_app.py: 1 Medium severity (SQL Injection – B608) and 1 High severity (Flask Debug Mode – B201). |
| Safe app | `python app/secure_app.py` | Started successfully. Flask development server running at http://127.0.0.1:5000. Debug mode: OFF. |

## 5. Conclusion
The review identified unsafe SQL construction, unsafe HTML rendering, debug-mode exposure, and insufficient input validation in the intentionally insecure sample. The safer implementation applies parameterized SQL, output escaping, input validation, and safer runtime settings. Attach genuine screenshots as evidence.
