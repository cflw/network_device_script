from ..基础接口 import 全局显示
from ..命令行接口 import 模式
from .. import 华三
from . import 基本表信息
class C全局显示v7(全局显示.I全局显示, 模式.I显示模式):
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	#模式
	def f模式_设备(self):
		from . import 设备模式
		if self.m设备.m型号 in (华三.E型号.msr3620, 华三.E型号.s5820v2):
			return 设备模式.C设备显示_模拟v7_1(self)
		else:
			return 设备模式.C设备显示v7(self)
	#显示
	def f显示_当前配置(self):
		v命令 = "display current-configuration"
		v输出 = self.m设备.f执行显示命令(v命令, a自动换页 = True)
		return v输出
	def 显示_启动配置(self):
		v命令 = "display saved-configuration"
		v输出 = self.m设备.f执行显示命令(v命令, a自动换页 = True)
		return v输出
