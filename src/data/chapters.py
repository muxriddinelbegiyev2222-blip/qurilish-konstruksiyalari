"""
Dasturning mundarijasi (bo'limlar va mavzular).
Chap tomondagi ro'yxat shu fayldan olinadi.

Yangi mavzu qo'shish uchun shu yerga qo'shing.
"""

STRUCTURE = [
    {
        "id": "1",
        "title": "1-QISM. ASOSLAR",
        "icon": "🏠",
        "sections": [
            {"id": "1.1", "title": "Uy qanday turadi?"},
            {"id": "1.2", "title": "Uyga ta'sir etuvchi yuklar"},
            {"id": "1.3", "title": "Mustahkamlik, ustuvorlik, bikrlik"},
            {"id": "1.4", "title": "Qavat soni va konstruksiya o'zgarishi"},
        ],
    },
    {
        "id": "2",
        "title": "2-QISM. TUPROQ VA POYDEVOR",
        "icon": "⛏️",
        "sections": [
            {"id": "2.1", "title": "Tuproq turlari"},
            {"id": "2.2", "title": "Gruntning ko'tarish qobiliyati (R)"},
            {"id": "2.3", "title": "Muzlash chuqurligi (O'zbekiston)"},
            {"id": "2.4", "title": "Poydevor turlari"},
            {"id": "2.5", "title": "Lenta poydevorini hisoblash"},
            {"id": "2.6", "title": "Ustunli poydevor"},
            {"id": "2.7", "title": "Qoziqli poydevor"},
            {"id": "2.8", "title": "Plita (monolit) poydevor"},
            {"id": "2.9", "title": "Podval (yerto'la) devori"},
        ],
    },
    {
        "id": "3",
        "title": "3-QISM. USTUNLAR (KOLONNALAR)",
        "icon": "🏛️",
        "sections": [
            {"id": "3.1", "title": "Ustun turlari va materiallari"},
            {"id": "3.2", "title": "1-3 qavatli uylar uchun o'lchamlar"},
            {"id": "3.3", "title": "Armatura diametri va foizi (0.4%)"},
            {"id": "3.4", "title": "Xomutlar — diametr, qadam, joylashuv"},
            {"id": "3.5", "title": "Ustunlar orasidagi masofa"},
            {"id": "3.6", "title": "Seysmik talablar"},
            {"id": "3.7", "title": "To'liq hisoblash misoli"},
        ],
    },
    {
        "id": "4",
        "title": "4-QISM. TO'SLINLAR (BALKA)",
        "icon": "➖",
        "sections": [
            {"id": "4.1", "title": "To'sin turlari"},
            {"id": "4.2", "title": "Yog'och to'sin hisoblash"},
            {"id": "4.3", "title": "Temir-beton to'sin"},
            {"id": "4.4", "title": "Metall to'sin (dvutavr)"},
        ],
    },
    {
        "id": "5",
        "title": "5-QISM. DEVORLAR",
        "icon": "🧱",
        "sections": [
            {"id": "5.1", "title": "Devor materiallari (taqqoslash)"},
            {"id": "5.2", "title": "Yuk ko'taruvchi devor hisobi"},
            {"id": "5.3", "title": "Bo'linma devorlar"},
            {"id": "5.4", "title": "Armopoyas (seysmik kamar)"},
        ],
    },
    {
        "id": "6",
        "title": "6-QISM. POL VA SHIP",
        "icon": "🪵",
        "sections": [
            {"id": "6.1", "title": "Pol turlari"},
            {"id": "6.2", "title": "Yig'ma plita tanlash"},
            {"id": "6.3", "title": "Monolit plita hisoblash"},
            {"id": "6.4", "title": "Yog'och pol hisoblash"},
            {"id": "6.5", "title": "Zinapoya hisoblash"},
        ],
    },
    {
        "id": "7",
        "title": "7-QISM. TOM",
        "icon": "🏘️",
        "sections": [
            {"id": "7.1", "title": "Tom turlari"},
            {"id": "7.2", "title": "Stropila (tom karkasi) hisoblash"},
            {"id": "7.3", "title": "Tom yopmalari"},
            {"id": "7.4", "title": "Tom issiqlik izolyatsiyasi"},
        ],
    },
    {
        "id": "8",
        "title": "8-QISM. SEYSMIKA",
        "icon": "🌋",
        "sections": [
            {"id": "8.1", "title": "Seysmik zona xaritasi"},
            {"id": "8.2", "title": "Seysmik yuk"},
            {"id": "8.3", "title": "Seysmik himoya usullari"},
            {"id": "8.4", "title": "Antiseysmik kamar (armopoyas)"},
        ],
    },
    {
        "id": "9",
        "title": "9-QISM. CHIZMALAR",
        "icon": "📐",
        "sections": [
            {"id": "9.1", "title": "Chizma asoslari"},
            {"id": "9.2", "title": "Poydevor plani va qirqimi"},
            {"id": "9.3", "title": "Ustun chizmasi (armatura sxemasi)"},
            {"id": "9.4", "title": "Devor plani"},
            {"id": "9.5", "title": "Pol plani"},
            {"id": "9.6", "title": "Tom plani va qirqimi"},
            {"id": "9.7", "title": "Armatura chizmasi"},
            {"id": "9.8", "title": "AutoCAD / ArchiCAD asoslari"},
        ],
    },
    {
        "id": "10",
        "title": "10-QISM. KALKULYATORLAR",
        "icon": "🧮",
        "sections": [
            {"id": "10.1", "title": "Yuk yig'ish kalkulyatori"},
            {"id": "10.2", "title": "Poydevor kalkulyatori"},
            {"id": "10.3", "title": "Ustun kalkulyatori"},
            {"id": "10.4", "title": "To'sin kalkulyatori"},
            {"id": "10.5", "title": "Plita kalkulyatori"},
        ],
    },
    {
        "id": "11",
        "title": "11-QISM. YAKUNIY LOYIHA",
        "icon": "🎓",
        "sections": [
            {"id": "11.1", "title": "2 qavatli uy loyihasi (0 dan)"},
            {"id": "11.2", "title": "Materiallar ro'yxati (smeta)"},
            {"id": "11.3", "title": "Chizmalar to'plami"},
        ],
    },
]


def get_total_sections() -> int:
    """Jami mavzular soni."""
    return sum(len(q["sections"]) for q in STRUCTURE)


def find_section(section_id: str) -> dict | None:
    """Mavzuni ID bo'yicha topish."""
    for qism in STRUCTURE:
        for sec in qism["sections"]:
            if sec["id"] == section_id:
                return sec
    return None


def get_all_section_ids() -> list[str]:
    """Barcha mavzu ID lari ro'yxati."""
    ids = []
    for qism in STRUCTURE:
        for sec in qism["sections"]:
            ids.append(sec["id"])
    return ids
