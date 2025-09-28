"""
Task 1 — Hello Qubits (with tiny TODOs)
Goal: prepare |0⟩ and |1⟩, apply X and H, and visualize on the Bloch sphere.
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
from pathlib import Path

OUT_DIR = Path("outputs/task1"); OUT_DIR.mkdir(parents=True, exist_ok=True)

def save_fig(fig, filename: str):
    p = OUT_DIR / filename
    fig.savefig(p, dpi=150, bbox_inches="tight")
    print(f"[saved] {p}")

# --- |0⟩ (default) ---
qc0 = QuantumCircuit(1, name="zero_state")
sv0 = Statevector.from_instruction(qc0)
fig0 = plot_bloch_multivector(sv0); fig0.suptitle("|0⟩ on Bloch sphere")
save_fig(fig0, "bloch_zero.png")

# --- |1⟩ by applying X to |0⟩ ---
qc1 = QuantumCircuit(1, name="one_state")
# TODO(you): Apply X on qubit 0 to make |1⟩
# qc1.x(0)
if qc1.size() == 0:
    raise RuntimeError("TODO(you): add qc1.x(0) to prepare |1⟩")

sv1 = Statevector.from_instruction(qc1)
fig1 = plot_bloch_multivector(sv1); fig1.suptitle("|1⟩ on Bloch sphere")
save_fig(fig1, "bloch_one.png")

# --- X|0⟩ (redundant with |1⟩ but kept for clarity) ---
qc_x = QuantumCircuit(1, name="apply_X")
# TODO(you): Apply X on qubit 0 here as well
# qc_x.x(0)
if qc_x.size() == 0:
    raise RuntimeError("TODO(you): add qc_x.x(0) so this figure renders")
sv_x = Statevector.from_instruction(qc_x)
figx = plot_bloch_multivector(sv_x); figx.suptitle("X|0⟩ = |1⟩")
save_fig(figx, "bloch_after_X.png")

# --- H|0⟩ ---
qc_h = QuantumCircuit(1, name="apply_H")
# TODO(you): Put |0⟩ into superposition with Hadamard on qubit 0
# qc_h.h(0)
if qc_h.size() == 0:
    raise RuntimeError("TODO(you): add qc_h.h(0) to create superposition")
sv_h = Statevector.from_instruction(qc_h)
figh = plot_bloch_multivector(sv_h); figh.suptitle("H|0⟩ = (|0⟩+|1⟩)/√2")
save_fig(figh, "bloch_after_H.png")

# Optional experiments:
# qc_h1 = QuantumCircuit(1); qc_h1.x(0); qc_h1.h(0)
# save_fig(plot_bloch_multivector(Statevector.from_instruction(qc_h1)).suptitle("H|1⟩"),
#          "bloch_H_on_one.png")

print("[done] Task 1 — see outputs/task1/")
