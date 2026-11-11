ptr = open("salomlar.txt")

data = ptr.read().split("\n")

for qator in data:
    bolak = qator.split(",")
    mac = bolak[-2].split("-")
    for i in mac:
        if i.isdigit():
            break
    else:
        print(bolak[0], bolak[-2])

ptr.close()