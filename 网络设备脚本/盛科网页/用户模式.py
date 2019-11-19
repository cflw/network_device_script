import time
from ..基础接口 import 用户模式
class C用户模式ev6(用户模式.I用户模式):
	"""适用于: 浪潮s5350(v6.x)"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def f登录(self, a用户名 = "", a密码 = ""):
		time.sleep(0.5)
		w用户名 = self.m设备.f网页_查找("//*[@id='name']")
		w用户名.f输入(a用户名)
		w密码 = self.m设备.f网页_查找("/html/body/div/form/table/tbody/tr[2]/td[2]/input")
		w密码.f输入(a密码)
		w确定 = self.m设备.f网页_查找("/html/body/div/form/table/tbody/tr[5]/th/input")
		w确定.f点击()
		time.sleep(0.5)
		#取会话
		self.m设备.f解析登录后地址()
	def f模式_全局配置(self):
		from . import 全局配置
		return 全局配置.C全局配置ev6(self.m设备)
	def f模式_全局显示(self):
		from . import 全局显示
		return 全局显示.C全局显示ev6(self.m设备)