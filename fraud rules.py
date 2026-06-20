def calculate_rule_risk(amount, avg_amount, tx_count):
    risk_score = 0
    reasons = []

    if amount > avg_amount * 3:
        risk_score += 40
        reasons.append("Unusually high amount")

    if tx_count > 3:
        risk_score += 30
        reasons.append("Too many transactions quickly")

    if amount > 30000:
        risk_score += 30
        reasons.append("Very large transaction")

    return risk_score, reasons