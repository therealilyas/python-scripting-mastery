## ✅ VAZIFALAR

### OSON VAZIFALAR (Beginners)

#### Vazifa 1: Oddiy kalkulyator
```python
"""
Foydalanuvchidan 2 ta son va amal (+, -, *, /) ni so'rab,
natijani chiqaradigan dastur yozing.

Namuna:
Birinchi son: 10
Amal: +
Ikkinchi son: 5
Natija: 10 + 5 = 15
"""
```

#### Vazifa 2: Yosh kategoriyasi
```python
"""
Foydalanuvchidan yoshini so'rab, qaysi yoshga mansub
ekanligini aniqlaydigan dastur yozing:

0-12: Bola
13-19: O'smir
20-59: Kattalar
60+: Qariyalar

Namuna:
Yoshingiz: 25
Siz kattalar guruhiga kirasiz.
"""
```

#### Vazifa 3: Matn statistikasi
```python
"""
Foydalanuvchidan matn so'rab, quyidagi statistikani
chiqaradigan dastur yozing:

- Umumiy belgilar soni
- So'zlar soni
- Katta harflar soni
- Kichik harflar soni
- Raqamlar soni

Namuna:
Matn: Python 2024
Belgilar: 11
So'zlar: 2
Katta harflar: 1
Kichik harflar: 5
Raqamlar: 4
"""
```

#### Vazifa 4: Temperatura konvertor
```python
"""
Celsius dan Fahrenheit va Kelvin ga o'tkazuvchi
dastur yozing.

Formula:
F = C × 9/5 + 32
K = C + 273.15

Namuna:
Celsius: 25
Fahrenheit: 77.0
Kelvin: 298.15
"""
```

#### Vazifa 5: String manipulator
```python
"""
Foydalanuvchidan matn so'rab, quyidagi amallarni
bajaradigan dastur yozing:

1. Katta harf bilan
2. Kichik harf bilan
3. Teskari (reverse)
4. Har bir so'zni katta harf bilan (Title Case)
5. Bo'sh joylarni olib tashlash

Namuna:
Matn: hello world
1. HELLO WORLD
2. hello world
3. dlrow olleh
4. Hello World
5. helloworld
"""
```

---

### O'RTA VAZIFALAR (Intermediate)

#### Vazifa 6: Parol validator
```python
"""
Parol yaratish va tekshirish dasturi yozing. Parol quyidagi
shartlarga javob berishi kerak:

- Kamida 8 belgi
- Kamida 1 ta katta harf
- Kamida 1 ta kichik harf
- Kamida 1 ta raqam
- Kamida 1 ta maxsus belgi (!@#$%^&*)

Har bir shart uchun alohida tekshirish va natija chiqaring.

Namuna:
Parol: Hello123
✅ Uzunlik: To'g'ri (8+ belgi)
✅ Katta harf: Bor
✅ Kichik harf: Bor
✅ Raqam: Bor
❌ Maxsus belgi: Yo'q

Parol kuchi: 80/100
Status: Yaxshi parol
"""
```

#### Vazifa 7: BMI kalkulyator va tavsiya tizimi
```python
"""
BMI (Body Mass Index) hisoblab, kategoriyasini aniqlaydigan
va tavsiyalar beradigan dastur yozing.

Formula: BMI = vazn / (bo'y ** 2)

Kategoriyalar:
< 18.5: Ozg'inlik
18.5-24.9: Normal
25-29.9: Ortiqcha vazn
30+: Semizlik

Har bir kategoriya uchun maxsus tavsiyalar bering.

Qo'shimcha: Ideal vaznni ham hisoblang.
Ideal vazn = 22 * (bo'y ** 2)
"""
```

#### Vazifa 8: IP Address validator va analyzer
```python
"""
IP address ni tekshiruvchi va tahlil qiluvchi dastur yozing.

Tekshirishlar:
1. To'g'ri format (X.X.X.X)
2. Har bir oktet 0-255 oralig'ida
3. IP klassi (A, B, C, D, E)
4. Private yoki Public
5. Loopback tekshirish
6. Broadcast tekshirish

Namuna:
IP: 192.168.1.100
✅ Format: To'g'ri
✅ Oktets: To'g'ri
📊 Klass: C
🔒 Tur: Private
ℹ️  Loopback: Yo'q
ℹ️  Broadcast: Yo'q
"""
```

#### Vazifa 9: Valyuta konvertori (Multi-currency)
```python
"""
Ko'p valyutali konvertor dasturi yozing.

Valyutalar: USD, EUR, GBP, RUB, CNY, UZS

Foydalanuvchi:
1. Qaysi valyutadan
2. Qaysi valyutaga
3. Miqdor

Natija:
- O'zgartirilgan summa
- Kurs
- Teskari kurs
- Foiz farqi (spread)

Bonus: Bir necha valyutada ham ko'rsating.
"""
```

