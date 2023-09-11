var_nilai = 0
var_i = 1

for var_nilai in range (0,10):
    print("perulangan pertama ke ",var_nilai) 
    for var_i in range (1,3):
        print("perulangan ke ",var_nilai,", ",var_i)
    var_i = 1
print("var_nilai = ", int(var_nilai)+1, "= 10. Bernilai False")