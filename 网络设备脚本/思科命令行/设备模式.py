from ..基础接口 import 设备模式
from ..命令行接口 import 模式
from . import 硬件信息
from . import 系统信息
class C设备显示(设备模式.I设备显示, 模式.I显示模式):
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
		self.m版本信息 = None
	def fg版本信息(self):
		if self.m版本信息 == None:
			v输出 = self.m设备.f执行显示命令("show version")
			self.m版本信息 = 系统信息.C版本信息(v输出)
		return self.m版本信息
	#硬件
	def f显示_风扇(self):
		v输出 = self.m设备.f执行显示命令("show environment fan")
		return 硬件信息.f风扇信息(v输出)
	def f显示_电源(self):
		v输出 = self.m设备.f执行显示命令("show environment power")
		return 硬件信息.f电源信息(v输出)
	def f显示_温度(self):
		v输出 = self.m设备.f执行显示命令("show environment temperature")
		return 硬件信息.f温度信息(v输出)
	#系统
	def f显示_系统版本(self):
		return self.fg版本信息()
	def f显示_中央处理器利用率(self):
		v输出 = self.m设备.f执行显示命令("show processes cpu", a自动换页 = False)
		return 系统信息.f解析中央处理器利用率(v输出)
	def f显示_内存利用率(self):
		v输出 = self.m设备.f执行显示命令("show processes memory", a自动换页 = False)
		return 系统信息.f解析内存利用率(v输出)
class C设备配置(设备模式.I设备配置, 模式.C同级模式, C设备显示):
	def __init__(self, a):
		模式.C同级模式.__init__(self, a)
		C设备显示.__init__(self, a)
	def fs设备名(self, a名称):
		v命令 = "hostname " + str(a名称)
		self.f执行当前模式命令(v命令)
	def fs域名(self, a名称 = "a"):
		v命令 = "ip domain-name " + str(a名称)
		self.f执行当前模式命令(v命令)
