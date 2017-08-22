# coding:utf-8

import sys

from matplotlib import pyplot as plt 
import random
import matplotlib

#设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']   
plt.rcParams['font.family']='sans-serif' 
plt.rcParams['axes.unicode_minus'] = False


# 随机生成RGB颜色
def random_color():
    l = ["1","2","3","4",'5','6','7','8','9','0','A','B','C','D','E','F']
    slice = random.sample(l, 6)
    return "#"+"".join(slice)

# 生成图片
def make_pic(file_in, types):
    f = open(file_in)
    lines = f.readlines()
    m = {}
    for i in lines:
        i = i.strip()[1:-1]
        cols = i.split(",")
        m[cols[0]] = cols[1]

    plt.figure(figsize=(18,12))
    labels = m.keys()
    sizes = m.values()
    colors = []
    for i in range(len(m)):
        colors.append(random_color())
   
    patches,l_text,p_text = plt.pie(sizes,labels=labels,colors=colors,
				    labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
				    startangle = 90,pctdistance = 0.6)

    for t in l_text:
	t.set_size=10
    for t in p_text:
	t.set_size=10
    plt.axis('equal')
    plt.legend()
    if types=="1":
        plt.title(u"点击率最高的网站top10",{'fontsize':18,'fontweight':50}) 
        plt.savefig('images/web_click_most.png', format='png')
    elif types=="2":
        plt.title(u"返回结果排名为1的网站top10",{'fontsize':18,'fontweight':50}) 
        plt.savefig('images/rank_1_top10.png', format='png')
    elif types=="3":
        plt.title(u"点击顺序为1的网站top10",{'fontsize':18,'fontweight':50}) 
        plt.savefig('images/sequence_1_top10.png', format='png')
    else:
        print 'input is wrong'


if __name__ == '__main__':

    file_in = sys.argv[1]
    types = sys.argv[2]

    make_pic(file_in,types)

