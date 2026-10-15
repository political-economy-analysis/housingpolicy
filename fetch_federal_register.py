"""Pull documents for one agency from the Federal Register API into a CSV (no API key needed).

Examples:
  python3 fetch_federal_register.py federal-housing-finance-agency --limit 100 --out fhfa_last100.csv
  python3 fetch_federal_register.py housing-and-urban-development-department \
      --since 2026-09-01 --until 2026-10-01 --out hud_documents.csv

Agency slugs are listed at https://www.federalregister.gov/api/v1/agencies.json
Standard library only.
"""
import argparse, csv, json, urllib.parse, urllib.request

API = "https://www.federalregister.gov/api/v1/documents.json"
FIELDS = ["publication_date", "type", "document_number", "citation", "title", "action",
          "abstract", "docket_ids", "comments_close_on", "effective_on", "html_url", "pdf_url"]

ap = argparse.ArgumentParser()
ap.add_argument("agency")
ap.add_argument("--limit", type=int, help="stop after this many documents (newest first)")
ap.add_argument("--since", help="earliest publication date, YYYY-MM-DD")
ap.add_argument("--until", help="latest publication date, YYYY-MM-DD")
ap.add_argument("--out", required=True)
a = ap.parse_args()

params = {"conditions[agencies][]": a.agency, "per_page": 100, "order": "newest", "fields[]": FIELDS}
if a.since: params["conditions[publication_date][gte]"] = a.since
if a.until: params["conditions[publication_date][lte]"] = a.until
url = API + "?" + urllib.parse.urlencode(params, doseq=True)

docs = []
while url and (a.limit is None or len(docs) < a.limit):
    page = json.load(urllib.request.urlopen(url, timeout=30))
    docs += page["results"]
    url = page.get("next_page_url")
docs = docs[:a.limit]

with open(a.out, "w", newline="") as f:
    w = csv.writer(f); w.writerow(FIELDS)
    for d in docs:
        w.writerow([("; ".join(d.get(c) or []) if c == "docket_ids" else d.get(c)) for c in FIELDS])
if docs:
    print(f"{len(docs)} documents, {docs[-1]['publication_date']} to {docs[0]['publication_date']} -> {a.out}")
else:
    print("no documents returned")
