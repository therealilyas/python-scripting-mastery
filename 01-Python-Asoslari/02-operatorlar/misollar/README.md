# 🧠 MAVZU: OPERATORLAR — ODDIY MISOLLAR

Ushbu dasturda **Python** dasturlash tilidagi barcha **operator turlari** uchun  
asosiy va sodda misollar keltirilgan.

---

## 📘 Dastur haqida

Fayl nomi: `01-oddiy-misollar.py`  
Maqsad: Har bir operator turini amaliy misollar orqali o‘rganish.  
Natija: Har bir operatorning qanday ishlashini tushunish.

---

## 🧮 1️⃣ ARIFMETIK OPERATORLAR

**Arifmetik operatorlar** sonlar ustida hisob-kitob amallarini bajaradi:

| Operator | Ma’nosi | Misol |
|:--|:--|:--|
| `+` | Qo‘shish | `a + b` |
| `-` | Ayirish | `a - b` |
| `*` | Ko‘paytirish | `a * b` |
| `/` | Bo‘lish (float) | `a / b` |
| `//` | Butun bo‘lish (qoldiqsiz) | `a // b` |
| `%` | Qoldiq olish | `a % b` |
| `**` | Darajaga ko‘tarish | `a ** b` |

```python
a = 15
b = 4

print(f"a + b = {a + b}")   # Qo‘shish
print(f"a - b = {a - b}")   # Ayirish
print(f"a * b = {a * b}")   # Ko‘paytirish
print(f"a / b = {a / b:.2f}") # Bo‘lish
print(f"a // b = {a // b}") # Butun bo‘lish
print(f"a % b = {a % b}")   # Qoldiq
print(f"a ** b = {a ** b}") # Daraja
