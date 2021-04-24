import time
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 时间
from ..命令行接口 import 命令
from ..命令行接口 import 模式
def f解析时间sv3(a文本):
	#Clock display mode   :  default
	#Current system time  :  2000-02-11,03:03:05.678
	#Timezone offset      : +08:00-CCT
	v文本 = 字符串.f提取字符串之间(a文本, "Current system time  :  ", "\n", a结束严谨 = False)
	return time.strptime(v文本, "%Y-%m-%d,%H:%M:%S.%f")
class C时间显示sv3(时间.I时间显示, 模式.I显示模式):
	"""适用于: 浪潮s6550(v3.x)"""
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	def f显示_时间(self):
		v输出 = self.m设备.f执行显示命令("show clock")
		return f解析时间sv3(v输出)
class C时间sv3(模式.C同级模式, 时间.I时间配置):
	"""适用于: 浪潮s6550(v3.x)"""
	def __init__(self, a):
		模式.C同级模式.__init__(self, a)
	def fs日期时间(self, a日期时间):
		v时间 = 时间.f解析日期时间(a日期时间)
		v时间文本 = time.strftime("%H %M %S %Y %m %d", v时间)
		v命令 = "clock set " + v时间文本
		self.f执行当前模式命令(v命令)
	def fs时区(self, a时区):
		v时区 = 时间.f解析时区(a时区)
		v时区名, v符号, v时, v分 = 时间.f拆分时区(v时区)
		v命令 = 命令.C命令("clock timezone")
		v命令 += "+" if v符号 else "-"
		v命令 -= v时
		v命令 += v分
		v命令 += v时区名
		self.f执行当前模式命令(v命令)
