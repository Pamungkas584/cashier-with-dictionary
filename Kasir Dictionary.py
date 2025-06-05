import os
import time

data_Barang_template = {
    'nama' : 'nama',
    'harga' : 0
}

data_utama = {
    1 : {
        'nama' : 'Indomie',
        'harga' : 3000
    },
    2 : {
        'nama' : 'pensil',
        'harga' : 2000
    }

}

def welcome() : 
    ''' Ucapan Selamat datang '''
    os.system("cls")
    print(f'{"="*20:^20}')
    print(f'{"SELAMAT DATANG":^20}')
    print(f'{"="*20:^20}')

def terimakasih() : 
    ''' Ucapan Terimakasih '''
    os.system("cls")
    print(f'{"="*20:^20}')
    print(f'{"TERIMA KASIH":^20}')
    print(f'{"="*20:^20}')
    print(f"{"-"*50}")

def menu() :
    while True:
        print("Silahkan Pilih Menu yang tersedia :\n1. Tambahkan Produk \n2. Tampilkan Produk \n3. Jalankan Fungsi Kasir \n4. Exit")
        ChoiceMenu = int(input(f"(1/2/3/4)> "))
        if ChoiceMenu > 4 :
            print("\nMenu Tidak tersedia !!")
            continue
        else :
            break
    return ChoiceMenu

def Tambah_produk():
    while True:
        nomor_barang = len(data_utama)
        Data_Barang = dict.fromkeys(data_Barang_template.keys())
        Data_Barang['nama'] = input("Masukkan Nama Barang : ") # type: ignore
        Data_Barang['harga'] = int(input("Masukkan Harga Barang :"))  # type: ignore
        data_utama.update({nomor_barang + 1 : Data_Barang})
        
        tambahkan_lagi = input('Ingin menambahkan lagi?(y/n)\n> ')
        if tambahkan_lagi == "n" :
            break

def Tampilkan_produk() :
    print(f"{"No":<5} |\t {"Nama barang":<15} \t|\t{"Harga barang":>12}")
    print(f'{"-"*55}')
    for barang in data_utama :
        no_barang = barang
        nama_barang = data_utama[no_barang]['nama']
        harga_barang = data_utama[no_barang]['harga']
        print(f"{no_barang:<5} |\t {nama_barang:<15} \t|\tRp {harga_barang:>8,},-")

def kasir() :
    keranjang_belanja = {}
    total = 0
    while True :
        os.system("cls")
        jumlah_barang_dalam_keranjang = len(keranjang_belanja)
        Tampilkan_produk()
        Nomor_barang_dibeli = int(input("Masukkan Nomor Barang : "))
        Jumlah_barang_dibeli = int(input("Berapa Jumlah barang yang ingin di beli : "))
        keranjang = dict.fromkeys(data_Barang_template.keys())
        keranjang['nama'] = data_utama[Nomor_barang_dibeli]['nama']
        keranjang['harga'] = data_utama[Nomor_barang_dibeli]['harga']
        keranjang['jumlah'] = Jumlah_barang_dibeli
        keranjang['subtotal'] = Jumlah_barang_dibeli * data_utama[Nomor_barang_dibeli]['harga']
        keranjang_belanja.update({jumlah_barang_dalam_keranjang + 1 : keranjang})
        done_belanja = input("Sudah selesai dan ingin mencetak struk?(y/n)\n> ")
        if done_belanja == "y" :
            break
    
    os.system("cls")
    print("Mencetak struk...")
    time.sleep(3)
    os.system("cls")
    terimakasih()
    
    for subtotal in keranjang_belanja :
        no_barang = subtotal
        total += keranjang_belanja[no_barang]['subtotal']
    
    for detail in keranjang_belanja :
        nama_barang = keranjang_belanja[detail]['nama']
        harga_barang = keranjang_belanja[detail]['harga']
        jumlah_barang = keranjang_belanja[detail]['jumlah']
        sub = keranjang_belanja[detail]['subtotal']
        print(f"Nama Barang : {nama_barang}")
        print(f"Harga Barang : Rp {harga_barang:,},-")
        print(f"jumlah Barang : {jumlah_barang}")
        print(f"subtotal : Rp {sub:,},-\n")
    
    print(f'total : Rp {total:,},- \n')
    kembali = input("tekan apa saja untuk kembali")


while True :
    welcome()
    
    Tampilkan_menu = menu()
    if Tampilkan_menu == 1 :
        Tambah_produk()
        continue

    if Tampilkan_menu == 2 :
        Tampilkan_produk()
        kembali = input('Tekan Enter untuk kembali')
        continue
    
    if Tampilkan_menu == 3 :
        kasir()
        continue
    
    if Tampilkan_menu == 4 :
        break