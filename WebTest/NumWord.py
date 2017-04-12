# encoding=utf-8
def claswordnum(string):
    # print "词频统计"
    claswordnum = dict()
    wordall = string.split('\\')
    for value in wordall:
        if claswordnum.get(value):
            claswordnum[value] = claswordnum.get(value) + 1
        else:
            claswordnum[value] = 1
    return claswordnum
