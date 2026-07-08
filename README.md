# Price & Promotion RCA Tool

Enterprise Streamlit UI (Databricks Apps compatible) that recreates the
reference design pixel-for-pixel. Native Streamlit widgets can't reach the
polished SaaS look, so the whole interface is authored as semantic HTML +
one CSS stylesheet and rendered on a single full-fidelity surface. Streamlit
is used purely as the hosting framework.

## Project structure

```
price_promo_rca/
├── app.py                 # Entry point: injects CSS once, assembles + renders the page
├── components.py          # Reusable HTML component functions (render_nav, render_kpi_cards, …)
├── icons.py               # Inline-SVG icon registry (no external CDN — works offline)
├── data.py                # All display data (KPIs, table rows, investigation, root cause)
├── style.css              # Global stylesheet — CSS variables, all component styles
├── config.py              # App constants
├── affected_articles.json # Sample source data
├── app.yml                # Databricks Apps launch config
└── requirements.txt
```

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Databricks Apps

`app.yml` already contains the launch command. Sync this folder to your
workspace and start the app — it binds to `${DATABRICKS_APP_PORT}`.

## Design system (style.css)

Every colour, radius, shadow and spacing value is a CSS variable in
`:root`, so re-theming touches one place:

| Token        | Value                        |
|--------------|------------------------------|
| `--primary`  | `#1D4ED8`                    |
| `--border`   | `#E5E7EB`                    |
| `--bg`       | `#F8FAFC`                    |
| `--card`     | `#FFFFFF`                    |
| `--radius`   | `14px`                       |
| `--shadow`   | `0 2px 12px rgba(0,0,0,.06)` |
| font         | Inter, 8px spacing grid      |

## How the pieces fit

`app.py` calls the `render_*` functions in `components.py`, each of which
returns an HTML string built from `data.py` values and `icons.py` SVGs. The
assembled markup plus `style.css` is rendered as one document so the layout
is identical to the design reference and immune to Streamlit widget styling.

Components: `render_nav`, `render_pagehead`, `render_kpi_cards`,
`render_articles_table`, `render_investigation` (→ `render_info_card`,
`render_flow_card` → `render_pipeline` + `render_system_table`,
`render_root_cause`).

## Wiring real data

Replace the constants in `data.py` (or the `get_*` accessors) with your
Databricks / SQL queries. The component functions consume plain dicts/lists,
so as long as the shape matches, the UI updates with zero markup changes.
For example, `get_articles()` can read `affected_articles.json` or query a
table and return the same list-of-dicts structure.

## Responsive behaviour

Desktop layout is the default. Below 1180px the investigation grid and KPI
cards stack to two columns; below 720px everything collapses to a single
column. See the `@media` blocks at the bottom of `style.css`.
