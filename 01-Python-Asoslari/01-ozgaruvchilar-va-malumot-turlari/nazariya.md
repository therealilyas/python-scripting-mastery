
## 📚 Nazariya

### O'zgaruvchi nima?

O'zgaruvchi - bu kompyuter xotirasida ma'lumot saqlaydigan **konteyner** (idish).

**Real hayotda:**
```
📦 Quti = O'zgaruvchi
🍎 Olma = Qiymat
```

**Python da:**
```python
meva = "olma"
```

### O'zgaruvchi yaratish

Python da o'zgaruvchi yaratish juda oson:

```python
# Sintaksis
o'zgaruvchi_nomi = qiymat

# Misollar
ism = "Ali"
yosh = 25
maosh = 3000.50
talaba = True
```

**Muhim:** Python da o'zgaruvchi turini ko'rsatish shart emas!

**Taqqoslash:**

**Python:**
```python
ism = "Ali"  # Oddiy!
```

**Java:**
```java
String ism = "Ali";  # Tur ko'rsatish kerak
```

### O'zgaruvchi nomlash qoidalari

#### ✅ TO'G'RI:

```python
ism = "Ali"
yosh1 = 25
_maxfiy = "secret"
KONSTANTА = 100
ismFamiliya = "Ali Valiyev"  # camelCase
ism_familiya = "Ali Valiyev"  # snake_case (Python da tavsiya etiladi)
```

#### ❌ NOTO'G'RI:

```python
1ism = "Ali"           # Raqam bilan boshlanmaydi
ism-familiya = "Ali"   # Defis ishlatilmaydi
class = "10A"          # Kalit so'z ishlatilmaydi
ism familiya = "Ali"   # Bo'sh joy bo'lmaydi
```

#### 📋 Python kalit so'zlari (ishlatish mumkin emas):

```python
and, as, assert, break, class, continue, def, del, elif, else,
except, False, finally, for, from, global, if, import, in, is,
lambda, None, nonlocal, not, or, pass, raise, return, True,
try, while, with, yield
```

### O'zgaruvchi nomlash standartlari

**Python da (PEP 8):**

```python
# 1. snake_case - o'zgaruvchilar uchun
ism_familiya = "Ali Valiyev"
foydalanuvchi_yoshi = 25

# 2. SCREAMING_SNAKE_CASE - konstantalar uchun
PI = 3.14159
MAKSIMAL_URINISHLAR = 3

# 3. PascalCase - klasslar uchun (keyinroq o'rganamiz)
class FoydalanuvchiMalumotlari:
    pass
```

---

## 📊 Asosiy ma'lumot turlari

Python da 4 ta asosiy ma'lumot turi bor:

### 1. Integer (int) - Butun sonlar

```python
yosh = 25
temperatura = -10
ball = 0
katta_son = 1_000_000  # O'qish uchun qulay

print(type(yosh))  # <class 'int'>
```

**Amallar:**
```python
a = 10
b = 3

print(a + b)   # 13 - qo'shish
print(a - b)   # 7  - ayirish
print(a * b)   # 30 - ko'paytirish
print(a / b)   # 3.333... - bo'lish (float qaytaradi)
print(a // b)  # 3  - butun bo'lish
print(a % b)   # 1  - qoldiq
print(a ** b)  # 1000 - daraja
```

### 2. Float - O'nlik sonlar

```python
narx = 99.99
pi = 3.14159
temperatura = -5.5
ilmiy = 1.5e3  # 1.5 * 10^3 = 1500.0

print(type(narx))  # <class 'float'>
```

**Aniqlik muammosi:**
```python
print(0.1 + 0.2)  # 0.30000000000000004 (!)

# Yechim: round() funksiyasi
print(round(0.1 + 0.2, 2))  # 0.3
```

### 3. String (str) - Satrlar

```python
ism = "Ali"
familiya = 'Valiyev'
matn = """Ko'p qatorli
satr"""

print(type(ism))  # <class 'str'>
```

