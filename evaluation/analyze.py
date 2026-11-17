"""Generate comparison.csv, comparison.png and summary.txt from measured data."""
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
RESULTS = HERE / 'results.csv'
SESSIONS = HERE / 'sessions.csv'
SONAR = HERE / 'sonar_metrics.csv'

def main():
    if not RESULTS.exists():
        raise SystemExit('Run: python evaluation/collect.py first')
    df = pd.read_csv(RESULTS)
    if SESSIONS.exists():
        sessions = pd.read_csv(SESSIONS)
        if not sessions.empty:
            durations = sessions.groupby('mode', as_index=False)['minutes'].sum().rename(columns={'minutes': 'time_minutes'})
            df = df.merge(durations, on='mode', how='left')
    if SONAR.exists():
        sonar = pd.read_csv(SONAR)
        if not sonar.empty:
            df = df.merge(sonar, on='mode', how='left')
    df.to_csv(HERE / 'comparison.csv', index=False)
    measures = [c for c in ('time_minutes','tests_passed','coverage_percent','bugs','code_smells','vulnerabilities') if c in df.columns and df[c].notna().any()]
    if measures:
        fig, axes = plt.subplots(1, len(measures), figsize=(max(5, 4*len(measures)), 4))
        if len(measures) == 1:
            axes = [axes]
        for ax, measure in zip(axes, measures):
            df.plot.bar(x='mode', y=measure, ax=ax, legend=False, rot=20)
            ax.set_title(measure.replace('_', ' ').title())
            ax.set_xlabel('')
        fig.tight_layout()
        fig.savefig(HERE / 'comparison.png', dpi=160)
        plt.close(fig)
    notes = ['AI software development evaluation', '=' * 36,
             'CAUTION: starter implementations are DEMOS, not evidence of an AI effect.',
             'Use measured times and independently developed implementations for a real experiment.', '', df.to_string(index=False)]
    if 'time_minutes' in df.columns:
        times = df.set_index('mode')['time_minutes']
        if all(k in times.index for k in ('baseline','ai_assisted')) and pd.notna(times['baseline']) and pd.notna(times['ai_assisted']) and times['baseline'] > 0:
            reduction = (times['baseline'] - times['ai_assisted']) / times['baseline'] * 100
            notes.append(f'\nObserved time reduction: {reduction:.1f}% (pilot only)')
    (HERE / 'summary.txt').write_text('\n'.join(notes) + '\n', encoding='utf-8')
    print('\n'.join(notes))
    print('\nSaved evaluation/comparison.csv, comparison.png, summary.txt')

if __name__ == '__main__':
    main()
