import time
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 时间
from ..命令行接口 import 模式
from ..命令行接口 import 命令
#===============================================================================
# 信息
#===============================================================================
def f解析时间(a文本: str):
	"""display clock
	适用于: 华为s5700(v5.110)"""
	#2021-02-27 19:15:56-08:00
	#Saturday
	#Time Zone(China-Standard-Time) : UTC-08:00
	v时间s = a文本.split("\n")[0]
	v时区位置 = 字符串.f连续找最后(v时间s, ":", "-")
	if v时区位置 > 0:
		v时间s = v时间s[:v时区位置]
	v时间 = time.strptime(v时间s, "%Y-%m-%d %H:%M:%S")
	return v时间
#===============================================================================
# 模式
#===============================================================================
class C时间显示(时间.I时间显示, 模式.I显示模式):
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	def f显示_时间(self):
		v命令 = "display clock"
		v输出 = self.m设备.f执行显示命令(v命令)
		return f解析时间(v输出)
class C时间(模式.C同级模式, 时间.I时间配置):
	def __init__(self, a):
		模式.C同级模式.__init__(self, a)
	def fs日期时间(self, a日期时间):
		v时间 = 时间.f解析日期时间(a日期时间)
		v命令 = 命令.C命令("clock datetime")
		v命令 += time.strftime("%H:%M:%S %Y-%m-%d", v时间)
		self.m设备.f执行命令(v命令)
	def fs时区(self, a时区):
		v时区 = 时间.f解析时区(a时区)
		v时区名, v符号, v时, v分 = 时间.f拆分时区(v时区)
		v命令 = 命令.C命令("clock timezone")
		v命令 += v时区名
		v命令 += "add" if v符号 else "minus"
		v命令 += v时
		if v分:
			v命令 -= f":{v分}"
		self.m设备.f执行命令(v命令)