def hollowTriangle(x):
    for i in range(x):                      #untuk nilai i dalam range x, (x sebagai jumlah baris)
        if i<1:                             # i masih bernilai 0, untuk print baris pertama

            #'underscore' dikalikan dengan jumlah x, jika masih baris 1(x=1), maka tidak ada underscore yang muncul di awal & akhir
            print(('_' * (x-1))+'#', end='_'*(x-1))   
            print()

        #jika kondisi tak penuhi syarat if, kondisi baru berjalan. Khusus utk baris tengah (selain baris awal dan akhir)
        elif i < (x-1):                  
            for j in range(x-(i+1)):     #range untuk baris kedua.
                print('_', end='')       #print underscore pertama di setiap barisnya.
            print('#',end='')           #print pagar pertama di setiap baris. End kosong agar tidak ada spasi

            # untuk print underscore stelah pagar pertama. Jika melebihi range, ganti me-print pagar ke line 19.
            for j in range((i*2)-1):   #range adalah panjang yang mengikuti jumlah baris. (length dri jumlah underscore + pagar)
                print('_', end='')     #print 'underscore' yang berada diantara pagar, end kosong. 

            print('#',end='_'*(x-(i+1))) #print pagar yang diakhiri 'underscore' yg panjangnya mengecil jika i (jumlah baris) membesar
            print()

        #untuk me-print baris terakhir. Jumlah pagar akan sesuai dengan panjang diatasnya(jumlah underscore + pagar)
        else:
            print('#' *((x*2)-1))    

# hollowTriangle(1)
# hollowTriangle(4)
hollowTriangle(6)



