# Task 4 — Quantum Feature Maps

**Script to run:** `task-4/task_4.py`  
**Goal:** Encode `(x1, x2)` using a 2-qubit feature map; inspect amplitudes and circuit.

## How to run
```bash
python task-4/task_4.py
```

## Expected outputs
- `outputs/task4/feature_map_state.txt` — amplitudes with probabilities
- `outputs/task4/feature_map_circuit.txt` — ASCII circuit diagram

## What each section does
1) **Imports** — feature map, `Statevector`, numpy, filesystem.
2) **Output dir** — creates `outputs/task4/`.
3) **Hyperparameters** — choose `reps` and `(x1, x2)`.
4) **Binding** — assign classical inputs to the circuit parameters.
5) **Statevector** — print amplitudes and probabilities.
6) **Circuit diagram** — render to ASCII.
7) **(Optional)** — vary `reps`/inputs and compare outputs.

## Deliverables
- Two text files in `outputs/task4/`
- Filled `task-4/TODO.md`
