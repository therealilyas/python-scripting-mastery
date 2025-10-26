## 🏗️ LOYIHALAR

### Loyiha 1: Shaxsiy Ma'lumotlar Boshqaruvchisi

**Maqsad:** Foydalanuvchi ma'lumotlarini saqlash va boshqarish dasturi yaratish.

**Funksiyalar:**
- Foydalanuvchi ma'lumotlarini kiritish
- Ma'lumotlarni formatlash va ko'rsatish
- Oddiy validatsiya
- Foydalanuvchi ID yaratish

```python
# loyiha-1-malumotlar-boshqaruvchi.py

"""
SHAXSIY MA'LUMOTLAR BOSHQARUVCHISI
===================================
Foydalanuvchi ma'lumotlarini to'plash va boshqarish tizimi
"""

import re
from datetime import datetime

def banner():
    """Dastur banneri"""
    print("=" * 60)
    print(" " * 15 + "SHAXSIY MA'LUMOTLAR TIZIMI")
    print("=" * 60)
    print()

def email_tekshir(email):
    """Email manzil to'g'riligini tekshiradi"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def telefon_tekshir(telefon):
    """Telefon raqam formatini tekshiradi"""
    # Format: +998901234567 yoki 901234567
    pattern = r'^(\+998)?[0-9]{9}$'
    return re.match(pattern, telefon) is not None

def id_yaratish(ism, familiya, yosh):
    """Unikal foydalanuvchi ID yaratadi"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    user_id = f"{ism[:3].upper()}{familiya[:3].upper()}{yosh}{timestamp[-4:]}"
    return user_id

def malumot_toplash():
    """Foydalanuvchi ma'lumotlarini to'playdi"""
    
    print("📝 MA'LUMOTLARINGIZNI KIRITING\n")
    
    # Ism
    while True:
        ism = input("Ismingiz: ").strip()
        if len(ism) >= 2 and ism.isalpha():
            break
        print("❌ Ism kamida 2 harfdan iborat bo'lishi kerak!\n")
    
    # Familiya
    while True:
        familiya = input("Familiyangiz: ").strip()
        if len(familiya) >= 2 and familiya.isalpha():
            break
        print("❌ Familiya kamida 2 harfdan iborat bo'lishi kerak!\n")
    
    # Yosh
    while True:
        try:
            yosh = int(input("Yoshingiz: "))
            if 1 <= yosh <= 120:
                break
            print("❌ Yosh 1-120 oralig'ida bo'lishi kerak!\n")
        except ValueError:
            print("❌ Iltimos, raqam kiriting!\n")
    
    # Email
    while True:
        email = input("Email: ").strip().lower()
        if email_tekshir(email):
            break
        print("❌ Noto'g'ri email format! (misol: user@example.com)\n")
    
    # Telefon
    while True:
        telefon = input("Telefon (+998XXXXXXXXX): ").strip()
        if telefon_tekshir(telefon):
            # +998 qo'shish agar yo'q bo'lsa
            if not telefon.startswith("+998"):
                telefon = "+998" + telefon
            break
        print("❌ Noto'g'ri telefon format!\n")
    
    # Shahar
    shahar = input("Shahar: ").strip().title()
    
    # Kasb
    kasb = input("Kasb/Yo'nalish: ").strip()
    
    return {
        "ism": ism.capitalize(),
        "familiya": familiya.capitalize(),
        "yosh": yosh,
        "email": email,
        "telefon": telefon,
        "shahar": shahar if shahar else "Ko'rsatilmagan",
        "kasb": kasb if kasb else "Ko'rsatilmagan"
    }

def malumotlarni_korsatish(malumotlar):
    """Ma'lumotlarni chiroyli formatda ko'rsatadi"""
    
    # User ID yaratish
    user_id = id_yaratish(
        malumotlar["ism"], 
        malumotlar["familiya"], 
        malumotlar["yosh"]
    )
    
    print("\n" + "=" * 60)
    print(" " * 20 + "SIZNING PROFILINGIZ")
    print("=" * 60)
    
    print(f"\n👤 SHAXSIY MA'LUMOTLAR:")
    print(f"   To'liq ism    : {malumotlar['ism']} {malumotlar['familiya']}")
    print(f"   Yosh          : {malumotlar['yosh']} yosh")
    print(f"   User ID       : {user_id}")
    
    print(f"\n📧 ALOQA MA'LUMOTLARI:")
    print(f"   Email         : {malumotlar['email']}")
    print(f"   Telefon       : {malumotlar['telefon']}")
    
    print(f"\n📍 QO'SHIMCHA MA'LUMOTLAR:")
    print(f"   Shahar        : {malumotlar['shahar']}")
    print(f"   Kasb          : {malumotlar['kasb']}")
    
    print(f"\n📊 STATISTIKA:")
    print(f"   Ism uzunligi  : {len(malumotlar['ism'])} harf")
    print(f"   Email domeni  : {malumotlar['email'].split('@')[1]}")
    print(f"   Telefon kod   : {malumotlar['telefon'][:4]}")
    
    # Yoshga asoslangan kategoriya
    yosh = malumotlar['yosh']
    if yosh < 18:
        kategoriya = "Voyaga yetmagan"
    elif yosh < 30:
        kategoriya = "Yosh"
    elif yosh < 50:
        kategoriya = "O'rta yosh"
    else:
        kategoriya = "Katta yosh"
    
    print(f"   Yosh guruhi   : {kategoriya}")
    
    print("\n" + "=" * 60)

def statistika_hisoblash(malumotlar_royxati):
    """Ko'plab foydalanuvchilar statistikasi"""
    
    if not malumotlar_royxati:
        print("📊 Hozircha statistika yo'q!")
        return
    
    print("\n" + "=" * 60)
    print(" " * 20 + "UMUMIY STATISTIKA")
    print("=" * 60)
    
    # Umumiy foydalanuvchilar
    print(f"\n👥 Jami foydalanuvchilar: {len(malumotlar_royxati)}")
    
    # O'rtacha yosh
    ortacha_yosh = sum(m['yosh'] for m in malumotlar_royxati) / len(malumotlar_royxati)
    print(f"📊 O'rtacha yosh: {ortacha_yosh:.1f} yosh")
    
    # Eng katta va eng kichik yosh
    yoshlar = [m['yosh'] for m in malumotlar_royxati]
    print(f"👴 Eng katta yosh: {max(yoshlar)}")
    print(f"👶 Eng kichik yosh: {min(yoshlar)}")
    
    # Shaharlar statistikasi
    shaharlar = {}
    for m in malumotlar_royxati:
        shahar = m['shahar']
        shaharlar[shahar] = shaharlar.get(shahar, 0) + 1
    
    print(f"\n🏙️  SHAHARLAR BO'YICHA:")
    for shahar, soni in sorted(shaharlar.items(), key=lambda x: x[1], reverse=True):
        print(f"   {shahar}: {soni} ta")
    
    # Email provayderlar
    provayderlar = {}
    for m in malumotlar_royxati:
        provider = m['email'].split('@')[1]
        provayderlar[provider] = provayderlar.get(provider, 0) + 1
    
    print(f"\n📧 EMAIL PROVAYDERLAR:")
    for provider, soni in sorted(provayderlar.items(), key=lambda x: x[1], reverse=True):
        print(f"   {provider}: {soni} ta")
    
    print("\n" + "=" * 60)

def main():
    """Asosiy dastur"""
    
    malumotlar_royxati = []
    
    while True:
        banner()
        
        print("MENYU:")
        print("1. Yangi foydalanuvchi qo'shish")
        print("2. Barcha foydalanuvchilarni ko'rish")
        print("3. Umumiy statistika")
        print("4. Chiqish")
        
        tanlov = input("\nTanlovingiz (1-4): ").strip()
        
        if tanlov == "1":
            print("\n")
            malumotlar = malumot_toplash()
            malumotlarni_korsatish(malumotlar)
            malumotlar_royxati.append(malumotlar)
            
            input("\n⏎ Davom etish uchun Enter bosing...")
        
        elif tanlov == "2":
            print("\n")
            if not malumotlar_royxati:
                print("❌ Hozircha foydalanuvchilar yo'q!\n")
            else:
                for idx, mal in enumerate(malumotlar_royxati, 1):
                    print(f"\n--- Foydalanuvchi #{idx} ---")
                    print(f"Ism: {mal['ism']} {mal['familiya']}")
                    print(f"Yosh: {mal['yosh']}")
                    print(f"Email: {mal['email']}")
                    print(f"Telefon: {mal['telefon']}")
                    print(f"Shahar: {mal['shahar']}")
            
            input("\n⏎ Davom etish uchun Enter bosing...")
        
        elif tanlov == "3":
            statistika_hisoblash(malumotlar_royxati)
            input("\n⏎ Davom etish uchun Enter bosing...")
        
        elif tanlov == "4":
            print("\n👋 Xayr! Tizimdan chiqildi.\n")
            break
        
        else:
            print("\n❌ Noto'g'ri tanlov! Qaytadan urinib ko'ring.\n")
            input("⏎ Davom etish uchun Enter bosing...")

if __name__ == "__main__":
    main()
```

