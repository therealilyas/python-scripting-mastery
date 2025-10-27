# 02 - OPERATORLAR (OPERATORS)

### Mundarija

1. [Operatorlar](./nazariya.md)
2. [Misollar](./misollar/README.md)
3. [Loyihalar](./loyihalar/)

## 🎯 Mavzu maqsadi

Ushbu darsda siz:
- ✅ Python dagi barcha operator turlarini o'rganasiz
- ✅ Arifmetik operatorlar bilan hisob-kitob qilasiz
- ✅ Taqqoslash va mantiqiy operatorlarni tushunasiz
- ✅ Bitwise operatorlarni xavfsizlik uchun ishlatishni bilasiz
- ✅ Assignment va Identity operatorlarni egallaysiz
- ✅ Operator prioritetini (precedence) bilasiz

---

## 📚 Nazariya

### Operator nima?

Operator - bu ma'lum amalni bajarish uchun maxsus belgi yoki kalit so'z.

```python
a = 5 + 3
#   ^   ^
#   |   |
#   |   +---- Operatorlar
#   +-------- Operandlar (qiymatlar)
```

### Python dagi operator turlari

1. **Arifmetik operatorlar** (Arithmetic)
2. **Taqqoslash operatorlari** (Comparison)
3. **Mantiqiy operatorlar** (Logical)
4. **Bitwise operatorlar** (Bit darajasida)
5. **Assignment operatorlar** (Tayinlash)
6. **Identity operatorlar** (O'ziga xoslik)
7. **Membership operatorlar** (A'zolik)

---

## 1️⃣ ARIFMETIK OPERATORLAR

### Asosiy arifmetik operatorlar

```python
a = 10
b = 3

# Qo'shish (+)
print(a + b)    # 13

# Ayirish (-)
print(a - b)    # 7

# Ko'paytirish (*)
print(a * b)    # 30

# Bo'lish (/) - har doim float qaytaradi
print(a / b)    # 3.3333...

# Butun bo'lish (//) - faqat butun qism
print(a // b)   # 3

# Qoldiq (%)
print(a % b)    # 1

# Daraja (**)
print(a ** b)   # 1000 (10^3)
```

### Unary operatorlar (+ va -)

```python
x = 5

print(+x)   # 5 (ijobiy)
print(-x)   # -5 (salbiy)

# Ikki marta salbiy
print(-(-x))  # 5
```

### Arifmetik operatorlar bilan turli ma'lumot turlari

```python
# Integer bilan
print(10 + 5)       # 15 (int)
print(10 - 5)       # 5 (int)
print(10 * 5)       # 50 (int)
print(10 / 5)       # 2.0 (float!)
print(10 // 5)      # 2 (int)

# Float bilan
print(10.5 + 2.5)   # 13.0 (float)
print(10.5 - 2.5)   # 8.0 (float)
print(10.5 * 2)     # 21.0 (float)
print(10.5 / 2)     # 5.25 (float)
print(10.5 // 2)    # 5.0 (float!)

# String bilan (faqat + va *)
print("Hello" + " World")   # "Hello World"
print("Ha" * 3)             # "HaHaHa"
print(3 * "Ha")             # "HaHaHa"

# List bilan (+ va *)
print([1, 2] + [3, 4])      # [1, 2, 3, 4]
print([1, 2] * 3)           # [1, 2, 1, 2, 1, 2]
```

### Amaliy misollar

```python
# Foizni hisoblash
narx = 1000
chegirma_foiz = 15
chegirma = narx * chegirma_foiz / 100
yakuniy_narx = narx - chegirma

print(f"Asl narx: {narx} so'm")
print(f"Chegirma: {chegirma} so'm ({chegirma_foiz}%)")
print(f"Yakuniy narx: {yakuniy_narx} so'm")

# Juft yoki toqligini tekshirish
son = 17
if son % 2 == 0:
    print(f"{son} - juft son")
else:
    print(f"{son} - toq son")

# Darajani hisoblash
asos = 2
daraja = 10
natija = asos ** daraja
print(f"{asos}^{daraja} = {natija}")  # 1024

# Vaqtni sekunddan soat:daqiqa:sekund ga o'tkazish
umumiy_sekund = 3725
soat = umumiy_sekund // 3600
daqiqa = (umumiy_sekund % 3600) // 60
sekund = umumiy_sekund % 60
print(f"{umumiy_sekund} sekund = {soat}:{daqiqa:02d}:{sekund:02d}")
```

---

## 2️⃣ TAQQOSLASH OPERATORLARI

### Taqqoslash operatorlari ro'yxati

```python
a = 10
b = 5

# Teng (==)
print(a == b)    # False
print(10 == 10)  # True

# Teng emas (!=)
print(a != b)    # True
print(10 != 10)  # False

# Katta (>)
print(a > b)     # True
print(5 > 10)    # False

# Kichik (<)
print(a < b)     # False
print(5 < 10)    # True

# Katta yoki teng (>=)
print(a >= b)    # True
print(10 >= 10)  # True

# Kichik yoki teng (<=)
print(a <= b)    # False
print(10 <= 10)  # True
```

### Turli ma'lumot turlarini taqqoslash

```python
# Sonlarni taqqoslash
print(10 == 10.0)      # True (qiymat bir xil)
print(type(10) == type(10.0))  # False (tur har xil)

# Stringlarni taqqoslash
print("ali" == "Ali")  # False (case-sensitive)
print("abc" < "abd")   # True (leksikografik)

# Boolean taqqoslash
print(True == 1)       # True
print(False == 0)      # True
print(True == 2)       # False

# None taqqoslash
x = None
print(x == None)       # True (lekin is yaxshiroq)
print(x is None)       # True (tavsiya etiladi)
```

### Chained comparison (Zanjirli taqqoslash)

```python
x = 15

# Odatiy usul
if x > 10 and x < 20:
    print("x 10 va 20 orasida")

# Python usuli (chained)
if 10 < x < 20:
    print("x 10 va 20 orasida")

# Ko'proq misollar
a = 5
print(1 < a < 10)        # True
print(1 < a < 10 < 20)   # True
print(5 == a == 5)       # True
print(1 <= a <= 5)       # True
```

### Amaliy misollar

```python
# Yosh validatsiyasi
yosh = int(input("Yoshingiz: "))

if 0 < yosh < 150:
    print("To'g'ri yosh")
else:
    print("Noto'g'ri yosh")

# Baho tizimi
ball = 85

if ball >= 90:
    baho = "A'lo"
elif ball >= 80:
    baho = "Yaxshi"
elif ball >= 70:
    baho = "O'rta"
elif ball >= 60:
    baho = "Qoniqarli"
else:
    baho = "Qoniqarsiz"

print(f"Ball: {ball}, Baho: {baho}")

# Parol kuchini tekshirish
parol = "MyPass123"
uzunlik = len(parol)

if uzunlik < 6:
    kuch = "Juda zaif"
elif uzunlik < 8:
    kuch = "Zaif"
elif uzunlik < 12:
    kuch = "O'rta"
else:
    kuch = "Kuchli"

print(f"Parol uzunligi: {uzunlik}")
print(f"Parol kuchi: {kuch}")
```

---

## 3️⃣ MANTIQIY OPERATORLAR (LOGICAL)

### and, or, not operatorlari

```python
# AND - ikkala shart ham to'g'ri bo'lishi kerak
print(True and True)      # True
print(True and False)     # False
print(False and False)    # False

# OR - kamida bitta shart to'g'ri bo'lishi kerak
print(True or False)      # True
print(False or False)     # False
print(True or True)       # True

# NOT - shartni teskari qiladi
print(not True)           # False
print(not False)          # True
```

### Truth table (Haqiqat jadvali)

```python
# AND operatori
"""
A     | B     | A and B
------|-------|--------
True  | True  | True
True  | False | False
False | True  | False
False | False | False
"""

# OR operatori
"""
A     | B     | A or B
------|-------|--------
True  | True  | True
True  | False | True
False | True  | True
False | False | False
"""

# NOT operatori
"""
A     | not A
------|-------
True  | False
False | True
"""
```

### Mantiqiy operatorlar bilan amaliy misollar

```python
# Login tizimi
username = "admin"
password = "12345"

kirish_username = input("Username: ")
kirish_password = input("Password: ")

if kirish_username == username and kirish_password == password:
    print("✅ Muvaffaqiyatli kirildi!")
else:
    print("❌ Username yoki parol noto'g'ri!")

# Yosh va litsenziya tekshirish
yosh = 20
litsenziya = True

if yosh >= 18 and litsenziya:
    print("✅ Mashina haydashingiz mumkin")
else:
    print("❌ Mashina haydash mumkin emas")
    if yosh < 18:
        print("   Sabab: Yoshingiz yetarli emas")
    if not litsenziya:
        print("   Sabab: Litsenziya yo'q")

# Hafta kuni yoki dam olish kunini aniqlash
kun = "Shanba"

if kun == "Shanba" or kun == "Yakshanba":
    print("Dam olish kuni! 🎉")
else:
    print("Ish kuni 💼")

# Raqamni tekshirish
raqam = input("Raqam kiriting: ")

if raqam.isdigit() and int(raqam) > 0:
    print("✅ To'g'ri musbat raqam")
else:
    print("❌ Noto'g'ri kiritildi")
```

### Short-circuit evaluation

Python mantiqiy operatorlarni "short-circuit" usulida baholaydi:

```python
# AND - birinchi False bo'lsa, keyingisini tekshirmaydi
def birinchi():
    print("Birinchi funksiya")
    return False

def ikkinchi():
    print("Ikkinchi funksiya")
    return True

print(birinchi() and ikkinchi())
# Natija:
# Birinchi funksiya
# False
# (ikkinchi funksiya ishlamadi!)

# OR - birinchi True bo'lsa, keyingisini tekshirmaydi
def uchinchi():
    print("Uchinchi funksiya")
    return True

def to'rtinchi():
    print("To'rtinchi funksiya")
    return False

print(uchinchi() or to'rtinchi())
# Natija:
# Uchinchi funksiya
# True
# (to'rtinchi funksiya ishlamadi!)
```

### Complex logical expressions

```python
# Murakkab mantiqiy ifodalar
yosh = 25
daromad = 5000
kredit_tarixi = True
qarzdorlik = False

# Kredit olish shartlari
kredit_mumkin = (
    yosh >= 21 and
    yosh <= 65 and
    daromad >= 3000 and
    kredit_tarixi and
    not qarzdorlik
)

if kredit_mumkin:
    print("✅ Kredit olishingiz mumkin")
else:
    print("❌ Kredit olish mumkin emas")
    
    # Batafsil sabab
    if not (21 <= yosh <= 65):
        print(f"   - Yosh talabiga mos emas: {yosh}")
    if daromad < 3000:
        print(f"   - Daromad kam: {daromad} (kerak: 3000+)")
    if not kredit_tarixi:
        print("   - Kredit tarixi yo'q")
    if qarzdorlik:
        print("   - Qarzdorlik mavjud")
```

---

## 4️⃣ ASSIGNMENT OPERATORLAR (TAYINLASH)

### Oddiy assignment

```python
# Oddiy tayinlash
x = 10
print(x)  # 10

# Ko'p o'zgaruvchiga bir qiymat
a = b = c = 5
print(a, b, c)  # 5 5 5

# Bir necha o'zgaruvchiga har xil qiymat
x, y, z = 1, 2, 3
print(x, y, z)  # 1 2 3

# Qiymatlarni almashtirish
a, b = 10, 20
a, b = b, a
print(a, b)  # 20 10
```

### Compound assignment operatorlari

```python
x = 10

# += (qo'shib tayinlash)
x += 5      # x = x + 5
print(x)    # 15

# -= (ayirib tayinlash)
x -= 3      # x = x - 3
print(x)    # 12

# *= (ko'paytirib tayinlash)
x *= 2      # x = x * 2
print(x)    # 24

# /= (bo'lib tayinlash)
x /= 4      # x = x / 4
print(x)    # 6.0

# //= (butun bo'lib tayinlash)
x //= 2     # x = x // 2
print(x)    # 3.0

# %= (qoldiqni tayinlash)
x = 10
x %= 3      # x = x % 3
print(x)    # 1

# **= (darajaga oshirib tayinlash)
x = 2
x **= 3     # x = x ** 3
print(x)    # 8
```

### Stringlar bilan assignment

```python
# String qo'shish
matn = "Hello"
matn += " World"
print(matn)  # "Hello World"

# String takrorlash
yulduz = "*"
yulduz *= 10
print(yulduz)  # "**********"
```

### Listlar bilan assignment

```python
# List qo'shish
royxat = [1, 2, 3]
royxat += [4, 5]
print(royxat)  # [1, 2, 3, 4, 5]

# List takrorlash
sonlar = [1, 2]
sonlar *= 3
print(sonlar)  # [1, 2, 1, 2, 1, 2]
```

### Walrus operator (:=) - Python 3.8+

```python
# Oddiy usul
n = len([1, 2, 3, 4, 5])
if n > 3:
    print(f"Ro'yxat katta: {n} element")

# Walrus operator bilan
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"Ro'yxat katta: {n} element")

# While loop bilan
# Oddiy usul
line = input("Matn: ")
while line != "quit":
    print(f"Siz yozdingiz: {line}")
    line = input("Matn: ")

# Walrus bilan
while (line := input("Matn: ")) != "quit":
    print(f"Siz yozdingiz: {line}")
```

---

## 5️⃣ BITWISE OPERATORLAR

Bitwise operatorlar - sonlarni binary (ikkilik) darajasida boshqarish uchun.

### Bitwise operatorlar ro'yxati

```python
a = 60  # 0011 1100
b = 13  # 0000 1101

# & (AND) - ikkalasi ham 1 bo'lsa 1
print(a & b)   # 12 (0000 1100)

# | (OR) - kamida biri 1 bo'lsa 1
print(a | b)   # 61 (0011 1101)

# ^ (XOR) - faqat biri 1 bo'lsa 1
print(a ^ b)   # 49 (0011 0001)

# ~ (NOT) - bitlarni teskariga o'girish
print(~a)      # -61

# << (Left shift) - chapga siljitish
print(a << 2)  # 240 (1111 0000)

# >> (Right shift) - o'ngga siljitish
print(a >> 2)  # 15 (0000 1111)
```

### Binary formatda ko'rish

```python
a = 60
b = 13

print(f"a = {a:08b}")      # 00111100
print(f"b = {b:08b}")      # 00001101
print(f"a & b = {a&b:08b}") # 00001100
print(f"a | b = {a|b:08b}") # 00111101
print(f"a ^ b = {a^b:08b}") # 00110001
```

### CyberSecurity da bitwise operatorlar

```python
# 1. Flag-based permissions (Linux fayl ruxsatlari)
# Read = 4 (100), Write = 2 (010), Execute = 1 (001)

READ = 4    # 0100
WRITE = 2   # 0010
EXECUTE = 1 # 0001

# Ruxsatlarni o'rnatish
permissions = READ | WRITE | EXECUTE  # 0111 = 7
print(f"Permissions: {permissions}")  # 7 (rwx)

# Ruxsatni tekshirish
if permissions & READ:
    print("Read ruxsati bor")

if permissions & WRITE:
    print("Write ruxsati bor")

if permissions & EXECUTE:
    print("Execute ruxsati bor")

# 2. IP subnet mask manipulation
ip = 192 * (256**3) + 168 * (256**2) + 1 * 256 + 100
mask = 255 * (256**3) + 255 * (256**2) + 255 * 256 + 0

# Network address
network = ip & mask
print(f"Network: {(network >> 24) & 255}.{(network >> 16) & 255}.{(network >> 8) & 255}.{network & 255}")

# 3. Simple encryption/decryption (XOR cipher)
def xor_encrypt(text, key):
    """XOR shifrlash"""
    return ''.join(chr(ord(char) ^ key) for char in text)

def xor_decrypt(encrypted, key):
    """XOR deshifrlash (bir xil funksiya)"""
    return xor_encrypt(encrypted, key)

plaintext = "Secret"
key = 123

encrypted = xor_encrypt(plaintext, key)
print(f"Encrypted: {encrypted}")

decrypted = xor_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")

# 4. Bit masking for flags
# Network packet flags
SYN = 1 << 0  # 00000001
ACK = 1 << 1  # 00000010
FIN = 1 << 2  # 00000100
RST = 1 << 3  # 00001000
PSH = 1 << 4  # 00010000
URG = 1 << 5  # 00100000

# TCP SYN packet
packet_flags = SYN
print(f"Packet flags: {packet_flags:08b}")

# TCP SYN-ACK packet
packet_flags = SYN | ACK
print(f"Packet flags: {packet_flags:08b}")

# Check if ACK flag is set
if packet_flags & ACK:
    print("ACK flag set")
```

---

## 6️⃣ IDENTITY OPERATORLAR (is, is not)

Identity operatorlar - ikkita obyekt bir xil xotira manzilida joylashganligini tekshiradi.

```python
# is - bir xil obyektmi?
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True (qiymat bir xil)
print(a is b)   # False (har xil obyektlar)
print(a is c)   # True (bir xil obyekt)

# ID ni ko'rish
print(id(a))
print(id(b))
print(id(c))

# is not
print(a is not b)  # True
```

### None bilan ishlash

```python
x = None

# To'g'ri usul
if x is None:
    print("x None")

# Noto'g'ri usul (lekin ishlaydi)
if x == None:
    print("x None")

# is tezroq va xavfsizroq
```

### Small integer caching

Python -5 dan 256 gacha bo'lgan sonlarni keshda saqlaydi:

```python
a = 256
b = 256
print(a is b)  # True (keshda)

a = 257
b = 257
print(a is b)  # False (keshda emas)

# Lekin qiymat bir xil
print(a == b)  # True
```

---

## 7️⃣ MEMBERSHIP OPERATORLAR (in, not in)

Membership operatorlar - element to'plamda borligini tekshiradi.

```python
# Stringda
print('H' in 'Hello')      # True
print('x' in 'Hello')      # False
print('hell' in 'Hello')   # False (case-sensitive)
print('ell' in 'Hello')    # True

# Listda
royxat = [1, 2, 3, 4, 5]
print(3 in royxat)         # True
print(10 in royxat)        # False
print(3 not in royxat)     # False

# Tuple da
tuple_data = (10, 20, 30)
print(20 in tuple_data)    # True

# Set da
to'plam = {1, 2, 3, 4, 5}
print(3 in to'plam)        # True

# Dictionary da (kalit tekshiriladi)
lug'at = {'ism': 'Ali', 'yosh': 25}
print('ism' in lug'at)     # True
print('Ali' in lug'at)     # False (qiymat emas, kalit)
print('Ali' in lug'at.values())  # True
```

### Amaliy misollar

```python
# Email validatsiya
email = "user@example.com"
if '@' in email and '.' in email:
    print("✅ Email format to'g'ri")
else:
    print("❌ Email format noto'g'ri")

# Ruxsat berilgan belgilar
ruxsat_berilgan = "abcdefghijklmnopqrstuvwxyz0123456789"
username = input("Username: ")

if all(c.lower() in ruxsat_berilgan for c in username):
    print("✅ Username to'g'ri")
else:
    print("❌ Faqat harf va raqam ishlatish mumkin")

# SQL injection detection
user_input = input("Search: ")
xavfli_sozlar = ['DROP', 'DELETE', 'INSERT', 'UPDATE', '--', ';']

if any(soz in user_input.upper() for soz in xavfli_sozlar):
    print("⚠️  Xavfli so'rov aniqlandi!")
else:
    print("✅ Xavfsiz so'rov")
```

---

## 8️⃣ OPERATOR PRECEDENCE (USTUNLIK)

Operatorlar bajarilish tartibining ustuvor ligi:

```python
# Tartib (yuqoridan pastga):
# 1. ()              - Qavs
# 2. **              - Daraja
# 3. +x, -x, ~x      - Unary
# 4. *, /, //, %     - Ko'paytirish, bo'lish
# 5. +, -            - Qo'shish, ayirish
# 6. <<, >>          - Bitwise shift
# 7. &               - Bitwise AND
# 8. ^               - Bitwise XOR
# 9. |               - Bitwise OR
# 10. ==, !=, <, >, <=, >=, is, in  - Taqqoslash
# 11. not            - Mantiqiy NOT
# 12. and            - Mantiqiy AND
# 13. or             - Mantiqiy OR

# Misollar:
print(2 + 3 * 4)      # 14 (*, keyin +)
print((2 + 3) * 4)    # 20 (qavs birinchi)

print(10 / 2 * 3)     # 15.0 (chapdan o'ngga)
print(10 / (2 * 3))   # 1.666... (qavs birinchi)

print(5 < 10 and 3 > 1)   # True
print(5 < 10 or 3 < 1)    # True

print(not 5 < 10 and 3 > 1)  # False (not birinchi)
print(not (5 < 10 and 3 > 1)) # False (qavs birinchi)
```

### Qavs ishlatish - eng yaxshi amaliyot

```python
# Yomon - tushunish qiyin
if x > 0 and x < 100 or y == 50:
    pass

# Yaxshi - aniq va tushunarli
if (x > 0 and x < 100) or (y == 50):
    pass

# Yomon
result = a + b * c ** d / e

# Yaxshi
result = a + ((b * (c ** d)) / e)
```

---

## 💡 MISOLLAR

### 01 - Oddiy misollar

```python
# 01-oddiy-misollar.py

"""
OPERATORLAR - ODDIY MISOLLAR
Barcha operator turlarining sodda misollari
"""

print("="*60)
print(" "*20 + "OPERATORLAR")
print("="*60 + "\n")

# 1. ARIFMETIK OPERATORLAR
print("1. ARIFMETIK OPERATORLAR\n")

a = 15
b = 4

print(f"a = {a}, b = {b}\n")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b:.2f}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")
print(f"a ** b = {a ** b}")

print("\n" + "="*60 + "\n")

# 2. TAQQOSLASH OPERATORLARI
print("2. TAQQOSLASH OPERATORLARI\n")

x = 10
y = 20

print(f"x = {x}, y = {y}\n")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x >= y: {x >= y}")
print(f"x <= y: {x <= y}")

print("\n" + "="*60 + "\n")

# 3. MANTIQIY OPERATORLAR
print("3. MANTIQIY OPERATORLAR\n")

p = True
q = False

print(f"p = {p}, q = {q}\n")
print(f"p and q: {p and q}")
print(f"p or q: {p or q}")
print(f"not p: {not p}")
print(f"not q: {not q}")

print("\n" + "="*60 + "\n")

# 4. ASSIGNMENT OPERATORLAR
print("4. ASSIGNMENT OPERATORLAR\n")

num = 10
print(f"Boshlang'ich qiymat: {num}")

num += 5
print(f"num += 5: {num}")

num -= 3
print(f"num -= 3: {num}")

num *= 2
print(f"num *= 2: {num}")

num /= 4
print(f"num /= 4: {num}")

print("\n" + "="*60 + "\n")

# 5. MEMBERSHIP OPERATORLAR
print("5. MEMBERSHIP OPERATORLAR\n")

royxat = [1, 2, 3, 4, 5]
matn = "Python"

print(f"Royxat: {royxat}")
print(f"3 in royxat: {3 in royxat
}")
print(f"10 in royxat: {10 in royxat}")
print(f"10 not in royxat: {10 not in royxat}")

print(f"\nMatn: '{matn}'")
print(f"'P' in matn: {'P' in matn}")
print(f"'x' in matn: {'x' in matn}")
print(f"'Py' in matn: {'Py' in matn}")

print("\n" + "="*60 + "\n")

# 6. IDENTITY OPERATORLAR
print("6. IDENTITY OPERATORLAR\n")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = list1\n")

print(f"list1 == list2: {list1 == list2} (qiymat)")
print(f"list1 is list2: {list1 is list2} (obyekt)")
print(f"list1 is list3: {list1 is list3} (obyekt)")

print(f"\nlist1 ID: {id(list1)}")
print(f"list2 ID: {id(list2)}")
print(f"list3 ID: {id(list3)}")

print("\n" + "="*60 + "\n")

# 7. BITWISE OPERATORLAR
print("7. BITWISE OPERATORLAR\n")

m = 12  # 1100
n = 10  # 1010

print(f"m = {m} ({m:04b})")
print(f"n = {n} ({n:04b})\n")

print(f"m & n = {m & n} ({m & n:04b}) - AND")
print(f"m | n = {m | n} ({m | n:04b}) - OR")
print(f"m ^ n = {m ^ n} ({m ^ n:04b}) - XOR")
print(f"~m = {~m} - NOT")
print(f"m << 1 = {m << 1} ({m << 1:05b}) - Left shift")
print(f"m >> 1 = {m >> 1} ({m >> 1:03b}) - Right shift")

print("\n" + "="*60)
```

### 02 - O'rta darajadagi misollar

```python
# 02-orta-misollar.py

"""
OPERATORLAR - O'RTA DARAJADAGI MISOLLAR
Real hayotiy vazifalar
"""

import math

def banner(text):
    """Chiroyli banner chiqarish"""
    print("\n" + "="*70)
    print(f"{text:^70}")
    print("="*70 + "\n")

# 1. KALKULYATOR DASTURI
banner("ILMIY KALKULYATOR")

def kalkulyator():
    """Kengaytirilgan kalkulyator"""
    
    print("Mavjud amallar:")
    print("1. Qo'shish (+)")
    print("2. Ayirish (-)")
    print("3. Ko'paytirish (*)")
    print("4. Bo'lish (/)")
    print("5. Butun bo'lish (//)")
    print("6. Qoldiq (%)")
    print("7. Daraja (**)")
    print("8. Ildiz (sqrt)")
    print("9. Sinus (sin)")
    print("10. Kosinus (cos)")
    
    tanlov = input("\nAmal raqamini kiriting (1-10): ")
    
    if tanlov in ['1', '2', '3', '4', '5', '6', '7']:
        son1 = float(input("Birinchi son: "))
        son2 = float(input("Ikkinchi son: "))
        
        if tanlov == '1':
            natija = son1 + son2
            amal = "+"
        elif tanlov == '2':
            natija = son1 - son2
            amal = "-"
        elif tanlov == '3':
            natija = son1 * son2
            amal = "*"
        elif tanlov == '4':
            if son2 != 0:
                natija = son1 / son2
                amal = "/"
            else:
                print("❌ Xato: 0 ga bo'lish mumkin emas!")
                return
        elif tanlov == '5':
            if son2 != 0:
                natija = son1 // son2
                amal = "//"
            else:
                print("❌ Xato: 0 ga bo'lish mumkin emas!")
                return
        elif tanlov == '6':
            if son2 != 0:
                natija = son1 % son2
                amal = "%"
            else:
                print("❌ Xato: 0 ga bo'lish mumkin emas!")
                return
        elif tanlov == '7':
            natija = son1 ** son2
            amal = "**"
        
        print(f"\n✅ Natija: {son1} {amal} {son2} = {natija}")
    
    elif tanlov == '8':
        son = float(input("Son kiriting: "))
        if son >= 0:
            natija = math.sqrt(son)
            print(f"\n✅ √{son} = {natija}")
        else:
            print("❌ Xato: Manfiy sondan ildiz olib bo'lmaydi!")
    
    elif tanlov == '9':
        burchak = float(input("Burchak (gradus): "))
        radian = math.radians(burchak)
        natija = math.sin(radian)
        print(f"\n✅ sin({burchak}°) = {natija:.4f}")
    
    elif tanlov == '10':
        burchak = float(input("Burchak (gradus): "))
        radian = math.radians(burchak)
        natija = math.cos(radian)
        print(f"\n✅ cos({burchak}°) = {natija:.4f}")
    
    else:
        print("❌ Noto'g'ri tanlov!")

kalkulyator()

# 2. YOSH VA RUXSAT TEKSHIRUVCHI
banner("YOSH VA RUXSAT TEKSHIRUVCHI")

def yosh_tekshir():
    """Yoshga qarab ruxsatlarni aniqlash"""
    
    ism = input("Ismingiz: ")
    yosh = int(input("Yoshingiz: "))
    
    print(f"\n{'='*50}")
    print(f"Ism: {ism}")
    print(f"Yosh: {yosh}")
    print(f"{'='*50}\n")
    
    # Kategoriya aniqlash
    if yosh < 0 or yosh > 150:
        print("❌ Noto'g'ri yosh!")
        return
    elif yosh < 7:
        kategoriya = "Maktabgacha"
    elif yosh < 18:
        kategoriya = "Voyaga yetmagan"
    elif yosh < 65:
        kategoriya = "Kattalar"
    else:
        kategoriya = "Pensioner"
    
    print(f"📊 Kategoriya: {kategoriya}\n")
    
    # Ruxsatlar
    print("🔐 RUXSATLAR:\n")
    
    # Haydovchilik guvohnomasi
    if yosh >= 18:
        print("✅ Haydovchilik guvohnomasi olish mumkin")
    else:
        print(f"❌ Haydovchilik guvohnomasi ({18 - yosh} yildan keyin)")
    
    # Ovoz berish
    if yosh >= 18:
        print("✅ Saylovlarda ovoz berish mumkin")
    else:
        print(f"❌ Saylovlarda ovoz berish ({18 - yosh} yildan keyin)")
    
    # Alkogol
    if yosh >= 21:
        print("✅ Alkogol sotib olish mumkin")
    else:
        print(f"❌ Alkogol sotib olish ({21 - yosh} yildan keyin)")
    
    # Pensiya
    if yosh >= 65:
        print("✅ Pensiya olish mumkin")
    else:
        print(f"ℹ️  Pensiya ({65 - yosh} yildan keyin)")
    
    # Chegirmalar
    if yosh < 18 or yosh >= 65:
        print("✅ Transport va kinoda chegirma bor")
    else:
        print("ℹ️  Transport va kinoda chegirma yo'q")

yosh_tekshir()

# 3. PAROL KUCHINI TEKSHIRISH
banner("PAROL KUCHI TEKSHIRUVCHI")

def parol_kuchi_tekshir():
    """Parol kuchini batafsil tahlil qilish"""
    
    parol = input("Parol kiriting: ")
    
    # Statistika
    uzunlik = len(parol)
    katta_harf = sum(1 for c in parol if c.isupper())
    kichik_harf = sum(1 for c in parol if c.islower())
    raqam = sum(1 for c in parol if c.isdigit())
    maxsus = sum(1 for c in parol if c in "!@#$%^&*()_+-=[]{}|;:,.<>?")
    
    print(f"\n{'='*50}")
    print("PAROL TAHLILI")
    print(f"{'='*50}\n")
    
    # Uzunlik
    print(f"📏 Uzunlik: {uzunlik} belgi")
    if uzunlik >= 12:
        print("   ✅ Juda yaxshi uzunlik")
    elif uzunlik >= 8:
        print("   ⚠️  O'rta uzunlik (12+ tavsiya etiladi)")
    else:
        print("   ❌ Juda qisqa (8+ kerak)")
    
    # Katta harf
    print(f"\n🔤 Katta harflar: {katta_harf} ta")
    if katta_harf > 0:
        print("   ✅ Katta harf bor")
    else:
        print("   ❌ Katta harf yo'q")
    
    # Kichik harf
    print(f"\n🔡 Kichik harflar: {kichik_harf} ta")
    if kichik_harf > 0:
        print("   ✅ Kichik harf bor")
    else:
        print("   ❌ Kichik harf yo'q")
    
    # Raqam
    print(f"\n🔢 Raqamlar: {raqam} ta")
    if raqam > 0:
        print("   ✅ Raqam bor")
    else:
        print("   ❌ Raqam yo'q")
    
    # Maxsus belgi
    print(f"\n⚡ Maxsus belgilar: {maxsus} ta")
    if maxsus > 0:
        print("   ✅ Maxsus belgi bor")
    else:
        print("   ❌ Maxsus belgi yo'q")
    
    # Umumiy ball (100 ball tizimida)
    ball = 0
    
    # Uzunlik (40 ball)
    if uzunlik >= 16:
        ball += 40
    elif uzunlik >= 12:
        ball += 30
    elif uzunlik >= 8:
        ball += 20
    else:
        ball += uzunlik * 2
    
    # Katta harf (15 ball)
    if katta_harf > 0:
        ball += 15
    
    # Kichik harf (15 ball)
    if kichik_harf > 0:
        ball += 15
    
    # Raqam (15 ball)
    if raqam > 0:
        ball += 15
    
    # Maxsus belgi (15 ball)
    if maxsus > 0:
        ball += 15
    
    # Natija
    print(f"\n{'='*50}")
    print(f"UMUMIY BALL: {ball}/100")
    print(f"{'='*50}\n")
    
    # Xulosa
    if ball >= 80:
        print("🔒 JUDA KUCHLI PAROL!")
        print("   Ajoyib! Parolingiz juda xavfsiz.")
    elif ball >= 60:
        print("✅ YAXSHI PAROL")
        print("   Yaxshi parol, lekin yanada yaxshiroq qilish mumkin.")
    elif ball >= 40:
        print("⚠️  O'RTA PAROL")
        print("   Parolingizni kuchliroq qiling!")
    else:
        print("❌ ZAIF PAROL!")
        print("   Juda xavfli! Yangi parol o'ylab toping!")
    
    # Tavsiyalar
    print("\n💡 TAVSIYALAR:")
    if uzunlik < 12:
        print("   - Kamida 12 belgi ishlatish")
    if katta_harf == 0:
        print("   - Katta harflar qo'shish (A-Z)")
    if kichik_harf == 0:
        print("   - Kichik harflar qo'shish (a-z)")
    if raqam == 0:
        print("   - Raqamlar qo'shish (0-9)")
    if maxsus == 0:
        print("   - Maxsus belgilar qo'shish (!@#$%^&*)")
    
    # Oddiy parollar tekshirish
    oddiy_parollar = [
        'password', '12345678', 'qwerty', 'abc123', 
        'password123', 'admin', 'letmein', 'welcome'
    ]
    
    if parol.lower() in oddiy_parollar:
        print("\n⚠️⚠️⚠️  OGOHLANTIRISH! ⚠️⚠️⚠️")
        print("Bu parol juda oddiy va mashhur!")
        print("Hackerlar bir zumda topib olishi mumkin!")

parol_kuchi_tekshir()

# 4. BMI KALKULYATOR
banner("BMI KALKULYATOR")

def bmi_kalkulyator():
    """BMI hisoblash va tavsiyalar"""
    
    print("Body Mass Index (BMI) kalkulyatori\n")
    
    vazn = float(input("Vazningiz (kg): "))
    boy = float(input("Bo'yingiz (metr): "))
    
    # BMI hisoblash
    bmi = vazn / (boy ** 2)
    
    # Ideal vazn
    ideal_vazn_min = 18.5 * (boy ** 2)
    ideal_vazn_max = 24.9 * (boy ** 2)
    
    print(f"\n{'='*60}")
    print("NATIJALAR")
    print(f"{'='*60}\n")
    
    print(f"📊 Sizning BMI: {bmi:.2f}")
    print(f"⚖️  Ideal vazn oralig'i: {ideal_vazn_min:.1f} - {ideal_vazn_max:.1f} kg\n")
    
    # Kategoriya aniqlash
    if bmi < 16:
        kategoriya = "Jiddiy ozg'inlik"
        emoji = "🚨"
        xavf = "Juda yuqori"
        rang = "Qizil"
    elif bmi < 17:
        kategoriya = "O'rtacha ozg'inlik"
        emoji = "⚠️"
        xavf = "Yuqori"
        rang = "To'q sariq"
    elif bmi < 18.5:
        kategoriya = "Engil ozg'inlik"
        emoji = "⚠️"
        xavf = "O'rta"
        rang = "Sariq"
    elif bmi < 25:
        kategoriya = "Normal (sog'lom)"
        emoji = "✅"
        xavf = "Past"
        rang = "Yashil"
    elif bmi < 30:
        kategoriya = "Ortiqcha vazn"
        emoji = "⚠️"
        xavf = "O'rta"
        rang = "Sariq"
    elif bmi < 35:
        kategoriya = "1-darajali semizlik"
        emoji = "⚠️"
        xavf = "Yuqori"
        rang = "To'q sariq"
    elif bmi < 40:
        kategoriya = "2-darajali semizlik"
        emoji = "🚨"
        xavf = "Juda yuqori"
        rang = "Qizil"
    else:
        kategoriya = "3-darajali semizlik (ekstrem)"
        emoji = "🚨"
        xavf = "Ekstrem yuqori"
        rang = "To'q qizil"
    
    print(f"{emoji} Kategoriya: {kategoriya}")
    print(f"📈 Xavf darajasi: {xavf}")
    print(f"🎨 Rang: {rang}\n")
    
    # Vazn farqi
    if bmi < 18.5:
        farq = ideal_vazn_min - vazn
        print(f"📉 Ideal vazndan {farq:.1f} kg kam")
        print(f"   Maqsad: {farq:.1f} kg olish\n")
    elif bmi > 24.9:
        farq = vazn - ideal_vazn_max
        print(f"📈 Ideal vazndan {farq:.1f} kg ko'p")
        print(f"   Maqsad: {farq:.1f} kg yo'qotish\n")
    else:
        print("✅ Siz ideal vazn oralig'idasiz!\n")
    
    # Tavsiyalar
    print(f"{'='*60}")
    print("TAVSIYALAR")
    print(f"{'='*60}\n")
    
    if bmi < 18.5:
        print("📋 OVQATLANISH:")
        print("   - Kaloriya iste'molini oshiring")
        print("   - Protein va yog'larni ko'proq iste'mol qiling")
        print("   - Kichik-kichik, lekin tez-tez ovqatlaning (5-6 marta)")
        print("\n💪 MASHQLAR:")
        print("   - Og'irlik ko'tarish (strength training)")
        print("   - Mushak qurish mashqlari")
        print("   - Yogurt qiling va dam oling")
        
    elif bmi >= 25:
        print("📋 OVQATLANISH:")
        print("   - Kaloriya iste'molini kamaytiring")
        print("   - Ko'proq sabzavot va mevalar")
        print("   - Tez-tez ovqatlanishdan qoching")
        print("   - Shakar va yog'li ovqatlarni cheklang")
        print("\n💪 MASHQLAR:")
        print("   - Kuniga 30-60 daqiqa yugurishlar")
        print("   - Kardio mashqlar (yugurish, suzish)")
        print("   - Hafta 150+ daqiqa jismoniy faollik")
        
    else:
        print("✅ Sog'lom turmush tarzingizni davom ettiring!")
        print("\n📋 OVQATLANISH:")
        print("   - Muvozanatli ovqatlanish")
        print("   - Yetarli suv iste'mol qiling (2-3 litr)")
        print("\n💪 MASHQLAR:")
        print("   - Hafta 150 daqiqa o'rtacha intensivlik")
        print("   - 2-3 marta mushak mashqlari")
    
    print(f"\n⚕️  ESLATMA: Jiddiy holatda shifokor bilan maslahatlashing!\n")

bmi_kalkulyator()

# 5. VAQT VA SANA OPERATSIYALARI
banner("VAQT KONVERTOR")

def vaqt_konvertor():
    """Vaqtni turli birliklarga o'tkazish"""
    
    print("Vaqtni turli birliklarga o'tkazish\n")
    print("1. Sekunddan boshqa birliklarga")
    print("2. Daqiqadan boshqa birliklarga")
    print("3. Soatdan boshqa birliklarga")
    print("4. Kundan boshqa birliklarga")
    
    tanlov = input("\nTanlov (1-4): ")
    
    if tanlov == '1':
        sekund = float(input("Sekund: "))
        
        daqiqa = sekund / 60
        soat = sekund / 3600
        kun = sekund / 86400
        hafta = sekund / 604800
        
        print(f"\n{sekund} sekund =")
        print(f"   {daqiqa:.2f} daqiqa")
        print(f"   {soat:.2f} soat")
        print(f"   {kun:.4f} kun")
        print(f"   {hafta:.6f} hafta")
        
    elif tanlov == '2':
        daqiqa = float(input("Daqiqa: "))
        
        sekund = daqiqa * 60
        soat = daqiqa / 60
        kun = daqiqa / 1440
        
        print(f"\n{daqiqa} daqiqa =")
        print(f"   {sekund:.0f} sekund")
        print(f"   {soat:.2f} soat")
        print(f"   {kun:.4f} kun")
        
    elif tanlov == '3':
        soat = float(input("Soat: "))
        
        sekund = soat * 3600
        daqiqa = soat * 60
        kun = soat / 24
        hafta = soat / 168
        
        print(f"\n{soat} soat =")
        print(f"   {sekund:.0f} sekund")
        print(f"   {daqiqa:.0f} daqiqa")
        print(f"   {kun:.2f} kun")
        print(f"   {hafta:.4f} hafta")
        
    elif tanlov == '4':
        kun = float(input("Kun: "))
        
        sekund = kun * 86400
        daqiqa = kun * 1440
        soat = kun * 24
        hafta = kun / 7
        oy = kun / 30
        yil = kun / 365
        
        print(f"\n{kun} kun =")
        print(f"   {sekund:.0f} sekund")
        print(f"   {daqiqa:.0f} daqiqa")
        print(f"   {soat:.0f} soat")
        print(f"   {hafta:.2f} hafta")
        print(f"   {oy:.2f} oy")
        print(f"   {yil:.2f} yil")
    
    else:
        print("Noto'g'ri tanlov!")

vaqt_konvertor()
```
