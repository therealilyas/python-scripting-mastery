"""
PROJECT 01: Oddiy Kalkulyator 🧮
Boshlang‘ich daraja (Beginner)
"""

print("="*50)
print(" "*15 + "ODDIY KALKULYATOR")
print("="*50)

# Foydalanuvchidan ma'lumot olish
a = float(input("1-sonni kiriting: "))
b = float(input("2-sonni kiriting: "))

print("\nAmallar:")
print("1. Qo‘shish (+)")
print("2. Ayirish (-)")
print("3. Ko‘paytirish (*)")
print("4. Bo‘lish (/)")
print("5. Darajaga ko‘tarish (**)")

tanlov = input("\nTanlang (1-5): ")

# Arifmetik operatorlar orqali natija chiqarish
if tanlov == "1":
    print(f"Natija: {a} + {b} = {a + b}")
elif tanlov == "2":
    print(f"Natija: {a} - {b} = {a - b}")
elif tanlov == "3":
    print(f"Natija: {a} * {b} = {a * b}")
elif tanlov == "4":
    print(f"Natija: {a} / {b} = {a / b:.2f}")
elif tanlov == "5":
    print(f"Natija: {a} ** {b} = {a ** b}")
else:
    print("❌ Noto‘g‘ri tanlov kiritildi!")

print("="*50)
