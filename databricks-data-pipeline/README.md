# Data Quality Pipeline on Databricks

Built on the Databricks TPC-H sample data (7.5 million orders).

- Data quality checks: key uniqueness, null values and orphan records across tables (0 duplicates, 0 nulls, 0 orphans in 7.5M rows)
- Three-table joins (orders, customers, nations) with revenue aggregated by nation and market segment
- Window function ranking the top 3 customers per nation
- PySpark cleaning step (deduplicate, filter nulls, derive order year) saved as a managed table
- SQL validation of the saved table: row counts and revenue by year (1992 to 1998) match the source

Tools: Databricks SQL, PySpark, Delta tables
