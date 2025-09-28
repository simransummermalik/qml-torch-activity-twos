# Task 5 — Hybrid Classifier Skeleton

**Script to run:** `task-5/task_5.py`  
**Goal:** Compare a classical baseline vs. a “quantum-encoded” pipeline on `make_moons`.

## How to run
```bash
python task-5/task_5.py
```

## Expected output
- `outputs/task5/hybrid_report.txt` — baseline & quantum-encoded accuracies and settings

## What each section does
1) **Data** — loads `make_moons`, train/test split.
2) **Baseline pipeline** — standardize raw features → `LogisticRegression` → accuracy.
3) **Quantum-encoded pipeline** — feature map → statevector → probabilities (length 4) → standardize → `LogisticRegression` → accuracy.
4) **Report** — writes results to `outputs/task5/hybrid_report.txt`.
5) **(Optional)** — try SVM or different `reps`.

## Deliverables
- Report in `outputs/task5/`
- Filled `task-5/TODO.md`
