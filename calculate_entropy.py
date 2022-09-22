import math
import numpy as np

#输入矩阵的维数
# n = int(input('Enter the number of rows in matrix:'))
# a = [[0]*n for i in range(n)]
#
# for i in range(n):
#     for j in range(n):
#          a[i][j] = float(input())
# print(a)
n=2
a = [[0.1,0.5],[0.4,0.9]]

def X_Probability(a):
#计算X的概率
    x_probability  = []
    for i in range(len(a)):
        x = 0.0
        for j in range(len(a)):
            x = x + a[j][i]
        x_probability.append(x)
    return x_probability

def Y_Probability(a):
#计算Y的概率
    y_probability  = []
    for i in range(n):
        x = 0.0
        for j in range(n):
            x = x + a[i][j]
        y_probability.append(x)
    return y_probability

def XY_Entropy(a):
#计算XY的熵
    x = 0.0
    for i in range(n):
        for j in range(n):
            if a[i][j] != 0:
                x = x + a[i][j]*(-math.log2(a[i][j]))
            else:
                x = x
    return  x

def X_Entropy(a):
#计算X的熵
    x_probability = X_Probability(a)
    entropy = 0.0
    for i in range(len(x_probability)):
        if x_probability[i] != 0:
            entropy = entropy + x_probability[i]*(-math.log2(x_probability[i]))
        else:
            entropy = entropy
    return entropy

def Y_Entropy(a):
#计算Y的熵
    y_probablity = Y_Probability(a)
    entropy = 0.0
    for i in range(len(y_probablity)):
        if y_probablity[i] != 0:
            entropy = entropy + y_probablity[i]*(-math.log2(y_probablity[i]))
        else:
            entropy = entropy
    return entropy

def XunderY_Entropy(a):
#计算Y下的X的熵
    new_a = [[0]*n for i in range(n)]
    en_list = []
    entropy = 0.0
    y_probaility = Y_Probability(a)
    for i in range(n):
        for j in range(n):
            new_a[i][j] = a[i][j]/y_probaility[i]
    for i in range(n):
        entropy_row = 0.0
        for j in range(n):
            if new_a[i][j] != 0:
                entropy_row = entropy_row + new_a[i][j]*(-math.log2(new_a[i][j]))
            else:
                entropy_row = entropy_row
        en_list.append(entropy_row)
    for i in range(n):
        entropy = entropy + y_probaility[i]*en_list[i]

    return entropy

def YunderX_Entropy(a):
#计算X下的Y的熵
    entropy = XY_Entropy(a) - X_Entropy(a)
    return entropy


# print('X的熵：',X_Entropy(a),'\n',
#        'Y的熵：',Y_Entropy(a),'\n',
#        "XY的熵",XY_Entropy(a),'\n',
#       'X在Y下的熵',XunderY_Entropy(a),'\n',
#       "Y在X下的熵",YunderX_Entropy(a))

b=2.289390/(1.444*math.log2(3))
print(b)
a=0
list = [1/3,1/3,1/9,1/9,1/27,1/27,1/27]
for i in range(len(list)):
    a += -(list[i]*math.log(list[i],))
print(a)