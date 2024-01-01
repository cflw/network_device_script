from ..基础接口 import 设备模式
from ..命令行接口 import 模式
from . import 系统信息
from . import 硬件信息
class C设备显示_v7(设备模式.I设备显示, 模式.I显示模式):
	"""适用于: 华三s6900(v7.1.070)"""
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	#硬件
	def f显示_风扇(self):
		v输出 = self.m设备.f执行显示命令("display fan")
		return 硬件信息.f风扇信息_v7(v输出)
	def f显示_电源(self):
		v输出 = self.m设备.f执行显示命令("display power")
		return 硬件信息.f电源信息_v7(v输出)
	def f显示_温度(self):
		v输出 = self.m设备.f执行显示命令("display environment")
		return 硬件信息.f温度信息_v7(v输出)
	#系统
	def f显示_中央处理器利用率(self):
		v输出 = self.m设备.f执行显示命令("display cpu-usage")
		return 系统信息.f解析中央处理器利用率(v输出)
	def f显示_内存利用率(self):
		v输出 = self.m设备.f执行显示命令("display memory")
		return 系统信息.f解析内存利用率(v输出)
class C设备显示_ev7_1(设备模式.I设备显示, 模式.I显示模式):
	"""适用于: (模拟器)华三msr3620(v7.1.075), (模拟器)华三s5820v2(v7.1.075)"""
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	#硬件
	def f显示_风扇(self):
		v输出 = self.m设备.f执行显示命令("display fan")
		return 硬件信息.f简单风扇信息_v7(v输出)
	def f显示_电源(self):
		v输出 = self.m设备.f执行显示命令("display power")
		return 硬件信息.f简单电源信息_v7(v输出)
	def f显示_温度(self):
		v输出 = self.m设备.f执行显示命令("display environment")
		return 硬件信息.f温度信息模拟v7(v输出)
	#系统
	def f显示_中央处理器利用率(self):
		v输出 = self.m设备.f执行显示命令("display cpu-usage")
		return 系统信息.f解析中央处理器利用率(v输出)
	def f显示_内存利用率(self):
		v输出 = self.m设备.f执行显示命令("display memory")
		return 系统信息.f解析内存利用率(v输出)
