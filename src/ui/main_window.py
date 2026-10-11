"""
Asosiy dastur oynasi.
Chap sidebar (mundarija) + o'ng tomon (matn).
Yuqorida: logo, qidiruv, tema, profil.
"""
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QTextBrowser, QLineEdit,
    QPushButton, QMessageBox, QSplitter, QStatusBar, QProgressBar,
    QFrame, QMenu, QToolButton,
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QGuiApplication, QAction

from data.chapters import STRUCTURE, get_total_sections
from data.topics import get_topic, get_topics_count
from styles import qss


# ==================== HTML SHABLON ====================

HTML_WRAP = """
<style>
    body {
        color: {text};
        font-size: 15px;
        line-height: 1.75;
        margin: 12px;
        font-family: "Segoe UI", "Inter", sans-serif;
    }
    h1 {
        color: {accent};
        font-size: 27px;
        border-bottom: 2px solid {accent};
        padding-bottom: 12px;
        margin-top: 4px;
    }
    h2 {
        color: {accent2};
        font-size: 20px;
        margin-top: 28px;
        border-left: 4px solid {accent2};
        padding-left: 10px;
    }
    h3 {
        color: {accent};
        font-size: 17px;
        margin-top: 22px;
    }
    p.lead {
        font-size: 16px;
        color: {dim};
        font-style: italic;
        border-left: 3px solid {accent};
        padding-left: 14px;
        margin: 16px 0;
    }
    ul, ol {{
        margin-left: 18px;
        margin-top: 8px;
    }}
    li {{ margin: 6px 0; }}
    table {{
        border-collapse: collapse;
        width: 100%;
        margin: 16px 0;
        background: {surface};
        border-radius: 10px;
        overflow: hidden;
    }}
    th {{
        background: {accent};
        color: white;
        padding: 12px 14px;
        text-align: left;
        font-size: 14px;
    }}
    td {{
        padding: 11px 14px;
        border-top: 1px solid {border};
    }}
    tr:nth-child(even) td {{ background: {surface2}; }}
    .info {{
        background: rgba(56,189,248,0.12);
        border-left: 4px solid {accent};
        padding: 14px 18px;
        border-radius: 10px;
        margin: 16px 0;
    }}
    .warning {{
        background: rgba(245,158,11,0.12);
        border-left: 4px solid {accent2};
        padding: 14px 18px;
        border-radius: 10px;
        margin: 16px 0;
    }}
    .tip {{
        background: rgba(34,197,94,0.12);
        border-left: 4px solid #22C55E;
        padding: 14px 18px;
        border-radius: 10px;
        margin: 16px 0;
    }}
    b {{ color: {accent}; }}
    code {{
        background: {surface2};
        padding: 2px 8px;
        border-radius: 5px;
        font-family: "Consolas", "Courier New", monospace;
        font-size: 13.5px;
        color: {accent};
    }}
</style>
{body}
"""


