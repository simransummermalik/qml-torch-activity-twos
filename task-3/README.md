# Task 3 — Entanglement (Bell State)

**Script to run:** `task-3/task_3.py`  
**Goal:** `H` on q0 → `CNOT(q0→q1)`, measure both, observe correlated outcomes (00/11).

## How to run
```bash
python task-3/task_3.py
```

## Expected output
- `outputs/task3/bell_counts.png` — strong peaks at `00` and `11`

## What each section does
1) **Imports** — circuit, simulator, histogram plotting.
2) **Output dir** — creates `outputs/task3/`.
3) **Bell circuit** — `qc.h(0)` then `qc.cx(0,1)`.
4) **Measurement** — `qc.measure([0,1],[0,1])`.
5) **Run + counts** — shows mostly `00` and `11`.
6) **Plot** — saves histogram.
7) **(Optional)** — add `X` on q1 after CNOT and observe changes.

## Deliverables
- Histogram PNG in `outputs/task3/`
- Filled `task-3/TODO.md`
