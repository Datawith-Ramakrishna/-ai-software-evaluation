# AI Effect in Software Development — 4-hour Windows MVP

A working, **honestly labeled pilot evaluation framework** comparing Python development with and without ChatGPT. Python + pytest + coverage + pandas/matplotlib + Git + GitHub Actions; SonarQube Cloud is optional and **not required to run**.

> **Important:** Both shipped calculator implementations are reference/demo code to verify the pipeline. They were not developed in timed independent conditions. Their results are **not experimental evidence**. Replace them and measure real sessions before making claims about AI impact.

## Prerequisites
- Windows 10/11 with **Python 3.12** installed (`py -3.12 --version`)
- PowerShell and optionally Git (`git --version`)
- Internet for first-time pip package installation
- No Docker or SonarQube installation needed

## Quick start (PowerShell)
Open PowerShell in the extracted project folder and run:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe evaluation\collect.py
.\.venv\Scripts\python.exe evaluation\analyze.py
```

Or use `powershell -ExecutionPolicy Bypass -File scripts\setup_windows.ps1` followed by `powershell -ExecutionPolicy Bypass -File scripts\run_all_windows.ps1`. Using the venv's Python directly avoids activation-policy problems.

Results: `evaluation/results.csv`, `evaluation/comparison.csv`, `evaluation/comparison.png`, `evaluation/summary.txt` and XML/JSON test reports. Timing columns appear **only after real sessions have been recorded**.

## Conduct a real experiment
Read `docs/EXPERIMENT_PROTOCOL.md` first. For a quick pilot, keep the same task requirements and shared tests fixed. The demo code must be replaced with code produced under the appropriate condition.

**Manual baseline** (no AI):
```powershell
.\.venv\Scripts\python.exe evaluation\measure.py start baseline
# Write baseline\calculator.py yourself; test and debug it
$env:EVAL_MODE = 'baseline'
.\.venv\Scripts\python.exe -m pytest tests -q
.\.venv\Scripts\python.exe evaluation\measure.py stop
```

**AI-assisted condition** (record prompts in `docs/AI_PROMPTS.md`):
```powershell
.\.venv\Scripts\python.exe evaluation\measure.py start ai_assisted
# Develop ai_assisted\calculator.py using ChatGPT; test and debug it
$env:EVAL_MODE = 'ai_assisted'
.\.venv\Scripts\python.exe -m pytest tests -q
.\.venv\Scripts\python.exe evaluation\measure.py stop
```

Finally:
```powershell
.\.venv\Scripts\python.exe evaluation\collect.py
.\.venv\Scripts\python.exe evaluation\analyze.py
```

The timers append to `evaluation/sessions.csv`. Do not invent values. To repeat a new experiment, archive/remove sessions.csv first or the analysis will sum sessions by condition.

## Optional SonarQube Cloud — no local installation
1. Create a free SonarQube Cloud account at https://sonarcloud.io/ and import your GitHub repository. Availability and plan limits may change.
2. Create **two SonarQube projects**, one for `baseline`, one for `ai_assisted`. Copy the two project keys and organization key.
3. Replace placeholders in `sonar-baseline.properties` and `sonar-ai-assisted.properties`.
4. Follow SonarQube Cloud's current automatic GitHub analysis setup, **or** install the official SonarScanner CLI and authenticate with a token. Never commit a token.
5. For CLI scanning from the project root, in PowerShell set `$env:SONAR_TOKEN = 'your-token'` (locally only), then run:
   `sonar-scanner -Dproject.settings=sonar-baseline.properties -Dsonar.host.url=https://sonarcloud.io`
   and `sonar-scanner -Dproject.settings=sonar-ai-assisted.properties -Dsonar.host.url=https://sonarcloud.io`.
6. Copy the resulting **actual** counts for bugs, code smells and vulnerabilities into `evaluation/sonar_metrics.csv`, leaving unavailable metrics blank. Run analysis again.

The two scanner configurations isolate the source folders. The SonarQube Cloud interface and metric names may differ by analysis mode/version. If the current UI shows reliability, maintainability and security issues instead of these legacy names, document the actual metric definitions and adapt the CSV columns consistently. Do not treat unavailable data as zero.

## Git and CI/CD
```powershell
git init
git add .
git commit -m "Initial evaluation framework"
# Create a GitHub repository and push it; GitHub Actions runs automatically
```

The workflow `.github/workflows/ci.yml` tests both conditions on Python 3.12. It does not run SonarQube scanning until you configure that separately. **CI test runtime is not developer implementation time.**

## Suggested four-hour schedule
- **0:00–0:30:** extract ZIP, install dependencies, run both demo tests, freeze test requirements.
- **0:30–1:40:** replace demo implementations under baseline/AI conditions, log times and prompts.
- **1:40–2:20:** collect pytest and coverage, fix test configuration, inspect reports.
- **2:20–3:10:** run analysis and document comparisons; optionally configure SonarQube Cloud.
- **3:10–4:00:** push GitHub, verify Actions, finish experiment notes and German summary.

## Scientific limitations
This is a descriptive single-developer pilot. Repeated-task learning, prompt skill, task complexity and developer familiarity can confound comparisons. A defensible larger study needs matched tasks, counterbalanced order and multiple observations. The included starter implementations do not demonstrate an AI effect.
