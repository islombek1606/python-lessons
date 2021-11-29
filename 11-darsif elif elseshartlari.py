# son=50
# if son>0:
#     print("Musbat son")
# else:
#     print("Manfiy son")
# yosh=int(input("Yoshingidi kiriting? "))
# if yosh<=4:
#     print("Sizga kirish bepul")
# elif yosh<=12:
#     print("Sizga kirish 5000 so'm")
# else:
#     print("Sizga kirish 10000 so'm.")
# yosh1=int(input("Yoshdi kiriting?."))
# if yosh1<=5:
#     narx=0
# elif yosh1<12:
#     narx=5000
# elif yosh1<=18:
#     narx=8000
# else:
#     narx=10000
# print("Sizga kirish", narx, "so'm.")
# hafta=input("Bugun nima kun? ")
# if hafta.lower()=="shanba" or hafta.lower()=="yakshanba":
#     print("Bugun dam olish kuni.")
# else:
#     print("Bugun ish kuni.")

# kun=input("Bugun nima kun? ")
# harorat=float(input("Bugun havo harorati qanday"))
# if (kun.lower()=="yakshanba" or kun.lower()=="shanba") and harorat>=30:
#     print("Cho'milgani ketdik.")
# elif (kun.lower()=="yakshanba" or kun.lower()=="shanba") and harorat<=30:
#     print("bugun dam olish kuni.")
# pul=15000
# choy=True
# salat=False
# if choy or salat:
#     pul=pul+10000
# elif choy and salat:
#     pul=pul+15000
# print("Jami narx", pul,"so'm.")
# pul=1500
# non=True
# choy=False
# salat=True
# asarti=False
# if non: # Agar non olgan bo'lsa.
#     print("Mijoz non oldi.")
#     pul=pul+5000
# if choy:
#     print("Mijoz choy oldi.")
#     pul=pul+10000
# if salat:
#     print("Mijoz salat oldi.")
#     pul=pul+15000
# if asarti:
#     print("Mijoz asarti oldi.")
#     pul=pul+20000
# menu=["lagmon","chuchvara","shorva","Qozon kabaob","osh","mastava"]
# ovqat=input("Nima ovqat yeysiz?")
# if ovqat.lower() in menu:
#     print("buyurtmangiz qabul qilindi.")
# else:
#     print("Bizda bunday ovqat yo'q")
# ovqatlar=["lagmon","chuchvara","shorva","Qozon kabaob","osh","mastava"] # menyu
# buyurtma=["osh","chuchvara","shorva","manti","siltama"] # buyurtma
# for taom in ovqatlar: # ovqatlar degan ro'yxatni ichda harbir taom uchun(Taom degan o'zgaruvchiga elementdi yuklaydi.)
#     if taom in buyurtma: # Agar buyurtma ichdagi har bir taom uchun ovqat bomi yoqlilgini tekshiradi.Agar bolsa pasdagi kodni chiqaradi,
#         print("Ovqatlarda", taom, "bor")
#     else: # Akis xolda yo'q bolsa ushbu kodni amalga oshiradi.
#         print("Kechirasiz ovqatlkardegan ro'yxatda", taom, "yo'q")
ovqatlar=["lagmon","chuchvara","shorva","Qozon kabaob","osh","mastava"] 
buyurtma=["osh","chuchvara","shorva","manti","siltama"]
if buyurtma:
    for taom in buyurtma:
        if taom in ovqatlar:
            print("Menyuda", taom, "bor")
        else:
            print("Menyuda bunday", taom, "degan ovqat yo'q.")
else:
            print("Savatchangiz bo'sh.")

        





