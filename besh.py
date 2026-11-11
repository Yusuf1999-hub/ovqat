# dict -> lug'at 
# key : value


# dct = {"name":"Aziz", "second":"Karimov", "age":9, "salary":2026}
# dct['name'] = "Vali"
# dct['age'] = 20
# dct["position"] = "programmer"
# print(dct)


# dct = {
#     "brand" : "BMW",
#     "color" : "Qora",
#     "year"  : 2025,
#     "price" : 80000
# }

# dct['motor'] = "V8"

# for key in dct:
#     print(key, dct[key])

# for key, value in dct.items():
#     print(key, value)

# --------------------------------

# dct = {}

# for i in range(int(input(">> "))):
#     kalit = input("English: ")
#     qiymat = input("Uzbek: ")
#     dct[kalit] = qiymat

# print(dct)

# -------------------------------

# dct = {}
# lst = ["Avaz", "Voris", "Karim", "Voris", "Bek", "Bek"]
# for ism in lst:
#     dct[ism] = lst.count(ism)
# print(dct)

# --------------------------------

dct = {
    "Vali" : 80,
    "Ali" : 90,
    "Umid" : 30,
    "Karim" : 83,
    "Jumagul" : 60,
    "Bilol" : 50
}

# for kalit, qiymat in dct.copy().items():
#     if qiymat < 60:
#         dct.pop(kalit)

# print(dct)

# print(sum(dct.values())/len(dct))

# ball = max(dct.values())
# for kalit, qiymat in dct.items():
#     if ball == qiymat:
#         print(kalit)
#         break

print(max(dct, key=dct.get))
print(max(dct, key=lambda x: dct[x]))

# ---------------------------

# dct = {"name" : "Axmad",
#        "yosh" : 23,
#        "city" : "Tashkent"}
# dct['age'] = dct.pop("yosh")


# {} | {}    -> 2ta dict ni bir biriga qo'shib beradi