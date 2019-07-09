#!/usr/bin/env python
#coding:utf-8
####################################################
#Read.me getMd5.py
#脚本功能:获取文件或者文件目录的MD5值
#如何使用: 
#1,编辑文本exclude.txt,把要排除的目录和文件按行填写
#2,执行：python getMd5.py "文件目录"
####################################################

import os,sys  
#import md5  
import hashlib  
import socket  
import platform

#定义变量
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname) #获取本机IP，方便命名
#print ip
#读取exclude.txt 获取要排除的选项
exclude = []
read = open("exclude.txt","r")
for line in read.readlines():
	line = line.strip()
	exclude.append(line)
read.close
#print exclude
########################################
#获取字符串的MD5值  
def Get_Md5_Of_String(src):  
    md1 =hashlib.md5()  
    md1.update(src)  
    return md1.hexdigest()   
########################################  
#获取文件的MD5值
def Get_Md5_Of_File(filename):  
    if not os.path.isfile(filename):  
        return  
    myhash = hashlib.md5()  
    f = file(filename,'rb')  
    while True:  
        b = f.read(8096)  
        if not b :  
            break  
        myhash.update(b)  
    f.close()  
    return myhash.hexdigest()  
########################################  
#获取目录的MD5值
def Get_Md5_Of_Folder_win(dir): 
	if basename[-1] == "":
		MD5_URL = ip+"_"+basename[-2]+".md5"
	else:
		MD5_URL = ip+"_"+basename[-1]+".md5"
	basename = dir.split('\\')
	MD5_URL = ip+"_"+basename[-1]+".md5"
	outfile = open(MD5_URL,'w')
	MD5File = basename[-1]+".txt"
	outfile_with_dir = open(MD5File,'w')
    
	#os.walk遍历文件目录，root:当前文件夹目录 subdirs:当前文件加下目录名字 files:文件名称
	for root, subdirs, files in os.walk(dir):
		#print root+"######", subdirs,files
		for file in files:
			#遍历文件，并做选择性排除
			#print file
			if file in exclude:
				pass
			else:
				#for file in files:
				#遍历子目录，并做选择性排除
				#for subdir in subdirs:
				#	if subdir in exclude:
				#		pass
				dirs = root.split('\\')
				#dir = dirs[-1]
				if [dir for dir in dirs if dir in exclude]:
					pass
				else:
					#print root
					filefullpath = os.path.join(root,file)
      				#filerelpath = os.path.relpath(filefullpath,dir)
					#print filerelpath
					md5 = Get_Md5_Of_File(filefullpath)
					#print md5
					outfile.write(filefullpath+" "+md5+"\n" )
					outfile_with_dir.write(md5+"\n" )
	outfile.close() 
	with open(MD5File,'rw') as f:
		md5_sort = open("temp.txt",'w')
    	lines = f.readlines()
    	lines.sort(key=str.lower)
    	for line in lines:
        	md5_sort.write(line)
	md5_sort.close()
	os.remove(MD5_URL)
	return Get_Md5_Of_File("temp.txt")
	#os.remove("tmp.txt")
	
	
def Get_Md5_Of_Folder_lin(dir): 
	basename = dir.split('/')
	if basename[-1] == "":
		MD5_URL = ip+"_"+basename[-2]+".md5"
 	else:
		MD5_URL = ip+"_"+basename[-1]+".md5"
	outfile = open(MD5_URL,'w')
	MD5File = basename[-1]+".txt"
	outfile_with_dir = open(MD5File,'w')
	#os.walk遍历文件目录，root:当前文件夹目录 subdirs:当前文件加下目录名字 files:文件名称
	for root, subdirs, files in os.walk(dir):
		#print root+"######", subdirs,"**********",files
		for file in files:
			#遍历文件，并做选择性排除
			#print file
			if file in exclude:
				pass
			else:
				#for file in files:
				#遍历子目录，并做选择性排除
				#for subdir in subdirs:
				#	if subdir in exclude:
				#		pass
				dirs = root.split('/')
				#dir = dirs[-1]
				if [dir for dir in dirs if dir in exclude]:
					pass
				else:
					#print root
					filefullpath = os.path.join(root,file)
      				#filerelpath = os.path.relpath(filefullpath,dir)
					#print filefullpath
					md5 = Get_Md5_Of_File(filefullpath)
					#print md5
					outfile.write(file+" "+md5+"\n" )
					outfile_with_dir.write(md5+"\n" )
	outfile.close() 
	outfile_with_dir.close()
	
	with open(MD5File,'rw') as f:
		md5_sort = open("temp.txt",'w')
		lines = f.readlines()
    	lines.sort(key=str.lower)
    	for line in lines:
        	md5_sort.write(line)
	md5_sort.close()
	#os.remove(MD5File)
	return Get_Md5_Of_File("temp.txt")	
	#os.remove("tmp.txt")
########################################  
  
  
########################################  
#Get_Md5_Of_String("abc")  
#print Get_Md5_Of_File("1.txt")  
#print "###################################"  
#print Get_Md5_Of_Folder("/data/")
sysstr = platform.system()
if(sysstr =="Windows"):
	print Get_Md5_Of_Folder_win(sys.argv[1])
elif(sysstr == "Linux"):
	print Get_Md5_Of_Folder_lin(sys.argv[1])
else:
	pass
   
#print Get_Md5_Of_File("ela_index_delete.sh")
