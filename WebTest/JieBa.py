#encoding=utf-8
#coding=gbk

def particple(string):
    # print "JieBa分词"
    import jieba
    seg_list = jieba.cut(string)
    wordall = "\\".join(seg_list).encode("utf8")
    # print wordall
    return wordall