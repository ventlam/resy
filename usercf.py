#train is a dict consist of {user : [items]} ?
def userCF(train):
    #build inverse table for item_users
    train = {'gallahad': ['the pure','a'], 'robin': ['the brave']}
    item_users = dict()
    for u, items in train.items:
        for i in items.keys():  #  items is a list ?
            if i not in item_users:
                item_users[i] = set()
                print i
            item_users[i].add(u)
            print u
    # calculate co-rated items between users
    C = dict()
    M = dict()
    for i, users in item_users.items():
        for  u in users:
            N[u] += 1
            for v in users:
                if u == v:
                    continue
                C[u][v] += 1

    #calculate final simsilarity matrix w
    W = dict()
    for u, related_users in C.items():
        for v, cuv in related_users.items():
            W[u][[v] = cuv / math.sqrt(N(u) * N(v))
    return W

