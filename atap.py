import math


def hitung_miring(horizontal, sudut_derajat):
    sudut_rad = math.radians(sudut_derajat)
    return horizontal / math.cos(sudut_rad)


def hitung_luas_segitiga():
    print("\n=== PERHITUNGAN ATAP SEGITIGA ===")
    alas = float(input("Masukkan alas segitiga (horizontal) (m): "))
    tinggi_hor = float(input("Masukkan tinggi segitiga (horizontal) (m): "))
    sudut = float(input("Masukkan sudut kemiringan atap (derajat): "))

    tinggi_miring = hitung_miring(tinggi_hor, sudut)
    luas = 0.5 * alas * tinggi_miring

    print(f"\n>> Konversi tinggi horizontal menjadi miring:")
    print(f"tinggi_miring = {tinggi_hor} / cos({sudut}°) = {tinggi_miring:.2f} m")

    print(f"\n>> Rumus luas segitiga:")
    print(f"Luas = 0.5 × alas × tinggi")
    print(f"Luas = 0.5 × {alas} × {tinggi_miring:.2f} = {luas:.2f} m²")
    return luas


def hitung_luas_trapesium():
    print("\n=== PERHITUNGAN ATAP TRAPESIUM ===")
    atas = float(input("Masukkan panjang sisi atas (horizontal) (m): "))
    bawah = float(input("Masukkan panjang sisi bawah (horizontal) (m): "))
    tinggi_hor = float(input("Masukkan tinggi trapesium (horizontal) (m): "))
    sudut = float(input("Masukkan sudut kemiringan atap (derajat): "))

    tinggi_miring = hitung_miring(tinggi_hor, sudut)
    luas = 0.5 * (atas + bawah) * tinggi_miring

    print(f"\n>> Konversi tinggi horizontal menjadi miring:")
    print(f"tinggi_miring = {tinggi_hor} / cos({sudut}°) = {tinggi_miring:.2f} m")

    print(f"\n>> Rumus luas trapesium:")
    print(f"Luas = 0.5 × (atas + bawah) × tinggi")
    print(f"Luas = 0.5 × ({atas} + {bawah}) × {tinggi_miring:.2f} = {luas:.2f} m²")
    return luas


def hitung_luas_persegi_panjang():
    print("\n=== PERHITUNGAN ATAP PERSEGI PANJANG MIRING ===")
    panjang = float(input("Masukkan panjang atap (horizontal) (m): "))
    lebar_hor = float(input("Masukkan lebar atap (horizontal) (m): "))
    sudut = float(input("Masukkan sudut kemiringan atap (derajat): "))

    lebar_miring = hitung_miring(lebar_hor, sudut)
    luas = panjang * lebar_miring

    print(f"\n>> Konversi lebar horizontal menjadi miring:")
    print(f"lebar_miring = {lebar_hor} / cos({sudut}°) = {lebar_miring:.2f} m")

    print(f"\n>> Rumus luas persegi panjang:")
    print(f"Luas = panjang × lebar miring")
    print(f"Luas = {panjang} × {lebar_miring:.2f} = {luas:.2f} m²")
    return luas


def hitung_total_luas_atap():
    print("\n=== PERHITUNGAN TOTAL LUAS ATAP ===")
    jumlah = int(input("Masukkan jumlah sisi atap yang ingin dijumlahkan: "))
    total = 0
    daftar_luas = []

    for i in range(1, jumlah + 1):
        nilai = float(input(f"Masukkan luas atap ke-{i} (m²): "))
        daftar_luas.append(nilai)
        total += nilai

    # Buat string penjumlahan: 12.5 + 15.0 + 9.2 ...
    rumus = " + ".join(f"{luas:.2f}" for luas in daftar_luas)

    print(f"\n>> Rumus total luas:")
    print(f"Total luas = {rumus} = {total:.2f} m²")
    return total


def menu():
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Hitung luas atap segitiga")
        print("2. Hitung luas atap trapesium")
        print("3. Hitung luas atap persegi panjang miring")
        print("4. Hitung total luas atap dari beberapa sisi")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            hitung_luas_segitiga()
        elif pilihan == "2":
            hitung_luas_trapesium()
        elif pilihan == "3":
            hitung_luas_persegi_panjang()
        elif pilihan == "4":
            hitung_total_luas_atap()
        elif pilihan == "5":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1 - 5.")


if __name__ == "__main__":
    menu()
