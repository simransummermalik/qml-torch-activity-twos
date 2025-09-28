"""
Task 3 — Entanglement (with tiny TODOs)
Goal: create a Bell state with H on q0 then CNOT(q0→q1); measure both; see 00/11.
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from pathlib import Path

OUT_DIR = Path("outputs/task3"); OUT_DIR.mkdir(parents=True, exist_ok=True)
SHOTS = 5000

def save_fig(fig, filename: str):
    p = OUT_DIR / filename
    fig.savefig(p, dpi=150, bbox_inches="tight")
    print(f"[saved] {p}")

qc = QuantumCircuit(2, 2, name="bell_pair")

# TODO(you): 1) Put q0 in superposition (Hadamard)
# qc.h(0)
# TODO(you): 2) Entangle q1 with q0 using CNOT(control=0, target=1)
# qc.cx(0, 1)
if qc.size() == 0:
    raise RuntimeError("TODO(you): add qc.h(0) and qc.cx(0, 1) to build the Bell state")

# Measure both qubits
qc.measure([0, 1], [0, 1])

sim = AerSimulator()
tqc = transpile(qc, sim)
counts = sim.run(tqc, shots=SHOTS).result().get_counts(tqc)
print("Counts (expect mostly '00' and '11'):", counts)

fig = plot_histogram(counts); fig.suptitle(f"Bell state (shots={SHOTS})")
save_fig(fig, "bell_counts.png")

# Optional: uncomment to flip q1 after entanglement and observe changes.
# qc2 = QuantumCircuit(2, 2); qc2.h(0); qc2.cx(0,1); qc2.x(1); qc2.measure([0,1],[0,1])

print("[done] Task 3 — see outputs/task3/")
