import math  # Digunakan untuk akar real
# Untuk akar kompleks, kita hitung manual bagian real dan imajiner

print("=== Program Penghitung Akar Persamaan Kuadrat ===")
print("Persamaan: ax^2 + bx + c = 0")

# Input nilai a, b, c
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

# Hitung diskriminan
D = b**2 - 4*a*c
print(f"Diskriminan (D) = {D}")

# Kasus 1: D > 0 (akar real berbeda)
if D > 0:
    akar_D = math.sqrt(D)
    x1 = (-b + akar_D) / (2*a)
    x2 = (-b - akar_D) / (2*a)
    print("Akar-akar real dan berbeda:")
    print(f"x1 = {x1:.2f}")
    print(f"x2 = {x2:.2f}")

# Kasus 2: D = 0 (akar real kembar)
elif D == 0:
    x = -b / (2*a)
    print("Akar-akar real kembar:")
    print(f"x1 = x2 = {x:.2f}")

# Kasus 3: D < 0 (akar kompleks)
else:
    real_part = -b / (2*a)
    imag_part = math.sqrt(-D) / (2*a)
    x1 = f"{real_part:.2f} + {imag_part:.2f}i"
    x2 = f"{real_part:.2f} - {imag_part:.2f}i"
    print("Akar-akar kompleks:")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
