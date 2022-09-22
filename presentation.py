import re
import math
import random

def read_txt(path):
    "读取txt文档"
    f = open(path, 'r',encoding='utf-8')
    txt = str(f.read())
    txt = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。：？、~@#￥%……&*（）]+", "", txt)
    #正则表达式去除符号 替换的方法
    f.close()
    return txt

def spilt_txt(txt,num,direction='right'):
    '进行分割 num为分割的字符数 direction为分割的方向'
    "发现不需要分割的方向了"
    txt_temp =[]
    for i in range(len(txt)):
        if direction == 'right':
            a = txt[i:i+num]
            txt_temp.append(a)
        elif direction == 'left':
            a = txt[i-num:i]
            txt_temp.append(a)
    return txt_temp

def calculate_frequence(txt):
    "计算每个字的概率 返回一个字典"
    'dict :return'
    fre = {}
    num = len(txt)
    for i in txt:
        fre[i] = txt.count(i)/num
    fre = sorted(fre.items(),key=lambda x:x[1],reverse=True)
    return fre

def calculate_mutual_information(fre,fre_basic):
    '计算词的互信息'
    mutual_information = []
    for i in range(len(fre)):
        x=0
        a = 1
        for j in range(len(fre_basic)):
            if fre_basic[j][0] in fre[i][0]:
                a *= fre_basic[j][1]
            else:continue
        if a == 0 : a =1
        else:x = math.log2((fre[i][1])/a)
        mutual_information.append([fre[i][0],x])
        mutual_information = sorted(mutual_information, key=lambda x: x[1], reverse=True)
    return mutual_information


def calculate_conditional_entropy_right(fre,txt):
    "计算单词的右信息熵"
    conditional_entropy = []
    for i in range(len(fre)):
        x = 0
        s = fre[i][0]
        find = re.compile(s + "(\w?)")
        f_list = find.findall(txt)
        dict = {}
        for j in f_list:
            dict[j] = f_list.count(j)/len(f_list)
        for j in dict:
            x += -dict[j]*math.log2(dict[j])
        conditional_entropy.append([fre[i][0],x])
        conditional_entropy = sorted(conditional_entropy, key=lambda x: x[1], reverse=True)
    return conditional_entropy


def calculate_conditional_entropy_left(fre,txt):
    "计算单词的左信息熵"
    conditional_entropy = []
    for i in range(len(fre)):
        x = 0
        s = fre[i][0]
        find = re.compile("(\w?)"+s)
        f_list = find.findall(txt)
        dict = {}
        for j in f_list:
            dict[j] = f_list.count(j)/len(f_list)
        for j in dict:
            x += -dict[j]*math.log2(dict[j])
        conditional_entropy.append([fre[i][0],x])
        conditional_entropy = sorted(conditional_entropy, key=lambda x: x[1], reverse=True)
    return conditional_entropy

def select_new(list,num):
    "对list进行筛选，只选出大于num的值"
    x = []
    for i in range(len(list)):
        if list[i][1] > float(num):
            x.append(list[i])
#不能循环删除自己
        else:continue
    return x

if __name__ == '__main__':
    path = 'bailuyuan.txt'
    txt = read_txt(path)#读取txt
    txt1 = spilt_txt(txt,1)#逐字分割
    fre_basic = calculate_frequence(txt1)#计算每个字的概率
    txt2 = spilt_txt(txt,2)#两个字的分割 要是寻找三个字的词在这里分割为3就可以
    fre2 =calculate_frequence(txt2)#每个两字词的概率
    fre2 = select_new(fre2,0.00412)
    mul_infor_2 = calculate_mutual_information(fre2,fre_basic)#两字词的互信息
    mul_infor_2 = select_new(mul_infor_2,4.5524)#对互信息进行筛选
    cer_2 = calculate_conditional_entropy_right(mul_infor_2,txt)#计算右信息熵
    cer_2 = select_new(cer_2,0.0868)
    cel_2 = calculate_conditional_entropy_left(cer_2,txt)
    cel_2 = select_new(cel_2,0.0780)
    word = []
    for i in range(len(cel_2)):
        word.append(cel_2[i][0])
    print(word)
#期望的输出是
# 二字词：淡黄 长裙 蓬松 头发 展出 油画 感动
#三字词：一场梦 不知火