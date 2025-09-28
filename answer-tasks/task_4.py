"""
Task 4 — Quantum Feature Maps
Your goal:
1) Use ZZFeatureMap OR PauliFeatureMap with 2 features (x1, x2).
2) Bind numeric values and inspect the resulting quantum state.
3) Show how classical inputs embed into a quantum state.

Add your 1–2 sentence observation note here:
- e.g., "Binding x1,x2 creates a specific quantum state (amplitudes); feature map depth changes entanglement."
"""

# ---- Imports ----
from qiskit.circuit.library import ZZFeatureMap, PauliFeatureMap   # Common feature maps
from qiskit.circuit import ParameterVector                        # For symbolic params
from qiskit.quantum_info import Statevector                       # To inspect state
from qiskit import QuantumCircuit                                 # For drawing
from pathlib import Path
import numpy as np

# ---- Output directory ----
OUT_DIR = Path("outputs/task4")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def save_text(text: str, name: str):
    path = OUT_DIR / name
    path.write_text(text, encoding="utf-8")
    print(f"[saved] {path}")

# ---- 1) Choose a feature map ----
# Option A: ZZFeatureMap with 2 qubits (for x1, x2). Easier for beginners.
feature_map = ZZFeatureMap(feature_dimension=2, reps=2)  # reps controls depth

# (Alternative) PauliFeatureMap:
# feature_map = PauliFeatureMap(feature_dimension=2, reps=1, paulis=['Z','ZZ'])

# ---- 2) Create symbolic parameters and bind numeric values ----
x = ParameterVector("x", length=2)       # x[0] -> x1, x[1] -> x2
bound_circ = feature_map.assign_parameters({x[0]: 0.3, x[1]: 1.2}, inplace=False)

# ---- 3) Inspect the embedded state ----
# Convert the (bound) feature-map circuit into a statevector (no measurement).
sv = Statevector.from_instruction(bound_circ)

# Save a text report of amplitudes (magnitude and phase) for learning purposes.
amps = np.array(sv.data)  # complex amplitudes
report_lines = []
report_lines.append("Feature Map: ZZFeatureMap(feature_dimension=2, reps=2)")
report_lines.append("Binding: x1=0.3, x2=1.2")
report_lines.append("\nStatevector (amplitudes):")
for i, a in enumerate(amps):
    report_lines.append(f"  |{i:02b}>: {a.real:+.6f} {a.imag:+.6f}j  |a|^2={abs(a)**2:.6f}")
report_lines.append("\nSum of probabilities (should be 1.0): {:.6f}".format(float(np.sum(np.abs(amps)**2))))
save_text("\n".join(report_lines), "feature_map_state.txt")

# Also save an ASCII circuit diagram for reference.
circuit_diagram = bound_circ.draw(output="text")
save_text(str(circuit_diagram), "feature_map_circuit.txt")

print("[done] Task 4 complete. See outputs/task4 for state & circuit text files.")
