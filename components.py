# ══════════════════════════════════════════════════════════════
# COMPONENTS
# Each function returns an HTML string. Keeping markup out of app.py
# means no repeated HTML and easy pixel tweaks in one place.
# ══════════════════════════════════════════════════════════════

from icons import icon


# ─────────────────────────────────────────────────────────────
# 1 · TOP NAVIGATION
# ─────────────────────────────────────────────────────────────
def render_nav() -> str:
    return f"""
    <nav class="nav">
      <div class="nav__brand">
        <div class="nav__logo">{icon('logo')}</div>
        <span class="nav__title">Price &amp; Promotion RCA Tool</span>
      </div>
      <div class="nav__tabs">
        <button class="nav__tab nav__tab--active">{icon('dashboard')} Dashboard</button>
        <button class="nav__tab">{icon('search')} Investigations</button>
      </div>
      <div class="nav__spacer"></div>
      <div class="nav__search">
        {icon('search')}
        <input placeholder="Search articles, stores, promotions..." />
      </div>
      <button class="nav__icon"><span class="nav__dot"></span>{icon('bell')}</button>
      <button class="nav__icon">{icon('help')}</button>
      <div class="nav__avatar">
        <span class="nav__avatar-circle">JR</span>{icon('chevron-down')}
      </div>
    </nav>"""


# ─────────────────────────────────────────────────────────────
# 2 · PAGE HEADER + DATE-RANGE SWITCH
# ─────────────────────────────────────────────────────────────
def render_pagehead() -> str:
    ranges = ["Today", "Last 7 Days", "Last 30 Days"]
    btns = "".join(
        f'<button class="segment__btn{" segment__btn--active" if r == "Today" else ""}">{r}</button>'
        for r in ranges
    )
    return f"""
    <div class="pagehead">
      <div>
        <h1 class="pagehead__title">Pricing Ecosystem Overview</h1>
        <p class="pagehead__sub">Real-time monitoring of
          <b>DAP</b> ·· <b>DIH</b> ·· <b>SAIL</b> ·· <b>Algolia</b> ·· <b>Website</b></p>
      </div>
      <div class="segment">
        {btns}
        <button class="segment__btn">{icon('calendar')} Custom Range</button>
      </div>
    </div>"""


# ─────────────────────────────────────────────────────────────
# 3 · KPI CARDS
# ─────────────────────────────────────────────────────────────
def render_kpi_card(kpi: dict) -> str:
    return f"""
      <div class="kpi">
        <div class="kpi__icon kpi__icon--{kpi['tone']}">{icon(kpi['icon'])}</div>
        <div class="kpi__body">
          <span class="kpi__label">{kpi['label']}</span>
          <span class="kpi__value">{kpi['value']}</span>
        </div>
      </div>"""


def render_kpi_cards(kpis: list) -> str:
    cards = "".join(render_kpi_card(k) for k in kpis)
    return f'<div class="kpi-grid">{cards}</div>'


# ─────────────────────────────────────────────────────────────
# 4 · ARTICLES TABLE (+ search / filter / pagination)
# ─────────────────────────────────────────────────────────────
def render_search_field(placeholder: str) -> str:
    return f'<div class="field">{icon("search")}<input placeholder="{placeholder}" /></div>'


def _article_row(a: dict) -> str:
    sel = " is-selected" if a.get("selected") else ""
    issue = (f'<span class="issue issue--{a["issue_tone"]}">'
             f'{icon(a["issue_icon"])}{a["issue"]}</span>')
    return f"""
      <tr class="{sel.strip()}">
        <td class="cell-link">{a['article']}</td>
        <td>{a['product']}</td>
        <td>{a['store']}</td>
        <td>{a['store_name']}</td>
        <td>{a['uom']}</td>
        <td>{a['banner']}</td>
        <td>{issue}</td>
        <td class="cell-muted">{a['detected']}</td>
        <td class="col-actions"><span class="row-arrow">{icon('chevron-right')}</span></td>
      </tr>"""


