import time
from ..基础接口 import 时间 as 北向时间
from ..命令行接口 import 时间 as 南向时间
from ..命令行接口 import 模式
from ..命令行接口 import 命令
class C时间(模式.C同级模式, 南向时间.I时间配置):
	def __init__(self, a):
		南向时间.I时间配置.__init__(self, a)
	def fs日期时间(self, a日期时间):
		v时间 = 北向时间.f解析日期时间(a日期时间)
		v命令 = 命令.C命令("clock datetime")
		v命令 += time.strftime("%H:%M:%S %Y-%m-%d", v时间)
		self.m设备.f执行命令(v命令)
	def fs时区(self, a时区):
		v时区 = 北向时间.f解析时区(a时区)
		v时区名, v符号, v时, v分 = 北向时间.f拆分时区(v时区)
		v命令 = 命令.C命令("clock timezone")
		v命令 += v时区名
		v命令 += "add" if v符号 else "minus"
		v命令 += v时
		if v分:
			v命令 -= f":{v分}"
		self.m设备.f执行命令(v命令)