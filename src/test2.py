import random

range_lower = [97,122]
range_upper = [65,90]
range_digit = [48,57] 


offset2 = 562

pw = "2341zßehdß1ah10176821e1w1e219"

def adjust_pw(offset,pw):
    min = 33
    max = 126
    while offset != 0:
        print(offset)
        if offset < max:
            print("red_off")
            max= offset
        rint = random.randint(min,max)
        if offset - rint < min:
            print("rint=min")
            rint = offset
        pw += chr(rint)
        offset -= rint
    print(offset)
    return pw


print(adjust_pw(offset2,pw))