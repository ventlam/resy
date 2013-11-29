def UserSmarility(train):
    W = dict()
    for u in train.keys():
        for v in train.keys():
            if u == v:
                continue
            W[u][v]  = len(list(set(train[u]) & set(train[v])))
            W[u][v]  /= math.sqrt(len(train[u]) * len(train[v]) * 1.0)
    print W
    return W

train = {'vivi': ['a','b','c'],'vent': ['a','b']}
UserSmarility(train)

