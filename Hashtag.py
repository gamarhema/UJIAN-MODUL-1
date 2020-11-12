def Hashtag (string):
    x = string.title()                   #membuat setiap huruf pada awal kata menjadi kapital
    x2 = x.split()                       #membuat list berisi kata menjadi element sendiri-sendiri/terpisah
    if x2 == []:                         
        print("False")                   #jika list kosong atau " " maka akan return False
    else:
        z = '"#'+''.join(x2)+'"'          #jika tidak, maka akan di print dengan "#KATA YANG INGIN DI PRINT" tanpa spasi
        print(z)

Hashtag("Hello there how are you doing")
Hashtag("     Hello     World   ")
Hashtag("")

# print(type(""))
#Hashtag("Hello there how are you doing")// would return "#HelloThereHowAreYouDoing"

