# ══════════════════════════════════════════════════════════════
# ICONS — inline SVG registry (Lucide-style, self-contained)
# No external icon fonts/CDNs so it works offline in Databricks Apps.
# Use icon("name") to get the raw <svg> string.
# ══════════════════════════════════════════════════════════════

_STROKE = ('fill="none" stroke="currentColor" stroke-width="2" '
           'stroke-linecap="round" stroke-linejoin="round"')

_ICONS = {
    "logo":        f'<svg viewBox="0 0 24 24" {_STROKE}><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>',
    "dashboard":   f'<svg viewBox="0 0 24 24" {_STROKE}><rect x="3" y="3" width="7" height="9"/><rect x="14" y="3" width="7" height="5"/><rect x="14" y="12" width="7" height="9"/><rect x="3" y="16" width="7" height="5"/></svg>',
    "search":      f'<svg viewBox="0 0 24 24" {_STROKE}><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>',
    "bell":        f'<svg viewBox="0 0 24 24" {_STROKE}><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>',
    "help":        f'<svg viewBox="0 0 24 24" {_STROKE}><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
    "chevron-down":f'<svg viewBox="0 0 24 24" {_STROKE}><polyline points="6 9 12 15 18 9"/></svg>',
    "chevron-left":f'<svg viewBox="0 0 24 24" {_STROKE}><polyline points="15 18 9 12 15 6"/></svg>',
    "chevron-right":f'<svg viewBox="0 0 24 24" {_STROKE}><polyline points="9 18 15 12 9 6"/></svg>',
    "calendar":    f'<svg viewBox="0 0 24 24" {_STROKE}><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>',
    "filter":      f'<svg viewBox="0 0 24 24" {_STROKE}><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>',
    "arrow-left":  f'<svg viewBox="0 0 24 24" {_STROKE}><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>',
    "arrow-right": f'<svg viewBox="0 0 24 24" {_STROKE}><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
    "refresh":     f'<svg viewBox="0 0 24 24" {_STROKE}><polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg>',
    "dots":        f'<svg viewBox="0 0 24 24" {_STROKE}><circle cx="12" cy="12" r="1"/><circle cx="12" cy="5" r="1"/><circle cx="12" cy="19" r="1"/></svg>',
    # KPI icons
    "cube":        f'<svg viewBox="0 0 24 24" {_STROKE}><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>',
    "store":       f'<svg viewBox="0 0 24 24" {_STROKE}><path d="M3 9l1-5h16l1 5"/><path d="M4 9v11a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1V9"/><path d="M3 9a3 3 0 0 0 6 0 3 3 0 0 0 6 0 3 3 0 0 0 6 0"/><path d="M9 21v-6h6v6"/></svg>',
    "tag":         f'<svg viewBox="0 0 24 24" {_STROKE}><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg>',
    "globe":       f'<svg viewBox="0 0 24 24" {_STROKE}><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>',
    # Status
    "alert-circle":  f'<svg viewBox="0 0 24 24" {_STROKE}><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>',
    "alert-triangle":f'<svg viewBox="0 0 24 24" {_STROKE}><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
    "check":       '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
    "x":           '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>',
    # Recommended-action icons (filled for a bit more weight)
    "fire":        '<svg viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M12 2c1 3 3 4 3 7a3 3 0 0 1-6 0c0-1 .3-1.8.7-2.5C8 8 6 10 6 13a6 6 0 0 0 12 0c0-4-3-7-6-11z"/></svg>',
    "urgent":      '<svg viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M13 2L3 14h7l-1 8 10-12h-7l1-8z"/></svg>',
    "monitor":     f'<svg viewBox="0 0 24 24" {_STROKE}><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>',
}


def icon(name: str) -> str:
    """Return the raw inline <svg> markup for a named icon."""
    return _ICONS.get(name, "")
