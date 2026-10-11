"""
Dasturning kirish nuqtasi (entry point).

ISHLASH TARTIBI:
1. .env faylidan maxfiy kalitni o'qish
2. Saqlangan litsenziyani tekshirish
3. Agar litsenziya yo'q yoki noto'g'ri — aktivatsiya oynasini ko'rsatish
4. Litsenziya to'g'ri bo'lsa — asosiy oynani ochish

Ishga tushirish:
    python src/main.py
"""
import sys
import os

# ——— Path fix (EXE ichida va oddiy ishlatishda ham to'g'ri ishlashi uchun) ———
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# ——— .env faylini yuklash (agar mavjud bo'lsa) ———
try:
    from dotenv import load_dotenv
    # .env faylini ildiz papkadan qidirish
    ROOT_DIR = os.path.dirname(BASE_DIR)
    ENV_PATH = os.path.join(ROOT_DIR, ".env")
    if os.path.exists(ENV_PATH):
        load_dotenv(ENV_PATH)
except ImportError:
    # python-dotenv o'rnatilmagan — davom etamiz
    pass

# ——— Endi barcha modullar ishlaydi ———
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt

from licensing import (
    verify_key, load_saved_key, save_key,
    get_hwid, days_left,
)
from activation import ActivationDialog
from ui.main_window import MainWindow
from styles import qss


# ==================== YORDAMCHI FUNKSIYALAR ====================

def _log(msg: str):
    """Konsolga xabar yozish (debug uchun)."""
    print(f"[QK] {msg}")


def _show_error(title: str, message: str):
    """Xato oynasini ko'rsatish."""
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Critical)
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.exec()


def _check_existing_license():
    """
    Saqlangan litsenziyani tekshirish.
    Qaytaradi: payload dict yoki None
    """
    saved = load_saved_key()
    if not saved:
        _log("Saqlangan litsenziya topilmadi")
        return None

    res = verify_key(saved)
    if res["valid"]:
        _log(f"Litsenziya to'g'ri: {res['payload']['o']}")
        return res["payload"]

    _log(f"Litsenziya xato: {res['reason']}")
    return None


def _run_activation():
    """
    Aktivatsiya oynasini ko'rsatish va natijani qaytarish.
    Qaytaradi: payload dict yoki None (foydalanuvchi bekor qilsa)
    """
    dlg = ActivationDialog()
    result = dlg.exec()

    if result != dlg.DialogCode.Accepted or not dlg.key:
        _log("Aktivatsiya bekor qilindi")
        return None

    # Kalitni saqlash
    save_key(dlg.key)
    _log("Kalit saqlandi")

    # Tekshirish
    res = verify_key(dlg.key)
    if res["valid"]:
        return res["payload"]

    return None


# ==================== ASOSIY ====================

def main():
    """Dastur kirish nuqtasi."""

    # ——— 1. QApplication yaratish ———
    app = QApplication(sys.argv)
    app.setApplicationName("Qurilish Konstruksiyalari")
    app.setApplicationDisplayName("Qurilish Konstruksiyalari")
    app.setOrganizationName("QK")

    # ——— 2. Shrift va stil ———
    font = QFont("Segoe UI", 10)
    font.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
    app.setFont(font)

    # ——— 3. Dizayn (tungi rejim) ———
    app.setStyleSheet(qss("dark"))

    # ——— 4. Litsenziyani tekshirish ———
    _log("Dastur ishga tushmoqda...")
    _log(f"HWID: {get_hwid()}")

    payload = _check_existing_license()

    # ——— 5. Agar litsenziya yo'q — aktivatsiya ———
    if payload is None:
        _log("Aktivatsiya kerak")
        payload = _run_activation()

        if payload is None:
            _log("Dastur yopildi (aktivatsiya yo'q)")
            sys.exit(0)

    # ——— 6. Muddatni tekshirish va eslatish ———
    days = days_left(load_saved_key() or "")
    if days is not None and 0 <= days <= 7:
        QMessageBox.warning(
            None,
            "Diqqat!",
            f"⚠️ Litsenziya muddati yaqinlashmoqda!\n\n"
            f"Qolgan kun: {days}\n\n"
            f"Iltimos, sotuvchi bilan bog'lanib, yangilang.",
        )

    # ——— 7. Asosiy oynani ochish ———
    _log("Asosiy oyna ochilmoqda...")
    win = MainWindow(payload)
    win.show()

    # ——— 8. Dasturni ishga tushirish ———
    sys.exit(app.exec())


# ==================== KIRISH ====================

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Kutilmagan xato bo'lsa — xabar ko'rsatish
        import traceback
        traceback.print_exc()

        try:
            app = QApplication.instance() or QApplication(sys.argv)
            _show_error(
                "Kutilmagan xato",
                f"Dasturda xato yuz berdi:\n\n{e}\n\n"
                f"Iltimos, sotuvchiga xabar bering.",
            )
        except Exception:
            pass

        sys.exit(1)
