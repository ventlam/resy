http://restapi.amap.com/v3/place/text?types=%E9%A4%90%E9%A5%AE%E6%9C%8D%E5%8A%A1&city=010&offset=100&page=4&extensions=all&output=json&key=c84af8341b1cc45c801d6765cda96087#train is a dict consist of {user : [items]} ?
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

