import pandas as pd
import matplotlib.pyplot as plt
import os

# 設定中文字型
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'PingFang TC', 'Heiti TC', 'sans-serif'] 
plt.rcParams['axes.unicode_minus'] = False

def plot_weekly_comparison():
    # 檔案路徑
    dorms_file = 'merged_dorms.csv'
    settlement_file = 'settlement_202601.csv'
    
    # 1. 讀取與處理宿舍資料
    df_dorms = pd.read_csv(dorms_file)
    df_dorms['Datetime'] = pd.to_datetime(df_dorms['Datetime'])
    df_dorms.set_index('Datetime', inplace=True)
    
    # 計算所有宿舍的總用電量
    # 假設所有欄位都是宿舍數據 (merged_dorms.csv 結構應該是 Datetime, dorm1, dorm2...)
    df_dorms['Total_Consumption'] = df_dorms.sum(axis=1)
    
    # 2. 讀取與處理 srPrice 資料
    df_settlement = pd.read_csv(settlement_file, header=1)
    df_settlement['Datetime'] = pd.to_datetime(df_settlement['date']) + pd.to_timedelta(df_settlement['hour'], unit='h')
    df_settlement.set_index('Datetime', inplace=True)
    sr_price = df_settlement[['srPrice']]
    
    # 3. 合併資料
    merged = df_dorms[['Total_Consumption']].join(sr_price, how='inner')
    
    # 4. 篩選特定時間範圍 (2026-01-01 ~ 2026-01-07)
    start_date = '2026-01-01'
    end_date = '2026-01-07 23:00:00'
    mask = (merged.index >= start_date) & (merged.index <= end_date)
    weekly_data = merged.loc[mask]
    
    if weekly_data.empty:
        print("警告: 該時間範圍內沒有資料。")
        return

    # 5. 繪圖
    fig, ax1 = plt.subplots(figsize=(15, 7))
    
    # 加入夜間底色 (定義夜間為 18:00 ~ 06:00)
    # 我們遍歷每一天，分別畫出 00:00-06:00 和 18:00-24:00 的區塊
    unique_dates = pd.date_range(start=weekly_data.index.min().floor('D'), end=weekly_data.index.max().ceil('D'), freq='D')
    
    for d in unique_dates:
        # 凌晨時段 (00:00 - 06:00)
        ax1.axvspan(d, d + pd.Timedelta(hours=6), facecolor='gray', alpha=0.15, edgecolor=None)
        # 晚間時段 (18:00 - 24:00)
        ax1.axvspan(d + pd.Timedelta(hours=18), d + pd.Timedelta(hours=24), facecolor='gray', alpha=0.15, edgecolor=None)

    # 左軸: 總用電量 (實線)
    color_dorm = 'tab:blue'
    ax1.set_xlabel('時間')
    ax1.set_ylabel('整體宿舍總用電量 (kW)', color=color_dorm, fontweight='bold')
    ax1.plot(weekly_data.index, weekly_data['Total_Consumption'], color=color_dorm, label='總用電量', linewidth=2.5, linestyle='-')
    ax1.tick_params(axis='y', labelcolor=color_dorm)
    ax1.grid(True, alpha=0.3)
    
    # 右軸: srPrice (實線)
    ax2 = ax1.twinx()
    color_price = 'tab:red'
    ax2.set_ylabel('srPrice (價格)', color=color_price, fontweight='bold')
    ax2.plot(weekly_data.index, weekly_data['srPrice'], color=color_price, label='srPrice', linestyle='-', marker='o', markersize=3, linewidth=2)
    ax2.tick_params(axis='y', labelcolor=color_price)
    
    plt.title('2026/01/01 - 01/07 整體宿舍用電 vs srPrice 對照圖 (灰色背景為夜間 18:00-06:00)', fontsize=14)
    
    # 合併圖例
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    # 增加一個 dummy patch 用於圖例說明夜間
    import matplotlib.patches as mpatches
    night_patch = mpatches.Patch(color='gray', alpha=0.15, label='夜間時段')
    
    ax1.legend(lines_1 + lines_2 + [night_patch], labels_1 + labels_2 + ['夜間時段'], loc='upper left')
    
    plt.tight_layout()
    
    # 存檔
    if not os.path.exists('plots'):
        os.makedirs('plots')
        
    output_img = os.path.join('plots', 'Total_Dorm_vs_srPrice_Weekly_NightShaded.png')
    plt.savefig(output_img, dpi=150)
    plt.close()
    print(f"已儲存圖表: {output_img}")

if __name__ == "__main__":
    plot_weekly_comparison()
