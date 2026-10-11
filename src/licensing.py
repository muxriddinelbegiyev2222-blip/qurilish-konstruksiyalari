"""
Litsenziya tizimi — HWID + HMAC-SHA256 imzo.

QANDAY ISHLAYDI:
1. Sotuvchi maxfiy kalitni .env faylida saqlaydi
2. Har bir mijozga noyob litsenziya kaliti generatsiya qilinadi
3. Kalit ichida: mijoz ismi, muddat, HWID imzolangan holda yoziladi
4. Mijoz kalitni dasturga kiritadi
5. Dastur kalitni tekshiradi (imzo + muddat + HWID)
6. To'g'ri bo'lsa — dastur ochiladi

AFZALLIKLARI:
- Internet talab qilmaydi (offline ishlaydi)
- HWID bilan boshqa kompyuterga ko'chirib bo'lmaydi
- Muddat bilan vaqtincha sotish mumkin
- Imzo soxtalashtirishni oldini oladi
"""

import hmac
import hashlib
import base64
import json
import uuid
import subprocess
import platform
import os
from datetime import datetime, date


# ==================== MAXFIY KALIT ====================

def _load_secret() -> bytes:
    """
    Maxfiy kalitni .env faylidan o'qish.

    .env faylida shunday bo'lishi kerak:
    LICENSE_SECRET=SIZNING-KAMIDA-40-BELGILI-KALITINGIZ
    """
    key = os.getenv("LICENSE_SECRET", "")

    if not key:
        # ⚠️ Bu faqat test uchun! Ishlab chiqarishda .env ishlatilsin!
        key = "QK-DEFAULT-TEST-KEY-CHANGE-ME-NOW-2025-1234567890"

    return key.encode()


SECRET_KEY = _load_secret()


# ==================== HWID (KOMPYUTER ID) ====================

def get_hwid() -> str:
    """
    Kompyuterning noyob identifikatori.
    Qaytaradi: 16 belgili HEX string (masalan: 'A3F2B1C4D5E6F7A8')

    Windows: Motherboard UUID
    Linux: /etc/machine-id
    Mac: IOPlatformUUID
    """
    system = platform.system()
    raw = ""

    try:
        if system == "Windows":
            # Windows kompyuter UUID
            out = subprocess.check_output(
                "wmic csproduct get uuid",
                shell=True,
                creationflags=0x08000000,  # Konsol oynasini yashirish
                stderr=subprocess.DEVNULL,
            ).decode(errors="ignore")
            raw = out.split("\n")[1].strip()

        elif system == "Linux":
            if os.path.exists("/etc/machine-id"):
                with open("/etc/machine-id") as f:
                    raw = f.read().strip()
            else:
                raw = str(uuid.getnode())

        elif system == "Darwin":  # macOS
            out = subprocess.check_output(
                ["ioreg", "-rd1", "-c", "IOPlatformExpertDevice"]
            ).decode()
            for line in out.split("\n"):
                if "IOPlatformUUID" in line:
                    raw = line.split('"')[-2]
                    break
    except Exception:
        raw = ""

    # Agar hech narsa topilmasa, MAC addressdan foydalanamiz
    if not raw:
        raw = str(uuid.getnode())

    # SHA256 dan 16 belgi olamiz
    return hashlib.sha256(raw.encode()).hexdigest()[:16].upper()


# ==================== IMZO ====================

def _sign(data: bytes) -> str:
    """
    Ma'lumotni HMAC-SHA256 bilan imzolash.
    Natija: base64 string (imzo).
    """
    signature = hmac.new(SECRET_KEY, data, hashlib.sha256).digest()
    return base64.urlsafe_b64encode(signature).decode().rstrip("=")


# ==================== KALIT YARATISH (FAQAT SOTUVCHI) ====================

def generate_key(owner: str, expiry: str, hwid: str) -> str:
    """
    Sotuvchi tomonidan litsenziya kaliti yaratish.

    Parametrlar:
    -----------
    owner  : mijoz ismi (masalan: 'Alisher aka')
    expiry : tugash sanasi 'YYYY-MM-DD' yoki 'never' (muddatsiz)
    hwid   : mijoz HWID yoki 'any' (istalgan kompyuterga)

    Qaytaradi:
    ---------
    Litsenziya kaliti: 'base64.imzo' formatida

    Misol:
    -----
    >>> generate_key('Alisher aka', '2026-12-31', 'A3F2B1C4D5E6F7A8')
    'eyJvIjoiQWxpc2hlciBha2EiLCJlIjoiMjAyNi0xMi0zMSIsImgiOiJBM0YyQjFDNEQ1RTZGN0E4IiwidCI6IjIwMjUtMTAtMTIifQ.xyz123...'
    """
    payload = {
        "o": owner,                                       # egasi
        "e": expiry,                                      # tugash sanasi
        "h": hwid,                                        # HWID
        "t": datetime.now().strftime("%Y-%m-%d"),        # berilgan sana
    }

    # JSON ga o'girish
    raw = json.dumps(payload, separators=(",", ":"), ensure_ascii=False).encode()

    # Base64 ga o'girish (imzosiz qism)
    b = base64.urlsafe_b64encode(raw).decode().rstrip("=")

    # Imzo qo'shish
    return f"{b}.{_sign(raw)}"


