# Task 3 — Secure Coding Review

## Objective
Perform a small security review of a Python web application, identify weaknesses, apply secure coding fixes, and verify the safer implementation.

## 1. Environment
Use Python 3.10 or newer. VS Code is optional. Open this folder in VS Code and use its integrated terminal.

```bash
python --version
python -m venv .venv
```

Activate the environment:

PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```

Kali/Linux:
```bash
source .venv/bin/activate
```

Install packages:
```bash
python -m pip install -r requirements.txt
```

## 2. What is being reviewed?
- `app/insecure_app.py` is an intentionally unsafe teaching sample. Inspect it; do not expose or deploy it.
- `app/secure_app.py` is the remediated local demo.
- `tests/test_secure_app.py` checks important safer behavior.
- `reports/code-review-report.md` documents findings and fixes.

## 3. Run and test the safe app
```bash
python -m pytest -q
python app/secure_app.py
```
Visit `http://127.0.0.1:5000`. Try:
- `/?name=Student` — normal input.
- `/?name=<script>alert(1)</script>` — the input is rendered as text, not executable HTML.
- `/lookup?id=1` — valid numeric identifier.
- `/lookup?id=abc` — should return HTTP 400.

Stop the server with `Ctrl+C`.

## 4. Static analysis
```bash
python -m bandit -c bandit.yaml -r app
```
Bandit may flag the intentionally insecure sample. That is expected. Review each finding rather than hiding it. Run it on the secure file alone for a focused check:
```bash
python -m bandit -r app/secure_app.py
```

## 5. Your review evidence
Capture your own screenshots of:
1. `python --version`
2. `pytest` showing all tests passed
3. Bandit output and a short explanation of findings
4. Safe app open in the browser
5. Invalid input returning HTTP 400

Save screenshots in `screenshots/`. Update the report with the versions and actual results from your machine.
