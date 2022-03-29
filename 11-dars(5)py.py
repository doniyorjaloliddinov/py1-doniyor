
# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni 
#so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring.
# Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz,
# oydalanuvchi!" xabarini chiqaring
users = ["anvar123","zokir234","doni2030","yorqin8900","jaska"]
savol = input("Login kiriting: ")
if savol in users:
        print("Lo'gin band yangi login kiriting: ")
else:
    print(f"Assalomu alaykum {savol} xush kelibsiz")
 """
 
 """
#Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni
#2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 
son = int(input("Biror son kiriting: "))      
for a in range(2,11):
    if not(son%a):
        print(f"{son} soni {a} ga qoldiqsiz bo'linadi")

