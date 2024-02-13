from fuzzywuzzy import process


def list_status():
    with open("./equipmentInfo", "r") as file:
        for line in file:
            print(line)


def find_status(s):
    result = []
    with open("./equipmentInfo", "r") as file:
        for line in file:
            if process.extractOne(s, line):  # 判断查询字符串是否在当前行中
                result.append(line.strip())  # 将匹配的行添加到结果列表中
    for each in result:
        print(each)
