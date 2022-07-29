from sklearn.cluster import KMeans
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

iris = datasets.load_iris()
x = iris.data
y = iris.target

kmeans = KMeans(n_clusters=3)
kmeans_iris = kmeans.fit_predict(x)

x_decompose = PCA(2).fit_transform(x)


# calculate accuracy
# score = 0
#
# for i in range(150):
#     if y[i] == kmeans_iris[i]:
#         score += 1
#
# accuracy = round(score/150*100, 2)
#
# print(f"accuracy={accuracy}%")


# plot
colors = ['red', 'blue', 'green']
plt.figure()

for i in [0, 1, 2]:
    plt.scatter(x_decompose[kmeans_iris == i, 0],
                x_decompose[kmeans_iris == i, 1],
                alpha=0.7,
                c=colors[i],
                )

plt.title("Python Kmeans module")
plt.show()


