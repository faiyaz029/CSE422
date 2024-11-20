file1 = open('input.txt', 'r')

heu_value = {}
act_dist = {}

for line in file1:
        pr = line.split()
        node = pr[0]
        heu = int(pr[1])
        all_neighbors = pr[2:]
        heu_value[node] = heu
        act_dist[node] = {}
        for i in range(0, len(all_neighbors), 2):
            neighbor = all_neighbors[i]
            distance = int(all_neighbors[i+1])
            act_dist[node][neighbor] = distance


# print(f' this is heu_value {heu_value}')
# print(f' this is act_dist {act_dist}')

def a(start, goal):
    list1 = []
    lo_list = []
    dict1 = {}
    dict2 = {}
    parent = {}
    dict1[start] = 0
    dict2[start] =dict1[start] + heu_value[start]
    list1.append((dict2[start], start))

    while list1:
        list1.sort()

        # print(f' this is list1 --1 {list1}')

        current = list1.pop(0)[1]
        
        # print(f' this is current --2 {current}')
        
        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)

            # ###---------3
            # print(f' this is path --3 {path}')
            path.reverse()
            
            return path,dict1, #dict2, #list1, lo_list
        
        lo_list.append(current)
        #####---------5
        # print(f' this is lo_list --5 {lo_list}')

        for neighbor in act_dist[current]:
            v = dict2[current] + act_dist[current][neighbor] + heu_value[neighbor]
            if neighbor in lo_list:
                continue
            if neighbor not in [i[1] for i in list1]:
                list1.append((v, neighbor))
            elif v >= dict2[neighbor]:
                continue
            parent[neighbor] = current
            dict1[neighbor] =dict1[current] + act_dist[current][neighbor]
            dict2[neighbor] =dict1[neighbor] + heu_value[neighbor]
    return "NO PATH FOUND",dict1 

#path,dict1, = a('Arad', 'Sibiu')
path,dict1, = a('Arad', 'Bucharest')


if path == "NO PATH FOUND":
    print(path)
else:
    print(path)
   
    print(f'Total distance: {dict1[path[-1]]} km')
    #print(dict1)

    # print(f' this isdict1{dict1}')
    # print(f' this is f{dict2}')
    # print(f' this is list1{list1}')
    # print(f' this is lo_list{lo_list}')











file1.close()