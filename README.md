# Praktikum 2 - Stuktur kondisi

Nama : Fajar maher habibillah

Kelas : TI.24.A.5

NIM : 312410549

Mata Kuliah : Bahasa Pemograman

## penggunaan stuktur kondisi menggunakan statsment `if`,`else` dan `elif` dalam python
Dalam Python, `if` dan `else` digunakan untuk pengambilan keputusan berdasarkan kondisi tertentu. Program akan mengeksekusi blok kode tertentu jika kondisi pada `if` bernilai True, dan blok lainnya (yang berada di dalam `else`) jika kondisi tersebut `False`

apa itu `elif`?

`elif` adalah singkatan dari `else if`." Ini digunakan dalam struktur kontrol `if` untuk menambahkan kondisi tambahan setelah kondisi awal yang diuji. Jika kondisi pertama (yang diawali dengan `if`) adalah `False`, maka Python akan memeriksa kondisi-kondisi yang ada di setiap pernyataan `elif` secara berurutan. Jika salah satu dari kondisi `elif` tersebut adalah True, maka blok kode yang sesuai akan dieksekusi.

## penggunaan `if` dan `else` untuk gaji karyawan

```python
if gaji > 3000000:
    print ("gaji sudah di atas UMR")
    if berkeluarga:
        print ("wajib ikutan asuransi dan menabung ntuk pensiun")
```
memeriksa apakah gaji lebih dari 3.000.000.

jika true akan mencetak "gaji sudah di atas UMR"

memeriksa apakah sudah berkeluarga?

jika true maka akan mencetak "wajib ikutan asuransi dan menabung ntuk pensiun"

```python
else:
    print ("tidak perlu ikutan asuransi")
    if punya_rumah:
        print("wajib bayar pajak rumah")

```
jika kurang dari 3.000.000. maka akan mencetak "tidak perlu ikutan asuransi"

`if punya_rumah` kalau true akan mencetak "wajib bayar pajak rumah"

