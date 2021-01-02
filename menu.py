import _sqlite3
database = 'database.db'
import tempat_wisata as wisata
import admin as data_admin

con = _sqlite3.connect(database)
cursor = con.cursor()

def open ():
    print('SELAMAT DATANG \n =======================')
    menu = int(input('SILAHKAN PILIH MENU YANG DIINGINKAN'
                     '1. DAFTAR WISATA'
                     '2. DAFTAR HOTEL'))

def menu():
    if menu == 1:
        print('DAFTAR WISATA')
        pilihan = int(input('1. TAMPILKAN BERDASARKAN DAERAH'
                            '2. TAMPILKAN BERDASARKAN KATEGORI'))
        if pilihan == 1:
            daerah = int(input('PILIHAN DAERAH:'
                               ''))

def menu_wisata():
    pilihan = int(input('1. TAMPILKAN DAFTAR WISATA'
                    '2. TAMPILKAN DAFTAR WISATA BERDASARKAN DAERAH'
                    '3. TAMPILKAN DAFTAR WISATA BERDASARKAN KATEGORI WISATA'))
    if pilihan == 1:
        daftar = wisata.Wisata(None)
        daftar.daftar_wisata()
    else:
        print('no')

def menu_admin ():
    daftarAdmin = data_admin.Admin(None,None)
    daftarAdmin.daftar_data_admin()
    con.commit()

menu_admin()