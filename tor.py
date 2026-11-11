# tpl = (12, "salom", 45)

# print(tpl[0])
# tpl[0] = 100

# for i in tpl:
#     print(i)

# tpl = list(tpl)
# tpl[0] = "Karam"
# tpl = tuple(tpl)
# print(tpl)

# -----------------------------

lst = [(12, 45, 2), (2,3), (6,5,2)]
for index, tpl in enumerate(lst):
    tpl = list(tpl)
    tpl.append(15)
    tpl = tuple(tpl)
    lst[index] = tpl
print(lst)