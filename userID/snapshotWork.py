from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
import os
import shutil

print("ConnectPhone")
device = MonkeyRunner.waitForConnection()

Num = 0
rootPath = 'F:\Work\workScript\userID'
userfilepath = str(rootPath + '\\userID')
bookfilepath = str(rootPath + '\\bookID')

if os.path.exists(str(rootPath) + '\\Log'):
	print(str(rootPath) + '\\Log' + "file is exist")
else:
	os.mkdir(str(rootPath) + '\\Log')

if os.path.exists(str(rootPath) + '\\Success'):
	print(str(rootPath) + '\\Success' + "file is exist")
else:
	os.mkdir(str(rootPath) + '\\Success')

def start():
	device.shell('am force-stop com.itangyuan')
	MonkeyRunner.sleep(1)
	componentName = 'com.itangyuan/.module.portlet.FlashActivity'
	device.startActivity(component=componentName)
	MonkeyRunner.sleep(10)
	print("startapp")
	MonkeyRunner.sleep(2)
	device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
	#print("1")
	MonkeyRunner.sleep(3)
	device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
	#print("2")
	MonkeyRunner.sleep(3)
	device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
	#print("3")
	print("closeflash")
	MonkeyRunner.sleep(3)
	device.touch(633, 1265, 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	
	result = device.takeSnapshot()
	pic = result.getSubImage((0, 50, 720, 1230))
	MonkeyRunner.sleep(2)	

	resultTruePath = str(rootPath) + '\example\update.png'
	resultTrue=MonkeyRunner.loadImageFromFile(resultTruePath)

	if(pic.sameAs(resultTrue,0.9)):
		print("")
		device.touch(198, 1060, 'DOWN_AND_UP')
	else:
		print("1No")
		MonkeyRunner.sleep(10)
		device.touch(198, 1060, 'DOWN_AND_UP')
		
	print("start_My")
	device.drag((360,300),(360,1000),0.5,3)
	MonkeyRunner.sleep(1)

def exitUser():
	MonkeyRunner.sleep(2)
	device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(1)
	print("My")
	device.touch(633, 1265, 'DOWN_AND_UP')
	MonkeyRunner.sleep(2)
	device.press('KEYCODE_BACK ', 'DOWN_AND_UP')	
	print("openMore")
	device.drag((360,1000),(360,300),0.5,3)
	MonkeyRunner.sleep(2)
	device.touch(300, 1130, 'DOWN_AND_UP')
	MonkeyRunner.sleep(1)
	print("exitUser")
	device.drag((360,1000),(360,300),0.5,3)
	MonkeyRunner.sleep(3)
	device.touch(300, 1200, 'DOWN_AND_UP')
	print("=========================reStart=========================")
	MonkeyRunner.sleep(4)
	device.press('KEYCODE_BACK ', 'DOWN_AND_UP')	
	MonkeyRunner.sleep(2)
	device.drag((360,300),(360,1000),0.5,3)
	MonkeyRunner.sleep(2)
	device.drag((360,300),(360,1000),0.5,3)
	Num = 0

while True: 
	for userID in os.listdir(userfilepath):
		Num = 0
		userIDA = userID.split('_')[1]
		userIDA = str(userIDA)
		print("userID==========", userID)
		#print("userIDA==========",userIDA)
		userIDPath = userfilepath + "\\" + userID
		fulluserIDpath = str(userIDPath)

		#================= 1 ==================================
		device.touch(323, 298, 'DOWN_AND_UP')
		MonkeyRunner.sleep(2)
		try:
			device.type(userIDA)
		except:
			print("")
		MonkeyRunner.sleep(1)
		device.touch(324, 760, 'DOWN_AND_UP')
		MonkeyRunner.sleep(20)
		device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(4)
		
		Num = Num + 1
		print("Num==", Num)
		Numa = str(Num)
		print("snapshotOne")
		result = device.takeSnapshot()
		pic = result.getSubImage((0, 50, 720, 1230))
		MonkeyRunner.sleep(2)
		
		saveSnapshotPath = rootPath + '\\snapshotUser\\' + userID
		saveSnapshotPath = str(saveSnapshotPath)

		print("saveSnapshotPath===", saveSnapshotPath)
		if os.path.exists(saveSnapshotPath):
			print("file is exist")
		else:
			os.mkdir(saveSnapshotPath)
		#save onePic
		resultTruePath = str(rootPath) + "\\example\\1.png"
		print('resultTruePath===', resultTruePath)
		resultTrue = MonkeyRunner.loadImageFromFile(resultTruePath)
		
		if(pic.sameAs(resultTrue,0.8)):
			print("1YES")
			logPath = str(rootPath) + '\\Log\\log.txt'
			log = open(logPath, "a")
			log.write("1YES"+"\n")
			log.close()
			WritePath = saveSnapshotPath + '\\' + Numa + '_' + userIDA + '.png'
			pic.writeToFile(WritePath, "png")
		else:
			print("1No")
			logPath = str(rootPath) + '\\Log\\log.txt'
			log = open(logPath, "a")
			log.write("1No"+"\n")
			log.close()
			start()	
			Num = 0
			exitUser()
			break

		#================= 2 ==================================
		device.touch(350, 350, 'DOWN_AND_UP')
		MonkeyRunner.sleep(10)
		Num = Num + 1
		print("Num==", Num)
		Numa = str(Num)
		print("snapshotTwo")
		result = device.takeSnapshot()
		pic = result.getSubImage((0, 50, 720, 1230))
		MonkeyRunner.sleep(2)
		#save twoPic
		resultTruePath = str(rootPath) + "\\example\\2.png"
		resultTrue=MonkeyRunner.loadImageFromFile(resultTruePath)
		
		if(pic.sameAs(resultTrue,0.1)):
			print("2YES")
			logPath = str(rootPath) + '\\Log\\log.txt'
			log = open(logPath, "a")
			log.write("2YES"+"\n")
			log.close()
			WritePath = saveSnapshotPath + '\\' + Numa + '_' + userIDA + '.png'
			pic.writeToFile(WritePath, "png")
			MonkeyRunner.sleep(1)
			device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
			MonkeyRunner.sleep(2)
		else:
			print("2No")
			logPath = str(rootPath) + '\\Log\\log.txt'
			log = open(logPath, "a")
			log.write("2No"+"\n")
			log.close()
			start()
			Num = 0
			exitUser()
			break
		
		#================= 3 ==================================
		device.touch(620, 500, 'DOWN_AND_UP')
		MonkeyRunner.sleep(5)
		Num = Num + 1
		print("Num==", Num)
		Numa = str(Num)
		print("snapshotThree")
		result = device.takeSnapshot()
		pic = result.getSubImage((0, 50, 720, 1230))
		MonkeyRunner.sleep(2)
		#save threePic
		resultTruePath = str(rootPath) + "\\example\\3.png"
		resultTrue=MonkeyRunner.loadImageFromFile(resultTruePath)
			
		if(pic.sameAs(resultTrue,0.4)):
			print("3YES")
			logPath = str(rootPath) + '\\Log\\log.txt'
			log = open(logPath, "a")
			log.write("3YES"+"\n")
			log.close()
			WritePath = saveSnapshotPath + '\\' + Numa + '_' + userIDA + '.png'
			pic.writeToFile(WritePath, "png")
			MonkeyRunner.sleep(1)
			device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
			MonkeyRunner.sleep(2)
			device.touch(500, 760, 'DOWN_AND_UP')
			MonkeyRunner.sleep(1)
		else:
			print("3No")
			logPath = str(rootPath) + '\\Log\\log.txt'
			log = open(logPath, "a")
			log.write("3No"+"\n")
			log.close()
			start()
			Num = 0
			exitUser()
			break
		
		#================= 4 ==================================
		for bookID in os.listdir(bookfilepath):
			bookIDA = bookID.split('_')[1]
			bookIDA = str(bookIDA)
			print("bookID==========",bookID)
			#print("bookIDA==========",bookIDA)
			bookIDpath = bookfilepath + "/" + bookID
			fullbookIDpath = str(bookIDpath)
		
			device.touch(360, 1215, 'DOWN_AND_UP')
			MonkeyRunner.sleep(10)
			for i in range(20):
				device.drag((690,360),(30,360),0.5,3)
				MonkeyRunner.sleep(1)
			device.touch(135, 95, 'DOWN_AND_UP')
			MonkeyRunner.sleep(1)
			device.touch(135, 95, 'DOWN_AND_UP')
			MonkeyRunner.sleep(20)
			device.type(bookIDA)
			device.touch(220, 780, 'DOWN_AND_UP')
			MonkeyRunner.sleep(1)	
			#shutil.move(fullbookIDpath, r'C:\Users\Work\Desktop\Success')
			break
		Num = Num + 1
		print("Num==", Num)
		Numa = str(Num)
		print("snapshotFour")
		result = device.takeSnapshot()
		pic = result.getSubImage((0, 50, 720, 1230))
		MonkeyRunner.sleep(2)
		#save FourPic
		resultTruePath = str(rootPath) + "\\example\\4.png"
		resultTrue=MonkeyRunner.loadImageFromFile(resultTruePath)
		
		if(pic.sameAs(resultTrue,0.1)):
			print("4YES")
			logPath = str(rootPath) + '\\Log\\log.txt'
			log = open(logPath, "a")
			log.write("4YES"+"\n")
			log.close()
			WritePath = saveSnapshotPath + '\\' + Numa + '_' + userIDA + '.png'
			pic.writeToFile(WritePath, "png")
			MonkeyRunner.sleep(1)
		else:
			print("4No")
			logPath = str(rootPath) + '\\Log\\log.txt'
			log = open(logPath, "a")
			log.write("4No"+"\n")
			log.close()
			start()
			Num = 0
			exitUser()
			break
		
		#================= 5 ==================================
		device.touch(500, 800, 'DOWN_AND_UP')
		MonkeyRunner.sleep(20)
		Num = Num + 1
		print("Num==", Num)
		Numa = str(Num)
		print("snapshotFive")
		result = device.takeSnapshot()
		pic = result.getSubImage((0, 50, 720, 1230))
		MonkeyRunner.sleep(2)
		#save threePic
		resultTruePath = str(rootPath) + "\\example\\5.png"
		resultTrue=MonkeyRunner.loadImageFromFile(resultTruePath)
		
		if(pic.sameAs(resultTrue,0.1)):
			print("5YES")
			logPath = str(rootPath) + '\\Log\\log.txt'
			log = open(logPath, "a")
			log.write("5YES"+"\n")
			log.close()
			WritePath = saveSnapshotPath + '\\' + Numa + '_' + userIDA + '.png'
			pic.writeToFile(WritePath, "png")
			MonkeyRunner.sleep(1)	
			device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
			MonkeyRunner.sleep(2)
		else:
			print("5No")
			logPath = str(rootPath) + '\\Log\\log.txt'
			log = open(logPath, "a")
			log.write("5No"+"\n")
			log.close()
			MonkeyRunner.sleep(150)
			if(pic.sameAs(resultTrue,0.1)):
				print("RE5YES")
				WritePath = saveSnapshotPath + '\\' + Numa + '_' + userIDA + '.png'
				pic.writeToFile(WritePath, "png")
				MonkeyRunner.sleep(1)
				device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
				MonkeyRunner.sleep(2)
			else:
				print("5No")
				MonkeyRunner.sleep(1)
				start()
				Num = 0
				exitUser()
				break
		
		#================= 6 ==================================
		device.touch(390, 685, 'DOWN_AND_UP')
		MonkeyRunner.sleep(10)
		device.touch(530, 890, 'DOWN_AND_UP')
		MonkeyRunner.sleep(25)
		Num = Num + 1
		print("Num==", Num)
		Numa = str(Num)
		print("snapshotSix")
		result = device.takeSnapshot()
		pic = result.getSubImage((0, 50, 720, 1230))
		MonkeyRunner.sleep(2)
		#save SixePic
		resultTruePath = str(rootPath) + "\\example\\6.png"
		resultTrue=MonkeyRunner.loadImageFromFile(resultTruePath)
		
		if(pic.sameAs(resultTrue,0.1)):
			print("6YES")
			logPath = str(rootPath) + '\\Log\\log.txt'
			log = open(logPath, "a")
			log.write("6YES"+"\n")
			log.close()
			WritePath = saveSnapshotPath + '\\' + Numa+ '_' + userIDA + '.png'
			pic.writeToFile(WritePath, "png")
		else:
			print("6No")
			logPath = str(rootPath) + '\\Log\\log.txt'
			log = open(logPath, "a")
			log.write("6No"+"\n")
			log.close()
			MonkeyRunner.sleep(100)
			device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
			MonkeyRunner.sleep(3)
			device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
			MonkeyRunner.sleep(3)
			device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
			MonkeyRunner.sleep(3)
			Num = 0
			exitUser()
			break

		MonkeyRunner.sleep(2)
		device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(2)
		device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(2)
		device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(2)
		
		shutil.move(fullbookIDpath, str(rootPath + '\\Success'))
		shutil.move(fulluserIDpath, str(rootPath + '\\Success'))
		print("MovefulluserIDpath===", str(rootPath + '\\Success'))
		print("fulluserIDpath", fulluserIDpath)
		MonkeyRunner.sleep(2)
		exitUser()