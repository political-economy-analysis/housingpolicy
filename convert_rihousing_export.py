"""Convert the RIHousing dashboard export (Municipal.csv) into a clean UTF-8 CSV.

The Tableau export is UTF-16, tab-separated, with values like "$2,396" and "+ $212".

Usage: python3 convert_rihousing_export.py Municipal.csv rihousing_rent_survey_municipal.csv
"""
import csv, re, sys

def num(s):
    s = s.strip()
    if not s:
        return ""
    m = re.fullmatch(r"([+-])?\s*\$([\d,]+)", s)
    v = int(m.group(2).replace(",", ""))
    return -v if m.group(1) == "-" else v

lines = open(sys.argv[1], encoding="utf-16").read().splitlines()
with open(sys.argv[2], "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["municipality", "avg_rent_2025", "avg_rent_2020", "change_2020_2025"])
    for l in lines[1:]:
        p = l.split("\t") + ["", "", ""]
        w.writerow([p[0].strip(), num(p[1]), num(p[2]), num(p[3])])
