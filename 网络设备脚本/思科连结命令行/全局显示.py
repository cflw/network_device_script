from ..基础接口 import 全局显示
from ..命令行接口 import 模式
class C全局显示nv7_0(全局显示.I全局显示, 模式.I显示模式):
	"""适用于: 思科n9k系列(v7.0.*), 浪潮cn8000系列(v7.3), 浪潮cn61108pcv(v7.0)"""
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	#模式
	def f模式_设备(self):
		from . import 设备模式
		return 设备模式.C设备显示nv7_0(self)
	#显示
	def f显示_启动配置(self):
		v输出 = self.m设备.f执行显示命令("show startup-config")
		return v输出
	def f显示_当前配置(self):
		v输出 = self.m设备.f执行显示命令("show running-config")
		return v输出
class C全局显示nv7_3(C全局显示nv7_0):
	"""适用于: 思科n7k(v7.3.*)"""
	def __init__(self, a):
		C全局显示nv7_0.__init__(self, a)
class C全局显示nv9_2(C全局显示nv7_3):
	"""适用于: 浪潮cn61108pcv(v9.2.3)"""
	def __init__(self, a):
		C全局显示nv7_3.__init__(self, a)
	def f模式_设备(self):
		from . import 设备模式
		return 设备模式.C设备显示nv9_2(self)