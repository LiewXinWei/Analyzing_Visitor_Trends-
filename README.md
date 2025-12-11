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
```
**pge_project.py**  
Contains:

- Region lists for Asia, Europe, and Others  
- `VisitorsAnalyticsUtils` class  
- Command-line entry point in the `if __name__ == "__main__":` block  

**test_pge_project.py**  
Contains:

- A `unittest` test case that imports `VisitorsAnalyticsUtils` and checks that the CSV file is loaded successfully.

---

## 3. Requirements

- **Python**: 3.8 or higher  
- **Python packages**:
  - `pandas`
  - `numpy`

Install dependencies with:

```bash
pip install pandas numpy
```

---

## 4. Dataset Description

The program expects a CSV file named `Int_Monthly_Visitor.csv` in the project root folder.

- The **first column** should contain a year/month value as text (for example, `1978 Jan`).
- The **remaining columns** should be country/region columns that match the names defined in the script:

```python
asia_regions = [' Brunei Darussalam ', ' Indonesia ', ' Malaysia ', ' Philippines ', ' Thailand ',
                ' Viet Nam ', ' Myanmar ', ' Japan ', ' Hong Kong ', ' China ',' Taiwan ',
                ' Korea, Republic Of ', ' India ', ' Pakistan ', ' Sri Lanka ',
                ' Saudi Arabia ', ' Kuwait ', ' UAE ']

europe_regions = [' United Kingdom ', ' Germany ', ' France ' , ' Italy ', ' Netherlands ',
                  ' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ',
                  ' Scandinavia ', ' CIS & Eastern Europe ']

other_regions = [' USA ', ' Canada ', ' Australia ', ' New Zealand ', ' Africa ']
```

> **Note:** The column names in the CSV (including spaces) must match these strings, because they are used directly by the cleaning and filtering logic.

---

## 5. Main Class: `VisitorsAnalyticsUtils`

### 5.1 Initialisation

```python
analytics = VisitorsAnalyticsUtils(
    file_path=None,
    year_period=None,
    region=None,
    country=None
)
```

**Key attributes:**

- `self.df` – original loaded DataFrame  
- `self.parsed_df` – filtered DataFrame  
- `self.year_period` – integer from 1 to 4  
- `self.region` – integer from 1 to 3  

---

### 5.2 `user_input()` (Task 4)

Prompts the user via the console:

```text
Enter year period (1: 1978-1987, 2: 1988-1997, 3: 1998-2007, 4: 2008-2017):
Enter region (1: Asia, 2: Europe, 3: Others):
```

Validates that both inputs are integers.

Ensures:

- `year_period` is one of `{1, 2, 3, 4}`
- `region` is one of `{1, 2, 3}`

Prints a message and stops if the input is invalid.

---

### 5.3 `loadDataFile(file_path)` (Task 6)

Loads and cleans the CSV file.

**Steps:**

1. Reads the CSV file into `self.df` using `pandas.read_csv(file_path)`.
2. Combines all region columns:

   ```python
   columns_to_clean = asia_regions + europe_regions + other_regions
   ```

3. Cleans those columns:
   - Removes commas with `replace(",", "", regex=True)`
   - Replaces `" na "` with `NaN`
   - Converts values to numeric and fills missing values with `0.0`
4. Prints:

   ```text
   **** first 5 rows of data loaded ****
   ```

5. Returns `self.df.head(5)` for preview.

If `file_path` is `None`, an error message is printed instead.

---

### 5.4 `parseData()` (Task 7)

Filters the data by the selected region and year period.

Defines a mapping of columns to drop, depending on the selected region:

```python
region_map = {
    1: europe_regions + other_regions,  # keep Asia
    2: asia_regions + other_regions,    # keep Europe
    3: asia_regions + europe_regions    # keep Others
}
```

Drops irrelevant region columns and keeps:

- The original year/month column  
- Country columns from the chosen region group  

Extracts a numeric `Year` column from the first column:

- Takes the first four characters, strips whitespace, and converts to integer.

Defines year ranges:

```python
year_ranges = {
    1: range(1978, 1988),
    2: range(1988, 1998),
    3: range(1998, 2008),
    4: range(2008, 2018),
}
```

Filters rows whose `Year` falls within the selected range.

Saves the filtered data to a CSV file with a name such as:

```text
Filtered_Region{region}_Years_{start}-{end}.csv
```

Drops the original first column (keeping only the country columns and `Year`).

Prints:

- Number of entries  
- Year range  
- `self.parsed_df.info()`  

Returns a string summary of the `Year` column statistics.

---

### 5.5 `getTop3Countries()` (Task 8)

Calculates total visitors per country over the filtered period.

- Drops the last column (the `Year` column).
- Sums values across all rows for each country column.
- Sorts the result in descending order of visitors.
- Returns the full sorted `pandas.Series` of totals.

To see the top three countries:

```python
totals = analytics.getTop3Countries()
print(totals.head(3))
```

---

## 6. How to Run

From the project root:

```bash
python pge_project.py
```

You will be prompted to enter:

- Year period (1–4)  
- Region (1–3)  

The program will then:

- Load and clean `Int_Monthly_Visitor.csv`
- Filter according to your choices
- Save a filtered CSV file
- Print a summary of the parsed data and visitor totals

---

## 7. Running Unit Tests

Make sure `test_pge_project.py` is present and run:

```bash
python -m unittest test_pge_project.py
```

This will:

- Create an instance of `VisitorsAnalyticsUtils`
- Load `Int_Monthly_Visitor.csv`
- Print the number of rows and columns loaded

---

## 8. Example Programmatic Usage

If you want to use the class from another Python script (without interactive input):

```python
from pge_project import VisitorsAnalyticsUtils

analytics = VisitorsAnalyticsUtils()
analytics.year_period = 2  # 1988–1997
analytics.region = 1       # Asia

analytics.loadDataFile("Int_Monthly_Visitor.csv")
analytics.parseData()
totals = analytics.getTop3Countries()

print("Top 3 countries by total visitors:")
print(totals.head(3))
```




