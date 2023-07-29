from ..基础接口 import 全局显示
from ..命令行接口 import 模式
from . import 基本表信息
class C全局显示(全局显示.I全局显示, 模式.I显示模式):
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	#模式
	def f模式_设备(self):
		from . import 设备模式
		return 设备模式.C设备显示(self)
	#显示
	def f显示_启动配置(self):
		v输出 = self.m设备.f执行显示命令("show startup-config")
		return v输出
	def f显示_当前配置(self):
		v输出 = self.m设备.f执行显示命令("show running-config")
		return v输出
	def f显示_接口详细(self):
		v输出 = self.m设备.f执行显示命令("show interface")
		return 基本表信息.f接口详细(v输出)
	def f显示_接口表(self):
		v输出 = self.m设备.f执行显示命令("show interface status")
		return 基本表信息.f接口表(v输出)
	def f显示_网络接口表4(self):
		v输出 = self.m设备.f执行显示命令("show ip interface brief")
		return 基本表信息.f网络接口表4(v输出)
	def f显示_网络接口表6(self):
		v输出 = self.m设备.f执行显示命令("show ipv6 interface brief")
		return 基本表信息.f网络接口表6(v输出)
