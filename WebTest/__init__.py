# encoding=utf-8
# coding=gbk
import Txt, NumWord, JieBa
import sys, re, math


# 将各类新闻整合在一起
def first():
    print "first"
    reload(sys)
    sys.setdefaultencoding('gbk')
    clas = ["财经", "互联网", "健康", "教育", "军事", "旅游", "体育", "文化", "招聘"]
    for classs in clas:
        txtall = ""
        for n in range(10, 1611):
            try:
                txtall = txtall + Txt.readgbkall(
                    ("/home/yida/Desktop/新闻语料库/" + classs + "/" + str(n) + ".txt"))
            except:
                print "读取 " + classs + str(n) + " 出错,换用读取格式"
                try:
                    txtall = txtall + Txt.readgb18030all(
                        ("/home/yida/Desktop/新闻语料库/" + classs + "/" + str(n) + ".txt"))
                except:
                    print "读取 " + classs + str(n) + " 出错,换用读取格式"
                    try:
                        txtall = txtall + Txt.readutfall(
                            ("/home/yida/Desktop/新闻语料库/" + classs + "/" + str(n) + ".txt"))
                    except:
                        print "读取 " + classs + str(n) + " 出错"
                        Txt.writeall('a', "/home/yida/Desktop/测试集/读取错误.txt",
                                     "first " + classs + " " + str(n) + ".txt\n")
                print "成功"
        # print txtall
        try:
            Txt.writeall('w', "/home/yida/Desktop/测试集/" + classs + "/" + classs + ".txt", txtall)
        except:
            print "写入出错" + classs + str(n)
            Txt.writeall('a', "/home/yida/Desktop/测试集/写入错误.txt", "first " + classs + " " + str(n) + ".txt\n")


# 新闻分词并统计词频
def second():
    print "second"
    reload(sys)
    sys.setdefaultencoding('gbk')
    clas = ["财经", "互联网", "健康", "教育", "军事", "旅游", "体育", "文化", "招聘"]
    for classs in clas:
        txtall = ""
        try:
            txtall = txtall + Txt.readutfall(
                ("/home/yida/Desktop/测试集/" + classs + "/" + classs + ".txt"))
        except:
            print "读取 " + classs + " 出错"
            Txt.writeall('a', "/home/yida/Desktop/测试集/读取错误.txt", "second " + classs + ".txt\n")
        # 分词
        wordall = JieBa.particple(txtall)
        # 统计词频
        claswordnum = NumWord.claswordnum(wordall)

        # print str(claswordnum.get('涉'))

        # 写入
        try:
            Txt.writedict('w', "/home/yida/Desktop/测试集/" + classs + "/" + classs + "词频.txt", claswordnum)
        except:
            print "写入出错" + classs
            Txt.writeall('a', "/home/yida/Desktop/测试集/写入错误.txt", "second " + classs + "词频.txt\n")


# 整合得到总词频
def third():
    print "third"
    clas = ["财经", "互联网", "健康", "教育", "军事", "旅游", "体育", "文化", "招聘"]
    tatollwordnum = dict()
    for classs in clas:
        txtall = ""
        try:
            file = open(("/home/yida/Desktop/测试集/" + classs + "/" + classs + "词频.txt"), 'r')
            line = file.readline()
            patterm = re.compile("(.+?)\\\(\d+)")
            while line:
                match = patterm.search(line)
                if match:
                    if match.group(1) != "":
                        if tatollwordnum.get(match.group(1)):
                            tatollwordnum[match.group(1)] = tatollwordnum.get(match.group(1)) + int(match.group(2))
                        else:
                            tatollwordnum[match.group(1)] = int(match.group(2))
                            # else:
                            #     print "1111"
                # else:
                #     print "没有match"
                #     print line
                #     print "############"
                line = file.readline()
            file.closed
        except:
            print "读取出错" + classs + "词频.txt"
            Txt.writeall('a', "/home/yida/Desktop/测试集/读取错误.txt", "third " + classs + "词频.txt\n")
    # 写入
    try:
        Txt.writedict('w', "/home/yida/Desktop/测试集/总词频.txt", tatollwordnum)
    except:
        print "写入出错" + classs
        Txt.writeall('a', "/home/yida/Desktop/测试集/写入错误.txt", "third " + classs + "词频.txt\n")

        # print "######"
        # if tatollwordnum.get('百货店') != None:
        #     print str(tatollwordnum.get('百货店'))
        # else:
        #     print "0"


