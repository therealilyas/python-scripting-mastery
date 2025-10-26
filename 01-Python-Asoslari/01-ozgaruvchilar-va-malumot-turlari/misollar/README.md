## 💡 Misollar

### 01 - Oddiy misollar

```python
# oddiy-misollar.py

# 1. O'zgaruvchilar yaratish
ism = "Muhammad"
yosh = 20
bo'y = 1.75
talaba = True

print(f"Ism: {ism}")
print(f"Yosh: {yosh}")
print(f"Bo'y: {bo'y} metr")
print(f"Talabami: {talaba}")

print("\n" + "="*50 + "\n")

# 2. Matematik amallar
son1 = 15
son2 = 4

print(f"{son1} + {son2} = {son1 + son2}")
print(f"{son1} - {son2} = {son1 - son2}")
print(f"{son1} * {son2} = {son1 * son2}")
print(f"{son1} / {son2} = {son1 / son2}")
print(f"{son1} // {son2} = {son1 // son2}")
print(f"{son1} % {son2} = {son1 % son2}")
print(f"{son1} ** {son2} = {son1 ** son2}")

print("\n" + "="*50 + "\n")

# 3. String amallar
familiya = "Aliyev"
to'liq_ism = ism + " " + familiya
print(f"To'liq ism: {to'liq_ism}")
print(f"Uzunlik: {len(to'liq_ism)} belgi")
print(f"Katta harf: {to'liq_ism.upper()}")
print(f"Kichik harf: {to'liq_ism.lower()}")

print("\n" + "="*50 + "\n")

# 4. Type conversion
matn_son = "123"
haqiqiy_son = int(matn_son)
print(f"Matn: {matn_son}, Turi: {type(matn_son)}")
print(f"Son: {haqiqiy_son}, Turi: {type(haqiqiy_son)}")
print(f"Ikki barobar: {haqiqiy_son * 2}")
```

**Natija:**
```
Ism: Muhammad
Yosh: 20
Bo'y: 1.75 metr
Talabami: True

==================================================

15 + 4 = 19
15 - 4 = 11
15 * 4 = 60
15 / 4 = 3.75
15 // 4 = 3
15 % 4 = 3
15 ** 4 = 50625

==================================================

To'liq ism: Muhammad Aliyev
Uzunlik: 15 belgi
Katta harf: MUHAMMAD ALIYEV
Kichik harf: muhammad aliyev

==================================================

Matn: 123, Turi: <class 'str'>
Son: 123, Turi: <class 'int'>
Ikki barobar: 246
```

### 02 - O'rta darajadagi misollar

```python
# orta-misollar.py

# 1. Foydalanuvchi ma'lumotlari
print("=== FOYDALANUVCHI RO'YXATDAN O'TISH ===\n")

ism = input("Ismingiz: ")
familiya = input("Familiyangiz: ")
yosh = int(input("Yoshingiz: ")
email = input("Email: ")

print("\n" + "="*50)
print("Sizning ma'lumotlaringiz:")
print("="*50)
print(f"To'liq ism: {ism} {familiya}")
print(f"Yosh: {yosh}")
print(f"Email: {email}")
print(f"Foydalanuvchi ID: {ism.lower()}{yosh}")

print("\n" + "="*50 + "\n")

# 2. Oddiy kalkulyator
print("=== ODDIY KALKULYATOR ===\n")

son1 = float(input("Birinchi son: "))
amal = input("Amal (+, -, *, /): ")
son2 = float(input("Ikkinchi son: "))

if amal == "+":
    natija = son1 + son2
elif amal == "-":
    natija = son1 - son2
elif amal == "*":
    natija = son1 * son2
elif amal == "/":
    natija = son1 / son2 if son2 != 0 else "Xato: 0 ga bo'lish mumkin emas!"
else:
    natija = "Noto'g'ri amal!"

print(f"\nNatija: {son1} {amal} {son2} = {natija}")

print("\n" + "="*50 + "\n")

# 3. Matn tahlili
print("=== MATN TAHLILCHI ===\n")

matn = input("Matn kiriting: ")

print(f"\nStatistika:")
print(f"Uzunlik: {len(matn)} belgi")
print(f"So'zlar soni: {len(matn.split())}")
print(f"Katta harflar: {sum(1 for c in matn if c.isupper())}")
print(f"Kichik harflar: {sum(1 for c in matn if c.islower())}")
print(f"Raqamlar: {sum(1 for c in matn if c.isdigit())}")
print(f"Bo'sh joylar: {matn.count(' ')}")
```

