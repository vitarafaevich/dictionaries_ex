def dijkstring(ways, beg, end):
    intrv = {node: float('inf') for node in ways} #to start with lenght of every rode if infinity, key = node = узел
    intrv[beg] = 0                                #starting from the "starting" city
    vstd = set()                                  #for already processed vertices

    while len(vstd) < len(ways):
        crnt_nd = None
        crnt_dst = float('inf')

        for node in ways:
            if node not in vstd and intrv[node] < crnt_dst:
                crnt_dst = intrv[node]
                crnt_nd = node

        if crnt_nd is None:
            break

        vstd.add(crnt_nd)

        for near, dist in ways[crnt_nd].items():  #for nodes that are near. tuple of pairs of values
            dst = crnt_dst + int(dist)
            if dst < intrv[near]:
                intrv[near] = dst                 #if distance is shorter


    return intrv[end]


def functioning():
    cities = int(input('enter the number of cities: '))
    roads = int(input('enter the number of roads: '))
    ways = {}
    for i in range(roads):
        ln = input('enter the name of 2 cities and range between them separated by a space: ').split()
        ct_1, ct_2, dst = ln[0], ln[1], ln[2]
        if ct_1 not in ways:
            ways[ct_1] = {}
        if ct_2 not in ways:
            ways[ct_2] = {}
        ways[ct_1][ct_2] = dst
        ways[ct_2][ct_1] = dst
    return ways

line = input('enter the name of the cities u want to know the distance between: ').split()
cty_strt, cty_fnsh = line[0], line[1]

print(dijkstring(functioning(), cty_strt, cty_fnsh))
