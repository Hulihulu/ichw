#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.
__author__ = "Huruihua"
__pkuid__  = "1800011843"
__email__  = "1800011843@pku.edu.cn"
"""

import re,string,sys，collections
from urllib.request import urlopen


def wcount(lines, topn):
#定义单词统计函数

    newlines = ""
    for k in lines:
        if k not in string.punctuation:
            newlines = newlines + k
        else:
            newlines = newlines
    #去除字符串中的标点
    
    words = re.findall(r'\w+', newlines.lower())
    #利用正则表达式查找字符串中的单词，并返回一个列表
    
    answer = collections.Counter(words).most_common(topn)
    #利用collections中的Counter函数，统计列表中出现次数最多的n个单词的出现频次
    #返回值为一个列表
    
    for i in answer:
        print(i[0]+'\t'+str(i[1]))
         #将单词与出现频次用制表位分隔开
            
    pass



if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    if  len(sys.argv) == 2:
        doc = urlopen(sys.argv[1])
        docstr = doc.read().decode('utf-8') 
        doc.close()
        wcount(docstr，10)
        sys.exit(1)
        
    if  len(sys.argv) == 3:
        doc = urlopen(sys.argv[1])
        docstr = doc.read().decode('utf-8')
        doc.close()
        wcount(docstr,topn = int(sys.argv[2]))
        sys.exit(1）
       
