from ..基础接口 import 用户模式
class C用户模式(用户模式.I用户模式):
	"""适用于: mw155r"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def f登录(self, a密码 = ""):
		w密码框 = self.m设备.f查找("//input[@id='pcPassword']")
		w密码框.f输入(a密码)
		w确认 = self.m设备.f查找("//label[@id='loginBtn']")
		w确认.f点击()
		self.m设备.mi登录 = True
	def f模式_全局配置(self):
		from . import 全局配置
		return 全局配置.C全局配置(self.m设备)