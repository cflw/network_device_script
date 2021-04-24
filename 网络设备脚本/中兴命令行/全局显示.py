from ..命令行接口 import 全局显示
from . import 基本表信息
class C全局显示m6000(全局显示.I全局显示):
	def __init__(self, a):
		全局显示.I全局显示.__init__(self, a)
	#模式
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间显示(self)
	#显示配置
	def f显示_启动配置(self):
		v输出 = self.m设备.f执行显示命令("show startup-config")
		return v输出
	def f显示_当前配置(self):
		v输出 = self.m设备.f执行显示命令("show running-config")
		return v输出
	#显示具体
	def f显示_接口表(self):
		v命令 = "show interface brief"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 基本表信息.f接口表(v输出)
	def f显示_网络接口表4(self):
		v命令 = "show ip interface brief"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 基本表信息.f网络接口表4(v输出)
