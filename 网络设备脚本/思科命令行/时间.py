import time
import cflw代码库py.cflw时间 as 时间
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 时间 as 时间
from ..命令行接口 import 模式
from ..命令行接口 import 命令
def f解析时间(a文本):
	#由于时区名可以设置成奇怪的名字,为了避免奇怪的问题,解析时过滤掉时区
	#*09:09:36.935 UTC Thu Sep 29 2016
	v文本 = 字符串.f提取字符串之间(a文本, "*" if "*" in a文本 else None, "\n", a结束严谨 = False)
	v文本 = 字符串.f去词(v文本, 1)
	return time.strptime(v文本, "%H:%M:%S.%f %a %b %d %Y")
class C时间显示(时间.I时间显示, 模式.I显示模式):
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	def f显示_时间(self):
		v命令 = "show clock"
		v输出 = self.m设备.f执行显示命令(v命令)
		return f解析时间(v输出)
class C时间(模式.C同级模式, 时间.I时间配置):
	def __init__(self, a):
		模式.C同级模式.__init__(self, a)
	def fs日期时间(self, a日期时间):
		v时间 = 时间.f解析日期时间(a日期时间)
		v时间文本 = time.strftime("%H:%M:%S %b %d %Y", v时间)
		v命令 = "clock set " + v时间文本
		self.m设备.f执行用户命令(v命令)
	def fs时区(self, a时区):
		v时区 = 时间.f解析时区(a时区)
		v时区名, v符号, v时, v分 = 时间.f拆分时区(v时区)
		v命令 = 命令.C命令("clock timezone")
		v命令 += v时区名
		v命令 += "+" if v符号 else "-"
		v命令 -= v时
		if v分:
			v命令 += v分
		self.f执行当前模式命令(v命令)