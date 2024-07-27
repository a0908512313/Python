for i in temp:
    for j in temp:
        TEMP = abs(k - (i * j))
        if TEMP in lis:
            if TEMP < min(lis):
                temp.append(TEMP)
            else:
                break
        else:
            lis.append(TEMP)