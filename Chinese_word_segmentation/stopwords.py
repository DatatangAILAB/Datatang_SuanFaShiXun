#encoding=utf-8
import jieba
#加载停用词

b = []
a = open(r"cn_stopwords.txt",'rb').read()
text = jieba.cut(a)
for i in text:
     b.append(".join(i)")



