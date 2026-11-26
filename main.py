import os
import inquirer
from daftar_minuman import tampilkan_daftar_minuman
from create_data import tambah_data
from update_data import update_data
from read_data import baca_data
from delete_data import hapus_data

akun = {
    "akun": []
}



def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def menu_utama():
    pertanyaan = [
        inquirer.List(
            "menu",
            message="Pilih Menu",
            choices=["Login", "Registrasi", "Exit"],
        )
    ]
    jawaban = inquirer.prompt(pertanyaan)
    return jawaban["menu"]


def menu_admin():
    pertanyaan = [
        inquirer.List(
            "menu",
            message="Pilih Menu",
            choices=[
                "Tambah Daftar Minuman Baru",
                "Tampilkan Daftar Minuman",
                "Update Barang",
                "Hapus Daftar Minuman",
                "Exit",
            ],
        )
    ]
    jawaban = inquirer.prompt(pertanyaan)
    return jawaban["menu"]


def menu_pengguna():
    pertanyaan = [
        inquirer.List(
            "menu",
            message="Pilih Menu",
            choices=["Tampilkan Daftar Minuman", "Exit"],
        )
    ]
    jawaban = inquirer.prompt(pertanyaan)
    return jawaban["menu"]


def login():
    username = input("Masukkan Username Anda: ").strip()
    password = input("Masukkan Password Anda: ").strip()
    for data in akun["akun"]:
        if data[0] == username and data[1] == password:
            return data[2]
    return None


def registrasi():
    username = input("Masukkan Username Anda: ").strip()
    password = input("Masukkan Password Anda: ").strip()
    role = input("Masukkan Role Anda (admin/pengguna): ").lower().strip()

    if username == "" or password == "" or role == "":
        print("Username, Password, atau Role Tidak Boleh Kosong!")
        input("Tekan Enter Untuk Kembali...")
        return

    if role not in ("admin", "pengguna"):
        print("Role Hanya Boleh 'admin' atau 'pengguna'!")
        input("Tekan Enter Untuk Kembali...")
        return

    for data in akun["akun"]:
        if data[0] == username:
            print("Username Tersebut Telah Digunakan!")
            input("Tekan Enter Untuk Kembali...")
            return

    akun["akun"].append([username, password, role])
    print("Registrasi Berhasil!")
    input("Tekan Enter Untuk Kembali...")


def jalankan_admin():
    print("======LOGIN BERHASIL!=====")
    print("Selamat Datang, Admin")
    input("Tekan Enter Untuk Melanjutkan...")
    while True:
        bersihkan_layar()
        tampilkan_daftar_minuman()
        pilihan = menu_admin()
        if pilihan == "Tambah Daftar Minuman Baru":
            produk = input("Tambahkan Daftar Minuman: ").strip()
            harga = input("Tambahkan Harga: ")
            stok = input("Tambahkan Stok: ")
            tambah_data(produk, harga, stok)
        elif pilihan == "Tampilkan Daftar Minuman":
            baca_data()
        elif pilihan == "Update Barang":
            update_data()
        elif pilihan == "Hapus Daftar Minuman":
            hapus = input("Data Mana yang Ingin Anda Hapus: ")
            hapus_data(hapus)
        elif pilihan == "Exit":
            print("Terima kasih!")
            input("Tekan Enter Untuk Kembali...")
            break
        else:
            print("Pilihan Tidak Valid!")
            input("Tekan Enter Untuk Kembali...")


def jalankan_pengguna():
    while True:
        bersihkan_layar()
        pilihan = menu_pengguna()
        if pilihan == "Tampilkan Daftar Minuman":
            baca_data()
        elif pilihan == "Exit":
            print("Terima kasih!")
            break
        else:
            print("Pilihan Tidak Valid!")
            input("Tekan Enter Untuk Kembali...")


def main():
    while True:
        bersihkan_layar()
        pilihan = menu_utama()
        if pilihan == "Login":
            role = login()
            if role is None:
                print("Username atau Password Anda Salah!")
                input("Tekan Enter Untuk Kembali...")
            elif role == "admin":
                jalankan_admin()
            elif role == "pengguna":
                jalankan_pengguna()
            else:
                print("Role Tidak Tersedia!")
                input("Tekan Enter Untuk Kembali...")
        elif pilihan == "Registrasi":
            registrasi()
        elif pilihan == "Exit":
            print("Terima Kasih Telah Menggunakan Aplikasi Manajemen Stok Minuman!")
            break
        else:
            print("Pilihan Tidak Tersedia!")
            input("Tekan Enter untuk Kembali...")


if __name__ == "__main__":
    main()
