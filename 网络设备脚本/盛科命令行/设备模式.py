from ..基础接口 import 设备模式
from ..命令行接口 import 模式
from . import 系统信息
from . import 硬件信息
class C设备显示_ev6(设备模式.I设备显示, 模式.I显示模式):
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	def f显示_中央处理器利用率(self):
		v输出 = self.m设备.f执行显示命令("show processes cpu history")
		return 系统信息.f解析中央处理器利用率(v输出)
	def f显示_内存利用率(self):
		v输出 = self.m设备.f执行显示命令("show memory summary total")
		return 系统信息.f解析内存利用率(v输出)
	def f显示_电源(self):
		v输出 = self.m设备.f执行显示命令("show environment")
		return 硬件信息.f电源信息(v输出)
	def f显示_温度(self):
		v输出 = self.m设备.f执行显示命令("show environment")
		return 硬件信息.f温度信息(v输出)
class C设备显示_e580v6(C设备显示_ev6):
	"""适用于: 浪潮cn61108pcvh(v6.x)"""
	def f显示_风扇(self):
		v输出 = self.m设备.f执行显示命令("show environment")
		return 硬件信息.f风扇信息e580(v输出)
class C设备显示_e530v6(C设备显示_ev6):
	"""适用于: 浪潮s5350(v6.x)"""
	def __init__(self, a):
		C设备显示_ev6.__init__(self, a)
	def f显示_风扇(self):
		v输出 = self.m设备.f执行显示命令("show environment")
		return 硬件信息.f风扇信息e530(v输出)
