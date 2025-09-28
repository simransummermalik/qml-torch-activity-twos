# Task 2 — Measuring Superposition

**Script to run:** `task-2/task_2.py`  
**Goal:** Build `H + measure`, run many shots, and see ~50% `0` and ~50% `1` (Z-basis).

## How to run
```bash
python task-2/task_2.py
```

## Expected output
- `outputs/task2/superposition_measurement_hist.png` — histogram of counts

## What each section does
1) **Imports** — circuit, `AerSimulator`, histogram plotting.
2) **Output dir** — creates `outputs/task2/`.
3) **Circuit** — `qc.h(0)` then `qc.measure(0,0)`.
4) **Run** — transpile and execute with configurable `shots`.
5) **Counts + plot** — print counts dict and save histogram.

## Deliverables
- Histogram PNG in `outputs/task2/`
- Filled `task-2/TODO.md`
