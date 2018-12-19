import better_exceptions
import platform
import time
import os
import socket
import zmail
from PIL import ImageGrab

emailName = '*****@sina.com'
password = '*******'

report_subject = '周报'
report_contents = '各位领导，周五晚上好！'
report_path = '周报路径'
report_savePath = '保存路径'
#周报发送对象
report_mail = ['yanghou1991@sina.cn']
#周报cc对象
report_cc_mail = ['xx@mvtech.cc', 'xx@mvtech.cc', 'tony@mvtech.cc']


def getIP():
	ip = socket.gethostbyname(socket.gethostname())
	return ip


def getSystemVersion():
	return platform.platform()


def sendInformation(ip, systemVersion):
	info = 'ip:' + ip + "  " + 'system version:' + systemVersion
	print(info)
	mail_content = {
		'subject': 'information',
		'content_text': info
	}

	server = zmail.server(emailName, password)
	server.send_mail(emailName, mail_content)


def sendReport():
	mail_content = {
		'subject': report_subject,
		'content_text': report_contents,
		'attachments': report_path
	}

	server = zmail.server(emailName, password)
	server.send_mail(report_mail, mail_content, cc=report_cc_mail)


def saveReport():
	server = zmail.server(emailName, password)
	mail = server.get_latest()
	zmail.save_attachment(mail, report_savePath, overwrite=True)


def writeReport():
	mail_content = {
		'subject': report_subject,
		'attachments': report_path
	}

	server = zmail.server(emailName, password)
	server.send_mail(emailName, mail_content)


def getInformation():
	server = zmail.server(emailName, password)
	mail = server.get_latest()
	subject = mail['subject']
	return subject


if __name__ == '__main__':
	sendInformation(getIP(), getSystemVersion())
	while 1:
		message = getInformation()
		if message == 'send':
			sendReport()
		elif message == 'save':
			saveReport()
		elif message == 'write':
			writeReport()
