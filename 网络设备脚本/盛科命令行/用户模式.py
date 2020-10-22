import time
from ..命令行接口 import 用户模式
#===============================================================================
# cn系列(v6.x)
#===============================================================================
class C用户模式ev6(用户模式.I用户模式):
	"""适用于: 盛科e580(v6.x), 浪潮cn61108pcvh(v6.x), 浪潮s5350(v6.x)"""
	def __init__(self, a):
		用户模式.I用户模式.__init__(self, a)
	def f自动登录(self):
		self.f登录()
	#事件
	def f事件_进入模式后(self):
		self.m设备.f刷新()
		self.m设备.f输入_结束符()
		self.m设备.f输入_回车(-1, 5)
	#模式
	def f模式_全局配置(self):
		from . import 全局配置
		return 全局配置.C全局配置ev6(self)
	def f模式_全局显示(self):
		from . import 全局显示
		return 全局显示.C全局显示ev6(self)
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
		self.m设备.mf自动登录 = self.f自动登录
		time.sleep(0.5)
	def f保存配置(self):
		self.f执行当前模式命令("write")
