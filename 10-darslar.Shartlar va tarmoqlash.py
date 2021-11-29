# 8-Dars: Shartlar va tarmoqlar.
# sana: 03.11.2021
# Muallif: Amirov islombek
a=5
b=6
print(a==b)
print((a+1)==b)
print("anvar"=="Anvar") #Matindi taqqoslash 
print(10**2<2**10) #sonlardi taqqoslash
ism="ahmad"
print(ism!='Ahmad')
print(ism.title()=='Ahmad')
nums1=[1,2,3]
nums2=[1,2,4]
print(nums1!=nums2)
print(8**2>=7*8+7)
#x=10
#print(x*x<'x**2')
#print(x**x>=float(f"{x**2}"))
x=int(input("Istalgan sonni kriting?"))
if x>0:
    print("Musbat son")
else:
    print("Manfiy son")
yosh=int(input("Yoshingizdi kiriting?"))
if yosh<=7:
    print("Sizga kirish bepul")
else:
    print("sizga kirsh 5 ming so'm")
yosh1=int(input("Yoshingizdi kiriting?"))
if yosh1>=50: print("Siz nafaqa yoshiga yetibsiz") 
else: 
    print("Siz hal nafaqa yoshiga to'lmagansiz")
age=int(input("Sonni kiriting?"))
print('musbat son') if age>0 else print("manfiy son")
cars=['tico','matiz','jentra','malibu','captiva']
for car in cars:
    print(car.title()) if car=="matiz" else (car.upper)
javob=float(input("12*6 NECHIGA TENG"))
if javob==72:
    print("javob to'gri")
else:
    print("javob xato")
yil=int(input("Yilingizdi kiriting?"))
if 2021-yil<18:
    print(f"Siz5 {2021-yil} yoshda ekansiz sizga kirish mumkin emas!")
else:
    print(f"Siz {2021-yil} yoshda ekanszi sizga kirih mumkin! ")
login=input("Login kiriting")
if len(login)<=5:
    print("Siz kiritkan Login 5 harfdan ko'p bo'lish shart!")
else:
    print("Login qabul qilindi")
# AMALIYOT:
moshnar=["toyota",'mazda','hyundai','gm','kia']
for moshn in moshnar:
    print(moshn.upper()) if moshn=="gm" else print(moshn.title())
moshnar=["toyota",'mazda','hyundai','gm','kia']
for moshn in moshnar:
 if moshn!="Gm":
    print(moshn.upper()) 
login1=input("Logindi kiriting?")
if login1=="Admin":
    print("Hush kelibsiz,Admin")
else:
    print("Xush kelibsiz Login xato")
b=int(input("B sonini kiriting?"))
c=int(input("C sonini kiriting?"))
if b==c:
    print("Sonlar teng")
son=float(input("Istalgan sonni kiriting?"))
if son<0:
    print("Manfiy son")
else:
    print("Musbat son")
son1=int(input("Son kiriting?"))
if son1>0:
    print("Kiritgan sonizdi ildizi",son1**(1/2))
elif son<0:
    print("Musbat son kiriting")
son2=int(input("Biror son kiriting"))
if son2%2==0:
    print("Juft son")
else:
    print("Toq son")
# Amaliyot tugadi:


    