# TF-DIF
def fourth():
    print "fourth"
    clas = ["财经", "互联网", "健康", "教育", "军事", "旅游", "体育", "文化", "招聘"]
    claswn = [dict() for i in clas]
    taltollwm = dict()
    # 各类词频
    for i in range(len(clas)):
        try:
            file = open(("/home/yida/Desktop/测试集/" + clas[i] + "/" + clas[i] + "词频.txt"), 'r')
            line = file.readline()
            patterm = re.compile("(.+?)\\\(\d+)")
            while line:
                match = patterm.search(line)
                if match:
                    if match.group(1) != "":
                        if claswn[i].get(match.group(1)):
                            # print str(i) + "you" + classs + match.group(1) + str(claswn[i].get(match.group(1)))
                            break;
                        else:
                            claswn[i][match.group(1)] = int(match.group(2))
                # else:
                #     print "没有match,换行符"
                line = file.readline()
            file.closed
        except:
            print "读取出错" + classs + ".txt"
            Txt.writeall('a', "/home/yida/Desktop/测试集/读取错误.txt", "fourth " + clas[i] + "词频.txt\n")
            # if claswn[i].get('百货店') != None:
            #     print str(claswn[i].get('百货店'))
            # else:
            #     print "0"

    # 总词频
    try:
        file = open(("/home/yida/Desktop/测试集/总词频.txt"), 'r')
        line = file.readline()
        patterm = re.compile("(.+?)\\\(\d+)")
        while line:
            # print line
            match = patterm.search(line)
            if match:
                if match.group(1) != "":
                    if taltollwm.get(match.group(1)):
                        print"######"
                        break;
                    else:
                        taltollwm[match.group(1)] = int(match.group(2))
            else:
                print "没有match,换行符"
            line = file.readline()
        file.closed
    except:
        print "读取出错,总词频.txt"
        Txt.writeall('a', "/home/yida/Desktop/测试集/读取错误.txt", "fourth " + "总词频.txt\n")
    # print taltollwm["百货店"]

    # dfj = 词项j的新闻类频率= 包含词项j的新闻类数量
    dif = dict()
    for word, num in taltollwm.items():
        for j in range(len(clas)):
            if claswn[j].get(word):
                if dif.get(word):
                    dif[word] = dif.get(word) + 1
                else:
                    dif[word] = 1

    # print dif.get('百货店')
    # print "**************"

    # idfj = 词项j的反新闻类频率= log2 (N/ dfj)

    idfi = [dict() for i in clas]
    N = len(clas)
    for i in range(len(clas)):
        # idfi = dict()
        for word, num in claswn[i].items():
            # print  float(N)
            idfi[i][word] = float(math.log(float(N) / float(dif.get(word)), 10))

    # print idfi[0].get('百货店')

    taltolltrainingset = dict()
    for i in range(len(clas)):
        trainingset = dict()
        for word, num in idfi[i].items():
            if num > 0.6:
                patterm = re.compile("(\d+)")
                match = patterm.search(word)
                if match:
                    continue
                else:
                    trainingset[word] = claswn[i].get(word)
                    if taltolltrainingset.get(word):
                        taltolltrainingset[word] = taltolltrainingset[word] + int(claswn[i].get(word))
                    else:
                        taltolltrainingset[word] = int(claswn[i].get(word))

        Txt.writedict('w', "/home/yida/Desktop/测试集/" + clas[i] + "/" + clas[i] + "训练集.txt", trainingset)
        # print trainingset.get("百货店")
    Txt.writedict('w', "/home/yida/Desktop/测试集/总训练集.txt", taltolltrainingset)
    # print taltolltrainingset.get("百货店")


