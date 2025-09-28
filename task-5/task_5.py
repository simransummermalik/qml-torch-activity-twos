"""
Task 5 — Hybrid Classifier (with tiny TODOs)
Goal: compare baseline LR vs. a “quantum-encoded” pipeline using feature-map probabilities.
"""

import numpy as np
from pathlib import Path
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from qiskit.circuit.library import ZZFeatureMap
from qiskit.quantum_info import Statevector

OUT_DIR = Path("outputs/task5"); OUT_DIR.mkdir(parents=True, exist_ok=True)

def save_text(text: str, filename: str):
    p = OUT_DIR / filename
    p.write_text(text, encoding="utf-8")
    print(f"[saved] {p}")

# --- Data ---
X, y = make_moons(n_samples=600, noise=0.25, random_state=42)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=0, stratify=y)

# --- Baseline: LR on raw features (scaled) ---
sc_base = StandardScaler().fit(X_tr)
Xtr_b = sc_base.transform(X_tr); Xte_b = sc_base.transform(X_te)
clf_b = LogisticRegression(max_iter=200).fit(Xtr_b, y_tr)
acc_b = accuracy_score(y_te, clf_b.predict(Xte_b))

# --- Quantum-encoded: probabilities from a 2-qubit feature map ---
# TODO(you): pick a reps value (e.g., 2 or 3)
REPS = None
if REPS is None:
    raise RuntimeError("TODO(you): set REPS for the feature map (e.g., 2)")

fm = ZZFeatureMap(feature_dimension=2, reps=REPS)

def q_embed_to_probs(x_row: np.ndarray) -> np.ndarray:
    """
    TODO(you):
    - Bind x_row[0], x_row[1] to the feature map parameters.
      Hint: params_sorted = sorted(fm.parameters, key=lambda p: p.name)
      bound = fm.assign_parameters({params_sorted[0]: float(x_row[0]),
                                    params_sorted[1]: float(x_row[1])}, inplace=False)
    - Convert to statevector
    - Return np.abs(state)^2 (length 4)
    """
    # params_sorted = ...
    # bound = ...
    # sv = Statevector.from_instruction(bound)
    # return (np.abs(sv.data) ** 2).astype(np.float64)
    raise NotImplementedError("TODO(you): implement q_embed_to_probs() as described above")

# Build probability features
Xtr_qp = np.vstack([q_embed_to_probs(r) for r in X_tr])
Xte_qp = np.vstack([q_embed_to_probs(r) for r in X_te])

# Scale and learn
sc_q = StandardScaler().fit(Xtr_qp)
Xtr_q = sc_q.transform(Xtr_qp); Xte_q = sc_q.transform(Xte_qp)
clf_q = LogisticRegression(max_iter=300).fit(Xtr_q, y_tr)
acc_q = accuracy_score(y_te, clf_q.predict(Xte_q))

# --- Report ---
report = [
    "=== Hybrid Classifier (Didactic) ===",
    f"Baseline (raw features) accuracy:  {acc_b:.4f}",
    f"Quantum-encoded accuracy:          {acc_q:.4f}",
    f"Feature map reps: {REPS}",
    "Note: Using a simulator to convert quantum states into classical features.",
]
save_text("\n".join(report), "hybrid_report.txt")
print("\n".join(report))

# Optional: try SVM
# from sklearn.svm import SVC
# clf_q = SVC(kernel='rbf', C=1.0).fit(Xtr_q, y_tr)
# acc_q = accuracy_score(y_te, clf_q.predict(Xte_q))
# print("Quantum-encoded SVM accuracy:", acc_q)

print("[done] Task 5 — see outputs/task5/")
