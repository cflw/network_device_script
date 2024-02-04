import time
from ..华三命令行 import 用户模式 as 旧用户模式
from ..华为命令行.常量 import *
class C用户视图_v7(旧用户模式.C用户视图):
	def f模式_全局配置(self):
		from . import 全局配置
		return 全局配置.C系统视图_v7(self)
	def f模式_全局显示(self):
		from . import 全局显示
		return 全局显示.C全局显示_v7(self)
	#动作
	def f登录(self, a用户名 = "", a密码 = ""):
		self.m设备.f切换到当前连接()
		time.sleep(0.5)
		self.f记住登录(a用户名, a密码)
		self.m设备.f输入_回车()
		v输出 = self.m设备.f输出()[-100:]
		if not v输出:
			self.m设备.f输入_回车()
			time.sleep(0.5)
			v输出 = self.m设备.f输出()
		if "Automatic configuration" in v输出:	#刚开机,自动配置中,按ctrl+c中断
			self.m设备.f输入(c中断符)
			v输出 = self.m设备.f输出()
		if "login:" in v输出:
			v输出 = self.m设备.f执行命令(a用户名)
		if "Password:" in v输出:
			v输出 = self.m设备.f执行命令(a密码)
		time.sleep(0.5)
		self.m设备.mf自动登录 = self.f自动登录
		self.f切换到当前模式()
class C用户视图_ev7(C用户视图_v7):
	"""适用于: (模拟器)华三msr3620(v7.1.*), (模拟器)华三s5820v2(v7.1.*)"""
	def f模式_全局显示(self):
		from . import 全局显示
		return 全局显示.C全局显示_s5v7(self)
class C用户视图_s5v7(C用户视图_v7):
	"""适用于: 华三s5560x(v7.1.070 r6526)"""
	def f模式_全局显示(self):
		from . import 全局显示
		return 全局显示.C全局显示_s5v7(self)
class C用户视图_s7v7(C用户视图_v7):
	"""适用于: 紫光s8600x(v7.1.070), 紫光s7800xp(v7.1.*)"""
	def f模式_全局显示(self):
		from . import 全局显示
		return 全局显示.C全局显示_s7v7(self)
class C用户视图_us5v7(C用户视图_v7):
	"""适用于: 紫光s5200(v7.1.*)"""
	def f模式_全局显示(self):
		from . import 全局显示
		return 全局显示.C全局显示_us5v7(self)
class C用户视图_s9v7(C用户视图_v7):
	"""适用于: 华三S9810(v7.1.*)"""
	def f模式_全局显示(self):
		from . import 全局显示
		return 全局显示.C全局显示_s9v7(self)
class C用户视图_sv7_2019(C用户视图_v7):
	"""适用于: 华三s5560x(v7.1.070 r1119p20), 紫光s5600(v7.1.070 r7734p05)"""
	def f模式_全局显示(self):
		from . import 全局显示
		return 全局显示.C全局显示_sv7_2019(self)
