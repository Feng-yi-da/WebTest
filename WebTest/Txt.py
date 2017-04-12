# encoding=utf-8

def readgbkall(path):
    file = open(path, 'r')
    txtall = file.read().decode("gb2312")
    file.closed
    return txtall

def readgb18030all(path):
    file = open(path, 'r')
    txtall = file.read().decode("gb18030")
    file.closed
    return txtall

def readutfall(path):
    file = open(path, 'r')
    txtall = file.read()
    file.closed
    return txtall

def writeall(style, path, txtall):
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    file = open(path, style)
    file.write(txtall)
    file.closed

def writedict(style, path, dict):
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    file = open(path, style)
    for key, value in dict.items():
        file.write(key + "\\" + str(value) + "\n")
    file.closed

# print(readutfall("/home/yida/Desktop/测试集/财经.txt"))
# print(readgb18030all("/home/yida/Desktop/测试集/财经词频.txt"))
# print(readgbkall("/home/yida/Desktop/测试集/财经词频.txt"))