"""
Darslik mavzulari matni.
Har bir mavzu HTML formatida yozilgan.
"""

TOPICS = {

    # ================================================================
    # 1-QISM. ASOSLAR
    # ================================================================

    "1.1": {
        "title": "Uy qanday turadi?",
        "content": """
        <h1>Uy qanday turadi?</h1>

        <p class="lead">Tasavvur qiling: odam qanday turadi? <b>Suyagi</b>
        ko'taradi, <b>terisi</b> yopadi. Uy ham xuddi shunday tuzilgan.</p>

        <h2>Uyning 2 ta asosiy qismi</h2>

        <h3>1. KO'TARUVCHI qism — bu uyning "suyagi"</h3>
        <p>Bu qism butun uyning og'irligini ko'tarib turadi:</p>
        <ul>
            <li><b>Poydevor</b> — eng pastda, yerni "quchoqlab" turadi</li>
            <li><b>Yuk ko'taruvchi devorlar</b> — asosiy tayanch</li>
            <li><b>Ustunlar</b> — vertikal tayanchlar</li>
            <li><b>To'sinlar</b> — gorizontal tayanchlar</li>
            <li><b>Pol plitalari</b> — qavatlar orasidagi yopma</li>
            <li><b>Tom karkasi</b> — tomni ko'tarib turadi</li>
        </ul>

        <h3>2. O'RAB TURUVCHI qism — bu uyning "terisi"</h3>
        <p>Bu qism yukni ko'tarmaydi, faqat yopadi va himoya qiladi:</p>
        <ul>
            <li>Fasad pardoz (shtukaturka, bo'yoq, panel)</li>
            <li>Deraza va eshiklar</li>
            <li>Tom yopmasi (cherepitsa, shifer)</li>
            <li>Issiqlik izolyatsiyasi</li>
        </ul>

        <div class="info">
            <b>Nega buni bilish kerak?</b><br>
            Hisoblashda faqat <b>ko'taruvchi qism</b> hisobga olinadi.
            Deraza, bo'yoq, gulqog'oz uy og'irligini deyarli oshirmaydi.
        </div>

        <h2>Yuk yo'li — tomdan poydevorga</h2>
        <p>Yuk har doim <b>yuqoridan pastga</b> tushadi. Hech qachon
        aksincha emas!</p>

        <table>
            <tr>
                <th>Qadam</th>
                <th>Yuk qayerdan</th>
                <th>Yuk qayerga</th>
            </tr>
            <tr><td>1</td><td>Qor, shamol</td><td>→ Tom yopmasi</td></tr>
            <tr><td>2</td><td>Tom yopmasi</td><td>→ Stropila (karkas)</td></tr>
            <tr><td>3</td><td>Stropila</td><td>→ Devor / ustun</td></tr>
            <tr><td>4</td><td>Devor / ustun</td><td>→ Poydevor</td></tr>
            <tr><td>5</td><td>Poydevor</td><td>→ Tuproq</td></tr>
        </table>

        <h2>Hayotiy misol</h2>
        <p><b>Masala:</b> 2 qavatli g'isht uy, temir-beton pol, metall tom.
        Hisoblashda nimalar hisobga olinadi?</p>

        <p><b>Javob:</b> Faqat quyidagilar:</p>
        <ul>
            <li>Poydevor og'irligi</li>
            <li>Devor og'irligi</li>
            <li>Pol plitalari</li>
            <li>Tom karkasi va yopmasi</li>
            <li>Qor, odam, mebel (vaqtincha)</li>
        </ul>
        <p>Deraza, pardoz, santexnika — keyinroq qo'shiladi va kichik.</p>

        <h2>Turli qavatli uylarning taxminiy og'irligi</h2>
        <table>
            <tr>
                <th>Qavat soni</th>
                <th>Umumiy og'irlik</th>
                <th>1 m² ga</th>
            </tr>
            <tr><td>1 qavat</td><td>~100 tonna</td><td>~1 tonna</td></tr>
            <tr><td>2 qavat</td><td>~200 tonna</td><td>~1.5 tonna</td></tr>
            <tr><td>3 qavat</td><td>~300 tonna</td><td>~2 tonna</td></tr>
        </table>

        <div class="warning">
            <b>Muhim qoida:</b> Yukni yig'ishda hamma narsani emas,
            faqat <b>ko'taruvchi qismlarni</b> hisobga oling.
        </div>

        <div class="tip">
            <b>Amaliy topshiriq:</b> O'zingizning uyingiz yoki
            qurmoqchi bo'lgan uyingizning ko'taruvchi va o'rab turuvchi
            qismlarini ro'yxat qilib chiqing. Har birini 2 guruhga ajrating.
        </div>
        """,
    },

    "1.2": {
        "title": "Uyga ta'sir etuvchi yuklar",
        "content": """
        <h1>Uyga ta'sir etuvchi yuklar</h1>

        <p class="lead">Har qanday konstruksiya <b>yuk</b> ostida ishlaydi.
        Yukni to'g'ri hisoblamasak — uy qulashi mumkin.</p>

        <h2>3 xil yuk turi</h2>

        <h3>1. DOIMIY yuklar (har doim bor)</h3>
        <p>Bu yuklar uy qurilgandan keyin <b>hech qachon yo'qolmaydi</b>:</p>
        <ul>
            <li>Poydevorning o'z og'irligi</li>
            <li>Devorlar og'irligi</li>
            <li>Pol plitalari og'irligi</li>
            <li>Tom karkasi va yopmasi</li>
            <li>Tuproq bosimi (podval devoriga)</li>
        </ul>

        <h3>2. VAQTINCHA yuklar (ba'zan bor, ba'zan yo'q)</h3>
        <p><b>Uzoq muddatli:</b></p>
        <ul>
            <li>Mebel (shkaf, divan, stol)</li>
            <li>Jihozlar (muzlatgich, kir yuvish mashinasi)</li>
            <li>Saqlanadigan yuklar (ombor)</li>
        </ul>

        <p><b>Qisqa muddatli:</b></p>
        <ul>
            <li>Odamlar (1 kishi ≈ 80 kg)</li>
            <li>Qor (qishda)</li>
            <li>Shamol (kuchli kunlarda)</li>
        </ul>

        <h3>3. MAXSUS yuklar (kamdan-kam, lekin kuchli)</h3>
        <ul>
            <li><b>Seysmik</b> (zilzila) — O'zbekistonda eng muhim!</li>
            <li>Suv toshqini</li>
            <li>Portlash</li>
            <li>Avariya holatlari</li>
        </ul>

        <h2>Doimiy yuklar jadvali (1 m² uchun)</h2>
        <table>
            <tr>
                <th>Material / element</th>
                <th>Og'irlik (kg/m²)</th>
            </tr>
            <tr><td>G'isht devor (380 mm)</td><td>700 - 900</td></tr>
            <tr><td>Gazoblok devor (300 mm)</td><td>300 - 400</td></tr>
            <tr><td>Penoblok devor (300 mm)</td><td>200 - 300</td></tr>
            <tr><td>Temir-beton plita (200 mm)</td><td>500</td></tr>
            <tr><td>Yog'och pol (to'sin bilan)</td><td>150 - 200</td></tr>
            <tr><td>Monolit pol (150 mm)</td><td>375</td></tr>
            <tr><td>Metallocherepitsa tom</td><td>5 - 7</td></tr>
            <tr><td>Shifer tom</td><td>14 - 18</td></tr>
            <tr><td>Bitumli cherepitsa</td><td>8 - 12</td></tr>
        </table>

        <h2>Vaqtinchalik yuklar jadvali</h2>
        <table>
            <tr>
                <th>Yuk turi</th>
                <th>Qiymat (kg/m²)</th>
            </tr>
            <tr><td>Odamlar (turar-joy)</td><td>150 - 200</td></tr>
            <tr><td>Mebel</td><td>50 - 100</td></tr>
            <tr><td>Qor (Toshkent)</td><td>80</td></tr>
            <tr><td>Qor (Andijon, Namangan)</td><td>120</td></tr>
            <tr><td>Shamol (o'rtacha)</td><td>30 - 60</td></tr>
        </table>

        <h2>Hisobiy yuk nima? (γf koeffitsiyenti)</h2>
        <p>Yuklar hisoblashda <b>ishonchlilik koeffitsiyentiga</b>
        ko'paytiriladi, chunki real hayotda yuk har doim hisobdagidan
        ko'proq bo'lishi mumkin:</p>

        <table>
            <tr>
                <th>Yuk turi</th>
                <th>γf</th>
            </tr>
            <tr><td>Doimiy (beton, temir)</td><td>1.1</td></tr>
            <tr><td>Doimiy (yog'och, izolyatsiya)</td><td>1.2</td></tr>
            <tr><td>Vaqtinchalik (odam, mebel)</td><td>1.2 - 1.3</td></tr>
            <tr><td>Qor</td><td>1.4</td></tr>
            <tr><td>Shamol</td><td>1.4</td></tr>
        </table>

        <div class="info">
            <b>Formula:</b><br>
            <code>Hisobiy yuk = Me'yoriy yuk × γf</code>
        </div>

        <h2>Hayotiy misol</h2>
        <p><b>Masala:</b> 4×5 m xonada 10 kishi to'y qilyapti.
        Har biri 80 kg, stol-stullar 200 kg.</p>
        <p><b>Yechish:</b></p>
        <ul>
            <li>Odamlar: 10 × 80 = 800 kg</li>
            <li>Mebel: 200 kg</li>
            <li><b>Jami: 1000 kg = 1 tonna</b></li>
        </ul>
        <p>Bu 1 tonna <b>bitta xonaga</b> tushadi! Shuning uchun pol va
        to'sinlar bu vaznga chidashli bo'lishi kerak.</p>

        <div class="warning">
            <b>Diqqat:</b> Qor yuki viloyatga qarab farq qiladi.
            Tog'li hududlarda (Chorvoq, Chimyon) qor ko'proq —
            SHNQ 2.01.07 ga qarang.
        </div>

        <div class="tip">
            <b>Amaliy topshiriq:</b> O'z uyingizdagi bitta xonaning
            og'irligini hisoblang. Devor, pol, mebel, odamlar — hammasini
            qo'shing.
        </div>
        """,
    },

    "1.3": {
        "title": "Mustahkamlik, ustuvorlik, bikrlik",
        "content": """
        <h1>Mustahkamlik, ustuvorlik, bikrlik</h1>

        <p class="lead">Har qanday konstruksiya <b>3 ta shartni</b>
        bajarishi kerak. Aks holda u qulaydi yoki yaroqsiz bo'ladi.</p>

        <h2>1. MUSTAHKAMLIK — sinmasligi kerak</h2>
        <p><b>Ta'rif:</b> Konstruksiya yuk ostida <b>sinmasligi</b> va
        <b>yorilmasligi</b> kerak.</p>

        <p><b>Hayotiy misol:</b></p>
        <p>Temir-beton ustun 100 tonna yukni ko'taradi. Agar 150 tonna
        qo'ysangiz — ustun sinadi. Shuning uchun ustun kesimi va
        armatura to'g'ri hisoblanishi kerak.</p>

        <div class="info">
            <b>Formula:</b><br>
            <code>σ = N / A ≤ R</code><br><br>
            <b>σ</b> — kuchlanish (kg/sm²)<br>
            <b>N</b> — kuch (kg)<br>
            <b>A</b> — kesim yuzasi (sm²)<br>
            <b>R</b> — materialning hisobiy qarshiligi (kg/sm²)
        </div>

        <h2>2. USTUVORLIK (o'zgarmaslik) — ag'darilib tushmasligi</h2>
        <p><b>Ta'rif:</b> Konstruksiya <b>o'z holatini saqlab turishi</b>
        kerak. Ag'darilmasligi, siljib ketmasligi kerak.</p>

        <p><b>Hayotiy misol:</b></p>
        <p>Baland minora shamolda ag'darilib ketmasligi kerak.
        Ingichka va baland bino shamol yoki zilzilada ag'darilishi mumkin.
        Shuning uchun poydevor keng qilinadi yoki bino
        <b>og'irlashtiriladi</b>.</p>

        <h3>Ustuvorlik sharti:</h3>
        <p>Ag'daruvchi moment < ushlab turuvchi momentdan kichik bo'lishi kerak:</p>
        <code>M_ag'daruvchi &lt; M_ushlab_turuvchi</code>

        <h2>3. BIKRLIK (qattiqlik) — egilib ketmasligi</h2>
        <p><b>Ta'rif:</b> Konstruksiya yuk ostida <b>juda ko'p
        egilmasligi</b> kerak. Kichik egilish normal, katta egilish —
        xavfli.</p>

        <p><b>Hayotiy misol:</b></p>
        <p>Ingichka uzun taxtani ikki stulga qo'yib, o'rtasiga
        o'tirsangiz — egiladi. Xuddi shu taxtani ikki tomonidan
        mixlasangiz — egilmaydi. Sabab: <b>bikrlik oshdi</b>.</p>

        <h3>Bikrlik sharti (to'sin uchun):</h3>
        <p>Egilish oraliqning 1/200 - 1/400 qismidan oshmasligi kerak:</p>
        <code>f ≤ L / 200</code>
        <p>Masalan, 4 m to'sin uchun maksimal egilish 20 mm.</p>

        <h2>3 ta shart taqqoslash</h2>
        <table>
            <tr>
                <th>Shart</th>
                <th>Nimani tekshiradi</th>
                <th>Buzilsa nima bo'ladi</th>
            </tr>
            <tr>
                <td><b>Mustahkamlik</b></td>
                <td>Sinmasligi</td>
                <td>Ustun sinadi, plita yoriladi</td>
            </tr>
            <tr>
                <td><b>Ustuvorlik</b></td>
                <td>Ag'darilmasligi</td>
                <td>Bino yon tomonga ag'dariladi</td>
            </tr>
            <tr>
                <td><b>Bikrlik</b></td>
                <td>Ko'p egilmasligi</td>
                <td>Pol "chayqaladi", eshik qiyshiq</td>
            </tr>
        </table>

        <div class="warning">
            <b>Eng ko'p uchraydigan xato:</b><br>
            Odamlar faqat <b>mustahkamlikka</b> qaraydi, lekin
            <b>bikrlikni</b> unutadi. Natijada uy "qulab tushmasa ham",
            yashash qiyin bo'ladi.
        </div>

        <div class="tip">
            <b>Amaliy topshiriq:</b> Uyingizdagi eshik yoki deraza
            ochilib-yopilishida qiyinchilik bormi? Agar bo'lsa, demak
            konstruksiya bikrligi yetarli emas.
        </div>
        """,
    },

    "1.4": {
        "title": "Qavat soni va konstruksiya o'zgarishi",
        "content": """
        <h1>Qavat soni va konstruksiya o'zgarishi</h1>

        <p class="lead">Har bir qavat qo'shilganda uyning og'irligi
        <b>deyarli 2 barobar</b> oshadi. Shuning uchun konstruksiya
        ham mos ravishda kuchaytirilishi kerak.</p>

        <h2>1, 2, 3 qavatli uylar taqqoslash</h2>

        <table>
            <tr>
                <th>Element</th>
                <th>1 qavat</th>
                <th>2 qavat</th>
                <th>3 qavat</th>
            </tr>
            <tr>
                <td><b>Poydevor</b></td>
                <td>Sayoz lenta<br>40-60 sm</td>
                <td>Lenta<br>80-100 sm</td>
                <td>Kuchli lenta<br>100-120 sm</td>
            </tr>
            <tr>
                <td><b>Poydevor kengligi</b></td>
                <td>400 mm</td>
                <td>500-600 mm</td>
                <td>700-800 mm</td>
            </tr>
            <tr>
                <td><b>Devor qalinligi</b></td>
                <td>380 mm (g'isht)<br>300 mm (gazoblok)</td>
                <td>510 mm (g'isht)<br>400 mm (gazoblok)</td>
                <td>640 mm (g'isht)<br>karkas</td>
            </tr>
            <tr>
                <td><b>Pol turi</b></td>
                <td>Yog'och yoki plita</td>
                <td>Temir-beton plita</td>
                <td>Temir-beton plita</td>
            </tr>
            <tr>
                <td><b>Ustun kesimi</b></td>
                <td>250×250 mm</td>
                <td>300×300 mm</td>
                <td>400×400 mm</td>
            </tr>
            <tr>
                <td><b>Beton sinfi</b></td>
                <td>B15 (M200)</td>
                <td>B20 (M250)</td>
                <td>B25 (M350)</td>
            </tr>
            <tr>
                <td><b>Armatura (asosiy)</b></td>
                <td>Ø12 mm</td>
                <td>Ø14-16 mm</td>
                <td>Ø16-18 mm</td>
            </tr>
        </table>

        <h2>Nega 2 barobar oshadi?</h2>
        <p>Chunki 2-qavat qo'shilganda:</p>
        <ul>
            <li>Yana devor qo'shiladi</li>
            <li>Yana pol qo'shiladi</li>
            <li>Tom qo'shiladi (u ham og'ir)</li>
            <li>Foydali yuk ikki barobar oshadi</li>
        </ul>

        <h2>Materiallarga ta'siri</h2>

        <h3>Beton sinflari</h3>
        <table>
            <tr>
                <th>Sinf</th>
                <th>Marka</th>
                <th>Mustahkamlik</th>
                <th>Qayerda ishlatiladi</th>
            </tr>
            <tr>
                <td>B15</td><td>M200</td><td>196 kg/sm²</td>
                <td>1 qavat, ustunli poydevor</td>
            </tr>
            <tr>
                <td>B20</td><td>M250</td><td>255 kg/sm²</td>
                <td>2 qavat, poydevor, plita</td>
            </tr>
            <tr>
                <td>B25</td><td>M350</td><td>327 kg/sm²</td>
                <td>3 qavat, ustun</td>
            </tr>
            <tr>
                <td>B30</td><td>M400</td><td>392 kg/sm²</td>
                <td>Yuqori qavat, seysmik</td>
            </tr>
        </table>

        <h3>Armatura sinflari</h3>
        <table>
            <tr>
                <th>Sinf</th>
                <th>Eski belgisi</th>
                <th>Oquvchanlik chegarasi</th>
            </tr>
            <tr>
                <td>A400</td><td>A-III</td><td>400 MPa</td>
            </tr>
            <tr>
                <td>A500</td><td>A-IIIv</td><td>500 MPa</td>
            </tr>
            <tr>
                <td>A600</td><td>A-IV</td><td>600 MPa</td>
            </tr>
        </table>

        <div class="info">
            <b>Tavsiya:</b> 1-3 qavatli uylar uchun
            <b>A400 yoki A500</b> armatura ishlatish kifoya.
            <b>A600</b> faqat seysmik va sanoat uchun.
        </div>

        <h2>Qaysi holatda professional kerak?</h2>
        <table>
            <tr>
                <th>Qavat</th>
                <th>Kim loyihalashi mumkin</th>
            </tr>
            <tr>
                <td>1 qavat</td>
                <td>O'zingiz ham hisoblashingiz mumkin</td>
            </tr>
            <tr>
                <td>2 qavat</td>
                <td>Tajribali quruvchi bilan</td>
            </tr>
            <tr>
                <td>3 qavat</td>
                <td>Mutaxassis + siz nazorat qilasiz</td>
            </tr>
            <tr>
                <td>4+ qavat</td>
                <td>Faqat professional loyiha instituti</td>
            </tr>
        </table>

        <div class="warning">
            <b>MUHIM:</b> O'zbekiston seysmik hududda. 3 qavatli uy
            qurishda <b>majburiy</b> mutaxassis nazorati kerak.
            Aks holda zilzilada xavfli.
        </div>

        <div class="tip">
            <b>Amaliy topshiriq:</b> O'zingiz qurmoqchi bo'lgan uyning
            qavat sonini tanlang. Yuqoridagi jadvaldan konstruksiya
            elementlarini aniqlang va daftarga yozib qo'ying.
        </div>
        """,
    },
}


# ==================== YORDAMCHI FUNKSIYALAR ====================

def get_topic(section_id: str) -> dict:
    """Mavzu matnini olish. Topilmasa, standart qaytaradi."""
    if section_id in TOPICS:
        return TOPICS[section_id]
    return {
        "title": "Mavzu tayyorlanmoqda",
        "content": f"""
        <h1>Mavzu tayyorlanmoqda</h1>
        <p class="lead">Bu mavzu (<b>{section_id}</b>) hozircha
        to'ldirilmagan.</p>
        <p>Tez orada to'liq matn, jadvallar va chizmalar qo'shiladi.</p>
        <div class="info">
            <b>Eslatma:</b> Dastur yangilanib boriladi.
            Yangi versiyani olganingizda bu mavzu ham to'ladi.
        </div>
        """,
    }


def get_topics_count() -> int:
    """To'ldirilgan mavzular soni."""
    return len(TOPICS)


def has_topic(section_id: str) -> bool:
    """Mavzu to'ldirilganmi?"""
    return section_id in TOPICS
