# ════════════════════════════════════════════════════════════════
# PRICE & PROMOTION RCA TOOL
# Databricks App - Streamlit Frontend
# ════════════════════════════════════════════════════════════════

import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime

# ════════════════════════════════════════════════════════════════
# CONFIGURATION
# ════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="Price & Promotion RCA Tool",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .metric-card {
        background-color: #FFFFFF;
        border: 1px solid #E5E5E5;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }
    .badge-critical {
        background-color: #FFE0E0;
        color: #D32F2F;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
    }
    .badge-high {
        background-color: #FFF3CD;
        color: #FF9800;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
    }
    .badge-medium {
        background-color: #FFF3CD;
        color: #FF9800;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
    }
    .flow-box {
        border: 2px solid;
        border-radius: 8px;
        padding: 16px;
        text-align: center;
        font-weight: 600;
        margin: 10px;
    }
    .flow-box-healthy {
        border-color: #12B886;
        background-color: #E8F5E9;
    }
    .flow-box-diverge {
        border-color: #D32F2F;
        background-color: #FFE0E0;
    }
</style>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# LOAD MOCK DATA
# ════════════════════════════════════════════════════════════════

@st.cache_data
def load_affected_articles():
    """Load mock affected articles data."""
    # Hardcoded data (same as JSON file)
    data = [
        {
            "article_number": "1335363",
            "product_name": "Best Buy Peppers 1.14 kg",
            "store": "9665",
            "store_name": "FreshCo",
            "uom": "EA",
            "banner": "FreshCo",
            "region": "Western",
            "issue_type": "Price Mismatch",
            "severity": "CRITICAL",
            "last_detected": "2024-07-10 15:47 UTC"
        },
        {
            "article_number": "1335364",
            "product_name": "Organic Spinach 284g",
            "store": "9666",
            "store_name": "FreshCo",
            "uom": "EA",
            "banner": "FreshCo",
            "region": "Central",
            "issue_type": "Promotion Missing",
            "severity": "HIGH",
            "last_detected": "2024-07-10 15:32 UTC"
        },
        {
            "article_number": "1335365",
            "product_name": "2% Milk 2L",
            "store": "9667",
            "store_name": "SaveCo",
            "uom": "EA",
            "banner": "SaveCo",
            "region": "Eastern",
            "issue_type": "Cache Stale",
            "severity": "MEDIUM",
            "last_detected": "2024-07-10 15:12 UTC"
        },
        {
            "article_number": "1335366",
            "product_name": "Bananas 1.36 kg",
            "store": "9668",
            "store_name": "Foodland",
            "uom": "EA",
            "banner": "Foodland",
            "region": "Northern",
            "issue_type": "Price Mismatch",
            "severity": "HIGH",
            "last_detected": "2024-07-10 15:05 UTC"
        },
        {
            "article_number": "1335367",
            "product_name": "Chicken Breast 1kg",
            "store": "9669",
            "store_name": "IGA",
            "uom": "EA",
            "banner": "IGA",
            "region": "Western",
            "issue_type": "UOM Mismatch",
            "severity": "MEDIUM",
            "last_detected": "2024-07-10 14:58 UTC"
        }
    ]
    return pd.DataFrame(data)

@st.cache_data
def load_propagation_data():
    """Load mock propagation data."""
    data = {
        "1335363": {
            "sap": {"price": 6.99, "status": "Match", "time": "08:00 UTC"},
            "dih": {"price": 6.99, "status": "Match", "time": "08:15 UTC"},
            "sail": {"price": 5.99, "status": "Mismatch", "time": "09:00 UTC"},
            "algolia": {"price": 5.99, "status": "Mismatch", "time": "09:15 UTC"},
            "website": {"price": 5.99, "status": "Mismatch", "time": "Live"}
        },
        "1335364": {
            "sap": {"price": 4.49, "status": "Match", "time": "08:00 UTC"},
            "dih": {"price": 4.49, "status": "Match", "time": "08:15 UTC"},
            "sail": {"price": 4.49, "status": "Match", "time": "09:00 UTC"},
            "algolia": {"price": 4.49, "status": "Match", "time": "09:15 UTC"},
            "website": {"price": 4.49, "status": "Match", "time": "Live"}
        }
    }
    return data

# Load data
df_articles = load_affected_articles()
propagation_data = load_propagation_data()

# ════════════════════════════════════════════════════════════════
# SECTION 1: HEADER
# ════════════════════════════════════════════════════════════════

col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.title("💰 Price & Promotion RCA Tool")
    st.markdown("Real-time monitoring of SAP → DIH → SAIL → Algolia → Website")

with col2:
    time_period = st.selectbox(
        "Time Period",
        ["Today", "Last 7 Days", "Last 30 Days", "Custom Range"],
        label_visibility="collapsed"
    )

# ════════════════════════════════════════════════════════════════
# SECTION 2: KPI CARDS
# ════════════════════════════════════════════════════════════════

st.subheader("Key Metrics")

kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)

with kpi_col1:
    st.metric("Articles Affected", "342", "+12%")

with kpi_col2:
    st.metric("Stores Affected", "87", "+8%")

