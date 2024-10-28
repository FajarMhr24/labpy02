nama = input("Masukkan nama:")
uts = input("Masukkan nilai UTS:")
uas = input("Masukkan nilai UAS:")
tugas = input("Masukkan nilai Tugas:")

akhir = (int(tugas) * .2) + (int(uts) * .4) + (int(uas) * .4)
keterangan = ("TIDAK LULUS", "LULUS")[akhir > 60.0]

if akhir > 80:
    huruf = "A"
elif akhir > 70:
    huruf = "B"
elif akhir > 50:
    huruf = "C"
elif akhir > 40:
    huruf = "D"
else:
    huruf = "E"

print("\nnama       :",nama)
print("niilai uts   :",uts)
print("nilai uas    :",uas)
print("nilai tugas  :",tugas)
print("nilai tugas  :",akhir)
print("nilai tugas  :",huruf)
print("nilai tugas  :",keterangan)
