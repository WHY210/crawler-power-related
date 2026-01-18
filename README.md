# Power Related Data Crawler

This project provides a comprehensive crawler for fetching power-related data, including 

- Taipower generation （[台電機組過去發電量](https://data.gov.tw/dataset/37331)）
- Taipower flow data （[電力潮流](https://data.gov.tw/en/datasets/37326)）
- Taipower ancillary services settlement data（[日前輔助市場歷史結清價格與交易量](https://etp.taipower.com.tw/web/service_market/historical_settlement_trading)）
- NTU buildings demand（[台大數位電錶 *需在台大網域](https://epower.ga.ntu.edu.tw/?fbclid=IwAR1_crXmTrEojnqGZCh6z2hesnkZ1Bsd7YBEnyAyzEyHOoIvr-xjA8sBAqo)）
- NTU meters (not complete yet)

## Run

```bash
python src/run.py
```

Once executed, you will be presented with an interactive menu to select the specific data update you wish to perform:

1. Update Generator & Flow Data (Taipower)
2. Update Settlement Data (Taipower Ancillary)
3. Update NTU Buildings
   1. data is now aggregated into larger, category-specific CSV files
   2. automatically determines the last updated timestamp in your local files and only fetches new data
4. Update NTU Meters
5. Update PV (Manual/Selenium) *need data sources available upon request
6. Run with Custom Date Range (Historical Data Retrieval) (使用自訂日期範圍執行 - 歷史數據回補)
7. Run ALL
8. Exit (離開)

```text
data/ntu_power/
├── 行政.csv    # 圖書館、行政大樓...
├── 宿舍.csv    # 男一舍、女九舍...
├── 系館.csv    # 電機館、化學館...
├── 體育.csv    # 所有體育設施
└── 其他.csv    # 其他雜項設施
```

**Note**: All CSV files are now saved with `utf-8-sig` encoding.


## Advanced Usage

`python src/run.py --all`

`python src/run.py --buildings`

`python src/run.py --generators`

`python src/run.py --settlement`

`python src/run.py --meters`