### 03 - Murakkab misollar

```python
# murakkab-misollar.py

# 1. Parol kuchi tekshiruvchi
def parol_kuchini_tekshir(parol):
    """Parol kuchini baholaydi (0-100)"""
    
    kuch = 0
    
    # Uzunlik
    if len(parol) >= 8:
        kuch += 20
    if len(parol) >= 12:
        kuch += 10
    if len(parol) >= 16:
        kuch += 10
    
    # Katta harf
    if any(c.isupper() for c in parol):
        kuch += 15
    
    # Kichik harf
    if any(c.islower() for c in parol):
        kuch += 15
    
    # Raqam
    if any(c.isdigit() for c in parol):
        kuch += 15
    
    # Maxsus belgi
    maxsus = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if any(c in maxsus for c in parol):
        kuch += 15
    
    return min(kuch, 100)

print("=== PAROL KUCHI TEKSHIRUVCHI ===\n")

parol = input("Parolni kiriting: ")
kuch = parol_kuchini_tekshir(parol)

print(f"\nParol kuchi: {kuch}/100")

if kuch < 30:
    print("❌ Juda zaif parol!")
elif kuch < 60:
    print("⚠️  O'rta parol")
elif kuch < 80:
    print("✅ Yaxshi parol")
else:
    print("🔒 Juda kuchli parol!")

print("\n" + "="*50 + "\n")

# 2. Valyuta konvertori
print("=== VALYUTA KONVERTORI ===\n")

# Kurslar (2024 yil)
KURSLAR = {
    "USD": 12300,  # 1 USD = 12300 UZS
    "EUR": 13500,  # 1 EUR = 13500 UZS
    "RUB": 130,    # 1 RUB = 130 UZS
}

print("Mavjud valyutalar: USD, EUR, RUB, UZS")

dan = input("\nQaysi valyutadan: ").upper()
ga = input("Qaysi valyutaga: ").upper()
miqdor = float(input("Miqdor: "))

if dan == "UZS":
    if ga in KURSLAR:
        natija = miqdor / KURSLAR[ga]
    else:
        natija = "Xato"
elif ga == "UZS":
    if dan in KURSLAR:
        natija = miqdor * KURSLAR[dan]
    else:
        natija = "Xato"
else:
    # Ikkala valyuta ham UZS emas
    if dan in KURSLAR and ga in KURSLAR:
        uzs = miqdor * KURSLAR[dan]
        natija = uzs / KURSLAR[ga]
    else:
        natija = "Xato"

if isinstance(natija, float):
    print(f"\nNatija: {miqdor} {dan} = {natija:.2f} {ga}")
else:
    print("\nXato: Noto'g'ri valyuta kodi!")

print("\n" + "="*50 + "\n")

# 3. BMI (Body Mass Index) kalkulyator
print("=== BMI KALKULYATOR ===\n")

vazn = float(input("Vazningiz (kg): "))
boy = float(input("Bo'yingiz (metr): "))

bmi = vazn / (boy ** 2)

print(f"\nSizning BMI: {bmi:.2f}")

if bmi < 18.5:
    kategoriya = "Ozg'inlik"
    tavsiya = "Ko'proq ovqatlaning va sport bilan shug'ullaning"
elif bmi < 25:
    kategoriya = "Normal"
    tavsiya = "Juda yaxshi! Sog'lom turmush tarzingizni davom ettiring"
elif bmi < 30:
    kategoriya = "Ortiqcha vazn"
    tavsiya = "Ovqatlanishni nazorat qiling va sport bilan shug'ullaning"
else:
    kategoriya = "Semizlik"
    tavsiya = "Shifokor bilan maslahatlashing va sog'lom turmush tarziga o'ting"

print(f"Kategoriya: {kategoriya}")
print(f"Tavsiya: {tavsiya}")
```

### 04 - Hayotiy misollar (CyberSecurity)

