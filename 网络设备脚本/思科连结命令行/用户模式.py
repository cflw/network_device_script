import time
from ..命令行接口 import 用户模式
#===============================================================================
# cn系列(v7.x)
#===============================================================================
class C用户模式nv7_0(用户模式.I用户模式):
	"""适用于: 浪潮cn61108pcv(v7.0)"""
	def __init__(self, a):
		用户模式.I用户模式.__init__(self, a)
	#模式
	def f事件_进入模式后(self):
		self.f登录自动刷新()
	#显示
	def f显示_时间(self):
		v输出 = self.m设备.f执行显示命令("show clock")
		from . import 时间
		return 时间.f解析时间nv7(v输出)
	#模式
	def f模式_全局配置(self):
		from . import 全局配置
		return 全局配置.C全局配置nv7_0(self)
	def f模式_全局显示(self):
		from . import 全局显示
		return 全局显示.C全局显示nv7_0(self)
	#动作
	def f登录(self, a用户名 = "", a密码 = ""):
		self.m设备.f切换到当前连接()
		time.sleep(0.5)
		self.f记住登录(a用户名, a密码)
		v输出 = self.m设备.f输出()[-100:]
		if "Username:" in v输出:
			v输出 = self.m设备.f执行命令(self.m登录用户名)
		if "Password:" in v输出:
			self.m设备.f执行命令(self.m登录密码)
		self.f切换到当前模式()
		time.sleep(0.5)
	def f保存配置(self):
		self.f执行当前模式命令("write")
class C用户模式nv7_3(C用户模式nv7_0):
	"""适用于: 浪潮cn8000系列(v7.3)"""
	#模式
	def f模式_全局配置(self):
		from . import 全局配置
		return 全局配置.C全局配置nv7_3(self)
	#操作
	def f保存配置(self):
		self.f执行当前模式命令("copy running-config startup-config")
