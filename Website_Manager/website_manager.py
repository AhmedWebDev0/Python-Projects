Myweb =[]
a = 0

while a < 5 :

    web =input("Mfximum Allowed website https://\t")
    Myweb.append(f"https://{web.strip().lower()}")  
    a += 1
    print(f"Website Added ,{Myweb} Places Left")

else :

    print("Bookmak Is Full ,You con't Add more")



if len(Myweb) < 0 :

   Myweb.sort()
   
   index =0
   while len(Myweb) < index :
       
       print(Myweb[index])
       index+=1
