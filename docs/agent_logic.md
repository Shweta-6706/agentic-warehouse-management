Agent Decision Layer

Objective:
Convert numerical metrics into actionable decisions.
Risk Classification

Products are categorized as:
Safe → Stock comfortably above ROP
Warning → Approaching ROP
Critical → Below ROP

Priority Score Calculation:-

Priority score incorporates:
Depletion urgency
Demand volatility
Growth rate

Higher score = higher operational urgency

Warehouse Ranking
All SKUs are evaluated and sorted:
ranked = sorted(products, key=priority_score, reverse=True)
This allows decision-makers to focus on the top-risk products first.

Deterministic Agent Design:
This agent does not rely on LLM reasoning.

Instead, it uses:
Structured thresholds
Mathematical models
Explicit scoring rules

This ensures reproducibility and auditability.
