import math


def hitung_persegi():
    sisi = float(input("Masukkan panjang sisi persegi: "))
    luas = sisi ** 2
    keliling = 4 * sisi

    # Output dengan rumus dan penjelasan
    print("\n=== Hasil Perhitungan Persegi ===")
    print(f"Rumus Luas      = sisi × sisi")
    print(f"               = {sisi} × {sisi}")
    print(f"               = {luas}")
    print(f"Luas Persegi    = {luas}")

    print(f"\nRumus Keliling  = 4 × sisi")
    print(f"               = 4 × {sisi}")
    print(f"               = {keliling}")
    print(f"Keliling Persegi = {keliling}")


def hitung_persegi_panjang():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)

    # Output dengan penjelasan rumus
    print("\n=== Hasil Perhitungan Persegi Panjang ===")

    print(f"Rumus Luas      = panjang × lebar")
    print(f"               = {panjang} × {lebar}")
    print(f"               = {luas}")
    print(f"Luas Persegi Panjang = {luas}")

    print(f"\nRumus Keliling  = 2 × (panjang + lebar)")
    print(f"               = 2 × ({panjang} + {lebar})")
    print(f"               = 2 × {panjang + lebar}")
    print(f"               = {keliling}")
    print(f"Keliling Persegi Panjang = {keliling}")


def hitung_segitiga():
    print("Asumsikan segitiga sama kaki.")
    alas = float(input("Masukkan panjang alas: "))
    tinggi = float(input("Masukkan tinggi: "))

    # Hitung sisi miring menggunakan Pythagoras
    setengah_alas = alas / 2
    sisi_miring = math.sqrt(setengah_alas**2 + tinggi**2)

    # Hitung luas dan keliling
    luas = 0.5 * alas * tinggi
    keliling = alas + 2 * sisi_miring

    # Tampilkan hasil lengkap dengan rumus
    print("\n=== Hasil Perhitungan Segitiga Sama Kaki ===")

    print(f"Rumus Luas      = 1/2 × alas × tinggi")
    print(f"               = 1/2 × {alas} × {tinggi}")
    print(f"               = {luas}")
    print(f"Luas Segitiga   = {luas}")

    print(f"\nHitung sisi miring:")
    print(f"sisi miring     = √((alas/2)² + tinggi²)")
    print(f"               = √(({alas}/2)² + {tinggi}²)")
    print(f"               = √({setengah_alas**2} + {tinggi**2})")
    print(f"               = √({sisi_miring**2})")
    print(f"               = {sisi_miring:.2f}")

    print(f"\nRumus Keliling  = alas + 2 × sisi miring")
    print(f"               = {alas} + 2 × {sisi_miring:.2f}")
    print(f"               = {keliling:.2f}")
    print(f"Keliling Segitiga = {keliling:.2f}")


def hitung_lingkaran():
    jari = float(input("Masukkan jari-jari lingkaran: "))
    phi = math.pi  # atau bisa pakai 3.1416
    luas = math.pi * jari ** 2
    keliling = 2 * math.pi * jari

    # Tampilkan hasil lengkap dengan penjelasan
    print("\n=== Hasil Perhitungan Lingkaran ===")

    print(f"Rumus Luas      = π × r²")
    print(f"               = {phi:.4f} × {jari}²")
    print(f"               = {phi:.4f} × {jari**2}")
    print(f"               = {luas:.2f}")
    print(f"Luas Lingkaran  = {luas:.2f}")

    print(f"\nRumus Keliling  = 2 × π × r")
    print(f"               = 2 × {phi:.4f} × {jari}")
    print(f"               = {keliling:.2f}")
    print(f"Keliling Lingkaran = {keliling:.2f}")


def hitung_trapesium():
    print("\n=== TRAPESIUM SAMA KAKI ===")
    a = float(input("Masukkan panjang sisi sejajar a: "))
    b = float(input("Masukkan panjang sisi sejajar b: "))
    t = float(input("Masukkan tinggi trapesium (t): "))

    # Hitung panjang sisi miring
    selisih = abs(a - b) / 2
    sisi_miring = math.sqrt(selisih**2 + t**2)

    # Hitung luas dan keliling
    luas = 0.5 * (a + b) * t
    keliling = a + b + 2 * sisi_miring

    # Tampilkan hasil dengan penjelasan rumus
    print("\n=== Hasil Perhitungan Trapesium Sama Kaki ===")

    print(f"Rumus Luas      = ½ × (a + b) × t")
    print(f"               = ½ × ({a} + {b}) × {t}")
    print(f"               = ½ × {a + b} × {t}")
    print(f"               = {(a + b) * t / 2}")
    print(f"Luas Trapesium  = {luas}")

    print(f"\nHitung sisi miring:")
    print(f"sisi miring     = √[((a - b)/2)² + t²]")
    print(f"               = √[{selisih}² + {t}²]")
    print(f"               = √[{selisih**2} + {t**2}]")
    print(f"               = √({sisi_miring**2})")
    print(f"               = {sisi_miring:.2f}")

    print(f"\nRumus Keliling  = a + b + 2 × sisi miring")
    print(f"               = {a} + {b} + 2 × {sisi_miring:.2f}")
    print(f"               = {keliling:.2f}")
    print(f"Keliling Trapesium = {keliling:.2f}")


def main():
    while True:
        print("\n=== Aplikasi Penghitung Bangun Datar ===")
        print("1. Persegi")
        print("2. Persegi Panjang")
        print("3. Segitiga")
        print("4. Lingkaran")
        print("5. Trapesium")
        print("0. Keluar")
        pilihan = input("Pilih bangun datar (0-5): ")

        if pilihan == '1':
            hitung_persegi()
        elif pilihan == '2':
            hitung_persegi_panjang()
        elif pilihan == '3':
            hitung_segitiga()
        elif pilihan == '4':
            hitung_lingkaran()
        elif pilihan == '5':
            hitung_trapesium()
        elif pilihan == '0':
            print("Terima kasih telah menggunakan aplikasi.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()
