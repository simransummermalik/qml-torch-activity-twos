# answer-tasks/task_4.py  — Qiskit 2.x compatible
from qiskit.circuit.library import zz_feature_map   # function (new API)
from qiskit.quantum_info import Statevector
from pathlib import Path
import numpy as np

OUT = Path("outputs/task4")
OUT.mkdir(parents=True, exist_ok=True)

# Choose settings + inputs
reps = 2
x1, x2 = 0.3, 1.2

# Build the feature map circuit (2 qubits => feature_dimension=2)
fm = zz_feature_map(num_qubits=2, reps=reps, name="ZZFeatureMap")

# Grab the *actual* Parameter objects from the circuit (sorted for stability)
params = sorted(fm.parameters, key=lambda p: p.name)   # e.g., [Parameter('x[0]'), Parameter('x[1]')]

# Bind your numbers to those parameters (never create your own ParameterVector here)
bound = fm.assign_parameters({params[0]: x1, params[1]: x2}, inplace=False)

# Get the statevector and save human-readable outputs
sv = Statevector.from_instruction(bound)
amps = np.asarray(sv.data)

(OUT / "feature_map_state.txt").write_text(
    "\n".join([
        f"reps={reps}, x1={x1}, x2={x2}",
        "Statevector amplitudes (|00>, |01>, |10>, |11>):",
        *[f"  |{i:02b}>: {a.real:+.6f} {a.imag:+.6f}j   |a|^2={abs(a)**2:.6f}" for i, a in enumerate(amps)],
        f"Sum of probabilities: {float(np.sum(np.abs(amps)**2)):.6f}"
    ]),
    encoding="utf-8"
)

(OUT / "feature_map_circuit.txt").write_text(str(bound.draw(output="text")), encoding="utf-8")

print("[answers] task4 done → outputs/task4/")
