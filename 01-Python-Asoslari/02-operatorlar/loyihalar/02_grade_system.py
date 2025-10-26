"""
PROJECT 02: Ball Baholash Tizimi 🏫
O‘rta daraja (Medium)
"""

print("="*55)
print(" "*15 + "BALL BAHOLASH TIZIMI")
print("="*55)

ball = int(input("Talaba olgan balni kiriting (0-100): "))

# Taqqoslash va mantiqiy operatorlar yordamida baho aniqlash
if ball < 0 or ball > 100:
    print("❌ Noto‘g‘ri ball kiritildi!")
elif ball >= 90:
    baho = "A (A’lo)"
elif ball >= 80:
    baho = "B (Yaxshi)"
elif ball >= 70:
    baho = "C (Qoniqarli)"
elif ball >= 60:
    baho = "D (Yaqin)"
else:
    baho = "F (Qoniqarsiz)"

print(f"\nNatija: Sizning bahoyingiz → {baho}")

# Qo‘shimcha shart: o'tdi / yiqildi
accepted_score = ball >= 60
print(f"O‘tdingizmi? → {accepted_score}")

print("="*55)
