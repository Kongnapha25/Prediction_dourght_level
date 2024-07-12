import pandas as pd
import os

# กำหนดเส้นทางไฟล์ Excel
excel_files = [
    r'C:\Users\ASUS\Documents\Final_project\final_project-main\final_project-main\final_project2\data\save_rain_clean_excel\Rain-N1-2003-1998.xlsx',
    r'C:\Users\ASUS\Documents\Final_project\final_project-main\final_project-main\final_project2\data\save_rain_clean_excel\Rain-N2-2003-1998.xlsx',
    r'C:\Users\ASUS\Documents\Final_project\final_project-main\final_project-main\final_project2\data\save_rain_clean_excel\Rain-N1-2013-2004.xlsx',
    r'C:\Users\ASUS\Documents\Final_project\final_project-main\final_project-main\final_project2\data\save_rain_clean_excel\Rain-N2-2013-2004.xlsx',
    r'C:\Users\ASUS\Documents\Final_project\final_project-main\final_project-main\final_project2\data\save_rain_clean_excel\Rain-N1-2023-2014.xlsx',
    r'C:\Users\ASUS\Documents\Final_project\final_project-main\final_project-main\final_project2\data\save_rain_clean_excel\Rain-N2-2023-2014.xlsx'
]

# สร้าง DataFrame ว่างเพื่อเก็บข้อมูลที่รวมแล้ว
combined_df = pd.DataFrame()

# อ่านไฟล์ Excel และรวมเข้ากับ DataFrame
for file in excel_files:
    df = pd.read_excel(file)
    combined_df = pd.concat([combined_df, df], ignore_index=True)

# เรียงลำดับข้อมูลในคอลัมน์ "no" ใหม่
combined_df['no'] = range(1, len(combined_df) + 1)

# กำหนดเส้นทางในการบันทึกไฟล์
output_folder = r'data\save_rain_clean_excel\sumfile_rain'
os.makedirs(output_folder, exist_ok=True)  # สร้างโฟลเดอร์ถ้ายังไม่มี

output_file = os.path.join(output_folder, 'combined_rain_data.xlsx')

# บันทึก DataFrame ที่รวมแล้วเป็นไฟล์ Excel
combined_df.to_excel(output_file, index=False)

print(f"ไฟล์ที่รวมและเรียงลำดับแล้วถูกบันทึกที่: {output_file}")