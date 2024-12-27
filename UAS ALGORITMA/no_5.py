# Program untuk Menentukan Kategori Usia

def tentukan_kategori_usia(usia):
    """
    Fungsi untuk menentukan kategori usia berdasarkan aturan yang diberikan.
    :param usia: Usia dalam tahun
    :return: Kategori usia
    """
    if 0 <= usia <= 5:
        return "Balita"
    elif 6 <= usia <= 12:
        return "Anak-anak"
    elif 13 <= usia <= 17:
        return "Remaja"
    elif 18 <= usia <= 59:
        return "Dewasa"
    elif usia >= 60:
        return "Lansia"
    else:
        return "Usia tidak valid"

def main():
    print("=== Program Kategori Usia ===")
    try:
        usia = int(input("Masukkan usia Anda: 18"))
        if usia < 0:
            print("Usia tidak valid. Harap masukkan angka positif.")
            return

        kategori = tentukan_kategori_usia(usia)
        print(f"Kategori usia Anda: {kategori}")

    except ValueError:
        print("Input tidak valid. Harap masukkan angka bulat.")

if __name__ == "__main__":
    main()
