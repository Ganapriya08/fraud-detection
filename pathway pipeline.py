import pathway as pw
import numpy as np
from sklearn.ensemble import IsolationForest
from fraud_rules import calculate_rule_risk

# ---------------- ML MODEL SETUP ---------------- #

# Train simple model on normal transaction behaviour
normal_data = np.array([[1000], [2000], [3000], [4000], [5000]])
model = IsolationForest(contamination=0.1)
model.fit(normal_data)

# ---------------- PATHWAY ---------------- #

class TransactionSchema(pw.Schema):
    user_id: str
    amount: float
    location: str
    timestamp: str

transactions = pw.io.csv.read(
    "transactions.csv",
    schema=TransactionSchema,
    mode="streaming"
)

# User statistics
user_stats = transactions.groupby(transactions.user_id).reduce(
    avg_amount=pw.reducers.mean(transactions.amount),
    tx_count=pw.reducers.count()
)

joined = transactions.join(
    user_stats,
    transactions.user_id == user_stats.user_id
)

# Fraud detection logic
def detect_fraud(amount, avg_amount, tx_count):
    # Rule-based risk
    rule_risk, reasons = calculate_rule_risk(amount, avg_amount, tx_count)

    # ML anomaly detection
    prediction = model.predict([[amount]])

    if prediction[0] == -1:
        rule_risk += 40
        reasons.append("ML anomaly detected")

    status = "FRAUD" if rule_risk >= 70 else "NORMAL"

    return status, rule_risk, ", ".join(reasons) if reasons else "Safe"

results = joined.select(
    joined.user_id,
    joined.amount,
    joined.location,
    joined.timestamp,
    *pw.apply(
        detect_fraud,
        joined.amount,
        joined.avg_amount,
        joined.tx_count
    ).alias("status", "risk_score", "reason")
)

pw.io.csv.write(results, "fraud_results.csv")

pw.run()