# NYC Payroll Data Analysis

This project sets up an environment to analyze **NYC Payroll data**. The goal is to explore trends, visualize distributions, and create reproducible analyses using Python.  

## Project 
- looking at basic trends 
- looking at overtime statistics
## Dataset

- The full NYC Payroll dataset is **publicly available** via [NYC Open Data](https://data.cityofnewyork.us/).  
- The full dataset (~395 MB) is **excluded from the repository** due to GitHub file size limits.  
- A small **stratified sample** (`nyc_payroll_sample.csv`) is included for reproducibility and allows the analysis to run locally.  
- The sampling preserves distributions across **Fiscal Year** and **Agency Name**.

## Environment

- The project uses a **Python virtual environment** (`venv/`) to manage dependencies.  
- Required packages are listed in `requirements.txt`. Install with:

```bash
pip install -r requirements.txt