---

### Loyiha 2: Ma'lumot Turi Konvertor va Validator

**Maqsad:** Turli xil ma'lumot turlarini tekshirish va o'zgartirish vositasi.

```python
# loyiha-2-data-converter.py

"""
MA'LUMOT TURI KONVERTOR VA VALIDATOR
=====================================
Har xil ma'lumot turlarini tekshirish va o'zgartirish
"""

import re

def banner():
    """Dastur banneri"""
    print("\n" + "=" * 70)
    print(" " * 18 + "MA'LUMOT TURI KONVERTOR & VALIDATOR")
    print("=" * 70 + "\n")

def aniqla_va_tekshir(qiymat):
    """Qiymat turini aniqlaydi va to'g'riligini tekshiradi"""
    
    print(f"\n📝 Kiritilgan qiymat: '{qiymat}'")
    print(f"🔍 Python turi: {type(qiymat).__name__}")
    print(f"📏 Uzunlik: {len(str(qiymat))} belgi")
    
    # Turini aniqlash
    print("\n🎯 MUMKIN BO'LGAN TURLAR:")
    
    # Integer
    try:
        int_qiymat = int(qiymat)
        print(f"   ✅ Integer: {int_qiymat}")
    except:
        print(f"   ❌ Integer: O'zgartirib bo'lmaydi")
    
    # Float
    try:
        float_qiymat = float(qiymat)
        print(f"   ✅ Float: {float_qiymat}")
    except:
        print(f"   ❌ Float: O'zgartirib bo'lmaydi")
    
    # Boolean
    if qiymat.lower() in ['true', 'false', '1', '0', 'yes', 'no']:
        bool_map = {
            'true': True, '1': True, 'yes': True,
            'false': False, '0': False, 'no': False
        }
        bool_qiymat = bool_map.get(qiymat.lower())
        print(f"   ✅ Boolean: {bool_qiymat}")
    else:
        print(f"   ℹ️  Boolean: Mantiqiy qiymat emas")
    
    # Maxsus formatlar
    print("\n🔎 MAXSUS FORMATLAR:")
    
    # IP Address
    ip_pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    if re.match(ip_pattern, qiymat):
        print(f"   ✅ IP Address formatida")
        oktets = qiymat.split('.')
        valid = all(0 <= int(o) <= 255 for o in oktets)
        print(f"      To'g'ri IP: {'✅ Ha' if valid else '❌ Yo\'q'}")
    
    # Email
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, qiymat):
        print(f"   ✅ Email formatida")
        domain = qiymat.split('@')[1]
        print(f"      Domen: {domain}")
    
    # URL
    url_pattern = r'^https?://[^\s]+$'
    if re.match(url_pattern, qiymat):
        print(f"   ✅ URL formatida")
        protocol = qiymat.split('://')[0]
        print(f"      Protokol: {protocol}")
    
    # Telefon (Uzbekistan)
    phone_pattern = r'^(\+998)?[0-9]{9}$'
    if re.match(phone_pattern, qiymat.replace(' ', '')):
        print(f"   ✅ Telefon raqam formatida (UZ)")
    
    # Hex color
    hex_pattern = r'^#[0-9A-Fa-f]{6}$'
    if re.match(hex_pattern, qiymat):
        print(f"   ✅ Hex color formatida")
        r = int(qiymat[1:3], 16)
        g = int(qiymat[3:5], 16)
        b = int(qiymat[5:7], 16)
        print(f"      RGB: ({r}, {g}, {b})")
    
    # MAC Address
    mac_pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    if re.match(mac_pattern, qiymat):
        print(f"   ✅ MAC Address formatida")

def konvertor_menyu():
    """Konvertor menyusi"""
    
    print("\n📊 KONVERTOR TURLARI:")
    print("1. Raqamlar (Binary, Octal, Decimal, Hex)")
    print("2. Matn (Upper, Lower, Title, etc.)")
    print("3. Temperatura (C, F, K)")
    print("4. Uzunlik (km, m, cm, mm)")
    print("5. Hajm (L, ml, gal)")
    print("6. Og'irlik (kg, g, lb, oz)")
    print("0. Orqaga")
    
    tanlov = input("\nTanlov: ").strip()
    
    if tanlov == "1":
        raqam_konvertor()
    elif tanlov == "2":
        matn_konvertor()
    elif tanlov == "3":
        temperatura_konvertor()
    elif tanlov == "4":
        uzunlik_konvertor()
    elif tanlov == "5":
        hajm_konvertor()
    elif tanlov == "6":
        ogirlik_konvertor()

def raqam_konvertor():
    """Raqamlar orasida konvertatsiya"""
    
    print("\n🔢 RAQAM KONVERTOR\n")
    
    qiymat = input("Raqam kiriting: ").strip()
    
    try:
        # Agar binary bo'lsa
        if qiymat.startswith('0b'):
            decimal = int(qiymat, 2)
        # Agar octal bo'lsa
        elif qiymat.startswith('0o'):
            decimal = int(qiymat, 8)
        # Agar hex bo'lsa
        elif qiymat.startswith('0x'):
            decimal = int(qiymat, 16)
        # Oddiy decimal
        else:
            decimal = int(qiymat)
        
        print(f"\n📊 NATIJALAR:")
        print(f"   Decimal (10): {decimal}")
        print(f"   Binary (2):   {bin(decimal)}")
        print(f"   Octal (8):    {oct(decimal)}")
        print(f"   Hex (16):     {hex(decimal).upper()}")
        
        # Bit ma'lumotlari
        print(f"\n💾 BIT MA'LUMOTLARI:")
        print(f"   Bit length: {decimal.bit_length()} bit")
        print(f"   Bytes: {(decimal.bit_length() + 7) // 8} byte")
        
    except ValueError:
        print("❌ Xato: Noto'g'ri raqam formatı!")

def matn_konvertor():
    """Matn formatlarini o'zgartirish"""
    
    print("\n📝 MATN KONVERTOR\n")
    
    matn = input("Matn kiriting: ")
    
    print(f"\n📊 NATIJALAR:")
    print(f"   Original:    {matn}")
    print(f"   Uppercase:   {matn.upper()}")
    print(f"   Lowercase:   {matn.lower()}")
    print(f"   Title Case:  {matn.title()}")
    print(f"   Capitalize:  {matn.capitalize()}")
    print(f"   Swapcase:    {matn.swapcase()}")
    
    print(f"\n📏 STATISTIKA:")
    print(f"   Uzunlik:         {len(matn)} belgi")
    print(f"   So'zlar:         {len(matn.split())} ta")
    print(f"   Katta harflar:   {sum(1 for c in matn if c.isupper())} ta")
    print(f"   Kichik harflar:  {sum(1 for c in matn if c.islower())} ta")
    print(f"   Raqamlar:        {sum(1 for c in matn if c.isdigit())} ta")
    print(f"   Bo'sh joylar:    {matn.count(' ')} ta")
    
    # Teskari matn
    print(f"\n🔄 QO'SHIMCHA:")
    print(f"   Teskari:     {matn[::-1]}")

def temperatura_konvertor():
    """Temperatura konvertatsiyasi"""
    
    print("\n🌡️  TEMPERATURA KONVERTOR\n")
    
    try:
        qiymat = float(input("Temperatura: "))
        birlik = input("Birlik (C/F/K): ").upper()
        
        if birlik == 'C':
            celsius = qiymat
            fahrenheit = (celsius * 9/5) + 32
            kelvin = celsius + 273.15
        elif birlik == 'F':
            fahrenheit = qiymat
            celsius = (fahrenheit - 32) * 5/9
            kelvin = celsius + 273.15
        elif birlik == 'K':
            kelvin = qiymat
            celsius = kelvin - 273.15
            fahrenheit = (celsius * 9/5) + 32
        else:
            print("❌ Noto'g'ri birlik!")
            return
        
        print(f"\n📊 NATIJALAR:")
        print(f"   Celsius:    {celsius:.2f} °C")
        print(f"   Fahrenheit: {fahrenheit:.2f} °F")
        print(f"   Kelvin:     {kelvin:.2f} K")
        
        # Holat
        if celsius < 0:
            holat = "Muzlagan 🥶"
        elif celsius < 15:
            holat = "Sovuq ❄️"
        elif celsius < 25:
            holat = "Mo'tadil 😊"
        elif celsius < 35:
            holat = "Issiq 🌞"
        else:
            holat = "Juda issiq 🔥"
        
        print(f"   Holat: {holat}")
        
    except ValueError:
        print("❌ Xato: Noto'g'ri qiymat!")

def uzunlik_konvertor():
    """Uzunlik konvertatsiyasi"""
    
    print("\n📏 UZUNLIK KONVERTOR\n")
    
    try:
        qiymat = float(input("Qiymat: "))
        birlik = input("Birlik (km/m/cm/mm/mi/ft/in): ").lower()
        
        # Hammasini metrga o'tkazamiz
        if birlik == 'km':
            metr = qiymat * 1000
        elif birlik == 'm':
            metr = qiymat
        elif birlik == 'cm':
            metr = qiymat / 100
        elif birlik == 'mm':
            metr = qiymat / 1000
        elif birlik == 'mi':
            metr = qiymat * 1609.34
        elif birlik == 'ft':
            metr = qiymat * 0.3048
        elif birlik == 'in':
            metr = qiymat * 0.0254
        else:
            print("❌ Noto'g'ri birlik!")
            return
        
        print(f"\n📊 NATIJALAR:")
        print(f"   Kilometr: {metr / 1000:.6f} km")
        print(f"   Metr:     {metr:.4f} m")
        print(f"   Santimetr:{metr * 100:.2f} cm")
        print(f"   Millimetr:{metr * 1000:.1f} mm")
        print(f"   Milya:    {metr / 1609.34:.6f} mi")
        print(f"   Fut:      {metr / 0.3048:.4f} ft")
        print(f"   Dyuym:    {metr / 0.0254:.2f} in")
        
    except ValueError:
        print("❌ Xato: Noto'g'ri qiymat!")

def hajm_konvertor():
    """Hajm konvertatsiyasi"""
    
    print("\n🥤 HAJM KONVERTOR\n")
    
    try:
        qiymat = float(input("Qiymat: "))
        birlik = input("Birlik (L/ml/gal/oz): ").lower()
        
        # Hammasini litrga o'tkazamiz
        if birlik == 'l':
            litr = qiymat
        elif birlik == 'ml':
            litr = qiymat / 1000
        elif birlik == 'gal':
            litr = qiymat * 3.78541
        elif birlik == 'oz':
            litr = qiymat * 0.0295735
        else:
            print("❌ Noto'g'ri birlik!")
            return
        
        print(f"\n📊 NATIJALAR:")
        print(f"   Litr:     {litr:.6f} L")
        print(f"   Millilitr:{litr * 1000:.2f} ml")
        print(f"   Gallon:   {litr / 3.78541:.6f} gal")
        print(f"   Untsiya:  {litr / 0.0295735:.2f} oz")
        
    except ValueError:
        print("❌ Xato: Noto'g'ri qiymat!")

def ogirlik_konvertor():
    """Og'irlik konvertatsiyasi"""
    
    print("\n⚖️  OG'IRLIK KONVERTOR\n")
    
    try:
        qiymat = float(input("Qiymat: "))
        birlik = input("Birlik (kg/g/lb/oz): ").lower()
        
        # Hammasini kilogrammga o'tkazamiz
        if birlik == 'kg':
            kg = qiymat
        elif birlik == 'g':
            kg = qiymat / 1000
        elif birlik == 'lb':
            kg = qiymat * 0.453592
        elif birlik == 'oz':
            kg = qiymat * 0.0283495
        else:
            print("❌ Noto'g'ri birlik!")
            return
        
        print(f"\n📊 NATIJALAR:")
        print(f"   Kilogramm: {kg:.6f} kg")
        print(f"   Gramm:     {kg * 1000:.2f} g")
        print(f"   Funt:      {kg / 0.453592:.6f} lb")
        print(f"   Untsiya:   {kg / 0.0283495:.2f} oz")
        
    except ValueError:
        print("❌ Xato: Noto'g'ri qiymat!")

def main():
    """Asosiy dastur"""
    
    while True:
        banner()
        
        print("ASOSIY MENYU:")
        print("1. Qiymatni tahlil qilish va tekshirish")
        print("2. Konvertor (o'zgartirish)")
        print("3. Chiqish")
        
        tanlov = input("\nTanlovingiz (1-3): ").strip()
        
        if tanlov == "1":
            print("\n")
            qiymat = input("Qiymat kiriting: ").strip()
            aniqla_va_tekshir(qiymat)
            input("\n⏎ Davom etish uchun Enter bosing...")
        
        elif tanlov == "2":
            konvertor_menyu()
            input("\n⏎ Davom etish uchun Enter bosing...")
        
        elif tanlov == "3":
            print("\n👋 Xayr! Dasturdan chiqildi.\n")
            break
        
        else:
            print("\n❌ Noto'g'ri tanlov!\n")
            input("⏎ Davom etish uchun Enter bosing...")

if __name__ == "__main__":
    main()
```

---
