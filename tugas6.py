var_nilai = 0
var_i = 1

while (var_nilai < 10): 
    print("perulangan pertama ke ",var_nilai) 
    while (var_i < 3):
        print("perulangan ke ",var_nilai,", ",var_i)
        var_i += 1
    var_i = 1
    var_nilai +=1
print("var_nilai = ", int(var_nilai)+1, "= 10. Bernilai False")