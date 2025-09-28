"""
Task 4 — Quantum Feature Maps (with tiny TODOs)
Goal: use a 2-qubit feature map, bind (x1, x2), inspect state amplitudes and circuit.
"""

# If your environment warns the class is deprecated, you can switch to:
# from qiskit.circuit.library import zz_feature_map as ZZ_FEATURE_MAP_FUNC
# feature_map = ZZ_FEATURE_MAP_FUNC(2, reps=REPS)

from qiskit.circuit.library import ZZFeatureMap
from qiskit.quantum_info import Statevector
from pathlib import Path
import numpy as np

OUT_DIR = Path("outputs/task4"); OUT_DIR.mkdir(parents=True, exist_ok=True)

def save_text(text: str, filename: str):
    p = OUT_DIR / filename
    p.write_text(text, encoding="utf-8")
    print(f"[saved] {p}")

# TODO(you): choose reps (circuit depth) and input values to bind
REPS = None    # e.g., 2
X1  = None     # e.g., 0.3
X2  = None     # e.g., 1.2
if REPS is None or X1 is None or X2 is None:
    raise RuntimeError("TODO(you): set REPS, X1, and X2")

feature_map = ZZFeatureMap(feature_dimension=2, reps=REPS)

# TODO(you): bind X1 and X2 into the feature map.
# Hint: you can bind by parameter name order:
#   params_sorted = sorted(feature_map.parameters, key=lambda p: p.name)
#   bound = feature_map.assign_parameters({params_sorted[0]: X1, params_sorted[1]: X2}, inplace=False)
bound = None
if bound is None:
    raise RuntimeError("TODO(you): create 'bound' by assigning X1/X2 to feature_map parameters")

# Convert to statevector and write amplitudes
sv = Statevector.from_instruction(bound)
amps = np.array(sv.data)
lines = [
    f"Feature Map: ZZFeatureMap(d=2, reps={REPS})",
    f"Binding: x1={X1}, x2={X2}",
    "",
    "Statevector (amplitudes):",
]
for i, a in enumerate(amps):
    lines.append(f"  |{i:02b}>: {a.real:+.6f} {a.imag:+.6f}j   |a|^2={abs(a)**2:.6f}")
lines.append(f"\nSum of probabilities: {float(np.sum(np.abs(amps)**2)):.6f}")
save_text("\n".join(lines), "feature_map_state.txt")

# Also save ASCII circuit
circtxt = bound.draw(output="text")
save_text(str(circtxt), "feature_map_circuit.txt")

print("[done] Task 4 — see outputs/task4/")
