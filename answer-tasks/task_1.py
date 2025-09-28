"""
Task 1 — Hello Qubits
Your goal:
1) Make a circuit for |0⟩ and |1⟩
2) Apply X (flip) and H (superposition)
3) Visualize on the Bloch sphere

Add your 1–2 sentence observation note here:
- e.g., "H on |0> points to +X on the Bloch sphere; X flips |0> to |1>."
"""

# ---- Imports (each line explained) ----
from qiskit import QuantumCircuit            # Core object for building circuits
from qiskit.quantum_info import Statevector  # Lets us compute statevectors easily
from qiskit.visualization import plot_bloch_multivector  # Bloch sphere helper
import matplotlib.pyplot as plt              # For saving plots
from pathlib import Path                     # For safe file paths

# ---- Output directory ----
OUT_DIR = Path("outputs/task1")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ---- Helper: save figure to disk ----
def save_fig(fig, name: str):
    path = OUT_DIR / name
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"[saved] {path}")

# ---- 1) |0> and |1> as circuits ----
# A) |0> is the default starting state of a new 1-qubit circuit.
qc0 = QuantumCircuit(1, name="zero_state")

# B) |1> can be prepared by applying an X (NOT) gate to |0>.
qc1 = QuantumCircuit(1, name="one_state")
qc1.x(0)  # Flip |0> -> |1>

# ---- Visualize both on Bloch spheres ----
# We compute the statevector directly from the circuit's unitary part (ignores measurement).
sv0 = Statevector.from_instruction(qc0)  # |0>
sv1 = Statevector.from_instruction(qc1)  # |1>

# Plot both on Bloch spheres (multivector == supports multi-qubit; here it's 1-qubit).
fig0 = plot_bloch_multivector(sv0)
fig0.suptitle("|0> on Bloch sphere")
save_fig(fig0, "bloch_zero.png")

fig1 = plot_bloch_multivector(sv1)
fig1.suptitle("|1> on Bloch sphere")
save_fig(fig1, "bloch_one.png")

# ---- 2) Apply X and H gates and visualize ----
# Start from |0>, apply X -> |1>
qc_x = QuantumCircuit(1, name="apply_X")
qc_x.x(0)
sv_x = Statevector.from_instruction(qc_x)
figx = plot_bloch_multivector(sv_x)
figx.suptitle("X|0> = |1> on Bloch sphere")
save_fig(figx, "bloch_after_X.png")

# Start from |0>, apply H -> (|0> + |1>)/sqrt(2): points to +X axis on Bloch sphere.
qc_h = QuantumCircuit(1, name="apply_H")
qc_h.h(0)
sv_h = Statevector.from_instruction(qc_h)
figh = plot_bloch_multivector(sv_h)
figh.suptitle("H|0> = (|0> + |1>)/√2 on Bloch sphere")
save_fig(figh, "bloch_after_H.png")

print("[done] Task 1 complete. See PNGs in outputs/task1")
