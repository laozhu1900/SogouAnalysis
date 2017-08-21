# coding:utf-8

import sys

from matplotlib import pyplot as plt 
import random

def random_color():
    l = ["1","2","3","4",'5','6','7','8','9','0','A','B','C','D','E','F']
    slice = random.sample(l, 6)
    return "#"+"".join(slice)

def make_pic(file_in, file_out):
    f = open(file_in)
    lines = f.readlines()
    m = {}
    for i in lines:
        i = i.strip()[1:-1]
        cols = i.split(",")
        m[cols[0]] = cols[1]

    plt.figure(figsize=(18,9))
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

    plt.title("most clicks website top10") 
    plt.axis('equal')
    plt.legend()
    plt.savefig('images/web_click_most.png', format='png')


if __name__ == '__main__':

    file_in = sys.argv[1]
    file_out = sys.argv[2]

    make_pic(file_in, file_out)