**String amallar:**
```python
# Qo'shish (concatenation)
ism = "Ali"
familiya = "Valiyev"
to'liq_ism = ism + " " + familiya  # "Ali Valiyev"

# Ko'paytirish
print("Ha" * 3)  # "HaHaHa"

# Uzunlik
print(len("Python"))  # 6

# Indexlash
matn = "Python"
print(matn[0])   # P (birinchi belgi)
print(matn[-1])  # n (oxirgi belgi)

# Slicing
print(matn[0:3])   # Pyt
print(matn[2:])    # thon
print(matn[:4])    # Pyth
```

**String metodlari:**
```python
matn = "Python Dasturlash"

# Katta-kichik harf
print(matn.upper())      # PYTHON DASTURLASH
print(matn.lower())      # python dasturlash
print(matn.capitalize()) # Python dasturlash
print(matn.title())      # Python Dasturlash

# Bo'sh joylarni olib tashlash
matn2 = "  Python  "
print(matn2.strip())     # "Python"

# Almashtirish
print(matn.replace("Python", "Java"))  # Java Dasturlash

# Bo'lish
print(matn.split())      # ['Python', 'Dasturlash']

# Qidirish
print(matn.find("Das"))  # 7 (index)
print("Python" in matn)  # True
```

**String formatting:**
```python
# 1. f-string (tavsiya etiladi - Python 3.6+)
ism = "Ali"
yosh = 25
print(f"Mening ismim {ism}, yoshim {yosh}")
# Mening ismim Ali, yoshim 25

# 2. format()
print("Mening ismim {}, yoshim {}".format(ism, yosh))

# 3. % (eski usul)
print("Mening ismim %s, yoshim %d" % (ism, yosh))
```

### 4. Boolean (bool) - Mantiqiy qiymat

```python
rost = True
yolg'on = False

print(type(rost))  # <class 'bool'>
```

**Boolean amallar:**
```python
# Taqqoslash
print(5 > 3)       # True
print(10 == 10)    # True
print(5 != 3)      # True
print(7 <= 7)      # True

# Mantiqiy operatorlar
print(True and True)   # True
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# Amaliy misol
yosh = 18
litsenziya = True
haydash_mumkin = yosh >= 18 and litsenziya
print(haydash_mumkin)  # True
```

---

## 🔄 Type Conversion (Tur o'zgartirish)

### Avtomatik tur o'zgartirish

```python
# int + float = float
a = 10      # int
b = 3.5     # float
c = a + b   # 13.5 (float)

print(type(c))  # <class 'float'>
```

### Qo'lda tur o'zgartirish

```python
# str -> int
matn = "100"
son = int(matn)
print(son + 50)  # 150

# int -> str
yosh = 25
matn = str(yosh)
print("Yoshim: " + matn)  # Yoshim: 25

# str -> float
narx = "99.99"
son = float(narx)
print(son * 2)  # 199.98

# int -> bool
print(bool(0))   # False
print(bool(1))   # True
print(bool(-5))  # True
print(bool(""))  # False
print(bool("Hi")) # True
```

**Xato holatlar:**
```python
# Noto'g'ri tur o'zgartirish
try:
    son = int("hello")  # ValueError!
except ValueError:
    print("Xato: Matnni songa aylantirib bo'lmaydi")
```

---

## 📥📤 Input va Output

### print() - Chiqarish

```python
# Oddiy chiqarish
print("Salom")

# Ko'p qiymat
print("Ali", "Vali", "Hasan")  # Ali Vali Hasan

# sep parametri
print("Ali", "Vali", sep="-")  # Ali-Vali

# end parametri
print("Birinchi", end=" -> ")
print("Ikkinchi")  # Birinchi -> Ikkinchi

# Formatlash
ism = "Ali"
yosh = 25
print(f"Ism: {ism}, Yosh: {yosh}")
```

### input() - Kiritish

```python
# Oddiy input
ism = input("Ismingizni kiriting: ")
print(f"Salom, {ism}!")

# input() har doim string qaytaradi!
yosh = input("Yoshingiz: ")
print(type(yosh))  # <class 'str'>

# Songa o'zgartirish kerak
yosh = int(input("Yoshingiz: "))
print(type(yosh))  # <class 'int'>
```

---
