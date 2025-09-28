"""
Task 2 — Measuring Superposition (with tiny TODOs)
Goal: build H + measurement, run many shots, expect ≈ 50% 0 and 50% 1.
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from pathlib import Path

OUT_DIR = Path("outputs/task2"); OUT_DIR.mkdir(parents=True, exist_ok=True)

# TODO(you): pick the number of shots (try 5000 first, then 50000)
SHOTS = None
if SHOTS is None:
    raise RuntimeError("TODO(you): set SHOTS (e.g., 5000)")

def save_fig(fig, filename: str):
    p = OUT_DIR / filename
    fig.savefig(p, dpi=150, bbox_inches="tight")
    print(f"[saved] {p}")

# Build circuit: H on q0, measure into c0
qc = QuantumCircuit(1, 1, name="H_then_measure")
# TODO(you): add the H gate
# qc.h(0)
# TODO(you): add the measurement (q0 -> c0)
# qc.measure(0, 0)
if qc.size() == 0 or qc.num_clbits == 0:
    raise RuntimeError("TODO(you): add qc.h(0) and qc.measure(0, 0)")

sim = AerSimulator()
tqc = transpile(qc, backend=sim)
result = sim.run(tqc, shots=SHOTS).result()
counts = result.get_counts(tqc)
print("Counts:", counts)

fig = plot_histogram(counts); fig.suptitle(f"After H in Z-basis (shots={SHOTS})")
save_fig(fig, "superposition_measurement_hist.png")

print("[done] Task 2 — see outputs/task2/")
