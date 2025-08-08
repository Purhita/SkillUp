import math

print("=== PROGRAM PENGHITUNG AKAR PERSAMAAN KUADRAT ===")
print("Persamaan: ax² + bx + c = 0")
print()

# Meminta input dari pengguna
print("Masukkan nilai koefisien:")
a = float(input("Nilai a: "))
b = float(input("Nilai b: "))
c = float(input("Nilai c: "))

print(f"\nPersamaan yang dimasukkan: {a}x² + {b}x + {c} = 0")

# Cek apakah ini persamaan kuadrat (a tidak boleh 0)
if a == 0:
    print("KESALAHAN: Nilai a tidak boleh 0 (bukan persamaan kuadrat)")
else:
    # Hitung diskriminan (D = b² - 4ac)
    diskriminan = b**2 - 4*a*c
    print(f"Diskriminan (D = b² - 4ac) = {b}² - 4×{a}×{c} = {diskriminan}")
    
    # Tentukan jenis akar berdasarkan nilai diskriminan
    if diskriminan > 0:
        # Dua akar real berbeda
        print("Diskriminan > 0: Persamaan memiliki dua akar real berbeda")
        akar1 = (-b + math.sqrt(diskriminan)) / (2*a)
        akar2 = (-b - math.sqrt(diskriminan)) / (2*a)
        print(f"Akar 1 (x₁) = {akar1:.4f}")
        print(f"Akar 2 (x₂) = {akar2:.4f}")
        
    elif diskriminan == 0:
        # Dua akar real sama (akar kembar)
        print("Diskriminan = 0: Persamaan memiliki dua akar real sama (akar kembar)")
        akar = -b / (2*a)
        print(f"Akar kembar (x₁ = x₂) = {akar:.4f}")
        
    else:
        # Akar kompleks (tidak real)
        print("Diskriminan < 0: Persamaan memiliki akar kompleks (tidak real)")
        bagian_real = -b / (2*a)
        bagian_imajiner = math.sqrt(abs(diskriminan)) / (2*a)
        print(f"Akar 1 (x₁) = {bagian_real:.4f} + {bagian_imajiner:.4f}i")
        print(f"Akar 2 (x₂) = {bagian_real:.4f} - {bagian_imajiner:.4f}i")

print("\n=== PROGRAM SELESAI ===")
