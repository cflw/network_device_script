import time
from ..基础接口 import 用户模式
class C用户模式(用户模式.I用户模式):
	"""适用于: SG-6000-P1242(v5.5)"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def f模式_全局配置(self):
		from . import 全局配置
		return 全局配置.C全局配置(self.m设备)
	def f模式_全局显示(self):
		from . import 全局显示
		return 全局显示.C全局显示(self.m设备)
	def f登录(self, a用户名, a密码):
		w用户名 = self.m设备.f查找('//*[@id="login_username"]')
		w用户名.f输入(a用户名)
		w密码 = self.m设备.f查找('//*[@id="login_passwd"]')
		w密码.f输入(a密码)
		w登录 = self.m设备.f查找('//*[@id="login_button"]')
		w登录.f点击()
		self.m设备.f等待存在("/html/body/div[1]/div/div/div/div[1]/div/div[2]/div")
		time.sleep(1)
		self.m设备.f等待可用()