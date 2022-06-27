def parts_sums(ls):
    summ = sum(ls)
    lst = [summ]
    i=0
    for i in ls:
        summ -=i
        lst.append(summ)
    return lst
