qiymetler = [45, 100, 300, 15, 80]
cem = 0
for i in qiymetler:
    cem += i  # cem = cem + i
print(cem)
print(len(qiymetler))
orta_qiymet = cem / len(qiymetler)
print(f"orta_qiymet = {orta_qiymet}")