import pandas as pd

# Load the Excel file using raw string to avoid unicode escape errors
file_path = r'data/save_rain_clean_excel/sumfile_rain/combined_rain_data.xlsx'
rain_data = pd.read_excel(file_path, sheet_name='Sheet1')

# Ensure 'sum' column is numeric
rain_data['sum'] = pd.to_numeric(rain_data['sum'], errors='coerce')

# Calculate mean and standard deviation
mean_rainfall = rain_data['sum'].mean()
std_rainfall = rain_data['sum'].std()

# Calculate SPI
rain_data['SPI'] = (rain_data['sum'] - mean_rainfall) / std_rainfall

# Display the first few rows with the SPI column
print(rain_data[['no', 'station_id', 'station_name', 'month_year', 'sum', 'SPI']].head(30))
