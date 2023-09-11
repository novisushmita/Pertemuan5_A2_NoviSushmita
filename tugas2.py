awal = int(input("masukkan saldo awal\t: "))
sisa = awal
while (True):
    pengeluaran = int(input("masukkan pengeluaran hari ini (-1 untuk keluar): "))
    if pengeluaran == -1:
        print("sisa saldo = ",sisa)
        break
    sisa = sisa - pengeluaran
    if sisa < 0:
        print("saldo tidak cukup")
        print("sisa saldo ", sisa + pengeluaran)
        break