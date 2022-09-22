import math
import numpy as np


class 信源信道模型():
    """
    输入两个参数
    xinyuan：数组类型
    xindao：矩阵类型
    """
    def __init__(self,xinyuan,xindao):
        self.xinyuan = xinyuan
        self.xindao = xindao

    def calcuate_noise_enrtopy(self):
        noise_entropy = 0
        n = len(self.xinyuan)
        for i in range(n):
            for j in range(n):
                if self.xindao[i][j] != 0:
                    noise_entropy += -self.xindao[i][j]*self.xinyuan[i]*math.log2(self.xindao[i][j])
                else:continue
        return noise_entropy



    def calculate_mutual_information(self):
        mutual_information = 0
        n = len(self.xinyuan)
        for i in range(n):
            for j in range(n):
                x = 0
                if self.xindao[i][j] != 0:
                    for z in range(n):
                        if self.xindao[z][j] != 0:
                            x += self.xinyuan[z]*self.xindao[z][j]
                        else:continue
                    mutual_information += self.xinyuan[i]*self.xindao[i][j]*math.log2(self.xindao[i][j]/x)
                else:continue
        return mutual_information

    def calculate_doubtful_measure(self):
        x = 0
        n = len(self.xinyuan)
        for i in range(n):
            if self.xinyuan[i] != 0:
                x += -self.xinyuan[i]*math.log2(self.xinyuan[i])
            else:continue
        y = self.calculate_mutual_information()
        doubtful_measure = x-y
        return doubtful_measure




xinyuan = [0.1956,0.063,0.0105,0.023,0.035,0.105,0.0225,0.011,0.047,0.029,0.001,0.003,
           0.055,0.021,0.059,0.0654,0.0175,0.001,0.054,0.052,0.072,0.0225,0.008,0.012,
           0.002,0.012,0.001]
"""将信源按照数组类型输入，顺序为从空格到26个字母"""
n = len(xinyuan)
xindao = np.zeros((n,n))
for i in range(n):
    if i == 0:
        xindao[i][i] = 0.9
        xindao[i][n-1-i] = 0.1
    else:
        xindao[i][i] = 0.9
        xindao[i][i-1] = 0.1

# x = 信源信道模型(xinyuan,xindao)
# print("噪声熵为：", x.calcuate_noise_enrtopy(), "\n")
# print("疑义度为",x.calculate_doubtful_measure(), '\n')
# print('互信息为：',x.calculate_mutual_information(), '\n')
