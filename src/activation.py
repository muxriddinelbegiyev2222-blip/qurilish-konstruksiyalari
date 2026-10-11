"""
Aktivatsiya (login) oynasi.
Mijoz dasturni birinchi ochganda ko'radi.
"""
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox, QFrame,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication

from licensing import get_hwid, verify_key


class ActivationDialog(QDialog):
    """Litsenziya kalitini kiritish oynasi."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qurilish Konstruksiyalari — Aktivlashtirish")
        self.setFixedSize(560, 660)
        self.key = None
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
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ---------- SARLAVHA (gradient) ----------
        header = QFrame()
        header.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #1E3A8A,
                    stop:0.5 #2563EB,
                    stop:1 #7C3AED);
                border-top-left-radius: 16px;
                border-top-right-radius: 16px;
            }
        """)
        header.setFixedHeight(200)

        hl = QVBoxLayout(header)
        hl.setContentsMargins(30, 30, 30, 24)
        hl.setSpacing(8)

        icon = QLabel("🏗️")
        icon.setStyleSheet("""
            font-size: 56px;
            background: transparent;
        """)
        icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hl.addWidget(icon)

        title = QLabel("QURILISH KONSTRUKSIYALARI")
        title.setStyleSheet("""
            color: white;
            font-size: 19px;
            font-weight: 800;
            letter-spacing: 3px;
            background: transparent;
        """)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hl.addWidget(title)

        sub = QLabel("1-2-3 qavatli uylar uchun to'liq qo'llanma")
        sub.setStyleSheet("""
            color: rgba(255,255,255,0.9);
            font-size: 13px;
            background: transparent;
        """)
        sub.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hl.addWidget(sub)

        ver = QLabel("v1.0.0  •  SHNK normalariga mos")
        ver.setStyleSheet("""
            color: rgba(255,255,255,0.6);
            font-size: 11px;
            background: transparent;
        """)
        ver.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hl.addWidget(ver)

        root.addWidget(header)

        # ---------- ASOSIY QISM ----------
        body = QFrame()
        body.setStyleSheet("""
            QFrame {
                background: #0F172A;
                border-bottom-left-radius: 16px;
                border-bottom-right-radius: 16px;
            }
        """)

        bl = QVBoxLayout(body)
        bl.setContentsMargins(38, 30, 38, 30)
        bl.setSpacing(14)

        # --- HWID ---
        hwid_label = QLabel("💻  Kompyuter identifikatori (HWID)")
        hwid_label.setStyleSheet("""
            color: #94A3B8;
            font-size: 12.5px;
            font-weight: 600;
        """)
        bl.addWidget(hwid_label)

        hwid = get_hwid()

        hwid_row = QHBoxLayout()
        hwid_row.setSpacing(8)

        self.hwid_field = QLineEdit(hwid)
        self.hwid_field.setReadOnly(True)
        self.hwid_field.setStyleSheet("""
            QLineEdit {
                background: #1E293B;
                border: 1px solid #334155;
                border-radius: 10px;
                padding: 12px 14px;
                color: #38BDF8;
                font-size: 14px;
                font-weight: 700;
                letter-spacing: 3px;
                font-family: "Consolas", "Courier New", monospace;
            }
        """)
        hwid_row.addWidget(self.hwid_field, 1)

        copy_btn = QPushButton("📋")
        copy_btn.setToolTip("HWID ni nusxalash")
        copy_btn.setFixedSize(46, 46)
        copy_btn.setStyleSheet("""
            QPushButton {
                background: #1E293B;
                border: 1px solid #334155;
                border-radius: 10px;
                font-size: 18px;
                color: #E6EEF9;
            }
            QPushButton:hover {
                background: #334155;
                border-color: #38BDF8;
            }
            QPushButton:pressed {
                background: #1D4ED8;
            }
        """)
        copy_btn.clicked.connect(lambda: self._copy(hwid))
        hwid_row.addWidget(copy_btn)

        bl.addLayout(hwid_row)

        # --- Hint ---
        hint = QLabel(
            "☝️  Yuqoridagi HWID kodini sotuvchiga yuboring va "
            "litsenziya kalitini oling."
        )
        hint.setWordWrap(True)
        hint.setStyleSheet("""
            color: #94A3B8;
            font-size: 12.5px;
            background: #1E293B;
            border-left: 3px solid #38BDF8;
            border-radius: 8px;
            padding: 12px 14px;
        """)
        bl.addWidget(hint)

        bl.addSpacing(10)

        # --- Kalit kiritish ---
        key_label = QLabel("🔑  Litsenziya kaliti")
        key_label.setStyleSheet("""
            color: #94A3B8;
            font-size: 12.5px;
            font-weight: 600;
        """)
        bl.addWidget(key_label)

        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("Kalitni bu yerga qo'ying...")
        self.key_input.setStyleSheet("""
            QLineEdit {
                background: #1E293B;
                border: 1.5px solid #334155;
                border-radius: 10px;
                padding: 13px 14px;
                color: white;
                font-size: 13px;
                font-family: "Consolas", "Courier New", monospace;
            }
            QLineEdit:focus {
                border-color: #38BDF8;
                background: #0F172A;
            }
        """)
        self.key_input.returnPressed.connect(self._activate)
        bl.addWidget(self.key_input)

        bl.addSpacing(6)

        # --- Aktivlashtirish tugmasi ---
        btn = QPushButton("🔓   AKTIVLASHTIRISH")
        btn.setFixedHeight(52)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #2563EB,
                    stop:1 #7C3AED);
                border: none;
                border-radius: 12px;
                color: white;
                font-size: 15px;
                font-weight: 700;
                letter-spacing: 1.5px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #3B82F6,
                    stop:1 #8B5CF6);
            }
            QPushButton:pressed {
                background: #1D4ED8;
            }
        """)
        btn.clicked.connect(self._activate)
        bl.addWidget(btn)

        bl.addSpacing(6)

        # --- Footer ---
        footer = QLabel("© 2025 Qurilish Konstruksiyalari  •  Barcha huquqlar himoyalangan")
        footer.setStyleSheet("""
            color: #475569;
            font-size: 11.5px;
        """)
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        bl.addWidget(footer)

        root.addWidget(body)

    # ==================== NUSXALASH ====================
    def _copy(self, text: str):
        QGuiApplication.clipboard().setText(text)
        QMessageBox.information(
            self,
            "Nusxalandi",
            "HWID nusxalandi!\n\nEndi uni sotuvchiga yuboring.",
        )

    # ==================== AKTIVLASHTIRISH ====================
    def _activate(self):
        key = self.key_input.text().strip()

        if not key:
            QMessageBox.warning(
                self,
                "Diqqat",
                "Iltimos, litsenziya kalitini kiriting.",
            )
            return

        res = verify_key(key)

        if res["valid"]:
            self.key = key
            payload = res["payload"]

            QMessageBox.information(
                self,
                "Muvaffaqiyat! 🎉",
                f"Xush kelibsiz, {payload['o']}!\n\n"
                f"📅 Muddat: {payload['e']}\n"
                f"💻 HWID: {payload['h']}\n\n"
                f"Dasturdan foydalanishingiz mumkin.",
            )
            self.accept()
        else:
            QMessageBox.critical(
                self,
                "Rad etildi ❌",
                f"{res['reason']}\n\n"
                f"Iltimos, sotuvchi bilan bog'laning.",
            )
            self.key_input.selectAll()
            self.key_input.setFocus()
