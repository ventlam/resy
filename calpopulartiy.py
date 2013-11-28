def Pop(train, test, N):
    item_Pop = dict()                 ## 字典?
    for user, items in train.items(): ## 两个变量in for>
        for item in items.key()       ## itmes.keys?
            if item not in item_Pop:
                item_Pop[item] = 0
            item_Pop[item] +=1
    ret = 0
    n   = 0
    for user in train.keys():
        rank = GetRec(user, N)
        for item , pui in rank
            ret += math.log(1+item_Pop[item])
            n   += 1
        ret /= n * 1.0
        return ret
