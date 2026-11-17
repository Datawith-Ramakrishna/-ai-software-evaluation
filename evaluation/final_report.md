# AI Effect in Software Development — Final Windows MVP Evaluation Report

A completed **technical pilot evaluation framework** comparing baseline Python development with AI-assisted development using ChatGPT. The project uses **Python 3.12, pytest, coverage, pandas/matplotlib, Git, GitHub Actions, and SonarQube Cloud**.

> **Important:** The supplied calculator implementations are **reference/demo implementations**, not independently developed implementations under controlled conditions. The results verify the evaluation pipeline; they **do not establish that AI improves productivity or software quality**.

## 1. Project objective

The MVP demonstrates how to compare two development conditions:

- **Baseline:** Python implementation intended for development without AI assistance.
- **AI-assisted:** Python implementation intended for development with ChatGPT assistance.

The framework measures functional test results, local code coverage, static-analysis findings, source-code size, and recorded development sessions where available.

## 2. Tools and environment

| Component | Tool |
|---|---|
| Operating system | Windows |
| Programming language | Python 3.12 |
| Automated testing | pytest |
| Local coverage | coverage/pytest coverage reporting |
| Data collection and analysis | Python, pandas, matplotlib |
| Version control | Git and GitHub |
| CI/CD | GitHub Actions |
| Static analysis | SonarQube Cloud |

## 3. Project structure

```text
ai-software-evaluation/
├── baseline/
│   └── calculator.py
├── ai_assisted/
│   └── calculator.py
├── tests/
├── evaluation/
│   ├── collect.py
│   ├── analyze.py
│   ├── measure.py
│   ├── sessions.csv
│   ├── results.csv
│   ├── comparison.csv
│   ├── comparison.png
│   ├── summary.txt
│   ├── sonar_metrics.csv
│   └── final_report.md
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── sonar-baseline.yml
│       └── sonar-ai-assisted.yml
├── sonar-baseline.properties
├── sonar-ai-assisted.properties
├── requirements.txt
└── README.md
```

## 4. Run the evaluation (PowerShell)

From the project root:

```powershell
cd D:\ai-software-evaluation

.\.venv\Scripts\python.exe evaluation\collect.py
.\.venv\Scripts\python.exe evaluation\analyze.py
```

If the virtual environment has not yet been created:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

The evaluation scripts generate or update files such as `evaluation/results.csv`, `evaluation/comparison.csv`, `evaluation/comparison.png`, and `evaluation/summary.txt`.

## 5. Functional testing and coverage results

The recorded comparison file contains these results:

| Metric | Baseline | AI-assisted |
|---|---:|---:|
| Total tests | 9 | 9 |
| Passed tests | 9 | 9 |
| Failed tests | 0 | 0 |
| Skipped tests | 0 | 0 |
| Local code coverage | 100.0% | 100.0% |
| pytest exit code | 0 | 0 |

**Interpretation:** Both demo implementations passed the available test suite and achieved 100% *local* coverage. This demonstrates that the test pipeline runs successfully, not that either implementation is free from defects.

## 6. SonarQube Cloud results

Two separate SonarQube Cloud projects were configured to compare the calculator implementations:

- **Baseline project:** `datawith-ramakrishna_ai-evaluation-baseline`
- **AI-assisted project:** `datawith-ramakrishna_ai-evaluation-assisted`

The most recently reviewed SonarQube dashboards showed:

| Metric | Baseline | AI-assisted |
|---|---:|---:|
| Quality gate | Passed | Passed |
| Reported open issues | 0 | 0 |
| Reported security issues | 0 | 0 |
| Security rating | A | A |
| Code duplication | 0.0% | 0.0% |
| Lines of code | 26 | 22 |
| SonarQube-displayed coverage | 0.0% | 0.0% |

The AI-assisted implementation had **4 fewer lines of code**, a reduction of approximately **15.4%** relative to the baseline:

