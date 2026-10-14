"""Pull ACS 1-year rent burden (B25070) for Providence city and the Providence-Warwick MSA.

Usage: CENSUS_API_KEY=... python3 fetch_acs_rent_burden.py
"""
import csv, json, os, urllib.parse, urllib.request

KEY = os.environ["CENSUS_API_KEY"]
YEARS = [2019, 2021, 2022, 2023, 2024]  # no 2020 1-year release
GEOS = {
    "Providence city, RI": "for=place:59000&in=state:44",
    "Providence-Warwick, RI-MA Metro Area": "for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:39300",
}
VARS = ["B25070_001E", "B25070_002E", "B25070_003E", "B25070_004E", "B25070_005E",
        "B25070_006E", "B25070_007E", "B25070_008E", "B25070_009E", "B25070_010E",
        "B25070_011E", "B25064_001E", "B25003_003E"]
rows = []
for y in YEARS:
    for name, geo in GEOS.items():
        url = f"https://api.census.gov/data/{y}/acs/acs1?get=NAME,{','.join(VARS)}&{geo}&key={KEY}"
        try:
            d = json.load(urllib.request.urlopen(url, timeout=30))
        except Exception as e:
            print("skip", y, name, e); continue
        r = dict(zip(d[0], d[1])); r["year"] = y
        n = {v: int(r[v]) for v in VARS if r[v] is not None and int(r[v]) >= 0}
        total = n["B25070_001E"]; notcomp = n["B25070_011E"]
        burdened = sum(n[f"B25070_{i:03d}E"] for i in (7, 8, 9, 10))
        severe = n["B25070_010E"]
        base = total - notcomp
        rows.append({"year": y, "geography": r["NAME"], "renter_households": total,
                     "not_computed": notcomp, "cost_burdened_30plus": burdened,
                     "severely_burdened_50plus": severe,
                     "pct_cost_burdened": round(100 * burdened / base, 1),
                     "pct_severely_burdened": round(100 * severe / base, 1),
                     "median_gross_rent": n.get("B25064_001E"),
                     **{v: r[v] for v in VARS[:11]}})
with open("acs_rent_burden_providence.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for r in rows: print(r["year"], r["geography"], r["pct_cost_burdened"], r["pct_severely_burdened"], r["median_gross_rent"])
