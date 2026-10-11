"""
==========================================================
⚠️ FAQAT SOTUVCHI UCHUN. MIJOZGA BERMANG!
==========================================================

Litsenziya kaliti generatori.

Ishlatish:
    cd tools
    python keygen.py

Yoki argumentlar bilan:
    python keygen.py "Alisher aka" "2026-12-31" "A3F2B1C4D5E6F7A8"
"""
import sys
import os

# src papkasini path ga qo'shamiz
BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
SRC = os.path.join(ROOT, "src")
sys.path.insert(0, SRC)

# .env yuklash
try:
    from dotenv import load_dotenv
    ENV_PATH = os.path.join(ROOT, ".env")
    if os.path.exists(ENV_PATH):
        load_dotenv(ENV_PATH)
except ImportError:
    pass

from licensing import generate_key, get_hwid


# ==================== YORDAMCHI ====================

def _line(char="─", n=60):
    print(char * n)


def _print_header():
    _line("═")
    print("   🔑  QURILISH KONSTRUKSIYALARI — KALIT GENERATORI")
    _line("═")
    print()


def _print_key(key: str):
    _line()
    print("   ✅  KALIT YARATILDI!")
    _line()
    print()
    print(key)
    print()
    _line()
    print()


def _copy_to_clipboard(text: str) -> bool:
    """Kalitni clipboardga nusxalash (agar mumkin bo'lsa)."""
    try:
        if os.name == "nt":  # Windows
            import subprocess
            subprocess.run("clip", input=text.encode(), shell=True, check=True)
            return True
        elif sys.platform == "darwin":  # Mac
            import subprocess
            subprocess.run("pbcopy", input=text.encode(), check=True)
            return True
        else:  # Linux
            import subprocess
            try:
                subprocess.run(
                    ["xclip", "-selection", "clipboard"],
                    input=text.encode(), check=True,
                )
                return True
            except Exception:
                return False
    except Exception:
        return False


# ==================== ASOSIY ====================

def interactive():
    """Interaktiv rejimda so'rash."""
    _print_header()

    print("   Bu kompyuter HWID:", get_hwid())
    print("   (Agar o'zingizga kalit yaratsangiz, shu HWID ni ishlating)")
    print()

    owner = input("   👤 Mijoz ismi: ").strip()
    if not owner:
        owner = "Mijoz"

    print()
    print("   📅 Muddat formati: YYYY-MM-DD yoki 'never' (muddatsiz)")
    print("   Misol: 2026-12-31")
    expiry = input("   📅 Muddat: ").strip()
    if not expiry:
        expiry = "never"

    print()
    print("   💻 HWID — mijoz yuborgan 16 belgili kod.")
    print("   Yoki 'any' — istalgan kompyuterga ishlaydi.")
    hwid = input("   💻 HWID: ").strip().upper()
    if not hwid:
        hwid = "any"

    return owner, expiry, hwid


def main():
    # Argumentlar bilan ishlash
    if len(sys.argv) >= 4:
        owner = sys.argv[1]
        expiry = sys.argv[2]
        hwid = sys.argv[3].upper() if sys.argv[3] != "any" else "any"
    elif len(sys.argv) == 1:
        owner, expiry, hwid = interactive()
    else:
        print("❌ Foydalanish:")
        print("   python keygen.py                          # interaktiv")
        print("   python keygen.py 'Ism' 'YYYY-MM-DD' HWID  # argumentlar")
        sys.exit(1)

    # Kalit yaratish
    try:
        key = generate_key(owner=owner, expiry=expiry, hwid=hwid)
    except Exception as e:
        print(f"\n❌ Xato: {e}")
        sys.exit(1)

    # Ko'rsatish
    _print_key(key)

    print(f"   👤 Egasi:   {owner}")
    print(f"   📅 Muddat:  {expiry}")
    print(f"   💻 HWID:    {hwid}")
    print()

    # Clipboardga nusxalash
    if _copy_to_clipboard(key):
        print("   📋 Kalit clipboardga nusxalandi!")
        print()

    _line()
    print("   Ushbu kalitni mijozga yuboring.")
    print("   Mijoz dasturni ochib, kalitni kiritadi.")
    _line()

    # Yana yaratish?
    print()
    again = input("   Yana kalit yaratish? (h/y): ").strip().lower()
    if again in ("h", "ha", "y", "yes"):
        print()
        main()


if __name__ == "__main__":
    main()
