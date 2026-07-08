# ════════════════════════════════════════════════════════════════
# MOCK PROPAGATION DATA
# Realistic scenarios showing different types of discrepancies
# ════════════════════════════════════════════════════════════════

propagation_scenarios = {
    # ════════════════════════════════════════════════════════════════
    # SCENARIO 1: Price Mismatch at SAIL (Data Quality Issue)
    # Issue Type: CRITICAL - SAIL contains stale/incorrect pricing
    # ════════════════════════════════════════════════════════════════
    "1335363": {
        "sap": {
            "system": "SAP",
            "price": 6.00,
            "promotion_price": None,
            "status": "Match",
            "time": "06:00 UTC",
            "correlation_id": "SAP-001-2024-07-10",
            "notes": "Source of truth - correct price"
        },
        "dih": {
            "system": "DIH",
            "price": 6.00,
            "promotion_price": None,
            "status": "Match",
            "time": "06:15 UTC",
            "correlation_id": "DIH-001-2024-07-10",
            "notes": "Correctly synced from SAP"
        },
        "sail": {
            "system": "SAIL",
            "price": 6.68,
            "promotion_price": None,
            "status": "Mismatch",
            "time": "06:30 UTC",
            "correlation_id": "SAIL-001-2024-07-10",
            "notes": "DIVERGENCE POINT - Stale/incorrect pricing"
        },
        "algolia": {
            "system": "Algolia",
            "price": 6.68,
            "promotion_price": None,
            "status": "Mismatch",
            "time": "06:45 UTC",
            "correlation_id": "ALG-001-2024-07-10",
            "notes": "Propagated bad price from SAIL"
        },
        "website": {
            "system": "Website",
            "price": 6.68,
            "promotion_price": None,
            "status": "Mismatch",
            "time": "Live (Cached)",
            "correlation_id": "WEB-001-2024-07-10",
            "notes": "Displays incorrect price (+$0.68 loss)"
        }
    },

    # ════════════════════════════════════════════════════════════════
    # SCENARIO 2: All Systems Match (No Issues)
    # Issue Type: NONE - Everything working correctly
    # ════════════════════════════════════════════════════════════════
    "1335364": {
        "sap": {
            "system": "SAP",
            "price": 3.59,
            "promotion_price": None,
            "status": "Match",
            "time": "07:00 UTC",
            "correlation_id": "SAP-002-2024-07-10",
            "notes": "Correct price"
        },
        "dih": {
            "system": "DIH",
            "price": 3.59,
            "promotion_price": None,
            "status": "Match",
            "time": "07:15 UTC",
            "correlation_id": "DIH-002-2024-07-10",
            "notes": "Synced correctly"
        },
        "sail": {
            "system": "SAIL",
            "price": 3.59,
            "promotion_price": None,
            "status": "Match",
            "time": "07:30 UTC",
            "correlation_id": "SAIL-002-2024-07-10",
            "notes": "All systems aligned"
        },
        "algolia": {
            "system": "Algolia",
            "price": 3.59,
            "promotion_price": None,
            "status": "Match",
            "time": "07:45 UTC",
            "correlation_id": "ALG-002-2024-07-10",
            "notes": "Correct price in index"
        },
        "website": {
            "system": "Website",
            "price": 3.59,
            "promotion_price": None,
            "status": "Match",
            "time": "Live",
            "correlation_id": "WEB-002-2024-07-10",
            "notes": "Displaying correct price"
        }
    },

    # ════════════════════════════════════════════════════════════════
    # SCENARIO 3: Cache Stale at Algolia
    # Issue Type: HIGH - Algolia hasn't re-indexed recent change
    # ════════════════════════════════════════════════════════════════
    "1335365": {
        "sap": {
            "system": "SAP",
            "price": 2.99,
            "promotion_price": None,
            "status": "Match",
            "time": "05:00 UTC",
            "correlation_id": "SAP-003-2024-07-10",
            "notes": "Price changed at 05:00 UTC"
        },
        "dih": {
            "system": "DIH",
            "price": 2.99,
            "promotion_price": None,
            "status": "Match",
            "time": "05:15 UTC",
            "correlation_id": "DIH-003-2024-07-10",
            "notes": "Updated from SAP"
        },
        "sail": {
            "system": "SAIL",
            "price": 2.99,
            "promotion_price": None,
            "status": "Match",
            "time": "05:30 UTC",
            "correlation_id": "SAIL-003-2024-07-10",
            "notes": "Correct price"
        },
        "algolia": {
            "system": "Algolia",
            "price": 3.49,
            "promotion_price": None,
            "status": "Mismatch",
            "time": "04:30 UTC",
            "correlation_id": "ALG-003-2024-07-10",
            "notes": "DIVERGENCE POINT - Stale cache, last indexed 30min ago"
        },
        "website": {
            "system": "Website",
            "price": 3.49,
            "promotion_price": None,
            "status": "Mismatch",
            "time": "Live (Cached)",
            "correlation_id": "WEB-003-2024-07-10",
            "notes": "Displays old price (+$0.50 loss)"
        }
    },

    # ════════════════════════════════════════════════════════════════
    # SCENARIO 4: DIH Has Bad Data (Data Quality Issue)
    # Issue Type: CRITICAL - DIH not synced with SAP
    # ════════════════════════════════════════════════════════════════
    "1335366": {
        "sap": {
            "system": "SAP",
            "price": 5.49,
            "promotion_price": None,
            "status": "Match",
            "time": "06:00 UTC",
            "correlation_id": "SAP-004-2024-07-10",
            "notes": "Source of truth - correct price"
        },
        "dih": {
            "system": "DIH",
            "price": 4.99,
            "promotion_price": None,
            "status": "Mismatch",
            "time": "06:15 UTC",
            "correlation_id": "DIH-004-2024-07-10",
            "notes": "DIVERGENCE POINT - DIH data quality issue, not synced with SAP"
        },
        "sail": {
            "system": "SAIL",
            "price": 4.99,
            "promotion_price": None,
            "status": "Mismatch",
            "time": "06:30 UTC",
            "correlation_id": "SAIL-004-2024-07-10",
            "notes": "Propagated bad data from DIH"
        },
        "algolia": {
            "system": "Algolia",
            "price": 4.99,
            "promotion_price": None,
            "status": "Mismatch",
            "time": "06:45 UTC",
            "correlation_id": "ALG-004-2024-07-10",
            "notes": "Propagated bad data"
        },
        "website": {
            "system": "Website",
            "price": 4.99,
            "promotion_price": None,
            "status": "Mismatch",
            "time": "Live (Cached)",
            "correlation_id": "WEB-004-2024-07-10",
            "notes": "Displays wrong price (-$0.50 loss)"
        }
    },

    # ════════════════════════════════════════════════════════════════
    # SCENARIO 5: Promotion Missing (Never Propagated)
    # Issue Type: HIGH - Promotion defined in SAP but not propagated
    # ════════════════════════════════════════════════════════════════
    "1335367": {
        "sap": {
            "system": "SAP",
            "price": 8.99,
            "promotion_price": 7.49,
            "status": "Match",
            "time": "07:00 UTC",
            "correlation_id": "SAP-005-2024-07-10",
            "notes": "Active promotion: $8.99 → $7.49"
        },
        "dih": {
            "system": "DIH",
            "price": 8.99,
            "promotion_price": None,
            "status": "Mismatch",
            "time": "07:15 UTC",
            "correlation_id": "DIH-005-2024-07-10",
            "notes": "DIVERGENCE POINT - Promotion not propagated from SAP"
        },
        "sail": {
            "system": "SAIL",
            "price": 8.99,
            "promotion_price": None,
            "status": "Mismatch",
            "time": "07:30 UTC",
            "correlation_id": "SAIL-005-2024-07-10",
            "notes": "No promotion data"
        },
        "algolia": {
            "system": "Algolia",
            "price": 8.99,
            "promotion_price": None,
            "status": "Mismatch",
            "time": "07:45 UTC",
            "correlation_id": "ALG-005-2024-07-10",
            "notes": "No promotion in index"
        },
        "website": {
            "system": "Website",
            "price": 8.99,
            "promotion_price": None,
            "status": "Mismatch",
            "time": "Live (Cached)",
            "correlation_id": "WEB-005-2024-07-10",
            "notes": "Missing promotion - customer pays $1.50 more"
        }
    }
}