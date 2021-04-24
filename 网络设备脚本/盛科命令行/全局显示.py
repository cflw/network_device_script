from ..基础接口 import 全局显示
from ..命令行接口 import 模式
from . import 系统信息
#===============================================================================
# 全局显示
#===============================================================================
class C全局显示ev6(全局显示.I全局显示, 模式.I显示模式):
	"""适用于: 浪潮cn61108pcvh(v6.x)"""
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	#模式
	def f模式_设备(self):
		from . import 设备模式
		from .. import 浪潮
		if self.m设备.m型号 == 浪潮.E型号.s5350:
			return 设备模式.C设备显示e530v6(self)
		else:
			return 设备模式.C设备显示ev6(self)
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间显示ev6(self)
	#显示配置
	def f显示_当前配置(self):
		v输出 = self.m设备.f执行显示命令("show running-config")
		return v输出
	def f显示_启动配置(self):
		v输出 = self.m设备.f执行显示命令("show startup-config")
		return v输出
