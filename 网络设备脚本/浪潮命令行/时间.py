import time
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 时间 as 北向时间
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 时间 as 南向时间
def f解析时间sv3(a文本):
	#Clock display mode   :  default
	#Current system time  :  2000-02-11,03:03:05.678
	#Timezone offset      : +08:00-CCT
	v文本 = 字符串.f提取字符串之间(a文本, "Current system time  :  ", "\n", a结束严谨 = False)
	return time.strptime(v文本, "%Y-%m-%d,%H:%M:%S.%f")
def f解析时间cnv6(a文本):
	#09:17:30 UTC Tue Jul 09 2019
	v文本 = 字符串.f去词(a文本, 1)
	return time.strptime(v文本, "%H:%M:%S %a %b %d %Y")
def f解析时间cnv7(a文本):
	#15:12:04.631 UTC Sat Jul 06 2002
	#Time source is NTP
	v文本 = a文本.split("\n")[0]
	v文本 = 字符串.f去词(v文本, 1)
	return time.strptime(v文本, "%H:%M:%S.%f %a %b %d %Y")
class C时间sv3(模式.C同级模式, 南向时间.I时间配置):
	"""适用于: s6550(v3)"""
	def __init__(self, a):
		南向时间.I时间配置.__init__(self, a)
	def fs日期时间(self, a日期时间):
		v时间 = 北向时间.f解析日期时间(a日期时间)
		v时间文本 = time.strftime("%H %M %S %Y %m %d", v时间)
		v命令 = "clock set " + v时间文本
		self.f执行当前模式命令(v命令)
	def fs时区(self, a时区):
		v时区 = 北向时间.f解析时区(a时区)
		v时区名, v符号, v时, v分 = 北向时间.f拆分时区(v时区)
		v命令 = 命令.C命令("clock timezone")
		v命令 += "+" if v符号 else "-"
		v命令 -= v时
		v命令 += v分
		v命令 += v时区名
		self.f执行当前模式命令(v命令)
class C时间cnv6(模式.C同级模式, 南向时间.I时间配置):
	"""适用于: cn6000系列(v6)"""
	def __init__(self, a):
		南向时间.I时间配置.__init__(self, a)
	def fs日期时间(self, a日期时间):
		v时间 = 北向时间.f解析日期时间(a日期时间)
		v时间文本 = time.strftime("%H:%M:%S %m %d %Y", v时间)
		v命令 = "clock set " + v时间文本
		self.f执行当前模式命令(v命令)
	def fs时区(self, a时区):
		v时区 = 北向时间.f解析时区(a时区)
		v时区名, v符号, v时, v分 = 北向时间.f拆分时区(v时区)
		v命令 = 命令.C命令("clock set timezone")
		v命令 += v时区名
		v命令 += "add" if v符号 else "minus"
		v命令 += v时
		if v分:
			v命令 += v分
		self.f执行当前模式命令(v命令)
class C时间cnv7(模式.C同级模式, 南向时间.I时间配置):
	"""适用于: cn8000系列(v7), cn6000系列(v7)"""
	def __init__(self, a):
		南向时间.I时间配置.__init__(self, a)
	def fs日期时间(self, a日期时间):
		v时间 = 北向时间.f解析日期时间(a日期时间)
		v时间文本 = time.strftime("%H %M %S %d %B %Y", v时间)
		v命令 = "clock set " + v时间文本
		self.f执行当前模式命令(v命令)
	def fs时区(self, a时区):
		v时区 = 北向时间.f解析时区(a时区)
		v时区名, v符号, v时, v分 = 北向时间.f拆分时区(v时区)
		v命令 = 命令.C命令("clock timezone")
		v命令 += v时区名
		v命令 += "+" if v符号 else "-"
		v命令 -= v时
		v命令 += v分
		self.f执行当前模式命令(v命令)
	# @staticmethod
	# def f解析显示时间(a文本):
		#15:12:04.631 UTC Sat Jul 06 2002