def fifth():
    print "fifth"
    clas = ["财经", "互联网", "健康", "教育", "军事", "旅游", "体育", "文化", "招聘"]
    trainingset = [dict() for i in clas]
    taltollclasswm = [int() for i in clas]
    taltolltrainingset = dict()
    taltallwm = 0
    # 各类训练集
    for i in range(len(clas)):
        try:
            file = open(("/home/yida/Desktop/测试集/" + clas[i] + "/" + clas[i] + "训练集.txt"), 'r')
            line = file.readline()
            patterm = re.compile("(.+?)\\\(\d+)")
            while line:
                match = patterm.search(line)
                if match:
                    if match.group(1) != "":
                        if trainingset[i].get(match.group(1)):
                            print str(i) + "you" + classs + match.group(1) + str(claswn[i].get(match.group(1)))
                            break;
                        else:
                            trainingset[i][match.group(1)] = int(match.group(2))
                            taltollclasswm[i] = taltollclasswm[i] + int(match.group(2))
                            taltallwm = taltallwm + int(match.group(2))
                # else:
                #     print "没有match,换行符"
                line = file.readline()
            file.closed
        except:
            # print "读取出错" + clas[i] + ".txt"
            Txt.writeall('a', "/home/yida/Desktop/测试集/读取错误.txt", "fifth " + clas[i] + "词频.txt\n")

    # 总训练集
    try:
        file = open(("/home/yida/Desktop/测试集/总训练集.txt"), 'r')
        line = file.readline()
        patterm = re.compile("(.+?)\\\(\d+)")
        while line:
            # print line
            match = patterm.search(line)
            if match:
                if match.group(1) != "":
                    if taltolltrainingset.get(match.group(1)):
                        print"######3"
                        break;
                    else:
                        taltolltrainingset[match.group(1)] = int(match.group(2))
            else:
                print "没有match,换行符"
            line = file.readline()
        file.closed
    except:
        # print "读取出错,总词频.txt"
        Txt.writeall('a', "/home/yida/Desktop/测试集/读取错误.txt", "fifth " + "总训练集.txt\n")

    # for i in range(len(clas)):
    #     print trainingset[i].get("艺术")
    # print taltolltrainingset.get("艺术")



    tatollcorret = 0.0
    tatollnum = 0.0
    for classnum in range(len(clas)):
        corret = 0.0
        number = 0.0
        classs = clas[classnum]
        for j in range(1611, 1991):
            n = j
            try:
                testall = Txt.readgbkall(
                    ("/home/yida/Desktop/新闻语料库/" + classs + "/" + str(n) + ".txt"))
            except:
                # print "读取 " + classs + str(n) + " 出错,换用读取格式"
                try:
                    testall = Txt.readgb18030all(
                        ("/home/yida/Desktop/新闻语料库/" + classs + "/" + str(n) + ".txt"))
                except:
                    # print "读取 " + classs + str(n) + " 出错,换用读取格式"
                    try:
                        testall = Txt.readutfall(
                            ("/home/yida/Desktop/新闻语料库/" + classs + "/" + str(n) + ".txt"))
                    except:
                        # print "读取 " + classs + str(n) + " 出错"
                        Txt.writeall('a', "/home/yida/Desktop/测试集/读取错误.txt",
                                     "first " + classs + " " + str(n) + ".txt\n")
                        # print "成功"
            # print testall
            # number = 0
            # for i in range(len(clas)):
            #     print taltollclasswm[i]
            #     number = number + taltollclasswm[i]
            # print taltallwm
            # print number
            # 分词
            testwordall = JieBa.particple(testall)
            # 统计词频
            testwordnum = NumWord.claswordnum(testwordall)

            classspossbile = -1
            N = float(9)
            Num = float(taltallwm)
            tempPAB = 0.0
            for i in range(len(clas)):
                PAB = 1
                for word, num in testwordnum.items():
                    # print trainingset[i].get(word)
                    # print word
                    B = float(taltollclasswm[i])
                    if trainingset[i].get(word) != None:
                        A = float(trainingset[i].get(word))
                        if taltolltrainingset.get(word) != None:
                            C = float(taltolltrainingset.get(word))
                            PAB = PAB * ((A / B) * (1 / N)) / ((C / Num))
                            # PAB = PAB * Num / B
                            # print str(PAB) +" "+ str(tempPAB)
                if tempPAB < PAB:
                    tempPAB = PAB
                    classspossbile = i
            # print str(PAB) + " " + str(tempPAB)
            #     print str(i)+ " "+ str(classspossbile)
            # print clas[classspossbile]
            Txt.writeall('a', "/home/yida/Desktop/测试集/分类/" + clas[classnum] + "分类.txt",
                         (str(n) + ".txt " + clas[classspossbile] + "\n"))
            if clas[classspossbile] == clas[classnum]:
                corret = corret + 1.0
                tatollcorret = tatollcorret + 1.0
            number = number + 1.0
            tatollnum = tatollnum + 1.0
        print clas[classnum] + " " + str(corret / number)
    print str(tatollcorret / tatollnum)
    # print corret
    # print tatollnum



    # trainingset = [dict() for i in clas]
    # taltollclasswm = [int() for i in clas]
    # taltolltrainingset = dict()
    # taltallwm = 0




    # 1.16992500144


    # tfij = 词项j在新闻类i中的频率


    #
    # N = 9


# first()
# second()
# third()
fourth()
fifth()
