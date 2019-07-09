#!/usr/bin/env python
#coding:utf-8
####################################################
#Read.me update_md5.py
#脚本功能:更新版本数据库中版本库相关系统的MD5
#如何使用: 
#2,执行：python update_md5.py
####################################################


#from __future__ import unicode_literals
import sys
import mysql.connector
import os
import subprocess
import commands
import logging
from logging import handlers

class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }#日志级别关系映射

    def __init__(self,filename,level='info',when='D',backCount=10,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往屏幕上输出
        sh.setFormatter(format_str) #设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,interval=3,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.suffix = "%Y-%m-%d_%H-%M-%S.log"
        th.setFormatter(format_str)#设置文件里写入的格式
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)




config = {
        'user':'django',
        'password':'django',
        'host':'172.18.1.204',
        'port':'3306',
        'database':'jzsec_bbs',
        'raise_on_warnings':True,
    }


def exe_sql(sql,*val):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

def query_mysql(sql,*val):

	conn = mysql.connector.connect(**config)
	cursor = conn.cursor()
	cursor.execute(sql)
	results = cursor.fetchall()
	return results


def main(*val):
	#更新版本库ver_repostory，md5字段
	log = Logger('logs/update_md5.log',level='info')
	log.logger.info(u"开始更新版本库ver_repostory，md5字段")
	sql1 = "select id,process_path from ver_repostory"
	results1 = query_mysql(sql1)
	for line in results1:
		#print(line)
		id = line[0]
		path = line[1]
		process_path = path.encode("utf-8")
		#print(type(process_path))
		#md5 = os.system("python getmd5.py %s" %(process_path))
		(status, md5) = commands.getstatusoutput("python getmd5.py %s" %(process_path))
		print(status,md5,len(md5))
		exesql = "update ver_repostory set md5 = "+ "'"+md5+"'" +" where id ="+ str(id) 
		exesql_err= u"update ver_repostory set md5 = '无效md5,请查看原因！' where id ="+ str(id) 
		log.logger.info(exesql)
		try:
			exe_sql(exesql)	
		except Exception as err:
			log.logger.error(err)
			exe_sql(exesql_err)
	log.logger.info(u"更新版本库ver_repostory，md5字段完成")
	#更新服务器各系统ser_version，md5字段

	log.logger.info(u"开始更新版本库ver_repostory，md5字段")
	sql2 = "select id,ser_ip,process_path from ser_version"
	results2 = query_mysql(sql2)
	for line in results2:
		#print(line)
		id = line[0]
		ser_ip = line[1].encode("utf-8")
		print(type(ser_ip))
		#ser_ip = "10.1.177.8"
		path = line[2]
		process_path = path.encode("utf-8")
		print(process_path)
		#md5 = os.system("python getmd5.py %s" %(process_path))
		(status, md5) = commands.getstatusoutput("ansible %s -m shell -a 'cd /tmp/md5 && python getmd5.py %s' | awk '{if (NR>1){print $1}}'" %(ser_ip,process_path))
		print(status,md5,len(md5))
		exesql = "update ser_version set md5 = "+ "'"+md5+"'" +" where id ="+ str(id) 
		exesql_err = u"update ser_version set md5 = '无效md5,请查看原因！' where id ="+ str(id)
		if len(md5) != 32:
			exesql = exesql_err 
		log.logger.info(exesql)
		try:
			exe_sql(exesql)
			#pass	
		except Exception as err:
			log.logger.error(err)
			exe_sql(exesql_err)
	log.logger.info(u"更新版本库ser_version，md5字段完成")
if __name__ == "__main__":
	main()
