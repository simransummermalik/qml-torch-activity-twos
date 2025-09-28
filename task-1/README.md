# Task 1 — Hello Qubits

**Script to run:** `task-1/task_1_qubit.py`  
**Goal:** Prepare `|0⟩`, prepare `|1⟩` via `X`, apply `H` to get superposition, and visualize on the Bloch sphere.

## How to run
```bash
python task-1/task_1_qubit.py
```

## Expected outputs (saved under `outputs/task1/`)
- `bloch_zero.png` — `|0⟩` (north pole)  
- `bloch_one.png` — `|1⟩` (south pole)  
- `bloch_after_X.png` — `X|0⟩ = |1⟩`  
- `bloch_after_H.png` — `H|0⟩ = (|0⟩+|1⟩)/√2` (≈ +X axis)

## What each section does
1) **Imports** — Qiskit circuit, statevector, Bloch plotting.
2) **Output dir** — creates `outputs/task1/` so figures save headlessly.
3) **Build states** — `|0⟩` default; `qc1.x(0)` flips to `|1⟩`.
4) **Plot** — convert to pure states with `Statevector` and plot.
5) **X/H demos** — show effect of `X` and `H` on `|0⟩`.
6) **(Optional)** — try `H|1⟩` or add `Z` after `H`.

## Deliverables
- Four PNGs in `outputs/task1/`
- Filled `task-1/TODO.md`