#### Vazifa 10: Login tizimi
```python
"""
Oddiy login tizimi yarating.

Funksiyalar:
1. Ro'yxatdan o'tish (username, email, password)
2. Tizimga kirish (username, password)
3. Parolni tiklash (email tekshirish)

Validatsiyalar:
- Username: 3-20 belgi, faqat harf va raqam
- Email: to'g'ri format
- Password: kamida 8 belgi, kompleks

Ma'lumotlarni dictionary da saqlang.
"""
```

---

### QIYIN VAZIFALAR (Advanced/Challenge)

#### Vazifa 11: Log file parser va analyzer
```python
"""
Log fayl tahlilchisi yarating.

Log format:
IP - - [Date] "METHOD /path" STATUS SIZE

Misol:
192.168.1.100 - - [25/Oct/2024:10:30:45] "GET /admin" 401 1234

Quyidagilarni tahlil qiling:
1. Barcha IP addresslar
2. Eng ko'p so'rov yuborgan IP (Top 5)
3. HTTP metodlar statistikasi (GET, POST, etc)
4. Status code statistikasi (200, 404, 500, etc)
5. Eng ko'p so'ralgan yo'llar (paths)
6. Xavfli so'rovlar:
   - 401/403 statuslar
   - /admin yo'liga urinishlar
   - SQL injection belgilari
7. So'rovlar grafigi (soatga nechta so'rov)
8. Sizeable downloads (katta fayllar)

Natijani chiroyli formatda chiqaring.
"""
```

#### Vazifa 12: Network subnet calculator
```python
"""
Network subnet kalkulyatori yarating.

Input:
- IP address
- Subnet mask yoki CIDR (/24)

Output:
1. Network address
2. Broadcast address
3. First usable IP
4. Last usable IP
5. Total hosts
6. Usable hosts
7. Wildcard mask
8. Binary representation
9. IP class
10. Private/Public

Bonus:
- VLSM calculation
- Subnetting (kichik tarmoqlarga bo'lish)

Misol:
IP: 192.168.1.100/24

Network: 192.168.1.0
Broadcast: 192.168.1.255
First IP: 192.168.1.1
Last IP: 192.168.1.254
Total hosts: 256
Usable hosts: 254
Class: C
Type: Private
"""
```

#### Vazifa 13: Data type converter va encoder
```python
"""
Universal ma'lumot konvertori yarating.

Quyidagi konversiyalarni qo'llab-quvvatlash:

Number systems:
- Binary ↔ Decimal ↔ Octal ↔ Hexadecimal

Text encoding:
- ASCII ↔ Unicode ↔ Base64 ↔ Hex
- URL encoding/decoding
- HTML entities encoding/decoding

Hash:
- String → MD5, SHA1, SHA256

Network:
- IP → Binary → Decimal
- MAC address formatting

Date/Time:
- Timestamp ↔ Human readable
- Timezone conversion

Bonus: Batch conversion (bir necha qiymat)
"""
```

#### Vazifa 14: Password cracker simulator
```python
"""
Parol sinash simulyatori yarating (Educational purpose only!)

Metodlar:
1. Brute Force (barcha kombinatsiyalarni sinash)
   - Faqat raqamlar
   - Harflar va raqamlar
   - Barcha belgilar
   
2. Dictionary Attack (lug'at so'zlaridan)
   - Oddiy so'zlar
   - So'z + raqam kombinatsiyasi
   
3. Pattern-based (naqsh asosida)
   - 123456, qwerty, password, etc
   
4. Hybrid (kombinatsiyalangan)

Statistika:
- Urinishlar soni
- Sarflangan vaqt
- Tezlik (parol/soniya)
- Muvaffaqiyat ehtimolligi

Warning: Faqat o'z parollaringizni test qilish uchun!

Misol:
Target: 4 raqamli PIN kod
Method: Brute Force
Character set: 0-9
Max attempts: 10000
Estimated time: X sekund

Starting...
[####------] 4567/10000 (45.67%)
Time elapsed: 12.3s
Found: 7825
Total time: 27.1s
"""
```

#### Vazifa 15: Comprehensive data validator
```python
"""
To'liq ma'lumot validator tizimi yarating.

Quyidagilarni validate qiling:

1. Network related:
   - IP address (v4, v6)
   - MAC address
   - Port number
   - Domain name
   - URL

2. Personal info:
   - Email
   - Phone (international)
   - Credit card number (Luhn algorithm)
   - Passport number
   - Social security number

3. Code related:
   - ISBN
   - UUID
   - Hex color
   - Base64 string
   - JSON format

4. Date/Time:
   - Date formats (DD/MM/YYYY, etc)
   - Time formats
   - Timezone

5. Financial:
   - Credit card number
   - IBAN
   - Currency amount

Har bir uchun:
- Validation (to'g'ri/noto'g'ri)
- Error message
- Suggestions (agar noto'g'ri bo'lsa)
- Additional info (format, type, etc)

Bonus: Batch validation va report generation
"""
```

---
