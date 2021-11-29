# 8-Dars: Ro'yxatlar bilan ishlash.
# sana: 29.10.2021
# Muallif: Amirov islombek
cars=["gm",'devo',"tesla","kia",'bmw','audio','mersedes']
cars.sort()
print(cars) # Ro'yxatlarni alifbo ketma ketlikda chiqarib beradi.
cars=["gm",'devo',"tesla","kia",'bmw','audio','mersedes']
cars.sort(reverse=True)
print(cars) # bu ro'yxatdagi so'zni tartiblab ham teskari tartiblab chiqarib beradi
cars=["gm",'devo',"Tesla","kia",'bmw','audio','mersedes']
cars.sort()
print(cars) # Agarda ro'yxatni ishida birorta so'z katta harf bn yozilsa ro'yxatimizdi tartiblaganimizda ro'yxat boshga qo'yilib qoladi.
mehmonlar=["biloldin",'hamid',"javohir","samandar", "aziz",'sobir','jaloldin']
print("Sorted qaytargan ro'yxat:", sorted(mehmonlar))
print("Asil ro'yxat ko'rinishi:", mehmonlar)
print(sorted(mehmonlar, reverse=True))
sonlar=[10,-25,45,16,1,4,8,78]
sonlar.sort()
print(sonlar)
print(sorted(sonlar, reverse=True))
ismlar=['ali','vali','jamshid','qaxxor']
print(len(ismlar)) # Ro'yxatdagi elementlar sonini topish.
raqamlar=list(range(0,10))
raqamlar2=raqamlar[0:3]
print(raqamlar)
print(raqamlar2)
fruits=['olma','behi','anor','anjir','gilos']
fruits.reverse() # Ro'yxatni teskari tartibda chiqarish
print(fruits)
fruits.sort()
print(sorted(fruits, reverse=True))
narxlar=[25000,1200,100,78000,95000,1100]
arzon_narx=min(narxlar)
qimmat_narx=max(narxlar)
jami_narx=sum(narxlar)
print("eng arzon narx bu",arzon_narx, "so'm")
print("Eng arzon narx:", arzon_narx, "so'm", "eng qimmat narx:", qimmat_narx, "so'm", "jami summa", jami_narx, "so'm")
juft_sonlar=list(range(0,26,2))
toq_sonlar=list(range(1,26,2))
print("Juft sonlar ro'yxati:", juft_sonlar)
print("Toq sonlar ro'yxati:", toq_sonlar)
fruits1=['olma','behi','anor','anjir','gilos','o\'rik','nok']
mevalr=fruits1[0:3]
mevalar=fruits1[:2]
mevalar1=fruits1[2:]
print(fruits1)
print(mevalr)
print(mevalar)
print(mevalar1)
sonlar1=[25,45,78,99,96,75]
sonlar2=sonlar1[:]
sonlar2.append(int(88))
sonlar2.remove(78)
sonlar2[3]=56
del sonlar2[2]
print(sonlar1)
print(sonlar2)
telfonlar=("iphon","samsung",'noki','elgi')
telfonlar=list(telfonlar)
telfonlar.append("fly")
telfonlar.remove("iphon")
telfonlar[0]="artel"
telfonlar=tuple(telfonlar)
print(telfonlar)
# AMALIYOT:
davlatlar=["O'zbekiston",'Qozog\'iston','Afg\'oniston',"Turkmaniston",'Pokiston']
print(davlatlar)
print(len(davlatlar))
print(sorted(davlatlar))
print("Sorted qaytargan ro'yxat", sorted(davlatlar,reverse=True)) # Reverse() qaytargan ro'yxatni ortidan boshlab chiqarish
print("Asil ro'yxat o'zgarmas qoldi", davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)
juft_sonlar1=list(range(120,1200,2))
print(juft_sonlar1)
juft_sonlar_yigindisi=sum(juft_sonlar1)
print(juft_sonlar_yigindisi)
eng_katta_son=max(juft_sonlar1)
eng_kichk_son=min(juft_sonlar1)
sonlar_yigindisi=(eng_katta_son-eng_kichk_son)
print(sonlar_yigindisi)
print(len(juft_sonlar1))
print(juft_sonlar1[0:20])
print(juft_sonlar1[55:100])
print(juft_sonlar1[-21:-1])
taomlar=["osh","achchiq","siltama",'lag\'mon','chuchvara','sho\'rva']
print(taomlar)
nonushta=taomlar[:]
nonushta.append("mastava")
nonushta.append("dolma")
print("nonushtaga yeyiladign taomlar:",nonushta)
print(taomlar)
print(nonushta)
print(tuple(nonushta))
nonushta[0]="qaymoq va non"
print(tuple(nonushta))