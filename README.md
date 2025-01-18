# Project: Kingfisher Data Pipeline and Analysis

This repository contains a complete data pipeline to parse, store, and analyze product data from the [Kingfisher](https://kingfisher.kz/) online store. The project is divided into three main components:

- **Parser**: A Jupyter Notebook for web scraping.
- **Uploader**: A Python script to transfer the parsed data to a PostgreSQL database.
- **Analysis**: A Jupyter Notebook for data cleaning, visualization, and analysis.

---

## Folder Structure

```
repo/
|
|-- parser/
|   \-- Dual_Task.ipynb         # Jupyter Notebook for web scraping the online store.
|
|-- uploader/
|   \-- from_site_to_postgre.py # Python script to upload CSV data to PostgreSQL.
|
|-- analysis/
    |-- Analysis.ipynb          # Jupyter Notebook for data analysis and visualization.
    |-- avg_price.png           # Visualization of average prices.
    |-- price_distribution.png  # Visualization of price distribution.
    |-- price_range.png         # Visualization of price ranges.
```

---

## Parser

The **parser** folder contains the `Dual_Task.ipynb` notebook, which scrapes data from the [Kingfisher](https://kingfisher.kz/) website. This script captures product details such as:

- Product Name
- Category
- Price
- City

The parsed data is saved in a CSV file for further processing.

---

## Uploader

The **uploader** folder contains the `from_site_to_postgre.py` script, which uploads the parsed CSV data to a PostgreSQL database. The process uses Docker to set up the PostgreSQL instance. Below are the steps to replicate this setup:

### Step 1: Start PostgreSQL with Docker

Run the following command to start a PostgreSQL container:
```bash
docker run --name dual-test -e POSTGRES_PASSWORD=mysecretkey -p 5431:5432 -d postgres
```

### Step 2: Connect to PostgreSQL

Connect to the PostgreSQL instance:
```bash
psql -h localhost -p 5431 -U postgres
```

### Step 3: Create Database and Table

Inside the PostgreSQL console, run the following commands to create the database and table:

```sql
CREATE DATABASE kingfisher_data;

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    price VARCHAR(50) NOT NULL,
    city VARCHAR(100) NOT NULL
);
```

---

## Analysis

The **analysis** folder contains the `Analysis.ipynb` notebook, which performs data cleaning, visualization, and statistical analysis. Key steps include:

1. **Cleaning the Price Data**:
   - The parsed prices contained a "T" character (e.g., `10,000T`).
   - These "T" characters were removed to convert the prices into numeric data types for analysis.

2. **Visualization**:
   - `avg_price.png`: Displays average product prices.
   - `price_distribution.png`: Shows the distribution of product prices.
   - `price_range.png`: Highlights the range of prices across categories.

---

## Requirements

To replicate this project, install the following:

- Python 3.x
- Jupyter Notebook
- Docker
- PostgreSQL
- Required Python libraries (install using `pip`):
  ```bash
  pip install pandas numpy matplotlib seaborn psycopg2
  ```

---

## How to Use

1. **Run the Parser**:
   - Navigate to the `parser` folder.
   - Open `Dual_Task.ipynb` in Jupyter Notebook and run the code to scrape data.

2. **Upload Data to PostgreSQL**:
   - Navigate to the `uploader` folder.
   - Run the `from_site_to_postgre.py` script to upload the CSV data.

3. **Analyze Data**:
   - Navigate to the `analysis` folder.
   - Open `Analysis.ipynb` in Jupyter Notebook and run the code to analyze and visualize the data.

---

## Notes

- Ensure Docker is installed and running before starting the PostgreSQL container.
- Do not expose sensitive information such as database passwords or ports.
- The parsed price data may require additional cleaning (e.g., handling "T" characters).

---

## License

This project is licensed under the MIT License.

