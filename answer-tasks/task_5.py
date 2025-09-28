# answer-tasks/task_5.py — Qiskit 2.x compatible hybrid baseline vs quantum-encoded
import numpy as np
from pathlib import Path
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from qiskit.circuit.library import zz_feature_map
from qiskit.quantum_info import Statevector

OUT = Path("outputs/task5")
OUT.mkdir(parents=True, exist_ok=True)

# 1) Data
X, y = make_moons(n_samples=600, noise=0.25, random_state=42)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, stratify=y, random_state=0)

# 2) Baseline (classical) logistic regression on raw features
sc_b = StandardScaler().fit(X_tr)
Xtr_b = sc_b.transform(X_tr); Xte_b = sc_b.transform(X_te)
acc_b = accuracy_score(y_te, LogisticRegression(max_iter=300).fit(Xtr_b, y_tr).predict(Xte_b))

# 3) Quantum-encoded features via a ZZ feature map (2 qubits -> 4 probabilities)
reps = 2
fm = zz_feature_map(num_qubits=2, reps=reps)
param_list = sorted(fm.parameters, key=lambda p: p.name)

def q_probs(row):
    """Map one 2D sample -> bind into feature map -> statevector -> length-4 probs."""
    b = fm.assign_parameters(
        {param_list[0]: float(row[0]), param_list[1]: float(row[1])},
        inplace=False
    )
    sv = Statevector.from_instruction(b)
    return (np.abs(sv.data) ** 2).astype(np.float64)  # shape (4,)

Xtr_qp = np.vstack([q_probs(r) for r in X_tr])
Xte_qp = np.vstack([q_probs(r) for r in X_te])

# Standardize quantum features and train a simple classifier
sc_q = StandardScaler().fit(Xtr_qp)
Xtr_q = sc_q.transform(Xtr_qp); Xte_q = sc_q.transform(Xte_qp)
acc_q = accuracy_score(y_te, LogisticRegression(max_iter=300).fit(Xtr_q, y_tr).predict(Xte_q))

# 4) Report
rep = [
    "=== Hybrid Classifier (Didactic) ===",
    f"Baseline accuracy:        {acc_b:.4f}",
    f"Quantum-encoded accuracy: {acc_q:.4f}",
    f"Feature map reps:         {reps}",
    "Feature dimension:        2 qubits → 4 probs"
]
(OUT / "hybrid_report.txt").write_text("\n".join(rep), encoding="utf-8")
print("\n".join(rep))
print("[answers] task5 done → outputs/task5/")

