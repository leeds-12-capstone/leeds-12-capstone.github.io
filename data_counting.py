import pandas as pd

# File paths
file1 = "/Users/josephallred/Dropbox/Students Share/Data/Matching Financial Analysts/Data/Brokerage_Analystname.csv"
file2 = "/Users/josephallred/Dropbox/Students Share/Data/Matching Financial Analysts/Data/LSEG Workspace Brokerage-Analyst Names/LSEG_Oct24_report-brokerage-analyst.csv"

# Read the CSV files
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Get number of unique entries
unique_estimids = df1['ESTIMID'].nunique()
unique_contributors = df2['Contributor'].nunique()
unique_analysts = df2['Analysts'].nunique()

# Print results
print(f"Number of unique ESTIMID entries: {unique_estimids}")
print(f"Number of unique Contributor entries: {unique_contributors}")
print(f"Number of unique Analysts entries: {unique_analysts}")