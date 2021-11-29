# Mavzu: Listlar
# Muallif: Amirov Islombek
#sana: 23/11/2021yil
mevalar=["olma","anor","olcha","Shaftoli","Banan"]
narxlar=[12000,45000,87000,98000,1300,7400]
aralash_royxat=["bir","ikki","uch",4,5,6,7,8,-45,-1.2]
bosh_royxat=[]
print(mevalar[0]) # Ro'yxatdagi 0- elementdi indeksi bo'ycha chiqarish
print(mevalar[3])
print(mevalar[4].upper())
print(mevalar[0].title())
mevalar[2]="Ananas" # Ro'yatga indeks bo'yicha elementni nomini  yozib qo'shish element ro'yxatga qoshilganda indeks bo'ycha berilgan elementdi o'chirib yuborib o'rniga qqo'yiladi.
print(mevalar)
mevalar.append("O'rik") # Ro'yxatni oxiriga element qoshish. 
mevalar.append("Olxo'ri")
print(mevalar)
mevalar.insert(1,"nok") # Ro'yxatdagi elementdi o'chirmasdan  indeks bo'ycha element qoshish.
mevalar.insert(2,"Kivi")
print(mevalar)
print("birinchi meva:", mevalar[0]) # Ro'yxatdagi 0- elementdi chiqarish.
print("Ikkinchi meva:", mevalar[2].upper()) # Ro'yxatdagi 2-elementdi katta xarf bilan chiqarish.
print(narxlar)
print(narxlar[1]+narxlar[3]) # Narxlardagi 1- va 3- elementdi qo'shish.
print(sum(narxlar)) # Ro'yxatdagi narxlardi yigindisini hisoblash.
print(mevalar[2]+ " " + str(narxlar[2]))
cars=[]
cars.append("Malibu")
cars.append("Matiz")
cars.append("Jentira")
cars[2]="Tico"
print(cars)
cars.insert(2,"Trekker")
cars.insert(2,"Damas")
print(cars)
print(mevalar)
del mevalar[3]
print(mevalar)
mevalar.remove("Shaftoli")
print(mevalar)
bozorlik=["yog'","un","go'sht","makaron"]
mahsulot=bozorlik.pop(1)
print(mahsulot)
print("men bugun bozordan",mahsulot.title(), "sotib oldim olinmagan maxsulotlar", bozorlik)
# AMALIYOT:
ism=["Asadbek","Jahongir","Rustam","Boxodir"]
print(ism)
print("Salom",ism[1],"bugun choyxona bormi?",ism[2], "choyxonaga boramizmi?")
sonlar=[12, 25, 46, -45, -7.5, 86]
print(sonlar)
print(sonlar[1]+sonlar[3])
print(sonlar[1]/sonlar[3])
sonlar[3]=94
sonlar.append(6)
sonlar.insert(1,100)
print(sonlar)
t_shaxslar=["Amur temur","Zahiriddin muhammad bobur","Alisher Navoiy","Abu Ali ibn sino"]
z_shaxslar=["Shavkat Mirziyoyev","Islom Karimov","Bil Geyts","Stib Jons",]
tarixiy_shaxs=t_shaxslar.pop(-1)
zamonaviy_shaxs=z_shaxslar.pop(0)
print("Men tarixiy shaxslardan", tarixiy_shaxs, "bilan, zamonaviy shaxslardan esa", zamonaviy_shaxs, "bilan suhbat qilishdi istar edim.")
print("Men Tarixiy shaxslardan", t_shaxslar[0], "Bilan, zamonaviy shaxlardan esa", z_shaxslar[2], "Bilan suhbat qilishdi istar edim." )
friends=[]
friends.append("Shoxruh")
friends.append("Sanjar")
friends.append("Jaloliddin")
friends.append("Asilbek")
friends.append("Shoyat")
print(friends)
# friends.remove("Shoyat")
# friends.remove("Asilbek")
# print("Mehmonga kela oladigan do'stlar:", friends)
mehmonga_kelmaganlar=friends.pop(1)
print(mehmonga_kelmaganlar, "Mehmonga kemagan dostlardan. Mehmonga kelgan dostlar", friends)
friends.append("Sohib")
friends.append("Aziz")
print(friends)
friends[2]="Samandar"
friends.insert(3,"Laziz")
print(friends)
# AMALIYOT TUGADI. BUYUKLIK SODDALIKDADUR BUYUKLIK SARI OLG'A.
