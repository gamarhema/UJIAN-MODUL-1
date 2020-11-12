def sort_odd_even (num):
  _odd  = []                #membuat list kosong untuk digunakan sbagai list ganjil dan genap
  _even = []
  for i in num:             #looping untuk element dalam list input
      if i%2 == 0:          #jika modulo dari nilai i/2 sama dengan 0 (tak ada sisa pembagian), maka angka genap
          _even.append(i)
      else:                 #jika tidak(punya sisa pembagian), maka angka ganjil
          _odd.append(i)
  _odd.sort()                #mengurutkan list berisi angka ganjil dari kecil-besar --> [1, 3, 5]
  _even.sort(reverse=True)   #mengurutkan list berisi angka genap dari besar-kecil --> [8, 4, 2]
  new_list = _odd[:2]        #membuat list baru berisi 2 angka pertama dari list ganjil --> output [1, 3]
  new_even = _even[:2]       #membuat list baru berisi 2 angka genap pertama --> [8, 4]
  new_list.extend(new_even)  #menambahkan list new_even sebagai element baru dari new_list --> [1,3,8,4]
  new_list.extend(_odd[2:])  #sama seperti diatas, menambahkan angka ke 3 atau index (0,1,2) dri 'list ganjil' ke new_list -->[1,3,8,4,5]
  new_list.extend(_even[2:]) #menambahkan angka ke 3 atau index (0,1,2) dr 'list genap' ke new_list -->[1,3,8,4,5,2]
  print(new_list)


sort_odd_even([5, 3, 2, 8, 1, 4])
sort_odd_even([25, 36, 44, 0, 9, 17])
# sort_odd_even([])


# sort_odd_even([5, 3, 2, 8, 1, 4]) // would return [1, 3, 8, 4, 5, 2]
# odd numbers ascending: [1, 3,    5, ] ( Odds number in the index 0, 1, and 4)
# even numbers descending: [    8, 4,  2] (Evens number in the index 2,3, and 5)