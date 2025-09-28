"""
Task 2 — Measuring Superposition
Your goal:
1) Build a circuit with H + measurement.
2) Run on simulator with many shots.
3) Expect ~50% 0s and ~50% 1s.

Add your 1–2 sentence observation note here:
- e.g., "After H, measurement is random with ~equal chance of 0 or 1 across many shots."
"""

# ---- Imports ----
from qiskit import QuantumCircuit, transpile        # Build & compile circuits
from qiskit_aer import AerSimulator                 # Aer simulator backend
from qiskit.visualization import plot_histogram     # Convenience count histogram
import matplotlib.pyplot as plt
from pathlib import Path

# ---- Output directory ----
OUT_DIR = Path("outputs/task2")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def save_fig(fig, name: str):
    path = OUT_DIR / name
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"[saved] {path}")

# ---- 1) Build the circuit ----
qc = QuantumCircuit(1, 1, name="H_then_measure")  # 1 qubit, 1 classical bit
qc.h(0)            # Put qubit in superposition
qc.measure(0, 0)   # Measure qubit 0 into classical bit 0

# ---- 2) Run on simulator ----
sim = AerSimulator()                 # Choose a general-purpose simulator
tqc = transpile(qc, sim)             # Compile circuit for the backend
job = sim.run(tqc, shots=5000)       # Execute many shots to estimate probabilities
result = job.result()                # Block until results are available
counts = result.get_counts(tqc)      # Dictionary like {'0': ~2500, '1': ~2500}

print("Counts:", counts)

# ---- 3) Plot histogram ----
fig = plot_histogram(counts)
fig.suptitle("Measurement after H (expected ~50/50)")
save_fig(fig, "superposition_measurement_hist.png")

print("[done] Task 2 complete. See PNG in outputs/task2")
