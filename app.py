# ══════════════════════════════════════════════════════════════
# PriceGuard — Sobeys Pricing Discrepancy Tracker
# Streamlit (Databricks Apps).  Run locally with:  streamlit run app.py
# Self-contained POC: the whole interactive UI (HTML + CSS + JS,
# including the Sobeys logo) is embedded below — no external assets.
# For real data, replace the JS `ARTICLES` / `TEMPLATES` blocks with
# values injected from your Databricks queries.
# ══════════════════════════════════════════════════════════════

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="PriceGuard — Sobeys Pricing Discrepancy Tracker",
    page_icon="🟢",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
  #MainMenu, header, footer {visibility:hidden;}
  [data-testid="stSidebar"], [data-testid="collapsedControl"] {display:none;}
  [data-testid="stAppViewContainer"] {background:#F4F7F5;}
  .block-container {padding:0 !important; max-width:100% !important;}
  [data-testid="stHeader"] {height:0; background:transparent;}
  iframe {display:block;}
</style>
""", unsafe_allow_html=True)

UI = r'''<!-- PriceGuard — Sobeys Pricing Discrepancy Tracker (self-contained POC) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@500;600;700;800&family=Inter:wght@400;500;600;700&family=Roboto+Mono:wght@500;600&display=swap" rel="stylesheet">

<style>
:root{
  --brand:#00853F; --brand-deep:#006B33; --brand-tint:#E9F5EE; --brand-ring:rgba(0,133,63,.16);
  --ink:#0E1A14; --ink-2:#33413A; --muted:#6B7A72; --faint:#93A29A;
  --line:#E4EAE6; --line-2:#EEF2F0; --bg:#F4F7F5; --card:#FFFFFF;
  --red:#D62D2D; --red-tint:#FCECEC; --amber:#E08A00; --amber-tint:#FCF3E3;
  --ok:#12924E; --ok-tint:#E7F5EC; --slate:#CBD5D0;
  --shadow:0 1px 2px rgba(14,26,20,.04),0 8px 24px rgba(14,26,20,.05);
  --shadow-lg:0 12px 40px rgba(14,26,20,.10);
  --r:14px;
  --sans:'Inter',system-ui,sans-serif; --disp:'Sora',system-ui,sans-serif; --mono:'Roboto Mono',monospace;
}
*{box-sizing:border-box}
.ppr{font-family:var(--sans);color:var(--ink);background:var(--bg);
  -webkit-font-smoothing:antialiased;max-width:1320px;margin:0 auto;padding:0 22px 40px}
.ppr svg{display:block}
button{font-family:inherit;cursor:pointer;border:none;background:none}
::selection{background:var(--brand-ring)}

/* ---------- NAV ---------- */
.nav{display:flex;align-items:center;gap:18px;height:64px;position:sticky;top:0;z-index:40;
  background:rgba(244,247,245,.86);backdrop-filter:blur(10px);
  border-bottom:1px solid var(--line);margin:0 -22px 0;padding:0 22px}
.brand{display:flex;align-items:center;gap:11px}
.brand__logo{height:34px;width:auto;border-radius:7px;display:block}
.brand__sep{width:1px;height:24px;background:var(--line)}
.brand__word{font-family:var(--disp);font-weight:800;font-size:17px;letter-spacing:-.02em;color:var(--brand-deep);line-height:1}
.brand__sub{font-size:10.5px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--faint);margin-top:3px}
.nav__div{width:1px;height:26px;background:var(--line)}
.tabs{display:flex;gap:2px}
.tab{display:flex;align-items:center;gap:7px;padding:8px 14px;border-radius:9px;font-size:13.5px;
  font-weight:600;color:var(--muted);transition:.15s}
.tab svg{width:16px;height:16px}
.tab:hover{color:var(--ink-2);background:var(--line-2)}
.tab.is-on{color:var(--brand-deep);background:var(--brand-tint)}
.nav__grow{flex:1}
.nav__search{display:flex;align-items:center;gap:8px;width:290px;height:38px;padding:0 12px;
  background:var(--card);border:1px solid var(--line);border-radius:10px;transition:.15s}
.nav__search:focus-within{border-color:var(--brand);box-shadow:0 0 0 3px var(--brand-ring)}
.nav__search svg{width:15px;height:15px;color:var(--faint);flex:none}
.nav__search input{border:none;outline:none;width:100%;font-family:inherit;font-size:13px;color:var(--ink);background:none}
.nav__ic{position:relative;display:grid;place-items:center;width:38px;height:38px;border-radius:10px;color:var(--muted);transition:.15s}
.nav__ic:hover{background:var(--line-2);color:var(--ink)}
.nav__ic svg{width:18px;height:18px}
.nav__dot{position:absolute;top:8px;right:9px;width:7px;height:7px;border-radius:50%;background:var(--red);border:1.5px solid var(--bg)}
.nav__me{display:flex;align-items:center;gap:7px;padding:4px 8px 4px 4px;border-radius:30px;transition:.15s}
.nav__me:hover{background:var(--line-2)}
.nav__av{display:grid;place-items:center;width:30px;height:30px;border-radius:50%;
  background:linear-gradient(150deg,#2F9E5B,var(--brand-deep));color:#fff;font-size:11.5px;font-weight:700}
.nav__me svg{width:15px;height:15px;color:var(--muted)}

/* ---------- VIEWS ---------- */
.view{animation:rise .38s cubic-bezier(.22,1,.36,1)}
@keyframes rise{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

/* ---------- PAGE HEAD ---------- */
.phead{display:flex;justify-content:space-between;align-items:flex-end;gap:20px;padding:26px 0 18px}
.phead__eyebrow{display:flex;align-items:center;gap:7px;font-size:11px;font-weight:700;letter-spacing:.13em;
  text-transform:uppercase;color:var(--brand);margin-bottom:8px}
.phead__eyebrow .live{width:7px;height:7px;border-radius:50%;background:var(--brand);position:relative}
.phead__eyebrow .live::after{content:"";position:absolute;inset:-4px;border-radius:50%;background:var(--brand);opacity:.4;animation:pulse 2s infinite}
@keyframes pulse{0%{transform:scale(.7);opacity:.5}100%{transform:scale(2.4);opacity:0}}
.phead h1{font-family:var(--disp);font-weight:800;font-size:27px;letter-spacing:-.025em;margin:0 0 7px}
.phead__sub{font-size:13px;color:var(--muted);margin:0;display:flex;align-items:center;gap:9px;flex-wrap:wrap}
.chain{display:inline-flex;align-items:center;gap:9px}
.chain b{font-weight:600;color:var(--ink-2);font-size:12.5px}
.chain i{width:4px;height:4px;border-radius:50%;background:var(--slate);font-style:normal}
.seg{display:flex;gap:3px;padding:4px;background:var(--card);border:1px solid var(--line);border-radius:11px;flex:none}
.seg__b{padding:7px 13px;border-radius:8px;font-size:12.5px;font-weight:600;color:var(--muted);transition:.15s;display:flex;align-items:center;gap:6px;white-space:nowrap}
.seg__b svg{width:14px;height:14px}
.seg__b:hover{color:var(--ink)}
.seg__b.is-on{background:var(--brand);color:#fff;box-shadow:0 2px 8px var(--brand-ring)}

/* ---------- KPI (icon + value + label only) ---------- */
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:20px}
.kpi{position:relative;background:var(--card);border:1px solid var(--line);border-radius:var(--r);
  padding:20px 20px 18px;box-shadow:var(--shadow);transition:.2s}
.kpi:hover{transform:translateY(-3px);box-shadow:var(--shadow-lg);border-color:var(--slate)}
.kpi__ic{display:grid;place-items:center;width:42px;height:42px;border-radius:12px}
.kpi__ic svg{width:21px;height:21px}
.kpi__ic.indigo{background:var(--brand-tint);color:var(--brand-deep)}
.kpi__ic.green{background:var(--ok-tint);color:var(--ok)}
.kpi__ic.purple{background:#EFE9FB;color:#6D3FBF}
.kpi__ic.orange{background:var(--amber-tint);color:var(--amber)}
.kpi__val{font-family:var(--disp);font-weight:800;font-size:32px;letter-spacing:-.03em;margin-top:16px;line-height:1}
.kpi__lbl{font-size:12.5px;color:var(--muted);font-weight:500;margin-top:6px}

/* ---------- CARD / TABLE ---------- */
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--r);box-shadow:var(--shadow);overflow:hidden}
.card__head{display:flex;justify-content:space-between;align-items:center;gap:14px;padding:17px 20px;border-bottom:1px solid var(--line-2)}
.card__title{font-family:var(--disp);font-weight:700;font-size:15.5px;letter-spacing:-.01em;display:flex;align-items:center;gap:8px}
.count{font-size:12px;font-weight:600;color:var(--muted);background:var(--line-2);padding:2px 8px;border-radius:20px}
.card__tools{display:flex;gap:9px}
.field{display:flex;align-items:center;gap:8px;width:250px;height:36px;padding:0 11px;background:var(--bg);
  border:1px solid var(--line);border-radius:9px;transition:.15s}
.field:focus-within{border-color:var(--brand);background:var(--card);box-shadow:0 0 0 3px var(--brand-ring)}
.field svg{width:15px;height:15px;color:var(--faint);flex:none}
.field input{border:none;outline:none;background:none;width:100%;font-family:inherit;font-size:12.5px;color:var(--ink)}
.btn{display:flex;align-items:center;gap:7px;height:36px;padding:0 13px;border:1px solid var(--line);
  border-radius:9px;background:var(--card);font-size:12.5px;font-weight:600;color:var(--ink-2);transition:.15s}
.btn svg{width:15px;height:15px;color:var(--muted)}
.btn:hover{border-color:var(--slate);background:var(--bg)}

.twrap{overflow-x:auto}
.tbl{width:100%;border-collapse:collapse;min-width:820px}
.tbl thead th{text-align:left;font-size:10.5px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;
  color:var(--faint);padding:12px 16px;background:var(--line-2);white-space:nowrap}
.tbl thead th:first-child{padding-left:20px}
.tbl tbody td{padding:14px 16px;font-size:13px;color:var(--ink-2);border-bottom:1px solid var(--line-2);vertical-align:middle}
.tbl tbody td:first-child{padding-left:20px}
.tbl tbody tr{transition:.12s;cursor:pointer}
.tbl tbody tr:hover{background:var(--brand-tint)}
.tbl tbody tr:hover .go{opacity:1;transform:translateX(0)}
.tbl tbody tr:last-child td{border-bottom:none}
.a-num{font-family:var(--mono);font-weight:600;color:var(--brand-deep);font-size:12.5px}
.a-prod{font-weight:600;color:var(--ink)}
.store2{font-size:11px;color:var(--faint);margin-top:2px}
.uom{font-family:var(--mono);font-size:11.5px;color:var(--muted)}
.bnr{display:inline-block;font-size:11px;font-weight:600;padding:3px 9px;border-radius:6px;background:var(--brand-tint);color:var(--brand-deep);white-space:nowrap}
.issue{display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:600;padding:4px 10px;border-radius:20px;white-space:nowrap}
.issue svg{width:13px;height:13px}
.issue.red{background:var(--red-tint);color:var(--red)}
.issue.amber{background:var(--amber-tint);color:var(--amber)}
.tm{font-size:12px;color:var(--faint);font-family:var(--mono)}
.go{display:grid;place-items:center;width:26px;height:26px;border-radius:7px;color:var(--brand-deep);
  background:var(--brand-tint);opacity:0;transform:translateX(-4px);transition:.15s}
.go svg{width:15px;height:15px}
.col-r{text-align:right}
.tbl .empty{text-align:center;padding:44px;color:var(--faint);font-size:13px}

.pager{display:flex;justify-content:space-between;align-items:center;padding:14px 20px;border-top:1px solid var(--line-2)}
.pager__info{font-size:12.5px;color:var(--muted)}
.pager__c{display:flex;gap:5px;align-items:center}
.pg{min-width:32px;height:32px;padding:0 7px;border-radius:8px;font-size:12.5px;font-weight:600;color:var(--ink-2);border:1px solid transparent;transition:.13s;display:grid;place-items:center}
.pg svg{width:15px;height:15px}
.pg:hover:not(:disabled){background:var(--line-2)}
.pg.is-on{background:var(--brand);color:#fff}
.pg:disabled{color:var(--slate);cursor:not-allowed}

/* ---------- INVESTIGATION: INPUT PANE ---------- */
.invzero{max-width:540px;margin:26px auto 0;background:var(--card);border:1px solid var(--line);
  border-radius:18px;box-shadow:var(--shadow);padding:36px 40px 32px;text-align:center}
.invzero__art{width:210px;margin:0 auto 4px}
.invzero h2{font-family:var(--disp);font-weight:800;font-size:22px;letter-spacing:-.02em;margin:6px 0 8px}
.invzero p{font-size:13.5px;color:var(--muted);margin:0 auto;max-width:400px;line-height:1.55}
.invform{display:flex;flex-direction:column;gap:15px;text-align:left;margin-top:26px}
.invfield label{font-size:12px;font-weight:600;color:var(--ink-2);display:block;margin-bottom:7px}
.invfield input,.invfield select{width:100%;height:46px;padding:0 15px;border:1px solid var(--line);
  border-radius:11px;font-family:inherit;font-size:14px;color:var(--ink);background:var(--card);transition:.15s;outline:none;appearance:none}
.invfield input::placeholder{color:var(--faint)}
.invfield input:focus,.invfield select:focus{border-color:var(--brand);box-shadow:0 0 0 3px var(--brand-ring)}
.invfield.combo .combo__box{position:relative}
.invfield.combo .combo__box::after{content:"";position:absolute;right:16px;top:19px;width:8px;height:8px;border-right:2px solid var(--faint);border-bottom:2px solid var(--faint);transform:rotate(45deg);pointer-events:none}
.combo__list{position:absolute;top:calc(100% + 6px);left:0;right:0;background:var(--card);border:1px solid var(--line);border-radius:11px;box-shadow:var(--shadow-lg);max-height:210px;overflow-y:auto;z-index:30;padding:5px;display:none;list-style:none;margin:0}
.combo__list.show{display:block}
.combo__list li{padding:9px 12px;border-radius:8px;font-size:13px;color:var(--ink-2);cursor:pointer}
.combo__list li:hover{background:var(--brand-tint);color:var(--brand-deep)}
.combo__list li.combo__none{color:var(--faint);cursor:default}
.combo__list li.combo__none:hover{background:none;color:var(--faint)}
.invbtn{height:48px;border-radius:11px;background:var(--brand);color:#fff;font-family:var(--disp);font-weight:700;
  font-size:14px;display:flex;align-items:center;justify-content:center;gap:9px;transition:.18s;box-shadow:0 4px 14px var(--brand-ring)}
.invbtn svg{width:17px;height:17px}
.invbtn:hover{background:var(--brand-deep);transform:translateY(-1px)}
.inverr{display:none;align-items:center;gap:7px;color:var(--red);font-size:12.5px;font-weight:500;background:var(--red-tint);padding:9px 12px;border-radius:9px}
.inverr svg{width:15px;height:15px;flex:none}
.inverr.show{display:flex}

/* ---------- INVESTIGATION: RESULT ---------- */
.ihead{display:flex;align-items:center;gap:12px;padding:24px 0 18px;flex-wrap:wrap}
.back{display:flex;align-items:center;gap:7px;height:36px;padding:0 13px 0 10px;border-radius:9px;
  border:1px solid var(--line);background:var(--card);font-size:13px;font-weight:600;color:var(--ink-2);transition:.15s}
.back svg{width:16px;height:16px;color:var(--muted)}
.back:hover{border-color:var(--slate);background:var(--bg);transform:translateX(-2px)}
.ihead__t{font-family:var(--disp);font-weight:800;font-size:19px;letter-spacing:-.02em}
.ihead__t span{color:var(--brand-deep)}
.ihead__grow{flex:1}

.igrid{display:grid;grid-template-columns:300px 1fr;gap:18px;align-items:start}
.info__t,.flow__t{font-family:var(--disp);font-weight:700;font-size:14px;letter-spacing:-.01em}
.info{padding:18px}
.info__t{margin-bottom:6px}
.irow{display:flex;justify-content:space-between;gap:12px;padding:11px 0;border-bottom:1px solid var(--line-2)}
.irow:last-child{border-bottom:none;padding-bottom:0}
.irow__k{font-size:12px;color:var(--muted);flex:none}
.irow__v{font-size:12.5px;font-weight:600;color:var(--ink);text-align:right}
.irow__v.mono{font-family:var(--mono);font-weight:600}

.flow{padding:0}
.flow__head{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:17px 20px;border-bottom:1px solid var(--line-2);flex-wrap:wrap}
.legend{display:flex;gap:15px}
.legend__i{display:flex;align-items:center;gap:6px;font-size:11.5px;font-weight:600;color:var(--muted)}
.legend__d{width:9px;height:9px;border-radius:50%}

/* pipeline — signature */
.pipe{display:flex;align-items:stretch;gap:0;padding:30px 20px 22px;overflow-x:auto}
.pnode{flex:1;min-width:118px;position:relative;display:flex;flex-direction:column;align-items:center;text-align:center}
.pnode__dot{position:relative;width:52px;height:52px;border-radius:15px;display:grid;place-items:center;
  border:2px solid var(--line);background:var(--card);z-index:2;transition:.2s;opacity:0;transform:scale(.6)}
.pnode__dot svg{width:22px;height:22px}
.pnode.ok .pnode__dot{border-color:var(--ok);background:var(--ok-tint);color:var(--ok)}
.pnode.bad .pnode__dot{border-color:var(--red);background:var(--red-tint);color:var(--red)}
.pnode.div .pnode__dot{box-shadow:0 0 0 5px rgba(214,45,45,.14)}
.pnode.div .pnode__dot::after{content:"";position:absolute;inset:-2px;border-radius:15px;border:2px solid var(--red);animation:ring 1.8s ease-out infinite}
@keyframes ring{0%{transform:scale(1);opacity:.7}100%{transform:scale(1.5);opacity:0}}
.pnode__name{font-family:var(--disp);font-weight:700;font-size:13px;margin-top:11px}
.pnode__price{font-family:var(--mono);font-weight:600;font-size:15px;margin-top:5px}
.pnode.bad .pnode__price{color:var(--red)} .pnode.ok .pnode__price{color:var(--ink)}
.pnode__time{font-size:10.5px;color:var(--faint);margin-top:4px;line-height:1.4}
.pnode__flag{position:absolute;top:-18px;display:flex;align-items:center;gap:4px;font-size:9.5px;font-weight:800;
  letter-spacing:.04em;text-transform:uppercase;color:var(--red);background:var(--red-tint);padding:3px 7px;border-radius:20px;white-space:nowrap}
.pnode__flag svg{width:11px;height:11px}
.pconn{position:absolute;top:26px;left:calc(50% + 26px);width:calc(100% - 52px);height:2px;background:var(--line);z-index:1;overflow:hidden}
.pconn::before{content:"";position:absolute;inset:0;background:repeating-linear-gradient(90deg,var(--brand) 0 6px,transparent 6px 12px);
  background-size:200% 100%;animation:flow 1.1s linear infinite;opacity:.9}
.pconn.bad::before{background-image:repeating-linear-gradient(90deg,var(--red) 0 6px,transparent 6px 12px)}
@keyframes flow{to{background-position:-24px 0}}
.pnode:last-child .pconn{display:none}
.pnode.show .pnode__dot{opacity:1;transform:scale(1)}

/* comparison */
.cmp-wrap{border-top:1px solid var(--line-2);padding:6px 0 4px;overflow-x:auto}
.cmp{width:100%;border-collapse:collapse;min-width:860px}
.cmp thead th{text-align:left;font-size:10px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;
  color:var(--faint);padding:12px 16px;white-space:nowrap}
.cmp thead th:first-child{padding-left:20px}
.cmp tbody td{padding:13px 16px;font-size:12.5px;border-top:1px solid var(--line-2)}
.cmp tbody td:first-child{padding-left:20px}
.cmp .sys{font-family:var(--disp);font-weight:700;font-size:13px;color:var(--ink)}
.cmp .mono{font-family:var(--mono);font-size:12px;color:var(--muted)}
.cmp .money{font-family:var(--mono);font-weight:600;color:var(--ink)}
.cmp .money.bad{color:var(--red);background:var(--red-tint);border-radius:6px;padding:2px 7px}
.cmp .dash{color:var(--slate)}
.cmp tr.row-div{background:var(--red-tint)}
.pill{display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:700;padding:4px 9px;border-radius:20px}
.pill svg{width:12px;height:12px}
.pill.ok{background:var(--ok-tint);color:var(--ok)}
.pill.bad{background:var(--red-tint);color:var(--red)}

@media(max-width:1080px){
  .kpis{grid-template-columns:repeat(2,1fr)}
  .igrid{grid-template-columns:1fr}
  .nav__search{display:none}
}
@media(max-width:640px){.kpis{grid-template-columns:1fr}.tabs{display:none}.invzero{padding:28px 22px}}
</style>

<div class="ppr">
  <!-- NAV -->
  <nav class="nav">
    <div class="brand">
      <img class="brand__logo" src="data:image/png;base64,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" alt="Sobeys"/>
      <span class="brand__sep"></span>
      <div>
        <div class="brand__word">PriceGuard</div>
        <div class="brand__sub">Pricing Discrepancy Tracker</div>
      </div>
    </div>
    <div class="nav__div"></div>
    <div class="tabs">
      <button class="tab is-on" data-tab="dash"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="9"/><rect x="14" y="3" width="7" height="5"/><rect x="14" y="12" width="7" height="9"/><rect x="3" y="16" width="7" height="5"/></svg>Dashboard</button>
      <button class="tab" data-tab="inv"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>Investigations</button>
    </div>
    <div class="nav__grow"></div>
    <div class="nav__search">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      <input placeholder="Search articles, stores, promotions…"/>
    </div>
    <button class="nav__ic"><span class="nav__dot"></span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg></button>
    <button class="nav__ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg></button>
    <button class="nav__me"><span class="nav__av">GK</span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></button>
  </nav>

  <!-- DASHBOARD VIEW -->
  <section id="v-dash" class="view">
    <div class="phead">
      <div>
        <div class="phead__eyebrow"><span class="live"></span>Live monitoring</div>
        <h1>Pricing Ecosystem Overview</h1>
        <p class="phead__sub">Tracking price consistency across
          <span class="chain"><b>SAP</b><i></i><b>DIH</b><i></i><b>SAIL</b><i></i><b>Algolia</b><i></i><b>Website</b></span></p>
      </div>
      <div class="seg" id="seg">
        <button class="seg__b is-on">Today</button>
        <button class="seg__b">Last 7 days</button>
        <button class="seg__b">Last 30 days</button>
        <button class="seg__b"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>Custom</button>
      </div>
    </div>

    <div class="kpis" id="kpis"></div>

    <div class="card">
      <div class="card__head">
        <div class="card__title">Monitored Articles &amp; Stores<span class="count" id="rowcount"></span></div>
        <div class="card__tools">
          <div class="field">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
            <input id="search" placeholder="Search by article, product, store or banner…"/>
          </div>
          <button class="btn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>Filters</button>
        </div>
      </div>
      <div class="twrap">
        <table class="tbl">
          <thead><tr>
            <th>Article</th><th>Product</th><th>Store</th><th>UOM</th><th>Banner</th>
            <th>Issue</th><th>Last Detected</th><th class="col-r">Open</th>
          </tr></thead>
          <tbody id="rows"></tbody>
        </table>
      </div>
      <div class="pager">
        <span class="pager__info" id="pinfo"></span>
        <div class="pager__c" id="pager"></div>
      </div>
    </div>
  </section>

  <!-- INVESTIGATION VIEW (input pane OR result) -->
  <section id="v-inv" class="view" style="display:none"></section>
</div>

<script>
// ---------------- ICONS ----------------
const I = {
  cube:'<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/>',
  store:'<path d="M3 9l1-5h16l1 5"/><path d="M4 9v11a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1V9"/><path d="M3 9a3 3 0 0 0 6 0 3 3 0 0 0 6 0 3 3 0 0 0 6 0"/><path d="M9 21v-6h6v6"/>',
  tag:'<path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/>',
  globe:'<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
  alert:'<circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/>',
  tri:'<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
  check:'<polyline points="20 6 9 17 4 12"/>',
  x:'<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>',
  right:'<polyline points="9 18 15 12 9 6"/>',
  left:'<polyline points="15 18 9 12 15 6"/>',
  back:'<line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/>',
  refresh:'<polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/>',
  search:'<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>',
};
const svg=(n,w=2)=>`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round">${I[n]||''}</svg>`;
const money=v=>'$'+v.toFixed(2);

// ---------------- DATA ----------------
const KPIS=[
  {ic:'cube',tone:'indigo',val:'342',lbl:'Articles affected'},
  {ic:'store',tone:'green',val:'87',lbl:'Stores affected'},
  {ic:'tag',tone:'purple',val:'24',lbl:'Banners affected'},
  {ic:'globe',tone:'orange',val:'8',lbl:'Regions affected'},
];

// pipeline nodes: SAP -> DIH -> SAIL -> Algolia -> Website
const P=(sap,dih,sail,alg,web)=>[
  {name:'SAP',...sap,corr:'SAP'},{name:'DIH',...dih,corr:'DIH'},{name:'SAIL',...sail,corr:'SAIL'},
  {name:'Algolia',...alg,corr:'ALG'},{name:'Website',...web,corr:'WEB'}];
const N=(price,ok,time,promo=null)=>({price,promo,status:ok?'ok':'bad',time});

// two issue types only: Price mismatch / Promotion missing
const TEMPLATES={
  price_sail:{issue:'Price mismatch',tone:'red',
    pipe:P(N(6.00,1,'06:00'),N(6.00,1,'06:15'),N(6.68,0,'06:30'),N(6.68,0,'06:45'),N(6.68,0,'Live (cached)'))},
  price_algolia:{issue:'Price mismatch',tone:'red',
    pipe:P(N(2.99,1,'05:00'),N(2.99,1,'05:15'),N(2.99,1,'05:30'),N(3.49,0,'04:30'),N(3.49,0,'Live (cached)'))},
  price_dih:{issue:'Price mismatch',tone:'red',
    pipe:P(N(5.49,1,'06:00'),N(4.99,0,'06:15'),N(4.99,0,'06:30'),N(4.99,0,'06:45'),N(4.99,0,'Live (cached)'))},
  promo_missing:{issue:'Promotion missing',tone:'amber',
    pipe:P(N(8.99,1,'07:00',7.49),N(8.99,0,'07:15'),N(8.99,0,'07:30'),N(8.99,0,'07:45'),N(8.99,0,'Live (cached)'))},
};

const BANNERS=['Sobeys','FreshCo','Safeway','Foodland','IGA','Farm Boy','Longo\u2019s','Thrifty Foods'];
const REGIONS={Sobeys:'Atlantic',FreshCo:'Ontario',Safeway:'Western',Foodland:'Ontario',IGA:'Quebec','Farm Boy':'Ontario','Longo\u2019s':'Ontario','Thrifty Foods':'Western'};
const PRODS=['Best Buy Peppers 1.14 kg','Organic Spinach 284 g','Compliments 2% Milk 2 L','Bananas 1.38 kg','Chicken Breast 1 kg','Compliments Aged Cheddar 400 g','Sensations Sourdough 500 g','Roma Tomatoes 1 kg','Lean Ground Beef 1 lb','Free-Run Eggs 12 ct','Avocados 5 ct Bag','Atlantic Salmon 340 g','Greek Yogurt 750 g','Cavendish Fries 1 kg','Gala Apples 3 lb','Natural Peanut Butter 1 kg','Basmati Rice 2 kg','Not-From-Concentrate OJ 1.75 L','Cheerios 570 g','Baby Spinach 142 g'];
const STORES=[['9866','Parliament & Dundas'],['9871','Leslie & Lakeshore'],['9867','Queen & Cladetona'],['9868','Dufferin & Dupont'],['9852','Bloor & Dundas'],['9903','King & Spadina'],['9915','Yonge & Eglinton'],['9922','Bathurst & College']];
const TKEYS=['price_sail','promo_missing','price_algolia','price_dih','price_sail','price_algolia','promo_missing','price_dih','price_sail','promo_missing','price_algolia','price_dih','price_sail','promo_missing','price_algolia','price_dih','price_sail','promo_missing','price_algolia','price_dih'];

const ARTICLES=TKEYS.map((k,i)=>{
  const t=TEMPLATES[k], bn=BANNERS[i%BANNERS.length], st=STORES[i%STORES.length];
  const hh=String(6+(i%12)).padStart(2,'0'), mm=String((i*7)%60).padStart(2,'0');
  return {id:String(1335363+i),product:PRODS[i%PRODS.length],store:st[0],storeName:'FreshCo '+st[1],
    uom:'EA',banner:bn,region:REGIONS[bn]||'National',tkey:k,issue:t.issue,tone:t.tone,detected:`2024-07-10 ${hh}:${mm} UTC`};
});

// deterministic promo number (only shown where a promo price exists)
function hash(s){let h=0;for(let i=0;i<s.length;i++)h=(h*31+s.charCodeAt(i))>>>0;return h;}
function promoNo(id,sys){return 'PR-'+String(100000+hash(id+sys)%899999);}

let state={query:'',page:1,size:8};

// ---------------- KPI ----------------
function renderKPIs(){
  document.getElementById('kpis').innerHTML=KPIS.map(k=>`
    <div class="kpi">
      <div class="kpi__ic ${k.tone}">${svg(k.ic)}</div>
      <div class="kpi__val">${k.val}</div>
      <div class="kpi__lbl">${k.lbl}</div>
    </div>`).join('');
}

// ---------------- TABLE ----------------
function filtered(){
  const q=state.query.toLowerCase();
  return ARTICLES.filter(a=>!q||[a.id,a.product,a.store,a.storeName,a.banner,a.issue].join(' ').toLowerCase().includes(q));
}
function issueTag(a){return `<span class="issue ${a.tone}">${svg('alert')}${a.issue}</span>`;}
function renderTable(){
  const data=filtered(), total=data.length, pages=Math.max(1,Math.ceil(total/state.size));
  if(state.page>pages)state.page=pages;
  const start=(state.page-1)*state.size, slice=data.slice(start,start+state.size);
  document.getElementById('rowcount').textContent=`${total} items`;
  const tb=document.getElementById('rows');
  tb.innerHTML=slice.length?slice.map(a=>`
    <tr data-id="${a.id}">
      <td><span class="a-num">${a.id}</span></td>
      <td><div class="a-prod">${a.product}</div></td>
      <td>${a.store}<div class="store2">${a.storeName}</div></td>
      <td><span class="uom">${a.uom}</span></td>
      <td><span class="bnr">${a.banner}</span></td>
      <td>${issueTag(a)}</td>
      <td><span class="tm">${a.detected}</span></td>
      <td class="col-r"><span class="go">${svg('right')}</span></td>
    </tr>`).join(''):`<tr><td colspan="8" class="empty">No articles match "${state.query}".</td></tr>`;
  tb.querySelectorAll('tr[data-id]').forEach(r=>r.onclick=()=>openInvestigation(r.dataset.id));
  const from=total?start+1:0, to=Math.min(start+state.size,total);
  document.getElementById('pinfo').textContent=`Showing ${from}\u2013${to} of ${total} articles`;
  const pg=document.getElementById('pager');let h=`<button class="pg" ${state.page===1?'disabled':''} data-go="prev">${svg('left')}</button>`;
  pageList(state.page,pages).forEach(n=>h+=n==='…'?`<span class="pg" style="cursor:default">…</span>`:`<button class="pg ${n===state.page?'is-on':''}" data-go="${n}">${n}</button>`);
  h+=`<button class="pg" ${state.page===pages?'disabled':''} data-go="next">${svg('right')}</button>`;
  pg.innerHTML=h;
  pg.querySelectorAll('[data-go]').forEach(b=>b.onclick=()=>{const g=b.dataset.go;
    if(g==='prev')state.page--;else if(g==='next')state.page++;else state.page=+g;renderTable();});
}
function pageList(cur,tot){if(tot<=7)return Array.from({length:tot},(_,i)=>i+1);
  const s=new Set([1,2,tot-1,tot,cur-1,cur,cur+1]);const arr=[...s].filter(n=>n>=1&&n<=tot).sort((a,b)=>a-b);
  const out=[];arr.forEach((n,i)=>{if(i&&n-arr[i-1]>1)out.push('…');out.push(n);});return out;}

// ---------------- INVESTIGATION: INPUT PANE ----------------
const ART=`<svg class="invzero__art" viewBox="0 0 240 150" fill="none" xmlns="http://www.w3.org/2000/svg">
  <line x1="34" y1="72" x2="206" y2="72" stroke="#E4EAE6" stroke-width="3"/>
  <circle cx="40" cy="72" r="13" fill="#E9F5EE" stroke="#00853F" stroke-width="2.5"/>
  <circle cx="95" cy="72" r="13" fill="#E9F5EE" stroke="#00853F" stroke-width="2.5"/>
  <circle cx="150" cy="72" r="13" fill="#FCECEC" stroke="#D62D2D" stroke-width="2.5"/>
  <circle cx="205" cy="72" r="13" fill="#E9F5EE" stroke="#00853F" stroke-width="2.5"/>
  <path d="M147 69l6 6M153 69l-6 6" stroke="#D62D2D" stroke-width="2.2" stroke-linecap="round"/>
  <circle cx="150" cy="64" r="30" fill="#FFFFFF" fill-opacity="0.55" stroke="#006B33" stroke-width="4"/>
  <line x1="172" y1="86" x2="190" y2="104" stroke="#006B33" stroke-width="6" stroke-linecap="round"/>
</svg>`;

const UOMS=[{value:'EA',label:'EA — Each'},{value:'KG',label:'KG — Kilogram'},{value:'LB',label:'LB — Pound'},{value:'G',label:'G — Gram'},{value:'CS',label:'CS — Case'},{value:'PK',label:'PK — Pack'}];
// typable autocomplete: filters as you type, click to fill
function makeCombo(input,list,options){
  const render=(q='')=>{
    const f=options.filter(o=>o.label.toLowerCase().includes(q.toLowerCase()));
    list.innerHTML=f.length?f.map(o=>`<li data-v="${o.value}">${o.label}</li>`).join(''):'<li class="combo__none">No matches</li>';
    list.querySelectorAll('li[data-v]').forEach(li=>li.addEventListener('mousedown',e=>{
      e.preventDefault();input.value=li.textContent;list.classList.remove('show');}));
    list.classList.add('show');
  };
  input.addEventListener('focus',()=>render(input.value));
  input.addEventListener('input',()=>render(input.value));
  input.addEventListener('blur',()=>setTimeout(()=>list.classList.remove('show'),120));
}
function showInvInput(){
  setTab('inv');
  document.getElementById('v-inv').innerHTML=`
    <div class="ihead">
      <button class="back" onclick="showDash()">${svg('back')}Dashboard</button>
      <div class="ihead__t">New investigation</div>
    </div>
    <div class="invzero">
      ${ART}
      <h2>Trace a price discrepancy</h2>
      <p>Enter an article number to follow its price through every system — from SAP all the way to the storefront.</p>
      <div class="invform">
        <div class="invfield">
          <label for="inv-art">Article number</label>
          <input id="inv-art" inputmode="numeric" placeholder="e.g. 1335363" autocomplete="off"/>
        </div>
        <div class="invfield combo">
          <label for="inv-store">Store <span style="color:var(--faint);font-weight:500">(optional)</span></label>
          <div class="combo__box">
            <input id="inv-store" placeholder="Start typing a store…" autocomplete="off"/>
            <ul class="combo__list" id="inv-store-list"></ul>
          </div>
        </div>
        <div class="invfield combo">
          <label for="inv-uom">Unit of measure <span style="color:var(--faint);font-weight:500">(optional)</span></label>
          <div class="combo__box">
            <input id="inv-uom" placeholder="Start typing a UOM…" autocomplete="off"/>
            <ul class="combo__list" id="inv-uom-list"></ul>
          </div>
        </div>
        <div class="inverr" id="inv-err">${svg('alert')}<span id="inv-err-t"></span></div>
        <button class="invbtn" id="inv-go">${svg('search')}Trace price flow</button>
      </div>
    </div>`;
  document.getElementById('v-dash').style.display='none';
  document.getElementById('v-inv').style.display='block';
  window.scrollTo(0,0);

  const go=()=>{
    const v=document.getElementById('inv-art').value.trim();
    const err=document.getElementById('inv-err'), errt=document.getElementById('inv-err-t');
    if(!v){errt.textContent='Please enter an article number.';err.classList.add('show');return;}
    if(ARTICLES.find(a=>a.id===v)){openInvestigation(v);}
    else{errt.textContent=`No discrepancy found for article ${v}. Try one of the examples below.`;err.classList.add('show');}
  };
  document.getElementById('inv-go').onclick=go;
  document.getElementById('inv-art').addEventListener('keydown',e=>{if(e.key==='Enter')go();});
  makeCombo(document.getElementById('inv-store'),document.getElementById('inv-store-list'),
    STORES.map(s=>({value:s[0],label:`${s[0]} · FreshCo ${s[1]}`})));
  makeCombo(document.getElementById('inv-uom'),document.getElementById('inv-uom-list'),UOMS);
}

// ---------------- INVESTIGATION: RESULT ----------------
function firstBad(pipe){return pipe.findIndex(n=>n.status==='bad');}
function openInvestigation(id){
  setTab('inv');
  const a=ARTICLES.find(x=>x.id===id); if(!a){showInvInput();return;}
  const t=TEMPLATES[a.tkey], pipe=t.pipe, div=firstBad(pipe);

  const info=[
    ['Article number',a.id],['Product',a.product],['Store',`${a.store} · ${a.storeName}`],
    ['UOM',a.uom],['Banner',a.banner],['Region',a.region],['Detected',a.detected]];

  const pipeHTML=pipe.map((n,i)=>{
    const badConn=i>=div&&div!==-1;
    const flag=i===div&&div!==-1?`<div class="pnode__flag">${svg('tri')}Divergence</div>`:'';
    return `<div class="pnode ${n.status} ${i===div&&div!==-1?'div':''}">
      ${flag}
      <div class="pnode__dot">${svg(n.status==='ok'?'check':'x',2.6)}</div>
      <div class="pnode__name">${n.name}</div>
      <div class="pnode__price">${money(n.promo??n.price)}${n.promo?' <span style="color:var(--faint);text-decoration:line-through;font-size:11px">'+money(n.price)+'</span>':''}</div>
      <div class="pnode__time">${n.time}</div>
      ${i<pipe.length-1?`<div class="pconn ${badConn?'bad':''}"></div>`:''}
    </div>`;
  }).join('');

  const cmpHTML=pipe.map((n,i)=>`
    <tr class="${i===div&&div!==-1?'row-div':''}">
      <td><span class="sys">${n.name}</span></td>
      <td><span class="money ${n.status==='bad'&&i>=div?'bad':''}">${money(n.price)}</span></td>
      <td>${n.promo?`<span class="money">${money(n.promo)}</span>`:'<span class="dash">—</span>'}</td>
      <td>${n.promo?`<span class="mono">${promoNo(a.id,n.name)}</span>`:'<span class="dash">—</span>'}</td>
      <td class="mono">${n.corr}-${a.id}</td>
      <td class="mono">${n.time}${/Live|cached/i.test(n.time)?'':' UTC'}</td>
      <td>${n.status==='ok'?`<span class="pill ok">${svg('check')}Match</span>`:`<span class="pill bad">${svg('x')}Mismatch</span>`}</td>
    </tr>`).join('');

  document.getElementById('v-inv').innerHTML=`
    <div class="ihead">
      <button class="back" onclick="showInvInput()">${svg('search')}New search</button>
      <div class="ihead__t">Article <span>${a.id}</span> · ${a.product}</div>
      <div class="ihead__grow"></div>
      <button class="btn" onclick="showDash()">${svg('back')}Dashboard</button>
      <button class="btn">${svg('refresh')}Refresh</button>
    </div>
    <div class="igrid">
      <div class="card info">
        <div class="info__t">Article information</div>
        ${info.map(([k,v])=>`<div class="irow"><span class="irow__k">${k}</span><span class="irow__v ${/number/i.test(k)?'mono':''}">${v}</span></div>`).join('')}
      </div>
      <div class="card flow">
        <div class="flow__head">
          <span class="flow__t">Data propagation flow</span>
          <div class="legend">
            <span class="legend__i"><span class="legend__d" style="background:var(--ok)"></span>Match</span>
            <span class="legend__i"><span class="legend__d" style="background:var(--red)"></span>Mismatch</span>
            <span class="legend__i"><span class="legend__d" style="background:var(--brand)"></span>Data flow</span>
          </div>
        </div>
        <div class="pipe" id="pipe">${pipeHTML}</div>
        <div class="cmp-wrap">
          <table class="cmp">
            <thead><tr><th>System</th><th>Regular Retail Price</th><th>Promotional Price</th><th>Promo #</th><th>Correlation ID</th><th>Updated</th><th>Status</th></tr></thead>
            <tbody>${cmpHTML}</tbody>
          </table>
        </div>
      </div>
    </div>`;

  document.getElementById('v-dash').style.display='none';
  document.getElementById('v-inv').style.display='block';
  window.scrollTo(0,0);
  [...document.querySelectorAll('#pipe .pnode')].forEach((n,i)=>setTimeout(()=>n.classList.add('show'),120+i*130));
}

function showDash(){
  setTab('dash');
  document.getElementById('v-inv').style.display='none';
  document.getElementById('v-dash').style.display='block';
  window.scrollTo(0,0);
}
function setTab(name){document.querySelectorAll('.tab').forEach(t=>t.classList.toggle('is-on',t.dataset.tab===name));}

// ---------------- WIRING ----------------
renderKPIs();renderTable();
document.getElementById('search').addEventListener('input',e=>{state.query=e.target.value;state.page=1;renderTable();});
document.querySelectorAll('#seg .seg__b').forEach(b=>b.onclick=()=>{
  document.querySelectorAll('#seg .seg__b').forEach(x=>x.classList.remove('is-on'));
  if(!b.querySelector('svg'))b.classList.add('is-on');});
document.querySelectorAll('.tab').forEach(t=>t.onclick=()=>{t.dataset.tab==='inv'?showInvInput():showDash();});
</script>
'''

components.html(UI, height=1180, scrolling=True)
