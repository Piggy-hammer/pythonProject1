import csv

import pandas as pd
import numpy as np
import sklearn.decomposition

data = pd.read_csv(r'D:\equi.csv')
pca = sklearn.decomposition.PCA()
pca.fit(data)
print('特征向量\n', pca.components_)
print('各个成分各自的方差百分比（贡献率）\n', pca.explained_variance_ratio_)
# 特征向量的维度和长度
len(pca.components_), pca.components_.shape

# 根据计算结果，前四分主成分即达到贡献率99.77%，
pca = sklearn.decomposition.PCA(2)
pca.fit(data)
low_d = pca.transform(data)
print("结果")
print(low_d)
# 计算压缩维数：
np.array(list(data.shape)) - np.array(list(pca.components_.shape))
# 还原
inv_result = pca.inverse_transform(low_d)
print(inv_result)  # 降维有损
# 贡献率99.77%,但维数不变
print(inv_result.shape)
print(data)

f = open('D:\\222.csv', 'w', newline='')
writer = csv.writer(f, delimiter=',')
for i in low_d:
    writer.writerow(i)
f.close()
