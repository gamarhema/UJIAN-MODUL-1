def create_phone_number (number):
    list1 = number[:3]                #membuat list dari 3 angka pertama    #OUTPUT INDEX ke-(0,1,2)
    list2 = number[3:6]               #membuat list dari 3 angka berikutnya #OUTPUT INDEX ke-(3,4,5)
    list3 = number[6:]                #membuat list dari 4 angka terakhir #OUTPUT INDEX ke-(6,7,8,9)
    str1 = list(map(str,list1))       #mengubah element list1 menjadi string dengan fungsi map
    str2 = list(map(str, list2))      #mengubah element list2 menjadi string dengan fungsi map
    str3 = list(map(str,list3))       #mengubah element list3 menjadi string dengan fungsi map
    return '('+''.join(str1)+') '+''.join(str2)+'-'+''.join(str3)        
    #return output berupa print-out pada terminal diawali dengan tanda kurung (angka dari str1 yang telah di join tanpa separator)
    #dilanjutkan tutup kurung dan spasi agar ada jarak dengan 3 angka selanjutnya
    #melakukan join pada str2, juga tanpa separator spasi. Lalu dihubungkan dengan strip dan diakhiri str3 juga tanpa separator
print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))
print(create_phone_number([7,9,3,2,5,6,4,1,0,8]))