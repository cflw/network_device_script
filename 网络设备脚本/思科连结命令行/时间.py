import time
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 时间
from ..命令行接口 import 命令
from ..命令行接口 import 模式
def f解析时间_nv7(a文本):
	#15:12:04.631 UTC Sat Jul 06 2002
	#Time source is NTP
	v文本 = a文本.split("\n")[0]
	v文本 = 字符串.f去词(v文本, 1)
	return time.strptime(v文本, "%H:%M:%S.%f %a %b %d %Y")
class C时间显示_nv7(时间.I时间显示, 模式.I显示模式):
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	def f显示_时间(self):
		v输出 = self.m设备.f执行显示命令("show clock")
		return f解析时间_nv7(v输出)
class C时间_nv7(模式.C同级模式, 时间.I时间配置):
	"""适用于: 思科nexus9000(v7.0), 
	浪潮cn8000系列(v7.3), 浪潮cn61108pcv(v7.0)"""
	def __init__(self, a):
		模式.C同级模式.__init__(self, a)
	def fs日期时间(self, a日期时间):
		v时间 = 时间.f解析日期时间(a日期时间)
		v时间文本 = time.strftime("%H %M %S %d %B %Y", v时间)
		v命令 = "clock set " + v时间文本
		self.f执行当前模式命令(v命令)
	def fs时区(self, a时区):
		v时区 = 时间.f解析时区(a时区)
		v时区名, v符号, v时, v分 = 时间.f拆分时区(v时区)
		if len(v时区名) > 8:
			raise ValueError("时区名太长")
		v命令 = 命令.C命令("clock timezone")
		v命令 += v时区名
		v命令 += "+" if v符号 else "-"
		v命令 -= v时
		v命令 += v分
		self.f执行当前模式命令(v命令)