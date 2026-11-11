# print(natija:=len(input(">>> "))**3)

# a, b = 10, 5
# a, b = b, a 

# ------------------------ Slicing
# matn = "Foundation"
# print(matn[0])
# print(matn[-1])

# matn[0] = 'S'  # ERROR

# [start:stop:step]
# matn[1:5:1] # ound
# matn[1:5] # ound
# matn[:5] # Found
# matn[1:] # oundation
# matn[:] # Foundation
# matn[::2] # Fudto
# matn[::-1] # noitadnuoF

# ------------------------------

# str + str
# matn = "salom"
# matn = matn[:2] + "L" + matn[3:]
# print(matn)

# ------------------------------

# sana = input() # 10.12.2020
# sana = sana[:3] + "10" + sana[5:]
# print(sana)

# ------------------------------

# soz = input()
# if soz == soz[::-1]:
#     print("POLINDROM")
# else:
    # print("NOT POLINDROM")

natija = ""
for i in input(">> "):
    if i in "aeiou":
        natija += i.upper()
    else:
        natija += i
print(natija)




man hozir git o'rgandim