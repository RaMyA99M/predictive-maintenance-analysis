# predictive-maintenance-analysis
SQL and Python analysis of machine failure data for predictive maintenance insights

## Overview
This project analyzes machine sensor and operational data to identify failure patterns and operational risk factors.

## Business Problem
Unexpected machine failures increase downtime and maintenance cost. The goal of this analysis was to quantify failure rates, identify high-risk conditions, and support data-driven maintenance decisions.

## Dataset
Predictive Maintenance Classification Dataset (Kaggle)

## Tools Used
- SQL (SQLite)
- Python (pandas, matplotlib)
- Jupyter Notebook

## Key Analysis
- Calculated overall and segmented failure rates using SQL
- Compared operating parameters for failed vs non-failed cases
- Visualized failure trends and risk indicators in Python

## Key Insights
- Certain machine types show consistently higher failure rates
- Failed cases exhibit higher tool wear and torque on average
- Early monitoring of wear metrics could reduce unexpected failures

## Recommendations
- Implement threshold-based monitoring for tool wear
- Prioritize preventive maintenance for high-risk machine types
