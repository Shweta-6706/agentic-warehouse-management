System Architecture

Overview
The Agentic Warehouse Management System is a modular, deterministic decision-support engine designed for inventory risk analysis and stock optimization.
The architecture separates forecasting, optimization, and decision logic into independent modules for maintainability and scalability.

High-Level Flow--

User Input (CLI Arguments)
↓
Data Loader
↓
Forecasting Module
↓
Optimization Engine
↓
Agent Decision Layer
↓
Warehouse Ranking Engine
↓
Report Generation (Console + CSV)

Design Principles
1.Deterministic decision logic (no black-box dependency)
2.Modular architecture for extensibility
3.Separation of concerns
4.Testable business logic
5.Reproducible outputs

Module Responsibilities
1. data_loader.py
Reads CSV dataset
Parses historical demand
Ensures structured DataFrame format

2. forecasting.py
Moving average forecast
Volatility computation
Demand growth calculation

3. optimization.py
Safety stock computation
Reorder point calculation
EOQ formula implementation
Depletion time estimation

4. agent.py
Risk classification
Priority scoring
Recommendation logic

5. simulation.py
Demand adjustments
Lead time delays
Spike modeling
Scalability Considerations

The system can be extended with:
ARIMA/LSTM models
Multi-warehouse support
REST API interface
Dashboard visualization layer
