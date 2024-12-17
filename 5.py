def family_tree(num):
    tree = {}
    for i in range(num):
        parent, child = input('enter the parent and the child separated by a space: ').split()
        if parent not in tree:
            tree[parent] = []
        tree[parent].append(child)
    return tree


def counting(nm, tree):
    if nm not in tree:
        return 0
    connections = tree[nm]
    cntr = len(connections)
    for people in connections:
        cntr += counting(people, tree)
    return cntr


number = int(input('enter the number of parental relationships: '))
family = family_tree(number)
name = input('enter the name whose number of relatives u want to find: ')
print(counting(name, family))
