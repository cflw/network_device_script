import time
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 时间 as 北向时间
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 时间 as 南向时间
def f解析时间ev6(a文本):
	#09:17:30 UTC Tue Jul 09 2019
	v文本 = 字符串.f去词(a文本, 1)
	return time.strptime(v文本, "%H:%M:%S %a %b %d %Y")
class C时间ev6(模式.C同级模式, 南向时间.I时间配置):
	"""适用于: 盛科e580(v6.x), 浪潮cn61108pcvh(v6.x), 浪潮s5350(v6.x)"""
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
