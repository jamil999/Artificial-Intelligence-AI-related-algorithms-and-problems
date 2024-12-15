takelines = open('Input file.txt')

dict1 = {}
dict2 = {}
par_child = {}
already_ex = []

while True:
    takeline = takelines.readline().split()

    if takeline == []:
        break

    parent = takeline[0]
    hue = int(takeline[1])

    dict1[parent] = hue

    for ab in range(2, len(takeline), 2):
        child = takeline[ab]
        dis = int(takeline[ab + 1])
        dict2[parent, child] = dis

def a_star_algo(dict1, dict2, start, end):
    que = {}
    expanded = ''
    que[dict1[start] + 0] = start
    if start == end:
        return 'NO PATH FOUND'

    while que != {}:
        track1 = expanded  
        min_val = min(que.keys())
        expanded = que.pop(min_val)
        
        if expanded not in par_child.keys():
            par_child[expanded] = []
            for cd in dict2.keys():
                if cd[0] == expanded and cd[1] not in already_ex:
                    par_child[expanded].append(cd[1])
        already_ex.append(expanded)

        for chi in par_child[expanded]:
            if chi not in already_ex:
                var_ex = expanded
                var_chi = chi
                total = 0
                tr = True
                while tr:
                    total += dict2[(var_ex, var_chi)]
                    var_chi = var_ex
                    for xz,cz in par_child.items():
                        if var_chi in cz:
                            var_ex = xz
                    if var_ex == start :
                        for dfa,sdf in dict2.items():
                            if dfa[0] == var_ex and dfa[1] == var_chi:
                                total += sdf
                        tr = False
                        
                list1 =  list(que.values())
                list2 = list(que.keys())

                if chi in list1:
                    get = list1.index(chi)
                    if total < list2[get]:
                        que.pop(list2[get])
                        que[total + dict1[chi]] = chi
                    else:
                        pass
                else:
                    que[total + dict1[chi]] = chi
        
        if expanded == end:
            track2 = expanded
            the_path = []
            the_path.append(track2)
            the_path.append(track1)
            while track1 != start:
                for yk, yv in par_child.items():
                    for ya in yv:
                        if track1 == ya:
                            the_path.append(yk)
                            track1 = yk
            return the_path     
    if que == {} and expanded != end:
        return 'NO PATH FOUND'

start = input('Start node: ')
end = input('Destination: ')

path = a_star_algo(dict1, dict2, start, end)

if path != 'NO PATH FOUND':
    path = path[::-1]
    print('Path: ',end = '')
    for i in path:
        if i == end:
            print(i)
        else:
            print(i+' -> ',end='')
else:
    print(path)
    
diss = 0

if path != 'NO PATH FOUND':
    for i in range(0, len(path) - 1):
        diss += dict2[(path[i],path[i + 1])]
    print(f'Total distance: {diss} km')