def _pagination(p: dict) -> str:
    btns = [f'<button class="pager__btn"><span>{icon("chevron-left")}</span></button>']
    for n in p["pages"]:
        active = " pager__btn--active" if n == p["current"] else ""
        btns.append(f'<button class="pager__btn{active}">{n}</button>')
    btns.append('<span class="pager__ellipsis">…</span>')
    btns.append(f'<button class="pager__btn">{p["gap_to"]}</button>')
    btns.append(f'<button class="pager__btn">{icon("chevron-right")}</button>')
    return f"""
      <div class="pager">
        <span class="pager__info">{p['showing']}</span>
        <div class="pager__ctrls">{''.join(btns)}</div>
      </div>"""


def render_articles_table(articles: list, pagination: dict) -> str:
    heads = ["Article Number", "Product Name", "Store", "Store Name",
             "UOM", "Banner", "Issue Type", "Last Detected"]
    head_html = "".join(f"<th>{h}</th>" for h in heads) + '<th class="col-actions">Actions</th>'
    rows = "".join(_article_row(a) for a in articles)
    count = pagination["showing"].split("of ")[-1]
    return f"""
    <div class="card">
      <div class="card__head">
        <div class="card__title">Affected Articles &amp; Stores
          <span class="count">({count.replace(' items','')} items)</span></div>
        <div class="card__tools">
          {render_search_field("Search by Article, Store, or UOM...")}
          <button class="btn">{icon('filter')} Filters</button>
        </div>
      </div>
      <div class="tbl-wrap">
        <table class="tbl">
          <thead><tr>{head_html}</tr></thead>
          <tbody>{rows}</tbody>
        </table>
      </div>
      {_pagination(pagination)}
    </div>"""


# ─────────────────────────────────────────────────────────────
# 5 · INVESTIGATION HEADER
# ─────────────────────────────────────────────────────────────
def render_investigation_head(inv: dict) -> str:
    return f"""
    <div class="inv-head">
      <button class="inv-back">{icon('arrow-left')} Back to Dashboard</button>
      <span class="inv-title">Investigation: Article {inv['article']}</span>
      <span class="badge badge--critical">{inv['severity']}</span>
      <div class="inv-head__spacer"></div>
      <button class="btn">{icon('refresh')} Refresh Data</button>
      <button class="btn" style="padding:0 12px;">{icon('dots')}</button>
    </div>"""


# ─────────────────────────────────────────────────────────────
# 6 · ARTICLE INFORMATION CARD
# ─────────────────────────────────────────────────────────────
def render_info_card(info_rows: list) -> str:
    rows = "".join(
        f'<div class="info-row"><span class="info-row__k">{k}</span>'
        f'<span class="info-row__v">{v}</span></div>'
        for k, v in info_rows
    )
    return f"""
    <div class="card info-card">
      <div class="info-card__title">Article Information</div>
      {rows}
    </div>"""


# ─────────────────────────────────────────────────────────────
# 7 · PROPAGATION PIPELINE
# ─────────────────────────────────────────────────────────────
def _legend() -> str:
    dot_ok  = ('<span class="legend__dot"><svg viewBox="0 0 24 24" fill="#ECFDF3" '
               'stroke="#16A34A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
               '<circle cx="12" cy="12" r="10"/><polyline points="8 12 11 15 16 9"/></svg></span>')
    dot_bad = ('<span class="legend__dot"><svg viewBox="0 0 24 24" fill="#FEF2F2" '
               'stroke="#DC2626" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
               '<circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/>'
               '<line x1="9" y1="9" x2="15" y2="15"/></svg></span>')
    return f"""
      <div class="legend">
        <span class="legend__item">{dot_ok}Match</span>
        <span class="legend__item">{dot_bad}Mismatch</span>
        <span class="legend__item"><span class="legend__dot" style="background:#F59E0B"></span>Delayed</span>
        <span class="legend__item"><span class="legend__dot" style="background:#CBD5E1"></span>N/A</span>
      </div>"""


def render_pipeline_node(node: dict) -> str:
    ok = node["status"] == "ok"
    badge = (f'<div class="node__badge node__badge--{"ok" if ok else "bad"}">'
             f'{icon("check") if ok else icon("x")}</div>')
    diverge = ""
    if node.get("diverge"):
        diverge = (f'<div class="node__diverge">{icon("alert-triangle")}Divergence Point</div>')
    return f"""
      <div class="node-wrap">
        <div class="node node--{'ok' if ok else 'bad'}">
          <div class="node__name">{node['name']}</div>
          {badge}
          <div class="node__price">{node['price']}</div>
          <div class="node__time">{node['time']}</div>
        </div>
        {diverge}
      </div>"""