```python
# hayotiy-misollar.py

import re
from datetime import datetime

# 1. IP Address validatori
def ip_tekshir(ip):
    """IP manzil to'g'riligini tekshiradi"""
    
    pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    match = re.match(pattern, ip)
    
    if not match:
        return False
    
    # Har bir oktet 0-255 oralig'ida bo'lishi kerak
    for oktet in match.groups():
        if int(oktet) > 255:
            return False
    
    return True

print("=== IP ADDRESS VALIDATORI ===\n")

ip = input("IP manzilni kiriting: ")

if ip_tekshir(ip):
    print(f"✅ {ip} - To'g'ri IP manzil")
    
    # IP turi
    first_oktet = int(ip.split('.')[0])
    if first_oktet < 128:
        klass = "A"
    elif first_oktet < 192:
        klass = "B"
    elif first_oktet < 224:
        klass = "C"
    elif first_oktet < 240:
        klass = "D (Multicast)"
    else:
        klass = "E (Reserved)"
    
    print(f"Klass: {klass}")
    
    # Private IP?
    if ip.startswith("10.") or ip.startswith("192.168.") or ip.startswith("172."):
        print("Tur: Private IP")
    else:
        print("Tur: Public IP")
else:
    print(f"❌ {ip} - Noto'g'ri IP manzil!")

print("\n" + "="*50 + "\n")

# 2. Port scanner input validator
print("=== PORT SCANNER INPUT VALIDATOR ===\n")

ip_manzil = input("Target IP: ")
port_range = input("Port range (1-65535 yoki 80,443,8080): ")

# IP tekshirish
if not ip_tekshir(ip_manzil):
    print("❌ Xato: Noto'g'ri IP manzil!")
else:
    print(f"✅ Target: {ip_manzil}")
    
    # Port range tekshirish
    if '-' in port_range:
        # Range format: 1-1000
        try:
            start, end = map(int, port_range.split('-'))
            if 1 <= start <= 65535 and 1 <= end <= 65535 and start <= end:
                print(f"✅ Scanning ports: {start}-{end}")
                print(f"   Total ports: {end - start + 1}")
            else:
                print("❌ Xato: Port range 1-65535 oralig'ida bo'lishi kerak!")
        except:
            print("❌ Xato: Noto'g'ri format!")
    
    elif ',' in port_range:
        # List format: 80,443,8080
        try:
            ports = [int(p.strip()) for p in port_range.split(',')]
            if all(1 <= p <= 65535 for p in ports):
                print(f"✅ Scanning ports: {', '.join(map(str, ports))}")
                print(f"   Total ports: {len(ports)}")
            else:
                print("❌ Xato: Port raqamlari 1-65535 oralig'ida bo'lishi kerak!")
        except:
            print("❌ Xato: Noto'g'ri format!")
    else:
        # Single port
        try:
            port = int(port_range)
            if 1 <= port <= 65535:
                print(f"✅ Scanning port: {port}")
            else:
                print("❌ Xato: Port 1-65535 oralig'ida bo'lishi kerak!")
        except:
            print("❌ Xato: Noto'g'ri format!")

print("\n" + "="*50 + "\n")

# 3. Log entry parser
print("=== LOG ENTRY PARSER ===\n")

log_entry = input("Log entry kiriting:\n")

# Misol: "192.168.1.100 - - [25/Oct/2024:10:30:45 +0500] GET /admin HTTP/1.1 401"

# IP ni chiqarish
ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
ip_match = re.search(ip_pattern, log_entry)

if ip_match:
    ip = ip_match.group()
    print(f"IP: {ip}")

# Sana va vaqtni chiqarish
date_pattern = r'\[([^\]]+)\]'
date_match = re.search(date_pattern, log_entry)

if date_match:
    date_str = date_match.group(1)
    print(f"Date/Time: {date_str}")

# HTTP metodini chiqarish
method_pattern = r'(GET|POST|PUT|DELETE|HEAD|OPTIONS|PATCH)'
method_match = re.search(method_pattern, log_entry)

if method_match:
    method = method_match.group()
    print(f"Method: {method}")

# URL path ni chiqarish
path_pattern = r'(GET|POST|PUT|DELETE|HEAD|OPTIONS|PATCH)\s+([^\s]+)'
path_match = re.search(path_pattern, log_entry)

if path_match:
    path = path_match.group(2)
    print(f"Path: {path}")

# Status code ni chiqarish
status_pattern = r'\s(\d{3})\s*$'
status_match = re.search(status_pattern, log_entry)

if status_match:
    status = int(status_match.group(1))
    print(f"Status Code: {status}")
    
    # Status code tahlili
    if status < 200:
        status_type = "Informational"
    elif status < 300:
        status_type = "Success"
    elif status < 400:
        status_type = "Redirection"
    elif status < 500:
        status_type = "Client Error"
    else:
        status_type = "Server Error"
    
    print(f"Status Type: {status_type}")
    
    # Xavfli so'rovlar
    if status == 401 and method in ['POST', 'GET'] and '/admin' in log_entry:
        print("⚠️  WARNING: Mumkin bo'lgan admin panelga kirish urinishi!")
    elif status == 404 and method == 'GET':
        print("ℹ️  INFO: Resource topilmadi")
```