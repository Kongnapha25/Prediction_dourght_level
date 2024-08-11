import os
import pandas as pd

csv_files = [
    r'C:\Users\ASUS\Documents\Final_project\final_project-main\final_project-main\final_project2\data\rain_csv_original\Rain-N1-2003-1998.csv',
    r'C:\Users\ASUS\Documents\Final_project\final_project-main\final_project-main\final_project2\data\rain_csv_original\Rain-N1-2013-2004.csv',
    r'C:\Users\ASUS\Documents\Final_project\final_project-main\final_project-main\final_project2\data\rain_csv_original\Rain-N1-2023-2014.csv',
    r'C:\Users\ASUS\Documents\Final_project\final_project-main\final_project-main\final_project2\data\rain_csv_original\Rain-N2-2003-1998.csv',
    r'C:\Users\ASUS\Documents\Final_project\final_project-main\final_project-main\final_project2\data\rain_csv_original\Rain-N2-2013-2004.csv',
    r'C:\Users\ASUS\Documents\Final_project\final_project-main\final_project-main\final_project2\data\rain_csv_original\Rain-N2-2023-2014.csv'
]

# Loop through each Excel file
for file_path in csv_files:
    if os.path.exists(file_path):
        try:
            # Load data from Excel
            rain = pd.read_csv(file_path)

            # Drop rows with NaN values
            rain_dropna = rain.dropna()

            # Convert 'Unnamed: 2' column to datetime and then to date
            rain_dropna.loc[:, 'Unnamed: 2'] = pd.to_datetime(rain_dropna['Unnamed: 2'], errors='coerce').dt.date

            # Rename columns
            rain_dropna.rename(columns={
                "ปริมาณฝน(มิลลิเมตร)": "no",
                "Unnamed: 1": "station",
                "Unnamed: 2": "month_year",
                "Unnamed: 3": "day1",
                "Unnamed: 4": "day2",
                "Unnamed: 5": "day3",
                "Unnamed: 6": "day4",
                "Unnamed: 7": "day5",
                "Unnamed: 8": "day6",
                "Unnamed: 9": "day7",
                "Unnamed: 10": "day8",
                "Unnamed: 11": "day9",
                "Unnamed: 12": "day10",
                "Unnamed: 13": "day11",
                "Unnamed: 14": "day12",
                "Unnamed: 15": "day13",
                "Unnamed: 16": "day14",
                "Unnamed: 17": "day15",
                "Unnamed: 18": "day16",
                "Unnamed: 19": "day17",
                "Unnamed: 20": "day18",
                "Unnamed: 21": "day19",
                "Unnamed: 22": "day20",
                "Unnamed: 23": "day21",
                "Unnamed: 24": "day22",
                "Unnamed: 25": "day23",
                "Unnamed: 26": "day24",
                "Unnamed: 27": "day25",
                "Unnamed: 28": "day26",
                "Unnamed: 29": "day27",
                "Unnamed: 30": "day28",
                "Unnamed: 31": "day29",
                "Unnamed: 32": "day30",
                "Unnamed: 33": "day31",
                "Unnamed: 34": "sum",
            }, inplace=True)

            # Split 'station' column by '-' and create new columns 'station_id' and 'station_name'
            rain_dropna[['station_id', 'station_name']] = rain_dropna['station'].str.split('-', expand=True)

            # Drop 'station' column as it's no longer needed
            rain_dropna = rain_dropna.drop(columns=['station'])

            # Convert 'month_year' column to "01-1998" format using .strftime(), handling NaT values
            rain_dropna['month_year'] = rain_dropna['month_year'].apply(lambda x: x.strftime('%m-%Y') if pd.notna(x) else 'NaT')

            # Reorder columns
            new_columns = ['no', 'station_id', 'station_name', 'month_year', 'day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7',
                        'day8', 'day9', 'day10', 'day11', 'day12', 'day13', 'day14', 'day15', 'day16', 'day17', 'day18', 'day19',
                        'day20', 'day21', 'day22', 'day23', 'day24', 'day25', 'day26', 'day27', 'day28', 'day29', 'day30', 'day31', 'sum']
            rain_dropna = rain_dropna[new_columns]

            # Replace '-' and 'T' with 0 in all columns
            for col in rain_dropna.columns:
                rain_dropna.loc[:, col] = rain_dropna[col].apply(lambda x: 0 if x == '-' or x == 'T' else x)

            # Print first 10 rows of processed DataFrame
            print(rain_dropna.head(10))

            # Create folder for saving Excel files if it doesn't exist
            #save_folder_path = r'C:\Users\ASUS\Documents\Final_project\data\save_excel'
            #os.makedirs(save_folder_path, exist_ok=True)

            #  Generate file name for outputExcel file
            #file_name = os.path.basename(file_path).replace('.csv', '.xlsx')
            #excel_file_path = os.path.join(save_folder_path, file_name)

            # Save processed DataFrame to Excel file
           #rain_dropna.to_excel(excel_file_path, index=False, engine='openpyxl')
           # print(f"DataFrame saved to: {excel_file_path}")

            # Create folder for saving CSV files if it doesn't exist
            save_folder_path = r'C:\Users\ASUS\Documents\Final_project\data\save_csv'
            os.makedirs(save_folder_path, exist_ok=True)

            # Generate file name for output CSV file
            file_name = os.path.basename(file_path).replace('.xlsx', '.csv')  # Replace the extension
            csv_file_path = os.path.join(save_folder_path, file_name)

            # Save processed DataFrame to CSV file
            rain_dropna.to_csv(csv_file_path, index=False, encoding='utf-8-sig')
            print(f"DataFrame saved to: {csv_file_path}")

        except FileNotFoundError as e:
            print(f"Error: {e}")
            print(f"File not found: {file_path}")
    else:
        print(f"File not found: {file_path}")
