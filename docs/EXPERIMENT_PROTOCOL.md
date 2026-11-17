# Controlled evaluation protocol

## Research question
How does ChatGPT assistance affect implementation time, test success and static code-quality findings for a small Python task?

## Conditions
- **Baseline:** implement without ChatGPT, Copilot or other generative AI.
- **AI-assisted:** ChatGPT allowed; save the exact prompts and responses in `docs/AI_PROMPTS.md`.
- Use the same Python version, editor, hardware, fixed requirements and test suite.
- Start timing before implementation; stop after coding, debugging and final local test run. Include prompt-writing and AI-review time.
- Do not edit the shared test suite after starting a timed condition.
- Commit code after each condition, noting commit hashes.

## Task specification (both conditions)
Implement `calculate(a, b, operation)` in `calculator.py`.
Supported operations: `add`, `subtract`, `multiply`, `divide`.
Division by zero and unknown operations must raise `ValueError`.
Support negative numbers, floating-point inputs and zero.

## Important threats to validity
Doing the identical task twice introduces learning/carryover. The starter files are working demonstrations, **not independently observed experimental results**. For a credible pilot, use two matched tasks, alternate task-condition assignments or recruit multiple participants and counterbalance the order. A single-person four-hour pilot is descriptive only; do not claim statistical significance or causality.

## Record actual evidence
1. Delete or replace the starter `baseline/calculator.py` and implement it yourself with AI disabled.
2. Record `python evaluation/measure.py start baseline` and `... stop` around the full work session.
3. Create the AI version under `ai_assisted/calculator.py` using ChatGPT; record the AI timer.
4. Run `python evaluation/collect.py` and `python evaluation/analyze.py`.
5. Add optional SonarQube Cloud results to `evaluation/sonar_metrics.csv`.
6. Note developer, environment, date, task order, prompts, commits, issues and deviations in `docs/EXPERIMENT_NOTES.md`.

## Interpretation
- Time reduction (%) = (baseline minutes - AI minutes) / baseline minutes * 100.
- Test pass count and line coverage measure different things; neither proves functional correctness.
- SonarQube bugs, code smells and vulnerabilities are static findings, not confirmed defects or security exploits.
- Missing SonarQube metrics must stay blank, not zero.
