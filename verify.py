from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

np.random.seed(5)

iris = datasets.load_iris()
x = iris.data
y = iris.target

print(x)
x_decompose = PCA(2).fit_transform(x)
print(x_decompose)

colors = ['red', 'blue', 'green']

plt.figure()
for i in [0, 1, 2]:
    plt.scatter(x_decompose[y == i, 0],
                x_decompose[y == i, 1],
                alpha=0.7,
                c=colors[i],
                label=iris.target_names[i])

plt.title("Correct answer")
plt.legend()   # 圖例
plt.show()   # show

