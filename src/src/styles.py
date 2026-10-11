"""
Dizayn fayli.
Ikki mavzu: Dark (tungi) va Light (kunduzgi).
Barcha ranglar, shriftlar, tugmalar shu yerda.
"""

# ============ RANGLAR PALITRASI ============

DARK = {
    "bg": "#0B1220",
    "surface": "#111C33",
    "surface2": "#16233F",
    "sidebar": "#0E1729",
    "border": "#1E2D4D",
    "text": "#E6EEF9",
    "text_dim": "#94A3B8",
    "accent": "#38BDF8",
    "accent2": "#F59E0B",
    "success": "#22C55E",
    "danger": "#EF4444",
    "hover": "#1B2A4A",
    "selected": "#1D4ED8",
}

LIGHT = {
    "bg": "#F1F5F9",
    "surface": "#FFFFFF",
    "surface2": "#F8FAFC",
    "sidebar": "#FFFFFF",
    "border": "#E2E8F0",
    "text": "#0F172A",
    "text_dim": "#64748B",
    "accent": "#2563EB",
    "accent2": "#D97706",
    "success": "#16A34A",
    "danger": "#DC2626",
    "hover": "#EFF6FF",
    "selected": "#2563EB",
}


def qss(theme: str = "dark") -> str:
    """
    Qt Style Sheet qaytaradi. theme: 'dark' yoki 'light'.
    Butun dastur dizayni shu yerda yozilgan.
    """
    c = DARK if theme == "dark" else LIGHT

    return f"""
/* ============ UMUMIY ============ */
* {{
    font-family: "Segoe UI", "Inter", "Arial", sans-serif;
    outline: none;
}}

QMainWindow, QDialog {{
    background: {c['bg']};
    color: {c['text']};
}}

QWidget {{
    color: {c['text']};
    font-size: 14px;
}}

/* ============ SIDEBAR ============ */
#Sidebar {{
    background: {c['sidebar']};
    border-right: 1px solid {c['border']};
}}

#TopicTree {{
    background: transparent;
    border: none;
    padding: 8px 4px;
    font-size: 13.5px;
}}

#TopicTree::item {{
    padding: 9px 10px;
    border-radius: 8px;
    margin: 2px 6px;
    color: {c['text']};
}}

#TopicTree::item:hover {{
    background: {c['hover']};
}}

#TopicTree::item:selected {{
    background: {c['accent']};
    color: white;
    font-weight: 600;
}}

/* ============ SEARCH ============ */
#SearchBox {{
    background: {c['surface2']};
    border: 1px solid {c['border']};
    border-radius: 10px;
    padding: 10px 14px;
    color: {c['text']};
    font-size: 13.5px;
}}

#SearchBox:focus {{
    border: 1.5px solid {c['accent']};
    background: {c['surface']};
}}

/* ============ CONTENT VIEWER ============ */
#ContentViewer {{
    background: {c['surface']};
    border: 1px solid {c['border']};
    border-radius: 14px;
    padding: 8px;
    color: {c['text']};
}}

/* ============ BUTTONS ============ */
QPushButton {{
    background: {c['surface2']};
    border: 1px solid {c['border']};
    border-radius: 9px;
    padding: 9px 16px;
    color: {c['text']};
    font-size: 13.5px;
    font-weight: 500;
}}

QPushButton:hover {{
    background: {c['hover']};
    border-color: {c['accent']};
}}

QPushButton:pressed {{
    background: {c['surface']};
}}

#PrimaryBtn {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 {c['accent']}, stop:1 #7C3AED);
    border: none;
    color: white;
    font-weight: 600;
    padding: 12px 20px;
    font-size: 14px;
}}

#PrimaryBtn:hover {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #0EA5E9, stop:1 #8B5CF6);
}}

/* ============ INPUTS ============ */
QLineEdit {{
    background: {c['surface2']};
    border: 1px solid {c['border']};
    border-radius: 9px;
    padding: 10px 14px;
    color: {c['text']};
    font-size: 14px;
    selection-background-color: {c['accent']};
}}

QLineEdit:focus {{
    border: 1.5px solid {c['accent']};
}}

QTextEdit, QTextBrowser {{
    background: transparent;
    border: none;
    color: {c['text']};
    font-size: 14.5px;
}}

/* ============ SCROLLBAR ============ */
QScrollBar:vertical {{
    background: transparent;
    width: 10px;
    margin: 4px;
}}

QScrollBar::handle:vertical {{
    background: {c['border']};
    border-radius: 5px;
    min-height: 30px;
}}

QScrollBar::handle:vertical:hover {{
    background: {c['accent']};
}}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    height: 0;
}}

QScrollBar:horizontal {{
    background: transparent;
    height: 10px;
    margin: 4px;
}}

QScrollBar::handle:horizontal {{
    background: {c['border']};
    border-radius: 5px;
    min-width: 30px;
}}

/* ============ STATUS BAR ============ */
QStatusBar {{
    background: {c['sidebar']};
    color: {c['text_dim']};
    border-top: 1px solid {c['border']};
    font-size: 12.5px;
}}

/* ============ SPLITTER ============ */
QSplitter::handle {{
    background: transparent;
    width: 6px;
}}

QSplitter::handle:hover {{
    background: {c['accent']};
}}

/* ============ PROGRESS ============ */
QProgressBar {{
    background: {c['surface2']};
    border: none;
    border-radius: 6px;
    height: 8px;
    text-align: center;
    color: transparent;
}}

QProgressBar::chunk {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 {c['accent']}, stop:1 {c['accent2']});
    border-radius: 6px;
}}

/* ============ MESSAGEBOX ============ */
QMessageBox {{
    background: {c['surface']};
}}

QMessageBox QLabel {{
    color: {c['text']};
    font-size: 14px;
}}

/* ============ TOOLTIP ============ */
QToolTip {{
    background: {c['surface']};
    color: {c['text']};
    border: 1px solid {c['accent']};
    border-radius: 6px;
    padding: 6px 10px;
    font-size: 13px;
}}
"""
