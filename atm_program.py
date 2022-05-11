import random
import datetime
from customer import Customer

atm = Customer(id)

while True:

    id  = int(input("Masukkan pin : "))
    trial = 0

    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input("Pin Anda salah. Silakan Masukkan Lagi : "))
        trial += 1

        if trial == 3 :
            print("Anda 3 kali salah memasukkan pin. Silahkan ambil kartu dan coba lagi")
            exit()

    while True:
        print("Selamat Datang")
        print("1 - Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin \t 5 - Keluar ")
        selectMenu = int(input("Silakan Masukkan Menu : "))

        if selectMenu == 1:
            print("\nJumlah Saldo Anda Saat Ini Adalah : Rp. " + str(atm.checkBalance()) + "\n")
            print("------------------------------------------------------------\n\n")

        elif selectMenu == 2:
            nominal = float(input("Masukkan Nominal Debet : "))
            verify_withdraw = input ("Konfirmasi : Anda Akan Melakukan Debet dengan Nominal Rp "
                                    + str(nominal) + " (input Y/N) : ")
            if verify_withdraw == "Y":
                print("\nSaldo Awal Anda Adalah : " + str(atm.checkBalance()) + "\n")
            else:
                print("Transaksi dibatalkan\n\n")
                print("------------------------------------------------------------\n\n")
                break

            if nominal < atm.checkBalance():
                atm.withDrawBalance(nominal)
                print("Transaksi Debet Berhasil!")
                print("Sisa Saldo Sekarang : Rp. " + str(atm.checkBalance()) + " ")

            else:
                print("Maaf Saldo Anda Tidak Cukup untuk Melakukan Debet!")
                print("Silakan lakukan Penambahan Nominal Saldo")

            print("------------------------------------------------------------\n\n")

        elif selectMenu == 3:
            nominal = float(input("Masukkan Nominal Saldo : "))
            verify_deposit = input("Konfirmasi : Anda Akan Melakukan Penyimpanan dengan Nominal Rp "
                                    + str(nominal) + " (input Y/N) : ")
            if verify_deposit == "Y":
                atm.depositBalance(nominal)
                print("Saldo Anda Sekarang : Rp. " + str(atm.checkBalance()) + "\n")
            else:
                print("Transaksi dibatalkan\n\n")
                print("------------------------------------------------------------\n\n")
                break
            print("------------------------------------------------------------\n\n")

        elif selectMenu == 4:
            verify_pin = int(input("masukkan pin anda saat ini: "))
            while verify_pin != int(atm.checkPin()):
                print("pin anda salah, silakan masukkan pin: ")
            updated_pin = int(input("silakan masukkan pin baru: "))
            print("pin anda berhasil diganti!")
            verify_newpin = int(input("coba masukkan pin baru: "))
            if verify_newpin == updated_pin:
                print("pin baru anda sukses!")
            else:
                print("maaf, pin anda salah! ")

            print("------------------------------------------------------------\n\n")

        elif selectMenu == 5:
            print("Resi tercetak otomatis saat Anda keluar. Harap simpan tanda terima ini sebagai bukti transaksi Anda.")
            print("No. Rekord: ", random.randint(100000, 1000000))
            print("Tanggal: ", datetime.datetime.now())
            print("Saldo akhir: ", atm.checkBalance())
            print("Terima kasih telah menggunakan ATM Nisaa!")
            exit()
            print("------------------------------------------------------------\n\n")

        else :
            print("Mohon maaf menu yang Anda masukkan tidak tersedia")
            print("------------------------------------------------------------\n\n")