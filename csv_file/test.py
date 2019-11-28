import csv

# 文件头，一般就是数据名
fileHeader = ["name", "score"]
# 假设我们要写入的是以下两行数据
d1 = ["老王", "100"]
d2 = ["小李", "80"]
# 写入数据
csvFile = open("./your.csv", "w")
writer = csv.writer(csvFile)
# 写入的内容都是以列表的形式传入函数
writer.writerow(fileHeader)
writer.writerow(d1)
writer.writerow(d1)
csvFile.close()
