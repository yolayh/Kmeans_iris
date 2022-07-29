from sklearn.datasets import load_iris
import pandas
import random
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


iris = load_iris(as_frame=True)
iris_data = iris.data
# sepal length (cm)
# sepal width (cm)
# petal length (cm)
# petal width (cm)
iris_answer = iris.target
# ['setosa', 'versicolor', 'virginica']
iris_num = len(iris_data)
iris_dict = iris_data.to_dict()

# def distance_v1(a, b):
#     sepal_l = (iris_dict['sepal length (cm)'][a] - iris_dict['sepal length (cm)'][b]) ** 2
#     sepal_w = (iris_dict['sepal width (cm)'][a] - iris_dict['sepal width (cm)'][b]) ** 2
#     petal_l = (iris_dict['petal length (cm)'][a] - iris_dict['petal length (cm)'][b]) ** 2
#     petal_w = (iris_dict['petal width (cm)'][a] - iris_dict['petal width (cm)'][b]) ** 2
#     return (sepal_l + sepal_w + petal_l + petal_w) ** 0.5


def distance_v2(a: list, b: int):
    sepal_l = (a[0] - iris_dict['sepal length (cm)'][b]) ** 2
    sepal_w = (a[1] - iris_dict['sepal width (cm)'][b]) ** 2
    petal_l = (a[2] - iris_dict['petal length (cm)'][b]) ** 2
    petal_w = (a[3] - iris_dict['petal width (cm)'][b]) ** 2
    return (sepal_l + sepal_w + petal_l + petal_w) ** 0.5


def set_list(num):
    a = iris_dict['sepal length (cm)'][num]
    b = iris_dict['sepal width (cm)'][num]
    c = iris_dict['petal length (cm)'][num]
    d = iris_dict['petal width (cm)'][num]
    content_list = [a, b, c, d]

    return content_list


# initialization 隨機選3個點 並將其data轉換成list
cluster_centers = random.sample(range(0, iris_num), 3)
c_list_a = set_list(cluster_centers[0])
c_list_b = set_list(cluster_centers[1])
c_list_c = set_list(cluster_centers[2])


# 分類後list存放物件編號
class_0 = []
class_1 = []
class_2 = []

# input: center list
def classification(a, b, c):
    class_0.clear()
    class_1.clear()
    class_2.clear()
    for flower_num in range(iris_num):
        distance_a = distance_v2(a, flower_num)
        distance_b = distance_v2(b, flower_num)
        distance_c = distance_v2(c, flower_num)
        min_dis = min(distance_a, distance_b, distance_c)
        if min_dis == distance_a:
            class_0.append(flower_num)
        elif min_dis == distance_b:
            class_1.append(flower_num)
        else:
            class_2.append(flower_num)


def find_center(after_classify: list):
    sepal_l_sum = 0
    sepal_w_sum = 0
    petal_l_sum = 0
    petal_w_sum = 0

    for num in after_classify:
        sepal_l_sum += iris_dict['sepal length (cm)'][num]
        sepal_w_sum += iris_dict['sepal width (cm)'][num]
        petal_l_sum += iris_dict['petal length (cm)'][num]
        petal_w_sum += iris_dict['petal width (cm)'][num]

    quantity = len(after_classify)
    a = round(sepal_l_sum/quantity, 2)
    b = round(sepal_w_sum/quantity, 2)
    c = round(petal_l_sum/quantity, 2)
    d = round(petal_w_sum/quantity, 2)
    new_center = [a, b, c, d]

    return new_center


def collect_answer(answer: list):
    collected = []
    for num in answer:
        collected.append(set_list(num))

    return collected


def plotplot():
    quantity_0 = len(class_0)
    quantity_1 = len(class_1)
    quantity_2 = len(class_2)
    answer = [0 for num in range(quantity_0)] + [1 for num in range(quantity_1)] + [2 for num in range(quantity_2)]
    answer_set = collect_answer(class_0) + collect_answer(class_1) + collect_answer(class_2)
    answer_decompose = PCA(2).fit_transform(answer_set)

    colors = ['red', 'blue', 'green']

    plt.figure()

    for i in range(150):
        plt.scatter(answer_decompose[i][0],
                    answer_decompose[i][1],
                    alpha=0.7,
                    c=colors[answer[i]],
                    )

    plt.title("test")
    plt.show()

# execution
def kmeans_cluster(max_iter:int):
    global c_list_a
    global c_list_b
    global c_list_c
    k_iter = 0
    while k_iter <= max_iter:
        classification(c_list_a, c_list_b, c_list_c)
        new_c_list_a = find_center(class_0)
        new_c_list_b = find_center(class_1)
        new_c_list_c = find_center(class_2)

        #若中心點不再變動 termination
        if new_c_list_a == c_list_a and new_c_list_b == c_list_b and new_c_list_c == c_list_c:
            k_iter = max_iter + 5
        else:
            c_list_a = new_c_list_a
            c_list_b = new_c_list_b
            c_list_c = new_c_list_c
            max_iter += 1

        plotplot()


kmeans_cluster(30)








