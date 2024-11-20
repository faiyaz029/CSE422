file1 = open('input.txt', 'r')

heuristic_value = {}
actual_distance = {}

for line in file1:
        
        parts = line.split()
        node = parts[0]
        heuristic = int(parts[1])
        neighbors = parts[2:]
        heuristic_value[node] = heuristic
        actual_distance[node] = {}
        for i in range(0, len(neighbors), 2):
            neighbor = neighbors[i]
            distance = int(neighbors[i+1])
            actual_distance[node][neighbor] = distance

def a_star(start, end):
    open_list = []
    closed_list = []
    g = {}
    f = {}
    parent = {}
    g[start] = 0
    f[start] = g[start] + heuristic_value[start]
    open_list.append((f[start], start))
    while open_list:
        open_list.sort()
        current = open_list.pop(0)[1]
        if current == end:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path, g
        closed_list.append(current)
        for neighbor in actual_distance[current]:
            if neighbor in closed_list:
                continue
            if neighbor not in [i[1] for i in open_list]:
                open_list.append((f[current] + actual_distance[current][neighbor] + heuristic_value[neighbor], neighbor))
            elif f[current] + actual_distance[current][neighbor] + heuristic_value[neighbor] >= f[neighbor]:
                continue
            parent[neighbor] = current
            g[neighbor] = g[current] + actual_distance[current][neighbor]
            f[neighbor] = g[neighbor] + heuristic_value[neighbor]
    return "NO PATH FOUND", g

path, g = a_star('Arad', 'Bucharest')
if path == "NO PATH FOUND":
    print(path)
else:
    print(path)
   
    print()
    print("Total distance:", g[path[-1]], "km")