# %matplotlib inline

import tkinter as tk
from tkinter import filedialog
import requests
import pandas as pd
import numpy as np
from datetime import datetime
import calendar

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def date_range(year):
    start_date = f"{year}/01/01"
    end_date = f"{year}/12/31"
    dates = pd.date_range(start=start_date, end=end_date).strftime("%Y/%m/%d").tolist()
    return dates

def crawl_data():
    year = year_entry.get()
    path = path_entry.get()

    if not year.isdigit() or not 1900 <= int(year) <= 2100:
        result_label.config(text="Invalid year!")
        return

    if not path:
        result_label.config(text="Please choose a path!")
        return

    arrmeter = ['00A_P1_01','01A_P1_01','01A_P1_02','01A_P1_03','01A_P1_04','01A_P1_05','01A_P1_06','01A_P1_07','01A_P1_08','01A_P1_09','01A_P1_10','01A_P1_11','01A_P1_12','01A_P1_13','01A_P1_14','01A_P1_15','01A_P1_16','01A_P1_17','01A_P1_18','01B_P1_01','01B_P1_02','01B_P1_03','01B_P1_04','01B_P1_05','01B_P1_06','01B_P1_08','01B_P1_09','01B_P1_10','01B_P1_11','01B_P1_12','01B_P1_13','01C_P1_01','01D_P1_01','01D_P1_02','01D_P1_03','01D_P1_04','01D_P1_05','01E_P1_01','01E_P1_02','01E_P1_03','01E_P1_04','01E_P1_05','01E_P1_06','01E_P1_07','01E_P1_08','01E_P1_09','01E_P1_10','01E_P1_11','01E_P1_12','01F_P1_01','01F_P1_02','01F_P1_03','01F_P1_04','01F_P1_05','01F_P1_06','01F_P1_07','01F_P1_08','01F_P1_09','01F_P1_10','01F_P1_11','01F_P1_12','01F_P1_13','01G_P1_01','01G_P1_02','01H_P1_01','01H_P1_02','01I_P1_01','01I_P1_02','01I_P1_03','01I_P1_04','01I_P1_05','01I_P1_06','01J_P1_01','01J_P1_02','01J_P1_05','01J_P1_06','01J_P1_07','01J_P1_08','01J_P1_10','01J_P1_11','01J_P1_12','01J_P1_13','01J_P1_14','01J_P1_15','01J_P1_16','01J_P1_17','01J_P1_18','01J_P1_19','01J_P1_20','01J_P2_01','01J_P2_02','01J_P2_03','01J_P2_04','01J_P2_05','01J_P2_06','01J_P2_07','01J_P2_08','01J_P2_09','01J_P2_10','01K_P1_01','01K_P1_02','01L_P1_01','01M_P1_01','01M_P1_02','01M_P1_03','01M_P1_04','01M_P1_05','01M_P1_06','01M_P1_07','01M_P1_08','01M_P1_09','01M_P1_10','01M_P1_11','01M_P1_12','01M_P1_13','01M_P1_14','01M_P1_15','01M_P2_06','01N_P1_01','01N_P1_02','01N_P1_03','01O_P1_01','01O_P1_02','01P_P1_01','01Q_P1_01','01Q_P1_02','01Q_P1_03','01S_P1_01','01T_P1_01','01T_P1_02','01T_P1_03','01T_P1_04','01T_P1_05','01U_P1_01','01U_P1_02','01V_P1_01','01W_P1_01','01W_P1_02','01W_P1_03','01W_P1_04','01W_P1_05','01W_P1_06','01W_P1_07','01W_P1_08','01W_P1_09','01W_P1_10','01W_P1_11','01Z_P1_01','01Z_P1_02','01Z_P1_03','01Z_P1_04','02A_P1_01','02A_P1_02','02A_P1_03','02A_P1_04','02A_P1_05','02A_P1_06','02A_P1_07','02A_P1_08','02A_P1_09','02A_P1_10','02A_P1_11','02A_P1_12','02A_P1_13','02A_P1_14','02A_P2_01','02A_P2_02','02A_P2_03','02A_P2_04','02A_P2_05','02A_P2_06','02A_P2_08','02A_P2_09','02A_P2_10','02A_P2_12','02A_P2_14','02A_P3_03','02A_P3_04','02A_P3_05','02A_P3_06','02A_P3_07','02A_P3_08','02A_P3_09','02A_P3_10','02A_P3_11','02A_P3_12','02A_P3_13','02A_P3_14','02A_P3_17','02A_P3_18','02A_P3_19','02A_P3_20','02A_P3_21','02C_P1_01','02C_P1_03','02C_P1_04','02C_P1_05','02C_P1_06','02C_P1_07','02C_P1_08','02C_P1_09','02C_P1_10','02C_P1_11','02C_P1_12','02C_P1_13','02C_P1_14','02C_P1_15','02C_P1_16','02C_P1_17','02C_P1_18','02C_P1_19','02C_P1_20','02D_P1_01','02D_P1_02','02D_P1_04','02D_P1_05','02D_P1_06','02D_P1_08','02D_P1_10','02D_P1_11','02D_P1_13','02D_P2_01','02D_P2_02','02D_P2_03','02D_P2_04','02D_P2_05','02D_P2_06','02D_P2_07','02D_P2_08','02D_P2_09','02D_P2_10','02D_P2_11','02D_P2_12','02D_P2_13','02D_P2_14','02E_P1_01','02E_P1_02','02E_P1_03','02E_P1_04','02E_P1_05','02E_P1_06','02E_P1_07','02E_P1_08','02E_P1_09','02E_P1_10','02E_P1_11','02E_P1_13','02E_P1_14','02E_P1_15','02E_P1_16','02E_P1_17','02E_P1_18','02E_P1_19','02E_P1_20','02E_P1_21','02E_P1_23','02E_P1_24','02E_P1_25','02E_P2_01','02E_P2_02','02E_P2_03','02E_P2_04','02E_P2_05','02E_P2_06','02E_P2_07','02E_P2_08','02E_P2_09','02E_P2_10','02E_P2_11','02E_P2_12','02E_P2_14','02E_P2_15','02E_P2_18','02E_P2_19','02E_P2_20','02E_P2_21','02E_P2_22','02E_P2_23','02E_P3_01','02E_P3_02','02E_P3_03','02E_P3_04','02E_P4_01','02E_P4_02','02E_P5_01','02E_P5_02','02E_P5_03','02E_P5_04','02F_P1_01','02F_P1_02','02F_P1_03','02F_P1_04','02F_P1_07','02F_P1_08','02F_P1_09','02F_P1_10','02F_P1_11','02F_P1_12','02F_P1_14','02F_P1_17','02F_P1_18','02F_P2_01','02F_P2_02','02F_P2_03','02F_P2_04','02F_P2_05','02F_P2_06','02F_P2_07','02F_P2_08','02F_P2_09','02F_P2_10','02F_P2_11','02F_P2_12','02F_P2_13','02F_P2_14','02F_P2_15','02F_P2_16','02F_P2_17','02F_P2_18','02H_P1_01','02H_P1_02','02H_P1_03','02H_P1_04','02H_P1_05','02H_P1_06','02H_P1_07','02H_P1_08','02H_P1_09','02H_P1_10','02H_P1_11','02H_P1_12','02H_P1_13','02H_P1_14','02H_P2_01','02H_P2_02','02H_P2_03','02H_P2_04','02H_P2_05','02H_P2_06','02H_P2_07','02H_P2_08','02H_P2_09','02H_P2_10','02H_P2_11','02H_P2_12','02H_P2_13','02H_P2_14','02H_P2_16','02H_P2_17','02H_P2_18','03A_P1_01','03A_P1_02','03A_P1_03','03A_P1_04','03A_P1_05','03A_P1_07','03A_P1_08','03A_P1_09','03A_P1_10','03A_P1_11','03A_P1_12','03A_P1_13','03A_P1_14','03B_P1_01','03B_P1_02','03B_P1_03','03B_P1_04','03B_P1_05','03B_P1_06','03B_P1_07','03B_P1_08','03B_P1_09','03B_P1_10','03B_P1_11','03C_B1_01','03C_B1_02','03C_B1_03','03C_B1_04','03C_B1_05','03C_B1_06','03C_B2_01','03C_B3_01','03D_P1_01','03D_P1_02','03D_P1_03','03D_P1_04','03D_P1_05','03D_P1_06','03D_P1_07','03D_P1_08','03D_P1_09','03D_P1_10','03D_P1_11','03D_P1_12','03D_P1_13','03D_P1_15','03D_P2_01','03D_P2_02','03D_P2_03','03D_P2_04','03D_P2_05','03D_P2_06','03E_P1_01','03E_P1_02','03E_P1_03','03E_P1_04','03E_P1_05','03E_P1_06','03E_P1_07','03E_P1_08','03E_P1_10','03E_P1_11','03E_P1_12','03E_P1_13','03E_P1_14','03E_P1_15','03E_P2_01','03E_P2_02','03E_P2_03','03E_P2_04','03E_P2_05','03E_P2_06','03E_P2_07','03E_P2_08','03E_P2_09','03E_P2_10','03E_P2_11','03E_P2_12','03E_P2_13','03E_P2_14','03E_P2_15','03E_P2_16','03E_P2_17','03F_P1_01','03F_P1_02','03F_P1_03','03F_P1_04','03F_P1_05','03F_P1_06','03F_P1_07','03F_P1_08','03F_P1_09','03F_P1_10','03F_P1_11','03F_P1_12','03G_P1_10','03G_P1_11','03G_P1_12','03G_P1_13','03G_P1_14','03G_P1_15','03G_P1_16','03G_P1_17','03G_P1_18','03G_P1_19','03G_P1_20','03G_P1_21','03G_P1_22','03G_P1_23','03G_P1_24','03G_P1_25','03H_P1_01','04B_P1_01','04B_P1_02','04B_P1_03','04B_P1_04','04B_P1_05','04B_P1_06','04C_P1_01','04D_P1_01','04E_P1_01','04E_P1_02','04E_P1_03','04E_P1_04','04E_P1_05','04F_P1_01','04G_P1_01','04H_P1_01','04J_P1_01','04J_P1_02','05A_P1_01','05A_P1_02','05B_P1_01','05C_P1_01','05C_P1_02','05C_P1_03','05C_P1_04','05C_P1_05','05C_P1_06','05C_P1_07','05C_P1_08','05D_P1_01','05D_P1_02','05D_P1_03','05D_P1_04','05E_P1_01','05E_P1_02','05E_P1_03','05E_P1_04','05E_P1_05','05F_P1_01','05F_P1_02','05F_P1_03','05F_P1_04','05F_P1_05','05F_P1_06','05G_P1_01','05G_P1_02','05G_P1_03','05G_P1_04','05G_P1_05','05G_P1_06','05H_P1_01','05H_P1_02','05H_P1_03','05J_P1_02','05J_P1_03','05J_P1_04','05J_P1_05','05J_P1_06','05J_P1_07','05J_P1_08','05J_P1_09','05J_P1_10','05J_P1_11','05J_P2_01','05J_P2_02','05J_P2_03','05J_P2_04','05J_P2_05','05J_P2_06','05J_P2_07','05J_P3_01','05J_P3_02','05J_P3_03','05J_P3_04','05J_P3_05','05J_P4_01','05J_P4_02','05J_P4_03','05J_P4_04','05J_P4_05','05J_P4_06','05J_P4_07','05J_P4_08','05J_P5_01','05J_P5_02','05J_P5_03','05J_P5_04','05J_P5_05','05J_P5_06','05J_P5_07','05J_P5_08','05J_P5_09','05J_P5_10','05J_P5_11','05J_P5_12','05J_P6_01','05J_P6_02','05J_P6_03','05J_P6_04','05J_P6_05','05J_P6_06','05J_P6_07','05J_P6_08','05J_P6_09','05J_P6_10','05J_P6_11','05J_P6_12','05J_P6_13','05J_P6_14','05J_P6_15','05K_P1_01','05K_P1_02','05K_P1_03','05K_P1_04','05K_P1_05','05K_P1_06','05K_P1_07','05K_P1_08','05K_P1_09','05K_P1_10','05K_P1_11','05K_P1_12','06A_P1_01','06B_P1_01','06C_P1_01','06D_P1_01','06D_P1_02','06D_P1_03','06D_P1_04','06D_P1_05','06D_P1_06','06E_P1_01','06F_P1_01','06F_P1_02','06G_P1_01','06H_P1_01','07A_P1_01','07A_P1_02','07A_P1_03','07A_P1_04','07B_P1_01','07B_P1_02','07B_P1_03','07E_P1_01','07E_P1_02','07E_P1_03','07E_P1_04','07E_P1_05','07F_P1_01','07F_P1_02','07F_P1_03','07F_P1_04','07G_P1_01','07G_P1_02','07H_P1_01','07H_P1_02','07H_P1_03','07H_P1_04','07H_P1_06','07H_P1_07','07H_P1_08','07H_P1_09','07H_P1_10','07H_P1_11','07H_P1_12','07H_P1_13','07H_P1_15','07H_P1_16','07H_P1_17','07H_P1_18','07H_P1_19','07H_P1_20','07H_P1_21','07H_P1_22','07H_P1_23','07I_P1_01','08D_P1_01','08D_P1_02','08D_P1_03','08D_P1_04','08D_P1_05','08D_P1_06','08E_P1_01','08E_P1_2','08F_P1_01','08F_P1_02','08F_P1_03','08F_P1_04','08F_P1_05','at4022-1_3','at4022-1_4','at4022-1_5','at5014_2','at5017_3','at5017_4','at5017_5_1','at5018_1','at5018_2','at5018_3_1']
    url = 'https://epower.ga.ntu.edu.tw/fn2/dataq.aspx'

    for meter in arrmeter:
        electric_use = []
        dates = date_range(year)
        result_label.config(text=f"Processing data for {meter} in {year}...")
        root.update()  # 强制界面更新

        step = 6 if calendar.isleap(int(year)) else 5
        for i in range(0, len(dates), step):
            time1 = dates[i] + " 00:00"
            time2 = dates[i+step-1] + " 23:00"  # Adjusted for leap year
            payload = {
                'dtype': 'h',
                'build': str(meter),
                'dt1': str(time1),
                'dt2': str(time2),
            }

            response = requests.post(url, data=payload)
            data = pd.read_html(response.text)[1]
            electric_use_temp = data.iloc[:,3].tolist()[1:]
            electric_use.extend(electric_use_temp)

        electric_use = [float(value) if isfloat(value) else -1 for value in electric_use] # np.nan
        data = pd.DataFrame(electric_use)
        data = data.rename(columns={0: meter})
        data.to_excel(f"{path}/{meter}.xlsx", index=False)

    result_label.config(text="All data saved successfully!")

def browse_path():
    path = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, path)

# Create main window
root = tk.Tk()
root.title("NTU Meter Crawler UI")

# Year input
year_label = tk.Label(root, text="Select the year:")
year_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
current_year = datetime.now().year # Define a list of years from 2014 to the previous year
years = [str(year) for year in range(2014, current_year)]
year_entry = tk.StringVar(root) # Set a tkinter variable to store the selected year
year_entry.set(str(current_year - 1))  # Set default value to the previous year
year_menu = tk.OptionMenu(root, year_entry, *years) # Create the dropdown menu for selecting the year
year_menu.grid(row=0, column=1, padx=10, pady=5)

# Path input
path_label = tk.Label(root, text="Choose save location:")
path_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
path_entry = tk.Entry(root)
path_entry.grid(row=1, column=1, padx=10, pady=5)
browse_button = tk.Button(root, text="Browse", command=browse_path)
browse_button.grid(row=1, column=2, padx=5, pady=5)

# Crawl button
crawl_button = tk.Button(root, text="Crawl Data", command=crawl_data)
crawl_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Result label
result_label = tk.Label(root, text="", fg="green")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()

