import os
import subprocess  
import time

num = 0

# def PCL():
	# cmd = 'cmd.exe D:\\userID\\call.bat'  
	# p = subprocess.Popen("cmd.exe /c" + "D:\\userID\\call.bat abc", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	# curline = p.stdout.readline() 
	
	# while(curline != b''):  
		# print(curline)  
		# curline = p.stdout.readline()  
	# p.wait()  
	# print(p.returncode)  

while True:
	num = 0
	log = open(r"D:\userID\Log\log.txt")
	for AAA in log.readlines():
		print("STSRTnum=",num)
		print(AAA)
		if "No" in AAA:
			print("yes=")
			num = num + 1
			print("num=",num)
			if num >= 2:
				clslog = open(r"D:\userID\Log\log.txt","w+")
				clslog.truncate()
				clslog.close()
				log.close()
				num = 0
				time.sleep(1)
				command = 'taskkill /FI "WINDOWTITLE eq C:\Windows\system32\cmd.exe - mo*'
				os.system(command)
				time.sleep(5)
				print("================CLS============")
				os.popen('start monkeyrunner D:\\userID\\new.py')
				print("kill-process")
				break
			else:
				print("goon")
				time.sleep(1)
		else:
			print("no")
			time.sleep(1)