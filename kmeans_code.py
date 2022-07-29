# reference from "https://ithelp.ithome.com.tw/articles/10209058"

import numpy as np

x = np.random.randint(0, 500, 20)
y = np.random.randint(0, 500, 20)
kx = np.random.randint(0, 500, 3)   # numpy_array
ky = np.random.randint(0, 500, 3)   # numpy_array

print(f"x={x}, y={y}\nkx={kx}, ky={ky}")

def dis(x, y, kx, ky):
    return int(((kx-x)**2 + (ky-y)**2)**0.5)


def cluster(x, y, kx, ky):
    team = []
    for i in range(3):
        team.append([])

    for i in range(20):
        distance_1 = dis(x[i], y[i], kx[0], ky[0])
        distance_2 = dis(x[i], y[i], kx[1], ky[1])
        distance_3 = dis(x[i], y[i], kx[2], ky[2])
        min_distance = min(distance_1, distance_2, distance_3)
        if min_distance == distance_1:
            team[0].append([x[i], y[i]])
        elif min_distance == distance_2:
            team[1].append([x[i], y[i]])
        else:
            team[2].append([x[i], y[i]])

    return team



def re_seed(team, kx, ky):
    sumx = 0
    sumy = 0
    new_seed = []
    for index, nodes in enumerate(team):
        if nodes == []:
            new_seed.append([kx[index], ky[index]])
        for node in nodes:
            sumx += node[0]
            sumy += node[1]
        new_seed.append([int(sumx/len(nodes)), int(sumy/len(nodes))])
        print(f"new:{new_seed}")
        sumx = 0
        sumy = 0
    nkx = []
    nky = []
    for i in new_seed:
        nkx.append(i[0])
        nky.append(i[1])
    return nkx, nky

first = cluster(x, y ,kx, ky)
print(first)
re_seed(first, kx, ky)