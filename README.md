# Omnichannel Retail Sales and Inventory Analytics Dashboard

## 📌 Project Overview
This project aims to build an end-to-end data analytics pipeline that unifies fragmented data from offline Point of Sale (POS) systems and online storefronts. The goal is to provide actionable business intelligence to optimize inventory turnover and targeted marketing.

## 🛠 Tech Stack
- **Language:** Python 3.x
- **Libraries:** Pandas, NumPy (for data cleaning)
- **Database:** SQL (MySQL/PostgreSQL)
- **Visualization:** Power BI / Tableau
- **Version Control:** Git & GitHub

## 📂 Project Structure
- `/data`: Raw and cleaned datasets.
- `/notebooks`: Jupyter notebooks for data cleaning and EDA.
- `/sql_scripts`: SQL queries for metric extraction.
- `/reports`: Final business insights and PDF report.

- [x] ## 🧹 Data Cleaning Log (Week 1)
To ensure data integrity, the following cleaning steps were performed on the raw datasets:

1. **Data Integration:** Unified `pos_sales.csv` and `online_sales.csv` into a single master dataframe to create an omnichannel view.
2. **Handling Missing Values:** Identified NULL values in the `order_id` column and removed them as they were critical for transaction tracking.
3. **Duplicate Removal:** Detected and removed duplicate records to prevent the overestimation of total revenue.
4. **Temporal Standardization:** Converted `timestamp` strings into `datetime` objects to enable time-series analysis.
5. **Outlier Treatment:** Identified extreme price outliers (e.g., $99,999) using distribution analysis and removed them to prevent skewing the Average Order Value (AOV).
6. - **Transformations:** 
    - Converted `timestamp` to datetime objects.
    - Engineered `sales` column (`quantity * price`).
    - Extracted `month` and `year` for seasonality and YoY analysis.
 7. - Exported final cleaned master dataset.
- [ ] **Week 2: SQL Database Design & Aggregations** (Upcoming ⏳)
- [ ] **Week 3: Dashboard Architecture & Visualization** (Upcoming ⏳)
- [ ] **Week 4: Final Insights & Business Reporting** (Upcoming ⏳)
      
      
         
