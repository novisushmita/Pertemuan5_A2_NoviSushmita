jumlah_data = 0
data = 1

banyak_data = int(input("berapa banyak data yang akan dihitung? "))

while data <= banyak_data:
    nilai_data = int(input("masukkan nilai data ke-" + str(data) + " = "))
    jumlah_data += nilai_data
    data += 1

rata_rata = jumlah_data/banyak_data
print("rata-rata = ",rata_rata)