```text
(26 - 22) / 26 × 100 ≈ 15.4%
```

**Coverage clarification:** The SonarQube dashboards displayed 0.0% coverage because the local coverage report had not been imported into SonarQube. This does **not** contradict the independently generated 100% local coverage results.

**Metric clarification:** The existing `evaluation/comparison.csv` contains blank values for `bugs`, `code_smells`, and `vulnerabilities`. These missing CSV values should not be silently interpreted as zero. The zero reported issues above come from the reviewed SonarQube dashboard views, not from those blank CSV fields.

### Analysis scope

The SonarQube Cloud configuration uses `sonar.exclusions` to exclude the opposite implementation and unrelated project files from each scan. This was necessary because the current SonarQube Cloud analysis-scope behavior did not honor some older source-scoping properties.

The purpose is to compare the calculator source code rather than mistakenly attribute workflow or evaluation-script findings to the calculator implementations.

## 7. Development-time measurements

The `evaluation/sessions.csv` file currently contains one recorded session:

| Condition | Recorded session duration | Status |
|---|---:|---|
| Baseline | 0.308 minutes (approximately 18.5 seconds) | One recorded session |
| AI-assisted | Not recorded | Missing measurement |

The baseline entry was recorded on **17 November 2026 (UTC)**.

> **Important:** The recorded baseline session is not verified as the full time required to develop the implementation. Because no AI-assisted development session was recorded, a productivity improvement percentage **cannot be calculated**.

Do not substitute CI execution time, test runtime, or estimated development time for missing measurements.

## 8. GitHub Actions and CI/CD

The project includes automated workflows for:

- Running Python tests in GitHub Actions.
- Scanning the baseline implementation with SonarQube Cloud.
- Scanning the AI-assisted implementation with SonarQube Cloud.

The testing and SonarQube workflows were successfully run during the MVP setup.

**Note:** CI execution time measures automation runtime, not developer implementation time.

## 9. Scientific limitations

This is a **descriptive, single-project technical pilot**, not a controlled experiment proving an AI effect.

Key limitations include:

1. **Demo implementations:** The shipped calculator implementations were not independently developed under timed, controlled conditions.
2. **Incomplete timing:** Only one short baseline session is recorded; AI-assisted development time is missing.
3. **Small task:** A calculator module does not represent the complexity of larger software projects.
4. **Limited observations:** A single pair of implementations cannot establish general productivity or quality effects.
5. **Test limitations:** Passing tests and achieving 100% local coverage do not guarantee correctness or security.
6. **SonarQube coverage integration:** Coverage was measured locally but not imported into the SonarQube dashboards.
7. **Potential confounding:** Developer familiarity, task order, learning, and prompt quality may affect a future controlled comparison.

A stronger follow-up study would require matched tasks, fixed acceptance tests, independently produced implementations, recorded prompts, complete timing, and multiple observations.

## 10. Overall conclusion

The MVP successfully demonstrates an end-to-end workflow for **collecting, testing, analyzing, and comparing** baseline and AI-assisted Python implementations on Windows.

Both demo implementations passed **9 of 9 tests**, achieved **100% local coverage**, passed their **SonarQube Cloud quality gates**, and showed **zero reported open issues** on the reviewed dashboards. The AI-assisted calculator had **22 lines of code** versus **26 lines** for the baseline.

These results support the conclusion that **the evaluation infrastructure works for the supplied examples**. They do **not** demonstrate that AI assistance causes faster development, better security, or higher software quality.

**Final MVP status:** **Technical demonstration completed; controlled AI-impact experiment not yet conducted.**

## 11. Final repository update

After saving this report as `evaluation/final_report.md`, run:

```powershell
cd D:\ai-software-evaluation

git add evaluation/final_report.md
git commit -m "Add final MVP evaluation report"
git push origin main
```

The report can then be linked from the main `README.md`:

```markdown
[Read the final MVP evaluation report](evaluation/final_report.md)
```
