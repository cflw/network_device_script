from ..命令行接口 import 全局显示
from . import 系统信息
class C全局显示(全局显示.I全局显示):
	def f显示_启动配置(self):
		v输出 = self.m设备.f执行显示命令("show startup-config")
		return v输出
	def f显示_当前配置(self):
		v输出 = self.m设备.f执行显示命令("show running-config")
		return v输出
	def f显示_时间(self):
		v命令 = "show clock"
		v输出 = self.m设备.f执行显示命令(v命令)
		from . import 时间
		return 时间.f解析时间(v输出)
	def f显示_设备版本(self):
		return self.fg版本信息()
	def f显示_中央处理器利用率(self):
		v输出 = self.m设备.f执行显示命令("show processes cpu", a自动换页 = False)
		return 系统信息.f解析中央处理器利用率(v输出)
	def f显示_内存利用率(self):
		v输出 = self.m设备.f执行显示命令("show processes memory", a自动换页 = False)
		return 系统信息.f解析内存利用率(v输出)
