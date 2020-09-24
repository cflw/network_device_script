import time
from ..基础接口 import 用户模式
class C用户模式(用户模式.I用户模式):
	def __init__(self, a设备):
		self.m设备 = a设备
	def f登录(self, a密码 = "", a用户名 = None):
		time.sleep(0.5)
		w密码框 = self.m设备.f查找("//input[@id='lgPwd']")
		w密码框.f输入(a密码)
		w确定 = self.m设备.f查找("//input[@id='loginSub']")
		w确定.f点击()
		time.sleep(0.2)
	def f模式_全局配置(self):
		from . import 全局配置
		return 全局配置.C全局配置(self.m设备)