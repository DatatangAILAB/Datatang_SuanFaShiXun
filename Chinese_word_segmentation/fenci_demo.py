# encoding=utf-8
import jieba

with open(r'/home/zw/work/jiebafenci/fenci/人民日报数据.txt', 'r', encoding='utf-8') as f,open(r'/home/zw/work/jiebafenci/fenci/data.txt','w',encoding = 'utf-8') as g:
    for line in f:
        words = '/ '.join(jieba.cut(line)) 
        g.write(words)




