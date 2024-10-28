harga_reguler = 50000
harga_vip = 100000

tipe_tiket = input("Masukkan tipe tiket (Reguler/VIP): ").strip().lower()
status_member = input("Apakah Anda memiliki kartu member? (Y/T): ").strip().upper()

if tipe_tiket == "reguler":
    harga_tiket = harga_reguler
elif tipe_tiket == "vip":
    harga_tiket = harga_vip
else:
    print("Tipe tiket tidak valid!")
    exit()  

if status_member == "Y":
    diskon = 0.20 * harga_tiket
    harga_akhir = harga_tiket - diskon
    print(f"Anda mendapatkan diskon 20%! Potongan harga: Rp{diskon:.2f}")
else:
    harga_akhir = harga_tiket

print(f"Total harga yang harus dibayar: Rp{harga_akhir:.2f}")