# ==================== KALITNI TEKSHIRISH (DASTURDA) ====================

def verify_key(key: str) -> dict:
    """
    Litsenziya kalitini tekshirish.

    Qaytaradi:
    ---------
    {
        'valid': bool,      # Kalit to'g'rimi?
        'reason': str,      # Sabab (xato bo'lsa)
        'payload': dict     # Kalit ichidagi ma'lumot
    }
    """
    try:
        key = key.strip()

        # Format tekshiruvi
        if "." not in key:
            return {
                "valid": False,
                "reason": "Kalit formati noto'g'ri (nuqta yo'q)",
                "payload": None,
            }

        b, sig = key.rsplit(".", 1)

        # Base64 padding qo'shish
        pad = "=" * (-len(b) % 4)
        raw = base64.urlsafe_b64decode(b + pad)

        # Imzoni tekshirish
        expected = _sign(raw)
        if not hmac.compare_digest(sig, expected):
            return {
                "valid": False,
                "reason": "Kalit soxta yoki buzilgan",
                "payload": None,
            }

        # Payload ni o'qish
        payload = json.loads(raw)

        # Muddatni tekshirish
        if payload.get("e") != "never":
            try:
                exp = datetime.strptime(payload["e"], "%Y-%m-%d").date()
                today = date.today()
                if today > exp:
                    days_passed = (today - exp).days
                    return {
                        "valid": False,
                        "reason": f"Muddat tugagan: {payload['e']} "
                                  f"({days_passed} kun oldin)",
                        "payload": payload,
                    }
            except Exception:
                return {
                    "valid": False,
                    "reason": "Muddat formati noto'g'ri",
                    "payload": None,
                }

        # HWID ni tekshirish
        current_hwid = get_hwid()
        if payload.get("h") not in ("any", current_hwid):
            return {
                "valid": False,
                "reason": "Kalit boshqa kompyuterga bog'langan",
                "payload": payload,
            }

        # Hammasi to'g'ri
        return {
            "valid": True,
            "reason": "OK",
            "payload": payload,
        }

    except Exception as e:
        return {
            "valid": False,
            "reason": f"Kalit xatosi: {e}",
            "payload": None,
        }


# ==================== SAQLASH / O'QISH ====================

LICENSE_DIR = os.path.join(os.path.expanduser("~"), ".qurilish_dasturi")
LICENSE_PATH = os.path.join(LICENSE_DIR, "license.key")


def save_key(key: str) -> None:
    """Kalitni kompyuterga saqlash (keyingi ochilishda eslab qolish uchun)."""
    os.makedirs(LICENSE_DIR, exist_ok=True)
    with open(LICENSE_PATH, "w", encoding="utf-8") as f:
        f.write(key.strip())


def load_saved_key() -> str | None:
    """Saqlangan kalitni o'qish. Topilmasa None qaytaradi."""
    if os.path.exists(LICENSE_PATH):
        try:
            with open(LICENSE_PATH, encoding="utf-8") as f:
                return f.read().strip()
        except Exception:
            return None
    return None


def delete_key() -> None:
    """Kalitni o'chirish (deaktivatsiya)."""
    if os.path.exists(LICENSE_PATH):
        try:
            os.remove(LICENSE_PATH)
        except Exception:
            pass


def get_license_info(key: str) -> dict | None:
    """
    Kalitdan ma'lumot olish (tekshirmasdan).
    Faqat ko'rsatish uchun.
    """
    try:
        b, sig = key.strip().rsplit(".", 1)
        pad = "=" * (-len(b) % 4)
        raw = base64.urlsafe_b64decode(b + pad)
        return json.loads(raw)
    except Exception:
        return None


def days_left(key: str) -> int | None:
    """
    Kalitda necha kun qolgan?
    'never' bo'lsa None qaytaradi.
    """
    info = get_license_info(key)
    if not info:
        return None
    if info.get("e") == "never":
        return None
    try:
        exp = datetime.strptime(info["e"], "%Y-%m-%d").date()
        today = date.today()
        return (exp - today).days
    except Exception:
        return None
