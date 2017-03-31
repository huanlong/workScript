import os
f = open("d:\\userID\\AllID1.txt")             # 返回一个文件对象 
line = f.readline()             # 调用文件的 readline()方法
Num = 0
while line: 
	Num = Num + 1
	Numa = str(Num)
	line = str(line)
	line = line.strip()  #去掉换行符
	userID = line.split(',')[0]
	bookID = line.split(',')[1]
	# print("U=",userID)
	# print("B=",bookID)
	userIdName = Numa + '_' + userID
	bookIdName = Numa + '_' + bookID
	userIdPath = r'D:/userID/userID/'
	bookIdPath = r'D:/userID/bookID/'
	userIdFull_path=userIdPath + userIdName
	bookIdFull_path=bookIdPath + bookIdName
	print("userIdFull_path>>>",userIdFull_path)
	print("bookIdFull_path>>>",bookIdFull_path)
	userfile = open(userIdFull_path,'w')
	bookfile = open(bookIdFull_path,'w')
	userfile.close()
	bookfile.close()
	line = f.readline()
f.close()