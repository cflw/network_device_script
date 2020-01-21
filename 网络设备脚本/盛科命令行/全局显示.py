from ..命令行接口 import 全局显示
from . import 系统信息
#===============================================================================
# 全局显示
#===============================================================================
class C全局显示ev6(全局显示.I全局显示):
	"""适用于: 浪潮cn61108pcvh(v6.x)"""
	#显示
	def f显示_当前配置(self):
		v输出 = self.m设备.f执行显示命令("show running-config")
		return v输出
	def f显示_启动配置(self):
		v输出 = self.m设备.f执行显示命令("show startup-config")
		return v输出
	def f显示_时间(self):
		v输出 = self.m设备.f执行显示命令("show clock")
		from . import 时间
		return 时间.f解析时间ev6(v输出)
	def f显示_中央处理器利用率(self):
		v输出 = self.m设备.f执行显示命令("show processes cpu history")
		return 系统信息.f解析中央处理器利用率(v输出)
	def f显示_内存利用率(self):
		v输出 = self.m设备.f执行显示命令("show memory summary total")
		return 系统信息.f解析内存利用率(v输出)