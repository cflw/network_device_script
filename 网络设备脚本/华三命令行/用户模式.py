import time
import cflw代码库py.cflw字符串 as 字符串
from ..命令行接口 import 用户模式
from ..命令行接口 import 命令
from .常量 import *
class C用户视图(用户模式.I用户模式):
	c模式名 = "用户视图"
	def __init__(self, a):
		用户模式.I用户模式.__init__(self, a)
	def f事件_进入模式后(self):
		self.m设备.f刷新()
		self.m设备.f输入_结束符()
		self.m设备.f输入_回车()
		v输出 = self.m设备.f输出()
	def f自动登录(self):
		self.f登录()
		self.f提升权限()
	#模式
	def f模式_全局配置(self):
		from . import 全局配置
		if self.m设备.m版本 >= 7:
			return 全局配置.C系统视图v7(self)
		return 全局配置.C系统视图(self)
	def f模式_全局显示(self):
		from . import 全局显示:
		return 全局显示.C全局显示(self)
	#动作
	def f登录(self, a用户名 = "", a密码 = ""):
		self.m设备.f切换到当前连接()
		time.sleep(0.2)
		self.f记住登录(a用户名, a密码)
		self.m设备.f输入_回车()
		v输出 = self.m设备.f输出()[-100:]
		if not v输出:
			self.m设备.f输入(" ")
			v输出 = self.m设备.f输出()
		if "Automatic configuration" in v输出:	#刚开机,自动配置中,按ctrl+c中断
			self.m设备.f输入(c中断符)
			v输出 = self.m设备.f输出()
		if "Username:" in v输出:
			v输出 = self.f执行命令(a用户名)
		if "Password:" in v输出:
			v输出 = self.f执行命令(a密码)
		time.sleep(0.5)
		self.m设备.mf自动登录 = self.f自动登录
		self.f切换到当前模式()
	def f提升权限(self, a密码 = ""):
		self.f记住提权(a密码 = a密码)
		if self.m提权密码:
			v输出 = self.f执行命令("super")
		if "Password" in v输出:
			v输出 = self.f执行命令(self.m提权密码)
		if "Error" in v输出:
			raise RuntimeError(v输出)
		elif "User privilege level is" in v输出:
			v当前权限 = 南向设备.f取数字(v输出)[0]
			return (v当前权限, 3)
		else:
			raise RuntimeError("无法提升权限")
	def fs终端监视(self, a开关):
		v命令 = 命令.C命令("terminal monitor")
		v命令.f前置否定(a开关, c不)
		self.f执行当前模式命令(v命令)
	def f保存配置(self):
		v输出 = self.m设备.f执行命令("save")
		#The current configuration will be written to the device. Are you sure? [Y/N]:y
		if "[Y/N]" in v输出:
			v输出 = self.m设备.f执行命令("y")
		#Please input the file name(*.cfg)[flash:/startup.cfg]
		#(To leave the existing filename unchanged, press the enter key):
		if "enter" in v输出:
			self.m设备.f输入_回车()
			v输出 = self.m设备.f输出()
		#Validating file. Please wait...
		#Configuration is saved to device successfully.
	#连接
	def f连接_网络终端(self, a地址, **a参数):
		from ..华为命令行 import 连接
		return 连接.C网络终端(self, a地址, **a参数)
	def f连接_安全外壳(self, a地址, **a参数):
		from . import 连接
		return 连接.C安全外壳(self, a地址, **a参数)
