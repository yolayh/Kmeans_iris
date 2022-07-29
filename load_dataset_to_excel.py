from sklearn.datasets import load_iris
import pandas as pd

data = load_iris()
outputfile = "./iris.xls"  # 保存文件路径名
column = list(data['feature_names'])
dd = pd.DataFrame(data.data, index=range(150), columns=column)
dt = pd.DataFrame(data.target, index=range(150), columns=['outcome'])

jj = dd.join(dt, how='outer')  # 用到DataFrame的合并方法，将data.data数据与data.target数据合并
jj.to_excel(outputfile)  # 将数据保存到outputfile文件中