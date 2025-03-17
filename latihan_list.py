daftar_belanja = []

def tambah_item(item):
    daftar_belanja.append(item)
    print(f'"{item}" telah ditambahkan ke daftar belanja.')

def tampilkan_daftar():
    if daftar_belanja:
        print("\nDaftar Belanja:")
        for i, item in enumerate(daftar_belanja, 1):
            print(f"{i}. {item}")
    else:
        print("\nDaftar belanja kosong.")

def hapus_item(index):
    if 0 <= index < len(daftar_belanja):
        item = daftar_belanja.pop(index)
        print(f'"{item}" telah dihapus dari daftar belanja.')
    else:
        print("Index tidak valid!")

while True:
    print("\nMenu:")
    print("1. Tambah Item")
    print("2. Lihat Daftar Belanja")
    print("3. Hapus Item")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        item = input("Masukkan nama item: ")
        tambah_item(item)
    elif pilihan == "2":
        tampilkan_daftar()
    elif pilihan == "3":
        tampilkan_daftar()
        try:
            index = int(input("Masukkan nomor item yang akan dihapus: ")) - 1
            hapus_item(index)
        except ValueError:
            print("Harap masukkan angka yang valid!")
    elif pilihan == "4":
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")