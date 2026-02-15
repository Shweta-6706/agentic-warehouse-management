# Agentic Warehouse Management System

An engineered warehouse decision-support system that forecasts demand, optimizes inventory levels, ranks SKU risk, and generates deterministic stock recommendations using classical supply chain models and structured decision logic.

# Overview

This project implements a modular warehouse optimization engine that simulates how modern supply chains manage inventory risk.

The system:
* Processes structured product datasets (CSV)
* Forecasts demand using statistical methods
* Computes Reorder Point (ROP) and Economic Order Quantity (EOQ)
* Detects stockout and overstock risks
* Ranks products by operational urgency
* Supports scenario-based “what-if” simulations
* Generates exportable priority reports
* Includes automated unit tests

The decision engine runs deterministically and does not rely on LLM outputs for stock optimization.


# Problem Statement

Warehouses commonly struggle with:
* Stockouts caused by inaccurate demand estimation
* Overstocking leading to excessive holding costs
* Delayed prioritization of high-risk SKUs
* Inability to simulate supply chain disruptions

This system addresses these issues through structured forecasting, optimization models, and agent-based decision scoring.

## Core Features

# 1. Demand Forecasting Module
Implements statistical demand analysis:

* Moving Average Forecasting
* Volatility (standard deviation) measurement
* Demand growth rate detection

These metrics drive downstream optimization decisions.

# 2. Inventory Optimization Engine

Implements classical inventory control models:

Reorder Point (ROP)
Reorder Point = (Average Demand × Lead Time) + Safety Stock

Economic Order Quantity (EOQ)
EOQ = √(2DS / H)

Where:
* D = Annual demand
* S = Ordering cost
* H = Holding cost

These formulas are implemented directly in code and validated via automated tests.

# 3. Agentic Decision Logic

The decision layer evaluates:
* Forecasted demand
* Stock depletion timeline
* Demand volatility
* Growth trends
* Reorder thresholds

Each SKU is classified into:
* Safe
* Warning
* Critical

A dynamic priority score is computed to rank products by urgency.

# 4. Warehouse Ranking Engine

Instead of analyzing a single product, the system:

* Iterates across all SKUs
* Computes forecast + optimization metrics
* Assigns risk levels
* Sorts by priority score
* Outputs top critical products

This simulates a real operations dashboard backend.

# 5. What-If Simulation Engine

Supports scenario modeling:

* Demand increase/decrease %
* Lead time delays
* Demand spikes
* Supply disruption simulation

The system recalculates forecasts and optimization metrics dynamically.

# Example Output
WAREHOUSE PRIORITY REPORT

{'product_id': 'P039', 'priority_score': 86.1, 'risk_level': 'CRITICAL', 'depletion_days': 2.85, 'recommended_order_qty': 1857}
{'product_id': 'P038', 'priority_score': 85.07, 'risk_level': 'CRITICAL', 'depletion_days': 1.86, 'recommended_order_qty': 1630}

A full ranked report is automatically exported to:
warehouse_priority_report.csv

# System Architecture

User Input (CLI arguments)
↓
Data Loader
↓
Forecasting Module
↓
Optimization Engine
↓
Agent Decision Layer
↓
Ranking & Report Generation


# Project Structure
warehouse-agent/
│
├── main.py
├── data/
├── src/
│   ├── data_loader.py
│   ├── forecasting.py
│   ├── optimization.py
│   ├── agent.py
│   └── simulation.py
│
├── tests/
│   ├── test_forecasting.py
│   └── test_optimization.py
│
├── requirements.txt
└── README.md

# Installation
git clone https://github.com/your-username/warehouse-agent.git
cd warehouse-agent
pip install -r requirements.txt

# Running the System

Basic execution:
python main.py

With scenario simulation:
python main.py --demand_increase 20 --lead_delay 3 --spike

This will:

* Analyze all products
* Rank by priority
* Print top critical SKUs
* Export a full CSV report

# Running tests

python -m pytest

Example output:
3 passed in 0.11s

Automated tests validate:
* Forecasting logic
* EOQ computation
* Deterministic behavior

---

# Technology stack

| Component       | Technology                    |
| --------------- | ----------------------------- |
| Language        | Python                        |
| Data Processing | Pandas, NumPy                 |
| Forecasting     | Statistical Models            |
| Optimization    | Mathematical Inventory Models |
| Testing         | Pytest                        |
| Interface       | CLI-based                     |

---

# AI Usage Statement
AI tools were used as a learning and development assistant during the project.

All forecasting logic, inventory formulas, decision scoring, simulation logic, and ranking systems were implemented manually and validated through deterministic testing.

The core decision engine does not depend on LLM-generated outputs.


# Business Impact
This system enables:

* Reduced stockout probability
* Lower holding costs
* SKU prioritization
* Scenario-based planning
* Faster operational decisions

The underlying principles align with supply chain optimization techniques used in large-scale retail and logistics operations.

# Future Improvements
* ARIMA or LSTM forecasting models
* Multi-warehouse coordination
* Real-time API ingestion
* Web-based dashboard interface
* Cloud deployment

# License
Built for educational and research purposes.