with kpi_col3:
    st.metric("Banners Affected", "24", "+15%")

with kpi_col4:
    st.metric("Regions Affected", "8", "-3%")

st.divider()

# ════════════════════════════════════════════════════════════════
# SECTION 3: AFFECTED ARTICLES LIST
# ════════════════════════════════════════════════════════════════

st.subheader(f"Affected Articles & Stores ({len(df_articles)} items)")

col1, col2 = st.columns([0.8, 0.2])
with col1:
    search_term = st.text_input("Search by Article, Store, or UOM...")

# Filter dataframe
if search_term:
    filtered_df = df_articles[
        (df_articles["article_number"].str.contains(search_term, case=False)) |
        (df_articles["store_name"].str.contains(search_term, case=False)) |
        (df_articles["uom"].str.contains(search_term, case=False))
    ]
else:
    filtered_df = df_articles

# Display table
st.dataframe(
    filtered_df[["article_number", "product_name", "store", "store_name", "uom", "issue_type", "severity"]],
    use_container_width=True,
    hide_index=True,
    height=300
)

st.divider()

# ════════════════════════════════════════════════════════════════
# SECTION 4: INVESTIGATION DETAIL (Selectable)
# ════════════════════════════════════════════════════════════════

st.subheader("Investigation Details")

selected_article = st.selectbox(
    "Select an article to investigate:",
    options=df_articles["article_number"].tolist(),
    format_func=lambda x: f"{x} - {df_articles[df_articles['article_number']==x]['product_name'].values[0]}"
)

if selected_article:
    # Get selected article details
    article_row = df_articles[df_articles["article_number"] == selected_article].iloc[0]
    article_data = propagation_data.get(selected_article, {})
    
    # Investigation Header
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        st.markdown(f"### Investigation: Article {selected_article}")
        st.markdown(f"**{article_row['product_name']}** | {article_row['store_name']} (Store {article_row['store']}) | UOM: {article_row['uom']}")
    
    # Article Information (Left Side)
    with st.expander("Article Information", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**Article Number:** {article_row['article_number']}")
            st.markdown(f"**Product Name:** {article_row['product_name']}")
            st.markdown(f"**Store:** {article_row['store']}")
        with col2:
            st.markdown(f"**UOM:** {article_row['uom']}")
            st.markdown(f"**Banner:** {article_row['banner']}")
            st.markdown(f"**Region:** {article_row['region']}")
    
    # Data Propagation Flow
    st.markdown("### Data Propagation Flow")
    
    if article_data:
        # Create propagation visualization
        prop_col1, prop_col2, prop_col3, prop_col4, prop_col5 = st.columns(5)
        
        systems = ["sap", "dih", "sail", "algolia", "website"]
        system_labels = ["SAP", "DIH", "SAIL", "Algolia", "Website"]
        columns = [prop_col1, prop_col2, prop_col3, prop_col4, prop_col5]
        
        for col, system, label in zip(columns, systems, system_labels):
            with col:
                system_info = article_data.get(system, {})
                status = system_info.get("status", "Unknown")
                status_icon = "✓" if status == "Match" else "✗"
                status_color = "#12B886" if status == "Match" else "#D32F2F"
                
                st.markdown(f"""
                <div style='text-align: center; padding: 12px; border: 2px solid {status_color}; 
                            border-radius: 8px; background-color: {"#E8F5E9" if status == "Match" else "#FFE0E0"};'>
                    <div style='font-weight: 600; margin-bottom: 8px;'>{label}</div>
                    <div style='font-size: 20px; color: {status_color}; font-weight: 700;'>{status_icon}</div>
                    <div style='font-size: 14px; font-weight: 600; margin: 8px 0;'>${system_info.get("price", "—")}</div>
                    <div style='font-size: 11px; color: #666;'>{system_info.get("time", "—")}</div>
                </div>
                """, unsafe_allow_html=True)
    
    # System Comparison Table
    st.markdown("### System Comparison")
    
    comparison_data = {
        "System": ["SAP", "DIH", "SAIL", "Algolia", "Website"],
        "Regular Price": ["$6.99", "$6.99", "$5.99", "$5.99", "$5.99"] if selected_article == "1335363" else ["$4.49", "$4.49", "$4.49", "$4.49", "$4.49"],
        "Status": ["✓ Match", "✓ Match", "✗ Mismatch", "✗ Mismatch", "✗ Mismatch"] if selected_article == "1335363" else ["✓ Match", "✓ Match", "✓ Match", "✓ Match", "✓ Match"]
    }
    
    st.dataframe(pd.DataFrame(comparison_data), use_container_width=True, hide_index=True)
    
    # Confidence Score
    st.markdown("### Confidence Score")
    st.progress(0.97)
    st.markdown("97% - High confidence in root cause analysis")

# ════════════════════════════════════════════════════════════════
# FOOTER
# ════════════════════════════════════════════════════════════════

st.divider()
st.markdown("""
<div style='text-align: center; color: #999; font-size: 12px;'>
Last Updated: 2024-07-10 15:47:23 UTC | Data Freshness: 100%
</div>
""", unsafe_allow_html=True)