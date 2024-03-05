import random
ball = {
    1:200,
    2:300,
    3:50,
    4:80,
    5:"Priz",
    6:150,
    7:250,
    8:110,
    9:10,
    10:None
}
answer = "MUHAMMAD"
javoblar = ["-","-","-","-","-","-","-","-"]
counter = 0
while True:
    print("Al-Buxoriyning haqiqiy ismi")
    ask = input("Barabanni aylantirish uchun ENTER tugamsini bosing")
    if not ask:
        son = random.randint(1,10)
        if ball[son] == None:
            print("Bankrot")
            break
        elif ball[son]=="Priz":
            print("Sizga yutuq chiqdi")
        else:
            print("Sizda ",ball[son],"balingiz bor")
            harf = input("Harf kiriting").upper()
            if harf == answer:
                 print("Siz so'zni tug'ri topdingiz",answer)
                 break
            else:
                if harf in answer:
                    for i in answer:
                        if i == harf:
                            javoblar[counter]=answer[counter]
                        counter+=1
                    counter = 0
                    print(javoblar)
                    if ''.join(javoblar) == answer:
                                break
