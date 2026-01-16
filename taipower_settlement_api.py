import requests
import pandas as pd
from datetime import datetime, timedelta
import time

API_URL = "https://etp.taipower.com.tw/api/infoboard/settle_value/query"


def daterange(start, end):
    s = datetime.strptime(start, "%Y-%m-%d").date()
    e = datetime.strptime(end, "%Y-%m-%d").date()
    d = s
    while d <= e:
        yield d.strftime("%Y-%m-%d")
        d += timedelta(days=1)


def fetch_one_day(date_str, sleep_sec=0.3):
    resp = requests.get(API_URL, params={"startDate": date_str}, timeout=20)
    resp.raise_for_status()
    obj = resp.json()

    # ✅ 正確取出 24 小時資料
    data = obj.get("data")
    if not isinstance(data, list) or len(data) != 24:
        raise ValueError(f"{date_str} unexpected data format")

    rows = []
    for i, row in enumerate(data):
        out = {
            "date": date_str,
            "hour": f"{i:02d}",
        }
        for k, v in row.items():
            out[k] = v
        rows.append(out)

    time.sleep(sleep_sec)
    return rows


def main(start_date, end_date, out_csv):
    all_rows = []

    for d in daterange(start_date, end_date):
        try:
            print("[INFO] fetching", d, flush=True)
            rows = fetch_one_day(d)
            all_rows.extend(rows)
            print(f"[OK] {d} -> {len(rows)} rows", flush=True)
        except Exception as e:
            print(f"[ERROR] {d}: {e}", flush=True)

    if not all_rows:
        print("[FATAL] no data fetched, abort")
        return

    df = pd.DataFrame(all_rows)
    df.sort_values(["date", "hour"], inplace=True)
    df.to_csv(out_csv, index=False, encoding="utf-8-sig")

    print("[DONE] total rows:", len(df))
    print("[DONE] saved to:", out_csv)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 4:
        print("Usage: python taipower_settlement_api.py <start_date> <end_date> <out_csv>")
        raise SystemExit(1)

    main(sys.argv[1], sys.argv[2], sys.argv[3])
