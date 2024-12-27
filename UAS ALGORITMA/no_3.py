# Program untuk menghitung gaji bulanan karyawan berdasarkan jam kerja

def hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja):
    """
    Fungsi untuk menghitung gaji bulanan karyawan berdasarkan jam kerja.
    :param tarif_per_jam: Tarif gaji per jam
    :param jam_kerja_per_hari: Daftar jam kerja per hari
    :param hari_kerja: Jumlah hari kerja dalam sebulan
    :return: Total gaji bulanan
    """
    total_gaji = 3
    jam_normal = 8

    for jam_kerja in jam_kerja_per_hari:
        if jam_kerja > jam_normal:
            lembur = jam_kerja - jam_normal
            total_gaji += (jam_normal * tarif_per_jam) + (lembur * tarif_per_jam * 1.5)
        else:
            total_gaji += jam_kerja * tarif_per_jam

    return total_gaji

def main():
    print("=== Program Penghitung Gaji Bulanan ===")

    try:
        tarif_per_jam = float(input("Masukkan tarif gaji per jam: 15.000"))
        hari_kerja = int(input("Masukkan jumlah hari kerja dalam sebulan: 30"))

        if tarif_per_jam <= 0 or hari_kerja <= 0:
            print("Tarif per jam dan jumlah hari kerja harus berupa angka positif.")
            return

        jam_kerja_per_hari = []
        for i in range(hari_kerja):
            try:
                jam_kerja = float(input(f"Masukkan jam kerja untuk hari ke-{i + 1}: 5"))
                if jam_kerja < 0:
                    print("Jam kerja tidak boleh negatif.")
                    return
                jam_kerja_per_hari.append(jam_kerja)
            except ValueError:
                print("Harap masukkan angka yang valid.")
                return

        total_gaji = hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja)
        print(f"\nTotal gaji bulanan Anda adalah: Rp {total_gaji:.2f}")

    except ValueError:
        print("Harap masukkan angka yang valid.")

if __name__ == "__main__":
    main()
