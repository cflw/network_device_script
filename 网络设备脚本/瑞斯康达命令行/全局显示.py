import cflw代码库py.cflw字符串 as 字符串
from ..命令行接口 import 全局显示
from ..命令行接口 import 设备 as 南向设备
from . import 系统信息
#===============================================================================
# 全局显示
#===============================================================================
class C全局显示sv3(全局显示.I全局显示):
	"""适用于: 浪潮s6550(v3.x)"""
	#显示
	def f显示_当前配置(self):
		self.m设备.f执行命令("show running-config")
		# Being processed.This may take a few minutes,please wait......
		v输出 = self.m设备.f输出显示结果(a最小等待 = 5)
		v输出 = self.m设备.f处理显示结果(v输出)
		return v输出
	def f显示_启动配置(self):
		v输出 = self.m设备.f执行显示命令("show startup-config")
		return v输出
	def f显示_时间(self):
		v输出 = self.m设备.f执行显示命令("show clock")
		from . import 时间
		return 时间.f解析时间sv3(v输出)
	def f显示_中央处理器利用率(self):
		v输出 = self.m设备.f执行显示命令("show cpu-utilization")
		return 系统信息.f解析中央处理器利用率(v输出)
	def f显示_内存利用率(self):
		v输出 = self.m设备.f执行显示命令("show memory")
		return 系统信息.f解析内存利用率(v输出)