![foto](https://github.com/FajarMhr24/flochart/blob/e4e0d2060ceba52701da5e58b4c039a7093b7fd4/flowchart%20gaji.jpg)
## hasil kode program
![foto](https://github.com/FajarMhr24/foto/blob/401b430c11f856b56ceaf2f1edd39c6405c377f2/Screenshot%202024-10-28%20232514.png)

## pengunaan `if`,`else` dan `elif` untuk nilai 
```python
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
```
`if`: Mengecek apakah nilai akhir lebih dari 80.

Jika True, variabel huruf diisi dengan "A", dan program tidak memeriksa kondisi lainnya (blok selesai di sini).

`elif`: (else if) Memeriksa kondisi tambahan jika kondisi pertama (nilai akhir > 80) False.

Jika akhir > 70: Huruf diisi "B".
Jika akhir > 50: Huruf diisi "C".
Jika akhir > 40: Huruf diisi "D".

`else`: Menangani semua kondisi lainnya (yaitu jika nilai akhir ≤ 40). Dalam kasus ini, huruf diisi dengan "E".
![foto](https://github.com/FajarMhr24/flochart/blob/41fa20c572fe21a484cb60834afcec1e7f755fca/flowchart%20nilai.jpg)

## hasil kode program
![foto](https://github.com/FajarMhr24/foto/blob/401b430c11f856b56ceaf2f1edd39c6405c377f2/Screenshot%202024-10-28%20231944.png)

## pengunaan kondisi `OR`

```python
if a + b == c or b + c == a or c + a == b:
```
Pada baris ini, program memeriksa beberapa kondisi menggunakan operator logika `or`.
Operator `or` digunakan untuk menggabungkan beberapa kondisi. Jika salah satu dari kondisi yang digabungkan dengan `or` adalah `True`, maka seluruh pernyataan akan dianggap `True`.

![foto](https://github.com/FajarMhr24/flochart/blob/21fb1ac4d0f3331386a6775046b290b4bdb5cd85/Screenshot%202024-10-28%20201931.png)

## hasil kode program
![foto](https://github.com/FajarMhr24/foto/blob/401b430c11f856b56ceaf2f1edd39c6405c377f2/Screenshot%202024-10-28%20232740.png))

## pengunaan `if`, `else` dan `elif` untuk tiket bioskop

```python
if tipe_tiket == "reguler":
    harga_tiket = harga_reguler
elif tipe_tiket == "vip":
    harga_tiket = harga_vip
else:
    print("Tipe tiket tidak valid!")
    exit()  
```
kondisi `if`
Memeriksa apakah variabel `tipe_tiket` sama dengan "reguler".
Jika kondisi ini benar (True), maka nilai `harga_tiket` diatur ke `harga_reguler`.

Kondisi `elif`
Jika kondisi sebelumnya tidak terpenuhi (tipe_tiket bukan "reguler"), program akan memeriksa apakah `tipe_tiket` sama dengan "vip".
Jika benar, maka `harga_tiket` diatur ke harga_vip.

Kondisi `else`
Jika kedua kondisi di atas tidak terpenuhi (artinya `tipe_tiket` tidak valid), program mencetak pesan "Tipe tiket tidak valid!" dan kemudian menghentikan eksekusi program dengan `exit()`.

 ```python
if status_member == "Y":
    diskon = 0.20 * harga_tiket
    harga_akhir = harga_tiket - diskon
    print(f"Anda mendapatkan diskon 20%! Potongan harga: Rp{diskon:.2f}")
else:
    harga_akhir = harga_tiket
```
kondisi `if`
Memeriksa apakah `status_member` sama dengan "Y" (yang mungkin berarti pengguna adalah anggota).

Jika benar, maka:

Diskon dihitung sebagai 20% dari `harga_tiket`.
`harga_akhir` dihitung dengan mengurangi `diskon` dari `harga_tiket`.
Program mencetak pesan yang menyatakan bahwa pengguna mendapatkan diskon, termasuk jumlah potongan harga dalam format yang diinginkan.

Kondisi else:

Jika pengguna bukan anggota (status_member bukan "Y"), maka `harga_akhir` diatur sama dengan `harga_tiket` tanpa diskon

![foto](https://github.com/FajarMhr24/flochart/blob/d002b35d79150e945fd4b000acd25b71cad136e7/flowchart%20tiket%20bioskop.jpg)
## hasil kode program
![foto](https://github.com/FajarMhr24/foto/blob/401b430c11f856b56ceaf2f1edd39c6405c377f2/Screenshot%202024-10-28%20233327.png)

## penggunaa `if`, `elif` dan `else 

```python
if operator == '+':
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil}")
```
Memeriksa apakah operator yang dimasukkan adalah `+`.
Jika benar, maka kode menghitung jumlah `angka1` dan `angka2`, lalu mencetak hasilnya.

```python
elif operator == '-':
    hasil = angka1 - angka2
    print(f"Hasil: {angka1} - {angka2} = {hasil}")
elif operator == '*':
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} * {angka2} = {hasil}")
```
`elif` digunakan untuk memeriksa kondisi berikutnya, yaitu jika operator adalah `-` atau `*`.
Setiap blok `elif` melakukan operasi yang sesuai (pengurangan atau perkalian) dan mencetak hasilnya.

```python
elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan!")
```
Memeriksa apakah operator adalah `/`.
Sebelum melakukan pembagian, kode memeriksa apakah `angka2` tidak sama dengan 0.
Jika `angka2` tidak sama dengan 0, maka pembagian dilakukan dan hasilnya dicetak.
Jika `angka`2 sama dengan 0, kode mencetak pesan kesalahan karena pembagian dengan nol tidak diperbolehkan.

```python
else:
    print("Operator tidak valid! Silakan masukkan +, -, *, atau /.") 
```
Jika semua kondisi sebelumnya tidak terpenuhi (misalnya, pengguna memasukkan operator yang tidak valid), maka blok `else` dieksekusi.

Program akan mencetak pesan bahwa operator tidak valid dan meminta pengguna untuk memasukkan operator yang benar.
![foto](https://github.com/FajarMhr24/flochart/blob/f74809b52afd06b08d056d17116994dd6e36d442/flowchart%20kalkulator.jpg))

## hasil kode program
![foto](https://github.com/FajarMhr24/foto/blob/401b430c11f856b56ceaf2f1edd39c6405c377f2/Screenshot%202024-10-28%20233624.png)
