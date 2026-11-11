def exam(score:int)->bool:
    if score >= 60:
        return True
    else:
        return False


def Increase(mahsulotlar:list[tuple[str,int]]):
    new = []
    for mahsulot, narx in mahsulotlar:
        yangi = (mahsulot, round(narx*1.1,2))
        new.append(yangi)
    return new


def get_top_user(oquvchilar:list[tuple[str, int]]):
    dct = {}
    for ism, baho in oquvchilar:
        if ism not in dct:
            dct[ism] = baho 
        else:
            dct[ism] += baho
    return max(dct, key=dct.get)


def max_movies_to_watch (movies:list[tuple[int,int]]):
    natija = []
    for index, movie in enumerate(movies):
        test = [movie]
        for kino in movies[index+1:]:
            if test[-1][1] <= kino[0]:
                test.append(kino)
        if len(test) > len(natija):
            natija = test.copy()
    return len(natija), natija