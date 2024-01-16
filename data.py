import pandas 
import os 

FILE_PATH = 'data/data.csv'

# Get the absolute path to the CSV file
csv_file_path = os.path.join(os.getcwd(), FILE_PATH)

# Read the CSV file into a DataFrame
data = pandas.read_csv(csv_file_path)

# Detect and remove footer rows dynamically using the index of the first column
footer_index = data[data.iloc[:, 0] == 'footnoteSeqID'].index.max()
if pandas.notna(footer_index):
    data = data.iloc[: int(footer_index) + 1]
    
# Drop the 'footnote' column
data = data.drop(columns=['Value Footnotes'], errors='ignore')

# Filter rows based on a column value (pop >200000 in this case)
data = data[data['Value'] > 200000]

# Convert relevant columns to integers to avoid adding .0
int_columns = ['Value', 'Year']
data[int_columns] = data[int_columns].astype(int)

# Remove older data
data = data[data['Year'] > 2000]

# Add Coordinates column
data['Coordinates'] = None

# Group by 'City' and keep the row with the maximum 'Year' for each city
data = data.loc[data.groupby('City')['Year'].idxmax()]

# Save the filtered data by overwriting the original CSV file
data.to_csv(csv_file_path, index=False)

print(data)
