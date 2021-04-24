from ..基础接口 import 设备模式
from ..命令行接口 import 模式
class C设备显示(设备模式.I设备显示, 模式.I显示模式):
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
		#基础
	def f显示_版本(self):
		v命令 = "display version"
		v输出 = self.m设备.f执行显示命令(v命令, a自动换页 = True)
		return v输出
	def f显示_时间(self):
		from . import 时间
	def f显示_设备名(self):
		v命令 = "display current-configuration | include sysname"
		v输出 = self.m设备.f执行显示命令(v命令)
		return C输出分析.f从配置取设备名称(v输出)
	def f显示_运行时间(self):
		"从开机到现在所经过的时间"
		raise NotImplementedError()
	def f显示_开机日期(self):
		raise NotImplementedError()
	def f显示_序列号(self):
		raise NotImplementedError()
	def f显示_出厂日期(self):
		raise NotImplementedError()
