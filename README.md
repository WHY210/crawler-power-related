# Power Related Data Crawler

This project provides a comprehensive crawler for fetching power-related data, including

- Taipower generation （[台電機組過去發電量](https://data.gov.tw/dataset/37331)）
- Taipower flow data （[電力潮流](https://data.gov.tw/en/datasets/37326)）
- Taipower ancillary services settlement data（[日前輔助市場歷史結清價格與交易量](https://etp.taipower.com.tw/web/service_market/historical_settlement_trading)）
- NTU buildings demand（[台大校園數位電錶監視系統 *需在台大網域](https://epower.ga.ntu.edu.tw/?fbclid=IwAR1_crXmTrEojnqGZCh6z2hesnkZ1Bsd7YBEnyAyzEyHOoIvr-xjA8sBAqo)）
- NTU meters (not complete yet) （[台大校園數位電錶監視系統 *需在台大網域](https://epower.ga.ntu.edu.tw/?fbclid=IwAR1_crXmTrEojnqGZCh6z2hesnkZ1Bsd7YBEnyAyzEyHOoIvr-xjA8sBAqo)）

## Run

```bash
python src/run.py
```

Once executed, you will be presented with an interactive menu to select the specific data update you wish to perform:

1. Update Generator & Flow Data (Taipower)
   `python src/run.py --generators`
2. Update Settlement Data (Taipower Ancillary)
   `python src/run.py --settlement`
3. Update NTU Buildings
   `python src/run.py --buildings`data is categorized by Campus/Feeder/Subject based on Taipower metering data. Will automatically determines the last updated timestamp in your local files and only fetches new data.
4. Update NTU Meters
   `python src/run.py --meters`
5. Update PV (Manual/Selenium) *need data sources available upon request
6. Run with Custom Date Range (Historical Data Retrieval) (使用自訂日期範圍執行 - 歷史數據回補)
7. (a) Run ALL
   `python src/run.py --all`
8. (0) Exit

## File Structure

```text
data/
│ 
├──ntu_building/
│   ├── 校總區/
│   │   ├── SX65/
│   │   │   ├── 學生宿舍/
│   │   │   │   └── 女四.七舍.csv
│   │   │   └── ...
│   │   └── ...
│   └── ...
│
├──ntu_meter/
│   ├── 00A_P1_01臺大總變電站（高壓）_2026.xlsx
│   └── ...
│ 
├── taipower_flow/
│   ├── flow_2025.json
│   └── raw/       # (.gitignore)
│ 
└── taipower_generators/
    ├── generator_2025.json
    └── raw/       # (.gitignore)
```

**Note**: All CSV files are now saved with `utf-8-sig` encoding.
