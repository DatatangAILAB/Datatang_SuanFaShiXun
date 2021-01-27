# encoding=utf-8
import jieba
import jieba.posseg as pseg


with open(r'/home/zw/work/jiebafenci/cixing/人民日报数据.txt', 'r', encoding='utf-8') as f,open(r'/home/zw/work/jiebafenci/cixing/data.txt','w',encoding = 'utf-8') as g:
    for line in f:
        data = pseg.cut(line.rstrip().strip())
        for word in data:
            g.write(word.word)
            g.write(' /')
            g.write(word.flag+' ')
        g.write('\n')