class MainWindow(QMainWindow):
    """Dasturning asosiy oynasi."""

    def __init__(self, payload: dict):
        super().__init__()
        self.payload = payload
        self.theme = "dark"
        self.read_sections = set()  # o'qilgan mavzular

        self.setWindowTitle("Qurilish Konstruksiyalari — Professional darslik")
        self.resize(1300, 840)
        self._center()
        self._build_ui()

    # ==================== MARKAZLASHTIRISH ====================
    def _center(self):
        geo = QGuiApplication.primaryScreen().availableGeometry()
        self.move(
            (geo.width() - self.width()) // 2,
            (geo.height() - self.height()) // 2,
        )

    # ==================== INTERFEYS ====================
    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # Top bar
        root.addWidget(self._build_topbar())

        # Splitter (sidebar + content)
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setHandleWidth(2)
        splitter.addWidget(self._build_sidebar())
        splitter.addWidget(self._build_content())
        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([340, 960])
        root.addWidget(splitter, 1)

        # Status bar
        self._build_statusbar()

        # Boshlang'ich sahifa
        self._show_welcome()

    # ==================== TOP BAR ====================
    def _build_topbar(self) -> QWidget:
        bar = QFrame()
        bar.setFixedHeight(66)
        bar.setStyleSheet("""
            QFrame {
                background: #0E1729;
                border-bottom: 1px solid #1E2D4D;
            }
        """)
        l = QHBoxLayout(bar)
        l.setContentsMargins(22, 12, 22, 12)
        l.setSpacing(14)

        # Logo
        logo = QLabel("🏗️   QURILISH KONSTRUKSIYALARI")
        logo.setStyleSheet("""
            color: #38BDF8;
            font-size: 15px;
            font-weight: 800;
            letter-spacing: 1.5px;
        """)
        l.addWidget(logo)

        l.addStretch()

        # Qidiruv
        self.search = QLineEdit()
        self.search.setPlaceholderText("🔍   Mavzu qidirish...")
        self.search.setFixedWidth(340)
        self.search.setStyleSheet("""
            QLineEdit {
                background: #16233F;
                border: 1px solid #1E2D4D;
                border-radius: 10px;
                padding: 10px 14px;
                color: #E6EEF9;
                font-size: 13.5px;
            }
            QLineEdit:focus {
                border: 1.5px solid #38BDF8;
                background: #111C33;
            }
        """)
        self.search.textChanged.connect(self._filter_tree)
        l.addWidget(self.search)

        # Tema tugmasi
        theme_btn = QToolButton()
        theme_btn.setText("🌙")
        theme_btn.setToolTip("Tungi / Kunduzgi rejim")
        theme_btn.setFixedSize(42, 42)
        theme_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        theme_btn.setStyleSheet("""
            QToolButton {
                background: #16233F;
                border: 1px solid #1E2D4D;
                border-radius: 10px;
                font-size: 19px;
                color: #E6EEF9;
            }
            QToolButton:hover {
                background: #1B2A4A;
                border-color: #38BDF8;
            }
        """)
        theme_btn.clicked.connect(self._toggle_theme)
        l.addWidget(theme_btn)

        # Foydalanuvchi
        user_btn = QToolButton()
        user_btn.setText("👤")
        user_btn.setFixedSize(42, 42)
        user_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        user_btn.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        user_btn.setStyleSheet("""
            QToolButton {
                background: #16233F;
                border: 1px solid #1E2D4D;
                border-radius: 10px;
                font-size: 19px;
                color: #E6EEF9;
            }
            QToolButton:hover {
                background: #1B2A4A;
                border-color: #38BDF8;
            }
            QToolButton::menu-indicator { image: none; }
        """)

        menu = QMenu(user_btn)
        menu.setStyleSheet("""
            QMenu {
                background: #111C33;
                border: 1px solid #1E2D4D;
                border-radius: 10px;
                padding: 8px;
                color: #E6EEF9;
            }
            QMenu::item {
                padding: 10px 22px;
                border-radius: 7px;
                font-size: 13.5px;
            }
            QMenu::item:selected { background: #1D4ED8; }
            QMenu::item:disabled { color: #64748B; }
            QMenu::separator {
                height: 1px;
                background: #1E2D4D;
                margin: 6px 10px;
            }
        """)

        name = self.payload.get("o", "Foydalanuvchi")
        exp = self.payload.get("e", "-")

        info_act = QAction(f"👤   {name}", menu)
        info_act.setEnabled(False)
        menu.addAction(info_act)

        exp_act = QAction(f"📅   Muddat: {exp}", menu)
        exp_act.setEnabled(False)
        menu.addAction(exp_act)

        menu.addSeparator()

        lic_act = QAction("🔑   Litsenziya ma'lumotlari", menu)
        lic_act.triggered.connect(self._show_license_info)
        menu.addAction(lic_act)

        about_act = QAction("ℹ️   Dastur haqida", menu)
        about_act.triggered.connect(self._show_about)
        menu.addAction(about_act)

        menu.addSeparator()

        exit_act = QAction("🚪   Chiqish", menu)
        exit_act.triggered.connect(self.close)
        menu.addAction(exit_act)

        user_btn.setMenu(menu)
        l.addWidget(user_btn)

        return bar

    # ==================== SIDEBAR ====================
    def _build_sidebar(self) -> QWidget:
        side = QFrame()
        side.setObjectName("Sidebar")
        side.setMinimumWidth(310)
        side.setMaximumWidth(440)
        side.setStyleSheet("""
            #Sidebar {
                background: #0E1729;
                border-right: 1px solid #1E2D4D;
            }
        """)

        l = QVBoxLayout(side)
        l.setContentsMargins(14, 18, 14, 14)
        l.setSpacing(12)

        # Progress
        prog_box = QFrame()
        prog_box.setStyleSheet("""
            QFrame {
                background: #16233F;
                border-radius: 12px;
            }
        """)
        pb = QVBoxLayout(prog_box)
        pb.setContentsMargins(16, 14, 16, 14)
        pb.setSpacing(10)

        total = get_total_sections()

        row = QHBoxLayout()
        t1 = QLabel("📚   O'rganish jarayoni")
        t1.setStyleSheet(
            "color: #94A3B8; font-size: 12.5px; font-weight: 600; "
            "background: transparent;"
        )
        row.addWidget(t1)
        row.addStretch()

        self.prog_label = QLabel(f"0 / {total}")
        self.prog_label.setStyleSheet(
            "color: #38BDF8; font-size: 13px; font-weight: 700; "
            "background: transparent;"
        )
        row.addWidget(self.prog_label)
        pb.addLayout(row)

        self.progress = QProgressBar()
        self.progress.setRange(0, total)
        self.progress.setValue(0)
        self.progress.setTextVisible(False)
        self.progress.setStyleSheet("""
            QProgressBar {
                background: #0E1729;
                border: none;
                border-radius: 6px;
                height: 8px;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #38BDF8, stop:1 #F59E0B);
                border-radius: 6px;
            }
        """)
        pb.addWidget(self.progress)

        l.addWidget(prog_box)

        # Tree
        self.tree = QListWidget()
        self.tree.setStyleSheet("""
            QListWidget {
                background: transparent;
                border: none;
                padding: 8px 4px;
                font-size: 13.5px;
                color: #E6EEF9;
            }
            QListWidget::item {
                padding: 9px 12px;
                border-radius: 8px;
                margin: 2px 6px;
            }
            QListWidget::item:hover {
                background: #1B2A4A;
            }
            QListWidget::item:selected {
                background: #1D4ED8;
                color: white;
                font-weight: 600;
            }
        """)
        self.tree.itemClicked.connect(self._on_topic_click)
        self._populate_tree()
        l.addWidget(self.tree, 1)

        return side

    def _populate_tree(self):
        """Mundarijani to'ldirish."""
        self.tree.clear()

        for qism in STRUCTURE:
            # Qism sarlavhasi
            header_text = f"{qism.get('icon', '📖')}   {qism['title']}"
            header = QListWidgetItem(header_text)
            f = header.font()
            f.setBold(True)
            f.setPointSize(10)
            header.setFont(f)
            header.setData(Qt.ItemDataRole.UserRole, ("header", qism["id"]))
            header.setForeground(Qt.GlobalColor.white)
            header.setFlags(Qt.ItemFlag.ItemIsEnabled)
            self.tree.addItem(header)

            # Bo'limlar
            for sec in qism["sections"]:
                item = QListWidgetItem(f"      {sec['id']}    {sec['title']}")
                item.setData(Qt.ItemDataRole.UserRole, ("section", sec["id"]))
                item.setToolTip(sec["title"])
                self.tree.addItem(item)

    def _filter_tree(self, text: str):
        """Qidiruv orqali filtrlash."""
        text = text.lower().strip()

        for i in range(self.tree.count()):
            item = self.tree.item(i)
            data = item.data(Qt.ItemDataRole.UserRole)

            if not text:
                item.setHidden(False)
                continue

            if data and data[0] == "header":
                item.setHidden(True)
            elif data and data[0] == "section":
                item.setHidden(text not in item.text().lower())

    def _on_topic_click(self, item: QListWidgetItem):
        """Mavzuga bosilganda."""
        data = item.data(Qt.ItemDataRole.UserRole)
        if not data:
            return

        if data[0] == "header":
            return

        section_id = data[1]
        topic = get_topic(section_id)
        self._render(topic["title"], topic["content"])

        # O'qilgan deb belgilash
        if section_id not in self.read_sections:
            self.read_sections.add(section_id)
            self._update_progress()
            # Tree item ga ✓ qo'shish
            current_text = item.text()
            if "✓" not in current_text:
                item.setText(f"{current_text}  ✓")

        self.status_left.setText(f"📖   {topic['title']}")

    # ==================== CONTENT ====================
    def _build_content(self) -> QWidget:
        wrap = QWidget()
        l = QVBoxLayout(wrap)
        l.setContentsMargins(14, 14, 14, 14)

        self.viewer = QTextBrowser()
        self.viewer.setOpenExternalLinks(True)
        self.viewer.setStyleSheet("""
            QTextBrowser {
                background: #111C33;
                border: 1px solid #1E2D4D;
                border-radius: 14px;
                padding: 10px;
                color: #E6EEF9;
            }
        """)
        l.addWidget(self.viewer)

        return wrap

    def _render(self, title: str, body: str):
        """Matnni chiroyli HTML shablonda ko'rsatish."""
        if self.theme == "dark":
            colors = {
                "text": "#E6EEF9",
                "dim": "#94A3B8",
                "accent": "#38BDF8",
                "accent2": "#F59E0B",
                "border": "#1E2D4D",
                "surface": "#16233F",
                "surface2": "#1B2A4A",
            }
        else:
            colors = {
                "text": "#0F172A",
                "dim": "#64748B",
                "accent": "#2563EB",
                "accent2": "#D97706",
                "border": "#E2E8F0",
                "surface": "#FFFFFF",
                "surface2": "#F8FAFC",
            }

        self.viewer.setHtml(HTML_WRAP.format(body=body, **colors))

    def _show_welcome(self):
        """Boshlang'ich xush kelibsiz sahifasi."""
        total = get_total_sections()
        filled = get_topics_count()

        self._render("Xush kelibsiz!", f"""
        <h1>Qurilish Konstruksiyalari</h1>

        <p class="lead">
            1-2-3 qavatli uylarning konstruksiyasini noldan o'rganish uchun
            to'liq amaliy qo'llanma. SHNK normalariga mos.
        </p>

        <h2>Nimalarni o'rganasiz?</h2>
        <ul>
            <li>🏠 Uy qanday turadi va yuk qanday tushadi</li>
            <li>⛏️ Tuproq va poydevor turlari</li>
            <li>🏛️ Ustunlar (armatura, xomut, o'lchamlar)</li>
            <li>➖ To'sinlar (yog'och, temir-beton, metall)</li>
            <li>🧱 Devorlar va armopoyas</li>
            <li>🪵 Pol, ship, zinapoya</li>
            <li>🏘️ Tom va stropila</li>
            <li>🌋 Seysmik himoya (O'zbekiston uchun muhim!)</li>
            <li>📐 Chizmalar va AutoCAD</li>
            <li>🧮 Kalkulyatorlar va yakuniy loyiha</li>
        </ul>

        <h2>Statistika</h2>
        <table>
            <tr><th>Ko'rsatkich</th><th>Qiymat</th></tr>
            <tr><td>Jami mavzular</td><td>{total}</td></tr>
            <tr><td>To'ldirilgan</td><td>{filled}</td></tr>
            <tr><td>O'qilgan</td><td>{len(self.read_sections)}</td></tr>
        </table>

        <div class="info">
            <b>Qanday foydalanish kerak?</b><br>
            Chapdagi ro'yxatdan mavzuni tanlang. Yuqoridagi qidiruv orqali
            kerakli mavzuni tez topishingiz mumkin. O'qilgan mavzular
            yonida <b>✓</b> belgisi paydo bo'ladi.
        </div>

        <div class="tip">
            <b>Maslahat:</b> Mavzularni ketma-ket o'rganing —
            har biri oldingisiga asoslanadi. Har bir mavzuni o'qib bo'lgach,
            oxiridagi amaliy topshiriqni bajaring.
        </div>
        """)

    # ==================== STATUS BAR ====================
    def _build_statusbar(self):
        sb = QStatusBar()
        sb.setStyleSheet("""
            QStatusBar {
                background: #0E1729;
                color: #94A3B8;
                border-top: 1px solid #1E2D4D;
                font-size: 12.5px;
                padding: 4px 12px;
            }
        """)
        self.setStatusBar(sb)

        self.status_left = QLabel("Tayyor")
        sb.addWidget(self.status_left)

        self.status_right = QLabel("v1.0.0  •  SHNK normalariga mos")
        sb.addPermanentWidget(self.status_right)

    # ==================== TEMA ====================
    def _toggle_theme(self):
        self.theme = "light" if self.theme == "dark" else "dark"

        # Qayta render
        self._render("Rejim o'zgartirildi",
                     f"""
                     <h1>Rejim: {'🌙 Tungi' if self.theme == 'dark' else '☀️ Kunduzgi'}</h1>
                     <p class="lead">Qulay rejim tanlandi.</p>
                     <p>Tungi rejim ko'zni charchatmaydi, kunduzgi rejim
                     yorug' joyda yaxshi ko'rinadi.</p>
                     """)

    # ==================== YORDAMCHI ====================
    def _update_progress(self):
        total = get_total_sections()
        count = len(self.read_sections)
        self.progress.setValue(count)
        self.prog_label.setText(f"{count} / {total}")

    def _show_license_info(self):
        p = self.payload
        QMessageBox.information(
            self,
            "Litsenziya ma'lumotlari",
            f"👤 Egasi: {p.get('o', '-')}\n\n"
            f"📅 Muddat: {p.get('e', '-')}\n\n"
            f"💻 HWID: {p.get('h', '-')}\n\n"
            f"📆 Berilgan: {p.get('t', '-')}",
        )

    def _show_about(self):
        QMessageBox.information(
            self,
            "Dastur haqida",
            "Qurilish Konstruksiyalari\n"
            "Versiya: 1.0.0\n\n"
            "1-2-3 qavatli uylar uchun to'liq qo'llanma.\n"
            "SHNK normalariga mos.\n\n"
            "© 2025 Barcha huquqlar himoyalangan.",
        )
