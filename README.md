# AI-Assisted Software Development Evaluation — Python MVP

A working, **honestly labeled pilot evaluation framework** comparing Python development with and without ChatGPT. Python + pytest + coverage + pandas/matplotlib + Git + GitHub Actions; SonarQube Cloud is optional and **not required to run**.

> **Important:** Both shipped calculator implementations are reference/demo code to verify the pipeline. They were not developed in timed independent conditions. Their results are **not experimental evidence**. Replace them and measure real sessions before making claims about AI impact.

## MVP implementation status (November 2026)

The technical demonstration has been completed. The project has separate baseline and AI-assisted calculator implementations, automated pytest and coverage collection, GitHub Actions CI, and two SonarQube Cloud scan workflows. The latest CI and both SonarQube workflows were reported passing after the final fixes.

### Recorded comparison

| Metric | Baseline | AI-assisted |
|---|---:|---:|
| Automated tests | 9/9 passed | 9/9 passed |
| Local coverage | 100% | 100% |
| SonarQube quality gate | Passed | Passed |
| SonarQube security rating | A | A |
| Issues in calculator-specific analysis | 0 | 0 |
| SonarQube lines of code | 26 | 22 |
| Development time | One recorded session: 0.308 minutes | Not recorded |

The AI-assisted reference code is four lines (approximately 15.4%) shorter. This does **not** establish that AI increased productivity or quality. The baseline timing record is only a short recorded session, not verified total development time. SonarQube's dashboard showed 0% coverage because local coverage reports were not imported; **100% above refers to local pytest coverage**.

The comparison CSV contains blank SonarQube bug, code-smell, and vulnerability columns; dashboard observations should not be mistaken for automatically imported CSV measurements.

### Final report
[Read the final MVP evaluation report](evaluation/final_report.md).

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

## SonarQube Cloud — configured for this MVP (optional for local runs)
1. This MVP already has two SonarQube Cloud projects. For a fork or new installation, create an account at https://sonarcloud.io/ and import your own repository. Availability and plan limits may change.
2. Existing projects: [baseline](https://sonarcloud.io/dashboard?id=datawith-ramakrishna_ai-evaluation-baseline&branch=main) and [AI-assisted](https://sonarcloud.io/dashboard?id=datawith-ramakrishna_ai-evaluation-assisted&branch=main). For a fork, create your own two projects and copy their keys and organization key.
3. For a fork, update `sonar-baseline.properties` and `sonar-ai-assisted.properties` with your own keys.
4. The repository runs scans through `.github/workflows/sonar-baseline.yml` and `.github/workflows/sonar-ai-assisted.yml` using a GitHub Actions `SONAR_TOKEN` secret. For your own repository, configure that secret; never commit a token. Alternatively, use the official SonarScanner CLI.
5. For CLI scanning from the project root, in PowerShell set `$env:SONAR_TOKEN = 'your-token'` (locally only), then run:
   `sonar-scanner -Dproject.settings=sonar-baseline.properties -Dsonar.host.url=https://sonarcloud.io`
   and `sonar-scanner -Dproject.settings=sonar-ai-assisted.properties -Dsonar.host.url=https://sonarcloud.io`.
6. Copy the resulting **actual** counts for bugs, code smells and vulnerabilities into `evaluation/sonar_metrics.csv`, leaving unavailable metrics blank. Run analysis again.

The two scanner configurations use `sonar.exclusions` to isolate each calculator implementation; the newer SonarQube analysis scope does not honor `sonar.sources` in this setup. The SonarQube Cloud interface and metric names may differ by analysis mode/version. If the current UI shows reliability, maintainability and security issues instead of these legacy names, document the actual metric definitions and adapt the CSV columns consistently. Do not treat unavailable data as zero.

## Git and CI/CD

The project is maintained in [GitHub](https://github.com/Datawith-Ramakrishna/-ai-software-evaluation). After making changes, commit and push them from the repository root:

```powershell
git add .
git commit -m "Update evaluation project"
git push origin main
```

The workflow `.github/workflows/ci.yml` tests both conditions on Python 3.12. Separate workflows `.github/workflows/sonar-baseline.yml` and `.github/workflows/sonar-ai-assisted.yml` run SonarQube Cloud scans. **CI test runtime is not developer implementation time.**

## Scientific limitations
This is a descriptive single-developer pilot. Repeated-task learning, prompt skill, task complexity and developer familiarity can confound comparisons. A defensible larger study needs matched tasks, counterbalanced order and multiple observations. The included starter implementations do not demonstrate an AI effect.
