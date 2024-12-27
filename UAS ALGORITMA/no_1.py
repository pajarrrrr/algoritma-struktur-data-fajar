# Program untuk meminta biodata pengguna dan menampilkannya

def main():
    print("=== Program Biodata ===")

    # Meminta input dari pengguna
    nama = input("Masukkan nama Anda: Fajar ramdan faidillah")
    usia = input("Masukkan usia Anda: 18")
    alamat = input("Masukkan alamat Anda: Pangkalpinang")
    hobi = input("Masukkan hobi Anda: Badminton")

    # Menampilkan biodata dalam format rapi
    print("\n=== Biodata Anda ===")
    print(f"Nama    : {nama} Fajar ramdan faidillah")
    print(f"Usia    : {usia} 18")
    print(f"Alamat  : {alamat} Pangkalpinang")
    print(f"Hobi    : {hobi} Badmintoon")

if __name__ == "__main__":
    main()
