from ..命令行接口 import 全局配置
from ..基础接口 import 操作
class C全局配置m6000(全局配置.I全局配置):
	def __init__(self, a):
		全局配置.I全局配置.__init__(self, a)
	#命令
	def fg进入命令(self):
		return "configure terminal"
	#模式
	def f模式_接口(self, a接口, a操作 = 操作.E操作.e设置):
		v接口 = 接口.f创建接口m6000(a接口)
		return 接口.C接口m6000(self, v接口)