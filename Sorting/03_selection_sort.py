def selection_sort(l):
    start = 0
    for j in range(1,len(l)):
        for i in range(j,len(l)):
            if l[i]<l[start]:
                l[i],l[start] = l[start],l[i]
        start += 1

    return l