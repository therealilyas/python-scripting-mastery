"""
PROJECT 03: LOGIN TIZIMI 🔐
Yuqori daraja (Advanced)
"""

print("="*60)
print(" "*20 + "LOGIN TIZIMI")
print("="*60)

# Foydalanuvchilar bazasi (list ichida dictionary)
users = [
    {"username": "ilyas", "password": "12345"},
    {"username": "admin", "password": "admin123"},
    {"username": "guest", "password": "guest"}
]

# Foydalanuvchi kiritadi
kiritilgan_username = input("Foydalanuvchi nomi: ").strip().lower()
kiritilgan_password = input("Parol: ").strip()

# Tekshirish (membership + mantiqiy)
found = False
for user in users:
    if user["username"] == kiritilgan_username and user["password"] == kiritilgan_password:
        found = True
        break

if found:
    print("\n✅ Tizimga muvaffaqiyatli kirdingiz!")
else:
    print("\n❌ Login yoki parol noto‘g‘ri!")

# Qo‘shimcha tekshiruvlar (identity + membership)
print("\n🔍 Tekshiruvlar:")
print(f"kiritilgan_username in foydalanuvchilar ro‘yxati? → {kiritilgan_username in [u['username'] for u in users]}")
print(f"users[0] is users[1] → {users[0] is users[1]}  # Har xil obyektlar")
print(f"users[0] == users[1] → {users[0] == users[1]}  # Qiymat jihatdan teng emas")

print("="*60)
