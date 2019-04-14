missingNumbers=[]
smallestInteger=None

def func(olist):
    maxNum = max(olist)
    minNum = min(olist)
    for a in range(minNum,maxNum + 1):
        if a not in olist and a >= 1:
            missingNumbers.append(a)
            smallestInteger = min(missingNumbers)
            return smallestInteger
        elif a < 1:
            return 1
        else:
            b = maxNum + 1
            while b <= 1:
                b = b + 1
            smallestInteger = b
    return smallestInteger



print(func([1, 3, 6, 4, 1, 2])) #5
print(func([1, 2, 3]))  #4
print(func([-1,-3])) #1


        