def render_pipeline(nodes: list) -> str:
    arrow = f'<div class="node-arrow">{icon("arrow-right")}</div>'
    parts = []
    for i, node in enumerate(nodes):
        parts.append(render_pipeline_node(node))
        if i < len(nodes) - 1:
            parts.append(arrow)
    return f'<div class="pipeline">{"".join(parts)}</div>'


# ─────────────────────────────────────────────────────────────
# 8 · SYSTEM COMPARISON TABLE
# ─────────────────────────────────────────────────────────────
def status_pill(status: str) -> str:
    if status == "ok":
        return f'<span class="pill pill--ok">{icon("check")}Match</span>'
    if status == "bad":
        return f'<span class="pill pill--bad">{icon("x")}Mismatch</span>'
    return '<span class="pill pill--na">N/A</span>'


def render_system_table(rows: list) -> str:
    heads = ["System", "Regular Price", "Promotion Price", "Promo #",
             "Last Updated", "Correlation ID", "Status"]
    head_html = "".join(f"<th>{h}</th>" for h in heads)
    body = ""
    for r in rows:
        price_cls = "cell-bad" if r["bad_price"] else ""
        promo = f'<td class="dash">{r["promo"]}</td>' if r["promo"] == "—" else f'<td>{r["promo"]}</td>'
        promo_no = f'<td class="dash">{r["promo_no"]}</td>' if r["promo_no"] == "—" else f'<td>{r["promo_no"]}</td>'
        body += f"""
          <tr>
            <td class="sys-name">{r['system']}</td>
            <td class="{price_cls}">{r['regular']}</td>
            {promo}{promo_no}
            <td>{r['updated']}</td>
            <td>{r['corr']}</td>
            <td>{status_pill(r['status'])}</td>
          </tr>"""
    return f"""
      <div class="syscmp">
        <div class="syscmp__title">System Comparison</div>
        <table class="cmp">
          <thead><tr>{head_html}</tr></thead>
          <tbody>{body}</tbody>
        </table>
      </div>"""


def render_flow_card(inv: dict) -> str:
    return f"""
    <div class="card flow-card">
      <div class="flow-head">
        <span class="flow-head__title">Data Propagation Flow</span>
        {_legend()}
      </div>
      {render_pipeline(inv['pipeline'])}
      {render_system_table(inv['comparison'])}
    </div>"""


# ─────────────────────────────────────────────────────────────
# 9 · ROOT CAUSE SUMMARY
# ─────────────────────────────────────────────────────────────
def render_root_cause(rc: dict) -> str:
    actions = ""
    for i, a in enumerate(rc["actions"], start=1):
        actions += (f'<li class="rca__action"><span class="rca__num">{i}.</span>'
                    f'<span class="ico-{ {"fire":"fire","urgent":"urgent","monitor":"monitor"}[a["icon"]] }">'
                    f'{icon(a["icon"])}</span>'
                    f'<span><b>{a["label"]}</b> {a["text"]}</span></li>')
    return f"""
    <div class="rca">
      <div class="rca__head">{icon('alert-triangle')}
        <span class="rca__head-title">Root Cause Summary</span></div>
      <div class="rca__block">
        <div class="rca__label">Root Cause</div>
        <div class="rca__lead">{rc['cause']}</div>
      </div>
      <div class="rca__block">
        <div class="rca__label">Impact</div>
        <div class="rca__text">{rc['impact']}</div>
      </div>
      <div class="rca__block" style="margin-bottom:0;">
        <div class="rca__label">Recommended Actions</div>
        <ol class="rca__actions">{actions}</ol>
      </div>
    </div>"""


# ─────────────────────────────────────────────────────────────
# 10 · INVESTIGATION GRID (3-column layout)
# ─────────────────────────────────────────────────────────────
def render_investigation(inv: dict) -> str:
    return f"""
    {render_investigation_head(inv)}
    <div class="inv-grid">
      {render_info_card(inv['info'])}
      {render_flow_card(inv)}
      {render_root_cause(inv['root_cause'])}
    </div>"""
