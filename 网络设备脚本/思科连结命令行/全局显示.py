from ..命令行接口 import 全局显示
from . import 系统信息
from . import 硬件信息
class C全局显示nv7_0(全局显示.I全局显示):
	"""适用于: 思科n9k系列(v7.0.*), 浪潮cn8000系列(v7.3), 浪潮cn61108pcv(v7.0)"""
	def __init__(self, a):
		全局显示.I全局显示.__init__(self, a)
	def f显示_启动配置(self):
		v输出 = self.m设备.f执行显示命令("show startup-config")
		return v输出
	def f显示_当前配置(self):
		v输出 = self.m设备.f执行显示命令("show running-config")
		return v输出
	def f显示_时间(self):
		v输出 = self.m设备.f执行显示命令("show clock")
		from . import 时间
		return 时间.f解析时间(v输出)
	def f显示_设备版本(self):
		return self.fg版本信息()
	def f显示_中央处理器利用率(self):
		v输出 = self.m设备.f执行显示命令("show system resources")
		return 系统信息.f解析中央处理器利用率(v输出)
	def f显示_内存利用率(self):
		v输出 = self.m设备.f执行显示命令("show system resources")
		return 系统信息.f解析内存利用率(v输出)
class C全局显示nv7_3(C全局显示nv7_0):
	"""适用于: 思科n7k(v7.3.*)"""
class C全局显示nv9_2(C全局显示nv7_0):
	"""适用于: 浪潮cn61108pcv(v9.2.3)"""
	def f显示_资产(self):
		v命令 = "show inventory"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 硬件信息.f资产信息(v输出)
	def f显示_电源(self):
		v命令 = "show enviroment power"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 硬件信息.f电源信息(v输出)
	def f显示_风扇(self):
		v命令 = "show enviroment fan"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 硬件信息.f风扇信息(v输出)
	def f显示_温度(self):
		v命令 = "show enviroment temperature"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 硬件信息.f温度信息(v输出)
