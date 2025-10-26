# 01-oddiy-misollar.py

"""
🧠 MAVZU: OPERATORLAR - ODDIY MISOLLAR
Ushbu dasturda Python'dagi barcha operator turlari uchun
asosiy va sodda misollar keltirilgan.
"""

print("="*70)
print(" "*25 + "OPERATORLAR")
print("="*70 + "\n")

# ===============================================================
# 1. ARIFMETIK OPERATORLAR
# ===============================================================
print("1️⃣  ARIFMETIK OPERATORLAR\n")

a = 15
b = 4

print(f"a = {a}, b = {b}\n")
print(f"a + b = {a + b}     # Qo‘shish")
print(f"a - b = {a - b}     # Ayirish")
print(f"a * b = {a * b}     # Ko‘paytirish")
print(f"a / b = {a / b:.2f} # Bo‘lish (natija float)")
print(f"a // b = {a // b}   # Butun bo‘lish (qoldiqsiz)")
print(f"a % b = {a % b}     # Bo‘lishdan qoldiq")
print(f"a ** b = {a ** b}   # Darajaga ko‘tarish")

print("\n" + "="*70 + "\n")

# ===============================================================
# 2. TAQQOSLASH OPERATORLARI
# ===============================================================
print("2️⃣  TAQQOSLASH OPERATORLARI\n")

x = 10
y = 20

print(f"x = {x}, y = {y}\n")
print(f"x == y → {x == y}  # Tengmi?")
print(f"x != y → {x != y}  # Teng emasmi?")
print(f"x > y  → {x > y}   # Kattami?")
print(f"x < y  → {x < y}   # Kichikmi?")
print(f"x >= y → {x >= y}  # Katta yoki tengmi?")
print(f"x <= y → {x <= y}  # Kichik yoki tengmi?")

print("\n" + "="*70 + "\n")

# ===============================================================
# 3. MANTIQIY OPERATORLAR
# ===============================================================
print("3️⃣  MANTIQIY OPERATORLAR\n")

p = True
q = False

print(f"p = {p}, q = {q}\n")
print(f"p and q → {p and q}  # Ikkalasi ham True bo‘lsa True")
print(f"p or q  → {p or q}   # Kamida bittasi True bo‘lsa True")
print(f"not p   → {not p}     # True → False ga o‘zgaradi")
print(f"not q   → {not q}     # False → True ga o‘zgaradi")

print("\n" + "="*70 + "\n")

# ===============================================================
# 4. ASSIGNMENT (BIRIKTIRISH) OPERATORLAR
# ===============================================================
print("4️⃣  ASSIGNMENT OPERATORLAR\n")

num = 10
print(f"Boshlang‘ich qiymat: num = {num}\n")

num += 5
print(f"num += 5  → {num}")

num -= 3
print(f"num -= 3  → {num}")

num *= 2
print(f"num *= 2  → {num}")

num /= 4
print(f"num /= 4  → {num}")

num **= 3
print(f"num **= 3 → {num}")

num %= 7
print(f"num %= 7  → {num}")

print("\n" + "="*70 + "\n")

# ===============================================================
# 5. MEMBERSHIP (A'ZOLIK) OPERATORLAR
# ===============================================================
print("5️⃣  MEMBERSHIP OPERATORLAR\n")

royxat = [1, 2, 3, 4, 5]
matn = "Python"

print(f"Royxat: {royxat}")
print(f"Matn: '{matn}'\n")

print(f"3 in royxat → {3 in royxat}      # 3 royxatda bormi?")
print(f"6 in royxat → {6 in royxat}      # 6 royxatda bormi?")
print(f'\"Py\" in matn → {"Py" in matn}   # "Py" matnda bormi?')
print(f'\"java\" in matn → {"java" in matn} # "java" matnda bormi?')

print("\n" + "="*70 + "\n")

# ===============================================================
# 6. IDENTITY (SHAKHSIYLIK) OPERATORLAR
# ===============================================================
print("6️⃣  IDENTITY OPERATORLAR\n")

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x  # z x bilan bir xil obyektni ko‘rsatadi

print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}\n")

print(f"x is y → {x is y}   # Ular bir xil obyektmi?")
print(f"x == y → {x == y}   # Ular qiymat jihatdan tengmi?")
print(f"x is z → {x is z}   # z va x bir xil obyektmi?")
print(f"x is not y → {x is not y} # Ular har xil obyektmi?")

print("\n" + "="*70 + "\n")

# ===============================================================
# 7. BITWISE (BITLI) OPERATORLAR
# ===============================================================
print("7️⃣  BITWISE OPERATORLAR\n")

a = 10  # (1010)
b = 4   # (0100)

print(f"a = {a} (binary: {bin(a)})")
print(f"b = {b} (binary: {bin(b)})\n")

print(f"a & b = {a & b}   # Bitwise AND → {bin(a & b)}")
print(f"a | b = {a | b}   # Bitwise OR  → {bin(a | b)}")
print(f"a ^ b = {a ^ b}   # Bitwise XOR → {bin(a ^ b)}")
print(f"~a = {~a}         # Bitwise NOT → {bin(~a)}")
print(f"a << 2 = {a << 2} # Chapga siljitish (×4)")
print(f"a >> 2 = {a >> 2} # O‘ngga siljitish (÷4)")

print("\n" + "="*70)
print("✅  BARCHA OPERATORLAR MISOLLARI TUGADI")
print("="*70)
