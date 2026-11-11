def test():
    print("Salom dunyo")

def qoshmoq(a:int, b:int):
    return a+b

def olma(a:str, b:int):
    return a*b

def Count(a:str) -> dict:
    new = {}
    # for harf in a:
    #     new[harf]=a.count(harf)

    for harf in a:
        if harf not in new:
            new[harf] = 1
        else:
            new[harf] += 1
    return new


def salom(a, b=10, c=12):
    pass

# natija = test()
# print(natija)

# natija = qoshmoq(5, 10)
# print(natija)

# matn = input("Matn kiriting: ")
# miqdor = int(input("Nechta: "))
# natija = olma(matn, miqdor)
# print(natija)

# natija = Count("assalom")
# print(natija)

salom(5,4)