# Qiskit Beginner Tasks

Two flows:

- **answer-tasks/** — reference implementations (for checking work).
- **task-1 … task-5/** — learner tasks (what you run + TODOs to fill).

Per your tree, code files live at:
- `answer-tasks/task1_hello_qubits.py`
- `answer-tasks/task2_measure_superposition.py`
- `answer-tasks/task3_entanglement.py`
- `answer-tasks/task4_feature_maps.py`
- `answer-tasks/task5_hybrid_classifier.py`
- `task-1/task_1_qubit.py`
- `task-2/task_2.py`
- `task-3/task_3.py`
- `task-4/task_4.py`
- `task-5/task_5.py`

> Run the **task-N** scripts and fill their **TODO.md**. Use **answer-tasks** only to compare after you try.

## Setup
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```

## Run tasks
From repo root:
```bash
python task-1/task_1_qubit.py
python task-2/task_2.py
python task-3/task_3.py
python task-4/task_4.py
python task-5/task_5.py
```

Outputs are saved into `outputs/` subfolders.

## Submit
1) Fill the task’s `TODO.md` with your notes.
2) Run the script and verify artifacts exist in `outputs/`.
3) Commit and push:
```bash
git add .
git commit -m "Task <N>: results - <your_name>"
git push
```

## Troubleshooting
- If Aer import fails: `pip install --upgrade qiskit-aer`.
- If plots don’t show, open the saved PNGs in `outputs/` directly.
