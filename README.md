**Prof. Zhang—Individual Policy Analysis**

**Last updated: September 30, 2026**

**Alexander McAllister**

**Providence Rental Market**

**Step 1: Define the problem.** 

Home prices around the country have risen a dramatic 54% (JCHS 2026) since 2020, following these increases in real estate is an increase in the costs of renting. An estimated 49.9% of renters in the Providence-Warwick RI-MA Metropolitan Statistical Area (CBSA 39300) are cost burdened, defined as paying over 30% of their monthly income on housing. Too many residents are being strained by the increasing difficulty of meeting housing payments.

**Step 2: Assemble some evidence.** 

- Home price costs per month compound with the higher sale price to lead to an 84% increase in monthly homeownership expenses. JCHS State of the Nation’s Housing 2026 [link](https://www.jchs.harvard.edu/state-nations-housing-2026)

- Market yield on a 30 yr us treasury current at 5.3% Fred St louis [link](https://fred.stlouisfed.org/series/dgs30)

- 30 yr fixed rated mortgage at 6.95% Freddie Mac [link](https://www.freddiemac.com/pmms?gad_source=1&gad_campaignid=23396332682&gbraid=0AAAAA-zPkSrIk201EN21nq_kplAH0Ct3E&gclid=Cj0KCQjw8c3VBhCsARIsAA_xJ91xnAz3wDVt7hx9Uq0kDmhGCtbxbnyH2dd_c_w30CSdsCku9ipIihwaAklREALw_wcB)

- Bipartisan housing bill passes see Bipartisan Policy Center [link](https://bipartisanpolicy.org/issue-brief/inside-the-deal-whats-in-the-final-21st-century-road-to-housing-act/)

- Permitting costs key to driving home building costs and delaying projects [link](https://www.nahb.org/advocacy/top-priorities/solving-the-housing-affordability-crisis/housing-affordability-blueprint)

- Census data Providence MSA [link](https://www.census.gov/quickfacts/fact/table/providencecityrhodeisland/PST045225)

- Providence City Local Datasets [link](https://data.providenceri.gov/)

- Federal reserve FRED data for Prov-Warwick MSA [link](https://fred.stlouisfed.org/categories/30880)

- Harvard Joint Center for Housing Studies State of the Nations Housing 2026 [link](https://www.jchs.harvard.edu/state-nations-housing-2026)

- Comparative data from New York compiled by NYU’s Furman Center [link](https://www.furmancenter.org/data-tools-resources/)

**Step 3: Construct the alternatives.** Name at least three distinct policy solutions that could also solve the problem you stated in step one.

- **Option 1—**Through a coalition of local and state governments implement a patchwork of deregulatory laws that lower building costs and speed of development for multifamily units.

- **Option 2—**Implement rent controls through local legislation.

- **Option 3—**Seek public funds and private investment to renovate the many old industrial and vacant buildings for affordable housing.

**Step 4: Select the criteria.** What criteria do you think should be applied for choosing among them?

- Minimize the number of renters facing housing cost burdens.

- Maximize the available supply of high-quality affordable units.

- Maximize efficiency by deregulating cumbersome and outdated laws that increase building costs.

- Maximize economies of scale that may lower costs.

- Prioritize redistributive measures that provide inclusive prosperity.

**Step 5: Project the outcomes.** 

**Step 6: Confront the trade-offs.** 

**Step 7: Decide**

**Step 8: Tell your story.** 

## Data

All data was collected between September 30 and October 15, 2026. The files in this repo are snapshots: rerunning the steps below later returns newer data (the FHFA and HUD feeds change daily, and the property tax roll and ACS are updated yearly). To replicate the exact files, use the dates in the table.

| Source | Link | Date collected | File in this repo |
|---|---|---|---|
| FHFA: 100 most recent Federal Register documents (published 2022-06-27 to 2026-09-18) | [Federal Register API](https://www.federalregister.gov/developers/documentation/api/v1), agency `federal-housing-finance-agency` | October 1, 2026 | `fhfa_last100.csv` |
| HUD: Federal Register documents published September 1 to October 1, 2026 | [Federal Register API](https://www.federalregister.gov/developers/documentation/api/v1), agency `housing-and-urban-development-department` | October 1, 2026 | not in this repo |
| Providence 2020 Property Tax Roll | [Providence Open Data](https://data.providenceri.gov/Neighborhoods/2020-Property-Tax-Roll/y9h5-fefu) | September 30, 2026 | not in this repo (13.7 MB) |
| Providence 2025 Property Tax Roll (44,372 rows) | [Providence Open Data](https://data.providenceri.gov/Finance/2025-Property-Tax-Roll/6ub4-iebe/about_data) | October 14, 2026 | `2025_Property_Tax_Roll.csv` |
| Census ACS 1-year: rent burden (B25070), median gross rent (B25064) and renter households (B25003) for Providence city and the Providence-Warwick MSA; 2019 and 2021-2024 | [Census API, ACS 1-year](https://www.census.gov/data/developers/data-sets/acs-1year.html) | October 14, 2026 | `acs_rent_burden_providence.csv` |
| RIHousing Annual Rent Survey: average rent by municipality, 2025 vs. 2020 (39 municipalities) | [RIHousing Rent Survey](https://www.rihousing.com/public-information/rihousing-reports/ri-housing-rent-survey/) | October 14, 2026 | `rihousing_rent_survey_municipal.csv` |
| RI General Assembly: 2026 Public Laws list (427 chapters), coded Housing or Other per `CODEBOOK_RI_LEGISLATURE.md` | [RI Law Revision Office](https://webserver.rilegislature.gov/Lawrevision/plshort/pl2026sub.htm) | October 15, 2026 | `ri_legislature_public_laws_2026.csv` |
| Full text of the 32 RI 2026 public laws coded Housing (16 House/Senate pairs), from each chapter's page | `chapter_url` values in `ri_legislature_public_laws_2026.csv` (e.g. [chapter 242](http://webserver.rilegislature.gov/PublicLaws/law26/law26242.htm)) | October 15, 2026 | `ri_housing_laws_2026.csv` |

The Census Rental Housing Finance Survey (RHFS) API was tried and not used: it only publishes national tables (nothing for Providence, Rhode Island or the MSA), and one table alone has about 2.1 million rows.

## How to replicate the data collection

### Requirements

- Python 3.8 or later. Every script uses only the standard library, so there is nothing to install.
- `curl` (preinstalled on macOS and Linux).
- A free [Census API key](https://api.census.gov/data/key_signup.html), only for the ACS step. Census emails an activation link, and the key does not work until you click it. Pass the key as an environment variable so it never goes into the repo.

Run everything from the repo's root folder.

### 1. FHFA and HUD Federal Register documents

No key needed. `fetch_federal_register.py` pages through the [Federal Register API](https://www.federalregister.gov/developers/documentation/api/v1) and writes one CSV row per document. Columns: `publication_date`, `type`, `document_number`, `citation`, `title`, `action`, `abstract`, `docket_ids`, `comments_close_on`, `effective_on`, `html_url`, `pdf_url`.

```bash
# FHFA: the 100 most recent documents
python3 fetch_federal_register.py federal-housing-finance-agency --limit 100 --out fhfa_last100.csv

# HUD: everything published in a date range
python3 fetch_federal_register.py housing-and-urban-development-department \
  --since 2026-09-01 --until 2026-10-01 --out hud_documents.csv
```

Other agencies work the same way. Find the slug at https://www.federalregister.gov/api/v1/agencies.json.

Note: `fhfa_last100.csv` also has three extra columns at the end (`explicit_bill_mention`, `housing_topic_score`, `topic_hits`). They came from a one-off keyword analysis, run while looking for documents related to the bipartisan housing bill. The code for that step was not saved, so those three columns cannot be regenerated from this repo. The first 12 columns can.

### 2. Providence property tax rolls

No key needed. These are Socrata datasets on the city's open data portal. Download any year as a CSV by its dataset ID:

```bash
# 2025 roll (the file in this repo)
curl -L -o 2025_Property_Tax_Roll.csv \
  "https://data.providenceri.gov/api/views/6ub4-iebe/rows.csv?accessType=DOWNLOAD"

# 2020 roll (not in this repo)
curl -L -o 2020_Property_Tax_Roll.csv \
  "https://data.providenceri.gov/api/views/y9h5-fefu/rows.csv?accessType=DOWNLOAD"
```

The other years' IDs are in the dataset links on the portal (search "Property Tax Roll"). Each file has one row per parcel, including owner names and mailing addresses, which the city publishes as public record.

### 3. ACS rent burden

`fetch_acs_rent_burden.py` queries the ACS 1-year API for Providence city (place 59000 in Rhode Island) and the Providence-Warwick MSA (CBSA 39300), for 2019 and 2021-2024, and writes `acs_rent_burden_providence.csv`:

```bash
CENSUS_API_KEY=your_key python3 fetch_acs_rent_burden.py
```

How the columns are computed:

- `pct_cost_burdened` is the share of renter households paying 30% or more of income on rent and utilities (B25070 bands 7 to 10).
- `pct_severely_burdened` is the share paying 50% or more (band 10).
- Both exclude households where the rent share could not be computed (band 11), so the denominator is the total (band 1) minus band 11.
- There is no 2020 1-year release, so 2020 is skipped.
- The 2023 MSA figure is 49.9%, the number used in Step 1 above. The 2024 estimate is 52.6%.

To add a year or a place, edit `YEARS` or `GEOS` at the top of the script.

### 4. RIHousing rent survey (manual download, then a script)

RIHousing publishes this data only as an interactive Tableau dashboard, and Tableau blocks scripted downloads, so the export has to be done by hand in a browser:

1. Open the [RIHousing Rent Survey page](https://www.rihousing.com/public-information/rihousing-reports/ri-housing-rent-survey/) and scroll to the dashboard.
2. Choose the view that lists average rent by municipality with the 2025 and 2020 columns.
3. Click Download in the toolbar below the dashboard, then Data or Crosstab, then CSV. Save the file as `Municipal.csv`.
4. Convert it: `python3 convert_rihousing_export.py Municipal.csv rihousing_rent_survey_municipal.csv`

The export is UTF-16 and tab-separated, with values like `$2,396` and `+ $212`. The script turns it into a plain UTF-8 CSV with the columns `municipality`, `avg_rent_2025`, `avg_rent_2020`, `change_2020_2025`. Municipalities with no data in the export are left blank.

Caveat: the dashboard filter settings used for this export (for example the bedroom size) were not recorded, so the file's rent figures are not labeled by unit size. The same page also links a short PDF memo, "2025 Rent Survey Findings", with statewide summary figures.

### After refreshing any file

Update the "Date collected" column in the table above.
