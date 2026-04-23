# Advanced E-commerce Data Engineering Project

This project demonstrates a modular, production-ready data engineering pipeline for e-commerce analytics. It supports large datasets (Kaggle, API, MySQL, CSV, JSON), advanced ETL, and analytics in Jupyter notebooks.

## Structure
- `src/etl/` - ETL modules (MySQL, CSV, JSON, Kaggle, API)
- `notebooks/` - Jupyter notebooks for analytics
- `config/` - Configuration files
- `data/` - Place large e-commerce datasets here
- `tests/` - Unit and integration tests

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure your MySQL connection in `config/db_config.yaml`.
3. Download a Kaggle e-commerce dataset (e.g., [Kaggle E-Commerce Data](https://www.kaggle.com/datasets)) and place it in `data/`.

## Usage
- Run the main pipeline:
  ```bash
  python src/main.py
  ```
- Run Jupyter analytics:
  ```bash
  jupyter notebook notebooks/ecommerce_analytics.ipynb
  ```

## Features
- Ingest from MySQL, CSV, JSON, Kaggle, and public APIs
- Advanced data transformation and analytics
- Write results to MySQL or data warehouse
- Jupyter notebooks for reporting and visualization
- Modular, extensible, and production-ready design
