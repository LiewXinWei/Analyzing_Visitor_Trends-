# Task 3
import pandas as pd
import os
import numpy as np

# Task 7
asia_regions = [' Brunei Darussalam ', ' Indonesia ', ' Malaysia ', ' Philippines ', ' Thailand ',
                ' Viet Nam ', ' Myanmar ', ' Japan ', ' Hong Kong ', ' China ',' Taiwan ',
                ' Korea, Republic Of ', ' India ', ' Pakistan ', ' Sri Lanka ', ' Saudi Arabia ', ' Kuwait ', ' UAE ']
            
europe_regions = [' United Kingdom ', ' Germany ', ' France ' , ' Italy ', ' Netherlands ',
                  ' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ',
                  ' Scandinavia ', ' CIS & Eastern Europe ']
    
other_regions = [' USA ', ' Canada ', ' Australia ', ' New Zealand ', ' Africa ']

class VisitorsAnalyticsUtils:
    # Task 4 
    def __init__(self, file_path=None, year_period=None, region=None, country=None):
        self.df = None
        self.year_period = year_period
        self.region = region
        self.country = country
        self.parsed_df = None

    def user_input(self):
        while True:
            try:
                self.year_period = int(input("Enter year period (1: 1978-1987, 2: 1988-1997, 3: 1998-2007, 4: 2008-2017): "))
                if self.year_period not in {1,2,3,4}:
                    print("\nPlease enter a number from 1 to 4. Please rerun the code!")
                    return
                self.region = int(input("Enter region (1: Asia, 2: Europe, 3: Others): "))
                if self.region not in {1,2,3}:
                    print("\nPlease enter a number from 1 to 3. Please rerun the code!")
                    return
                break
            except ValueError:
                print("Please only enter Integers")
                continue

    # Task 6 
    def loadDataFile(self, file_path):
        self.df = pd.read_csv(file_path)
    
        if file_path is not None:
            print("**** first 5 rows of data loaded ****")
            columns_to_clean = asia_regions + europe_regions + other_regions
            self.df[columns_to_clean] = self.df[columns_to_clean].replace(",", "", regex=True)
            self.df = self.df.replace(" na ", np.nan)
            self.df[columns_to_clean] = self.df[columns_to_clean].apply(pd.to_numeric).fillna(0.0)
            return self.df.head(5)
        else:
            print("Error loading data in, please recheck data!")
            return

    # Task 7            
    def parseData(self):
        region_map = {1: europe_regions + other_regions, 
                      2: asia_regions + other_regions, 
                      3: asia_regions + europe_regions}
        
        if self.df is None:
            print("No data loaded")
            return

        if self.region not in region_map:
            print("No such region")
            return
    
        self.parsed_df = self.df.drop(columns=[col for col in region_map[self.region] if col in self.df.columns])
    
        self.parsed_df["Year"] = pd.to_numeric(self.parsed_df.iloc[:, 0].astype(str).str.strip().str[:4], errors="coerce")
    
        year_ranges = {1: range(1978, 1988), 2: range(1988, 1998), 3: range(1998, 2008), 4: range(2008, 2018)}
    
        if self.year_period not in year_ranges:
            print("Invalid year period. Choose between 1 to 4.")
            return
    
        self.parsed_df = self.parsed_df[self.parsed_df["Year"].isin(year_ranges[self.year_period])].reset_index(drop=True)
    
        output_filename = f"Filtered_Region{self.region}_Years_{year_ranges[self.year_period].start}-{year_ranges[self.year_period].stop-1}.csv"
        self.parsed_df.to_csv(output_filename, index=False)
    
        self.parsed_df = self.parsed_df.drop(self.parsed_df.columns[0], axis=1)
    
        print(f"Index: {self.parsed_df.shape[0]} entries, {year_ranges[self.year_period].start} Jan to {year_ranges[self.year_period].stop-1} Dec")
        print(f"Saved filtered data to: {output_filename}")
        self.parsed_df.info()
    
        return f"\n*** Parsed Data (Years) ***\n{self.parsed_df['Year'].describe()}"
        
    # Task 8        
    def getTop3Countries(self):
        self.parsed_df = self.parsed_df.drop(self.parsed_df.columns[-1], axis=1)
        region_totals = self.parsed_df.sum().sort_values(ascending=False)
        print("\n*** Top 3 countries ***")
        return region_totals


if __name__ == "__main__":
    analytics = VisitorsAnalyticsUtils()
    analytics.user_input()
    print(analytics.loadDataFile("Int_Monthly_Visitor.csv"))
    print(analytics.parseData())
    print(analytics.getTop3Countries())
