print("Selamat datang di kalkulator Penghitung volume Balok Dan Kubus")
print("Daftar Pilihan")
print("1. Menghitung Volume Balok")
print("2. Menghitung Volume Kubus")
option=int(input("Silihakan Pilih :"))
if option == 1:
    p=int(input("Masukkan Panjang Balok :"))
    l=int(input("Masukkan Lebar Balok :"))
    t=int(input("Masukkan Tinggi Balok :"))
    v=p*l*t
    print("Ukuran Balok Anda Adalah :",v,"cm")
elif option==2:
    s=int(input("Masukkan Sisi Kubus :"))
    v=s**3
    print("Ukuran Balok Anda Adalah :",v,"cm")
    
else:
    print("Key Word Anda Salah! Silahkan Coba Run Lagi")