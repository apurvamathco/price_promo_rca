# ══════════════════════════════════════════════════════════════
# DATA LAYER
# All mock data for the RCA tool lives here so the UI stays clean.
# Swap these functions for real Databricks / SQL queries later.
# ══════════════════════════════════════════════════════════════

# ---- Top-line KPI figures --------------------------------------------------
KPIS = [
    {"label": "Articles Affected", "value": "342", "icon": "cube",  "tone": "indigo"},
    {"label": "Stores Affected",   "value": "87",  "icon": "store", "tone": "green"},
    {"label": "Banners Affected",  "value": "24",  "icon": "tag",   "tone": "purple"},
    {"label": "Regions Affected",  "value": "8",   "icon": "globe", "tone": "orange"},
]

# ---- Affected articles table (rows shown on the dashboard) -----------------
# `issue_tone` drives the icon colour: "red" = mismatch, "amber" = warning.
ARTICLES = [
    {"article": "1333363", "product": "Best Buy Peppers 1.14 kg", "store": "9866",
     "store_name": "Freshco Parliament & Dundas", "uom": "EA", "banner": "FreshCo",
     "issue": "Price Mismatch",     "issue_tone": "red",   "issue_icon": "alert-circle",
     "detected": "2024-07-10 18:47 UTC", "selected": True},
    {"article": "1333364", "product": "Organic Spinach 204g", "store": "9866",
     "store_name": "Freshco Leslie & Lakeshore", "uom": "EA", "banner": "Sobeys",
     "issue": "Promotion Missing",  "issue_tone": "amber", "issue_icon": "alert-circle",
     "detected": "2024-07-10 18:32 UTC", "selected": False},
    {"article": "1333365", "product": "2% Milk 2L.", "store": "9867",
     "store_name": "Freshco Queen & Cladetona", "uom": "EA", "banner": "Safeway",
     "issue": "Cache State",        "issue_tone": "amber", "issue_icon": "alert-triangle",
     "detected": "2024-07-10 18:12 UTC", "selected": False},
    {"article": "1333366", "product": "Bananaa 1.38 kg", "store": "9868",
     "store_name": "Freshco Dufferin & Dupont", "uom": "EA", "banner": "Foodland",
     "issue": "Price Mismatch",     "issue_tone": "red",   "issue_icon": "alert-circle",
     "detected": "2024-07-10 18:05 UTC", "selected": False},
    {"article": "1333367", "product": "Chicken Breast 1kg", "store": "9868",
     "store_name": "Freshco Bloor & Dundas", "uom": "EA", "banner": "IBA",
     "issue": "UOM Mismatch",       "issue_tone": "amber", "issue_icon": "alert-circle",
     "detected": "2024-07-10 14:05 UTC", "selected": False},
]

PAGINATION = {"showing": "Showing 1 to 5 of 342 items",
              "pages": [1, 2, 3, 4, 5], "gap_to": 69, "current": 1}

# ---- Investigation: the article currently under the microscope -------------
INVESTIGATION = {
    "article": "1335363",
    "severity": "Critical",
    "info": [
        ("Article Number", "1335303"),
        ("Product Name",   "Best Buy Peppers 1.14 kg"),
        ("Store",          "9866 (Freshco Parliament & Dundas)"),
        ("UOM",            "EA"),
        ("Banner",         "FreshCo"),
        ("Region",         "Western"),
        ("Issue Detected", "2024-07-10 16:47 UTC"),
    ],
    # Pipeline nodes, left → right. status: "ok" | "bad". diverge flags the badge.
    "pipeline": [
        {"name": "SAP",     "status": "ok",  "price": "$6.00", "time": "06:00 UTC<br>2024-07-10", "diverge": False},
        {"name": "DIH",     "status": "ok",  "price": "$6.00", "time": "06:15 UTC<br>2024-07-10", "diverge": False},
        {"name": "SAIL",    "status": "bad", "price": "$6.68", "time": "06:00 UTC<br>2024-07-10", "diverge": True},
        {"name": "Algolia", "status": "bad", "price": "$6.68", "time": "06:15 UTC<br>2024-07-10", "diverge": False},
        {"name": "Website", "status": "bad", "price": "$6.68", "time": "Live (Cached)",           "diverge": False},
    ],
    # System comparison rows. `bad_price` shades the regular-price cell red.
    "comparison": [
        {"system": "SAP",     "regular": "$6.00", "promo": "—", "promo_no": "—",
         "updated": "2024-07-10 06:16 UTC", "corr": "SAP-001-2024-07-10", "status": "ok",  "bad_price": False},
        {"system": "DIH",     "regular": "$6.00", "promo": "—", "promo_no": "—",
         "updated": "2024-07-10 06:15 UTC", "corr": "DIH-001-2024-07-10", "status": "ok",  "bad_price": False},
        {"system": "SAIL",    "regular": "$6.68", "promo": "—", "promo_no": "—",
         "updated": "2024-07-10 06:15 UTC", "corr": "SAIL-001-2024-07-10", "status": "bad", "bad_price": True},
        {"system": "Algolia", "regular": "$6.68", "promo": "—", "promo_no": "—",
         "updated": "2024-07-10 06:15 UTC", "corr": "ALD-001-2024-07-10", "status": "bad", "bad_price": True},
        {"system": "Website", "regular": "$6.68", "promo": "—", "promo_no": "—",
         "updated": "Live (Cached)",        "corr": "WEB-001-2024-07-10", "status": "bad", "bad_price": True},
    ],
    "root_cause": {
        "cause": "SAIL contains stale/incorrect pricing.",
        "impact": ("Website displays <b>$6.68</b> but correct price is <b>$6.00</b> "
                   "(+ $0.68 loss). Affects approximately <b>2,249</b> customer transactions today."),
        "actions": [
            {"icon": "fire",    "label": "IMMEDIATE:", "text": "Verify DIH→SAIL pipeline"},
            {"icon": "urgent",  "label": "URGENT:",    "text": "Reprocess SAIL Ingestion"},
            {"icon": "monitor", "label": "MONITOR:",   "text": "Track subsequent updates"},
        ],
    },
}


def get_kpis():          return KPIS
def get_articles():      return ARTICLES
def get_pagination():    return PAGINATION
def get_investigation(): return INVESTIGATION
