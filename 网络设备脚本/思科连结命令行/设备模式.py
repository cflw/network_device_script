from ..基础接口 import 设备模式
from ..命令行接口 import 模式
from . import 系统信息
from . import 硬件信息
class C设备显示nv7_0(设备模式.I设备显示, 模式.I显示模式):
	"""适用于: 思科n9k系列(v7.0.*), 浪潮cn8000系列(v7.3), 浪潮cn61108pcv(v7.0)"""
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	#硬件
	def f显示_资产(self):
		v命令 = "show inventory"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 硬件信息.f资产信息(v输出)
	def f显示_风扇(self):
		v输出 = self.m设备.f执行显示命令("show environment fan")
		return 硬件信息.f风扇v7(v输出)
	def f显示_电源(self):
		v输出 = self.m设备.f执行显示命令("show environment power")
		return 硬件信息.f电源v7_电源(v输出)
	def f显示_温度(self):
		v输出 = self.m设备.f执行显示命令("show environment temperature")
		return 硬件信息.f温度v7(v输出)
	#系统
	def f显示_设备版本(self):
		return self.fg版本信息()
	def f显示_中央处理器利用率(self):
		v输出 = self.m设备.f执行显示命令("show system resources")
		return 系统信息.f解析中央处理器利用率(v输出)
	def f显示_内存利用率(self):
		v输出 = self.m设备.f执行显示命令("show system resources")
		return 系统信息.f解析内存利用率(v输出)
class C设备显示nv9_2(C设备显示nv7_0):
	"""适用于: 浪潮cn61108pcv(v9.2.3)"""
	def __init__(self, a):
		C设备显示nv7_0.__init__(self, a)
	#硬件
	def f显示_电源(self):
		v命令 = "show environment power"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 硬件信息.f电源v9(v输出)
	def f显示_风扇(self):
		v命令 = "show environment fan"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 硬件信息.f风扇v9(v输出)
	def f显示_温度(self):
		v命令 = "show environment temperature"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 硬件信息.f温度v9(v输出)
