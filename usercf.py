def userCF(train):
    #build inverse table for item_users
    item_users = dict()
    for u,items in train.items:
        for i in items.keys():
            if i not in item_users:
                item_users[i] = set()
            item_users[i].add(u)

