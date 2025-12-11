# Analyzing_Visitor_Trends-

## 1. Project Overview

This project analyses international monthly visitor arrivals using a CSV dataset (`Int_Monthly_Visitor.csv`).

The main Python script provides:

- Selection of a **year period**:
  - `1` → 1978–1987  
  - `2` → 1988–1997  
  - `3` → 1998–2007  
  - `4` → 2008–2017
- Selection of a **region**:
  - `1` → Asia  
  - `2` → Europe  
  - `3` → Others
- Data cleaning:
  - Remove commas from numeric fields
  - Replace `" na "` with missing values
  - Convert to numeric and fill missing values with `0.0`
- Filtering of data by:
  - Chosen year range
  - Chosen region
- Export of a filtered CSV file
- Calculation of total visitors per country and identification of the top countries

Unit tests are included to verify that the data file loads correctly.

---

## 2. File Structure

Suggested repository structure:

```text
.
├─ Int_Monthly_Visitor.csv      # Input data file (not included in repo)
├─ pge_project.py               # Main script with VisitorsAnalyticsUtils class
└─ test_pge_project.py          # Unit tests (Task 9)




