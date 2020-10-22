import time
from ..基础接口 import 异常
from ..命令行接口 import 用户模式 as 用户模式
class C用户视图(用户模式.I用户模式):
	def __init__(self, a):
		用户模式.I用户模式.__init__(self, a)
	def f事件_进入模式后(self):
		self.m设备.f刷新()
		self.m设备.f输入_结束符()
		self.m设备.f输入_回车()
		v输出 = self.m设备.f输出()
		if "commit" in v输出:
			self.m设备.f执行命令("n")
	def f自动登录(self):
		self.f登录()
		self.f提升权限()
	#模式
	def f模式_全局配置(self):
		from . import 全局配置
		return 全局配置.C系统视图(self)
	def f模式_全局显示(self):
		from . import 全局显示
		return 全局显示.C全局显示(self)
	#动作
	def f登录(self, a用户名 = "", a密码 = ""):
		self.m设备.f切换到当前连接()
		time.sleep(0.2)
		self.f记住登录(a用户名, a密码)
		self.m设备.f输入_回车()
		time.sleep(0.5)
		v输出 = self.m设备.f输出()
		if "Username:" in v输出:
			v输出 = self.m设备.f执行命令(self.m登录用户名)
		if "Password:" in v输出:
			v输出 = self.m设备.f执行命令(self.m登录密码)
		if "Error:" in v输出:
			if self.m设备.m检测异常:
				raise 异常.X登录(v输出)
		time.sleep(0.5)
		self.m设备.mf自动登录 = self.f自动登录
		self.f切换到当前模式()
	def f提升权限(self, a密码 = "", a级别 = 15):
		self.f记住提权(a密码 = a密码, a级别 = a级别)
		if self.m提权密码:
			v输出 = self.m设备.f执行命令("super")
		if "Password:" in v输出:
			v输出 = self.m设备.f执行命令(self.m提权密码)
	def f保存配置(self):
		v输出 = self.f执行当前模式命令("save")
		#  The current configuration will be written to the device. 
		#  Are you sure to continue? (y/n)[n]:
		if "continue?" in v输出:
			self.m设备.f执行命令("y")
	def fs终端监视(self, a开关):
		v命令 = 命令.C命令("terminal monitor")
		v命令.f前置否定(a开关, c不)
		self.f执行当前模式命令(v命令)
	#连接
	def f连接_网络终端(self, a地址, **a参数):
		from . import 连接
		return 连接.C网络终端(self, a地址, **a参数)
