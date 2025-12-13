import numpy as np
from sklearn import datasets

# Load the diabetes dataset
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# 添加一列全为 1 的变量作为 θ0 对应的变量
diabetes_X = np.c_[np.ones(diabetes_X.shape[0]), diabetes_X]

# 初始化参数
theta = np.zeros(diabetes_X.shape[1])

# 定义模型函数
def hypothesis(theta, X):
    return np.dot(X, theta)

# 定义学习率和迭代次数
alpha = 0.01
num_iters = 1000
m = len(diabetes_y)

# 定义梯度下降函数
def gradient_descent(X, y, theta, alpha, num_iters):
    for _ in range(num_iters):
        delta = np.dot(X.T, (np.dot(X, theta) - y)) / m
        theta -= alpha * delta
    return theta

# 训练模型
theta = gradient_descent(diabetes_X, diabetes_y, theta, alpha, num_iters)

print("训练得到的参数 theta：", theta)