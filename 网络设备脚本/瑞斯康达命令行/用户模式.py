import time
from ..命令行接口 import 用户模式
#===============================================================================
# s系列(v3.x)
#===============================================================================
class C用户模式sv3(用户模式.I用户模式):
	"""适用于: 浪潮s6550(v3.x)"""
	def __init__(self, a):
		用户模式.I用户模式.__init__(self, a)
	#模式
	def f模式_全局配置(self):
		from . import 全局配置
		return 全局配置.C全局配置sv3(self)
	def f模式_全局显示(self):
		from . import 全局显示
		return 全局显示.C全局显示sv3(self)
	#操作
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