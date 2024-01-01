import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 全局显示
from ..命令行接口 import 模式
from . import 系统信息
#===============================================================================
# 全局显示
#===============================================================================
class C全局显示_sv3(全局显示.I全局显示, 模式.I显示模式):
	"""适用于: 浪潮s6550(v3.x)"""
	#模式
	def f模式_设备(self):
		from . import 设备模式
		return 设备模式.C设备显示_sv3(self)
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间显示_sv3(self)
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
