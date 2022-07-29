import random

import matplotlib.pyplot as plt

hello_list = [
    [0, 7],
    [1, 5],
    [-1, 3],
    [8, 3],
    [7, 2],
    [8, 2],
    [1, -3],
    [2, -4],
    [1, -4],
]

def distance_v2(a: list, b: int):
    sepal_l = (a[0] - hello_list[b][0]) ** 2
    sepal_w = (a[1] - hello_list[b][1]) ** 2
    return (sepal_l + sepal_w) ** 0.5


# initialization 隨機選3個點 並將其data轉換成list
cluster_centers = random.sample(range(0, len(hello_list)), 3)
c_list_a = hello_list[cluster_centers[0]]
c_list_b = hello_list[cluster_centers[1]]
c_list_c = hello_list[cluster_centers[2]]

print(f"initial:center1:{c_list_a}, center2:{c_list_b}, center3:{c_list_c}")

# 分類後list存放物件編號
class_0 = []
class_1 = []
class_2 = []

# input: center list
def classification(a, b, c):
    plt.figure()
    class_0.clear()
    class_1.clear()
    class_2.clear()
    for flower_num in range(len(hello_list)):
        distance_a = distance_v2(a, flower_num)
        print(distance_a)
        distance_b = distance_v2(b, flower_num)
        print(distance_b)
        distance_c = distance_v2(c, flower_num)
        print(distance_c)
        if distance_a < distance_b and distance_a < distance_c:
            class_0.append(flower_num)
            color = "red"
        elif distance_b < distance_a and distance_b < distance_c:
            class_1.append(flower_num)
            color = "blue"
        else:
            class_2.append(flower_num)
            color = "green"

        plt.scatter(hello_list[flower_num][0], hello_list[flower_num][1], c={color})

    plt.title("ttt")
    plt.show()  # show



def find_center(after_classify: list):
    sepal_l_sum = 0
    sepal_w_sum = 0

    for num in after_classify:
        sepal_l_sum += hello_list[num][0]
        sepal_w_sum += hello_list[num][1]

    quantity = len(after_classify)
    new_center = [sepal_l_sum/quantity, sepal_w_sum/quantity]
    print(new_center)

    return new_center

# main
for iteration in range(3):
    print(f"iter:{iteration}")
    classification(c_list_a, c_list_b, c_list_c)
    c_list_a = find_center(class_0)
    c_list_b = find_center(class_1)
    c_list_c = find_center(class_2)




