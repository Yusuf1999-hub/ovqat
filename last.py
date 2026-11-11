import json 

with open("test.json") as ptr:
    data = json.load(ptr)
    dct = {}
    for inson in data:
        # if "Python" in inson['courses']:
        #     print(f"{inson['name']} {inson['age']}")
        for fan in inson['courses']:
            if fan not in dct:
                dct[fan] = 1 
            else:
                dct[fan] += 1
    print(dct)