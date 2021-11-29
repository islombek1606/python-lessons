# MAVZU: For sikllar bilan ishlash.
# SANA: 02.11.2021
mehmonlar=["ali","vali",'baxodir','aziz','salim','otabek','jamshid']
for mehmon in mehmonlar:
    print(mehmon)
talabalar=["ali","vali",'baxodir','aziz','salim','otabek','jamshid','sanjar','halim'] 
for talaba in talabalar:
    print(f"Hurmat {talaba.upper()}, sizni 1-sentyabir kuni yangi o'quv yili boshlangani sababli darsga kelishingizdi so'raymiz.")
print(f"Hurmat bilan maktab ma'muriyati!")
talabalar1=["ali","vali",'baxodir','aziz','salim','otabek','jamshid','sanjar','halim'] 
for talaba1 in talabalar1:
    print(talaba1.title())
print(talabalar1)
sonlar=list(range(0,11))
for son in sonlar:
    print(son)
print(sonlar)
ages=list(range(101))
for age in ages:
    print(f"{age},- sonning kvadrati {age**2}")
sonlar1=list(range(0,21))
sonlar_kvadrati=[]
for son1 in sonlar1:
    sonlar_kvadrati.append(son1**2)
print(sonlar1)
print(sonlar_kvadrati)
#dostlar=[]
#print("Beshta do'stingizni kiriting?")
#for n in  range(5):
    #dostlar.append(input(f"{n+1}- do'stingizdi kiriting?"))
    #print(dostlar)
# AMALIYOT:
ismlar=["xasan",'xusan','botir','sarvar','rustam']
for ism in ismlar:
    print(ism.upper())
print("Kod 5 marta takrorlandi")
toq_sonlar=list(range(10,101))
for x in toq_sonlar:
    print(f"{x} ning kubi={x**3} ga teng")
kinolar=[]
print("5 ta eng sevimli kinolaringizdi kiriting?")
for kino in range(5):
    kinolar.append(input(f"{kino+1}- Sevimli kinoyizdi kiriting?"))
print(kinolar)
odamlar=[]
print(f"bugun mechta odam bilan suxbatlashdiz?")
for odam in range(5):
    odamlar.append(input(f"{odam+1}-suxbatlashgan odamim"))
print(odamlar)
    