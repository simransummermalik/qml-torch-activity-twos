"""
Task 3 — Entanglement
Your goal:
1) Create a Bell state: H on q0, then CNOT(q0 -> q1).
2) Measure both qubits.
3) Check results are correlated (~'00' and '11' only).

Add your 1–2 sentence observation note here:
- e.g., "Bell state shows strong correlations; we see nearly only 00 and 11 with ~50/50 split."
"""

# ---- Imports ----
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from pathlib import Path

# ---- Output directory ----
OUT_DIR = Path("outputs/task3")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def save_fig(fig, name: str):
    path = OUT_DIR / name
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"[saved] {path}")

# ---- 1) Build Bell state circuit ----
qc = QuantumCircuit(2, 2, name="bell_pair")
qc.h(0)           # Create superposition on qubit 0
qc.cx(0, 1)       # Entangle: control=0, target=1
qc.measure([0,1], [0,1])  # Measure both into classical bits 0 and 1

# ---- 2) Simulate ----
sim = AerSimulator()
tqc = transpile(qc, sim)
job = sim.run(tqc, shots=5000)
result = job.result()
counts = result.get_counts(tqc)

print("Counts:", counts)  # Expect mostly '00' and '11'

# ---- 3) Plot ----
fig = plot_histogram(counts)
fig.suptitle("Bell State Measurement (H + CNOT)")
save_fig(fig, "bell_counts.png")

print("[done] Task 3 complete. See PNG in outputs/task3")
