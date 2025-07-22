# Task 9
import unittest
from pge_project import VisitorsAnalyticsUtils

class TestLoadDataFile(unittest.TestCase):
    def test_load_data_shape(self):
        analytics = VisitorsAnalyticsUtils()
        df = analytics.loadDataFile("Int_Monthly_Visitor.csv")

        rows, cols = analytics.df.shape

        print("Number of Columns")
        print(cols)
        print("Number of Rows")
        print(rows)

if __name__ == "__main__":
    unittest.main()

