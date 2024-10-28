angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operator = input("Masukkan operator (+, -, *, /): ").strip()

if operator == '+':
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil}")
elif operator == '-':
    hasil = angka1 - angka2
    print(f"Hasil: {angka1} - {angka2} = {hasil}")
elif operator == '*':
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} * {angka2} = {hasil}")
elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan!")
else:
    print("Operator tidak valid! Silakan masukkan +, -, *, atau /.") 
