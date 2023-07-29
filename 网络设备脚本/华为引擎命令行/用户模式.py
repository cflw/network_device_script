import time
from ..基础接口 import 异常
from ..基础接口 import 操作
from ..华为命令行 import 用户模式 as 旧用户模式
class C用户视图ne(旧用户模式.C用户视图):
	"""适用于: 华为ne40e(v8.180)"""
	def f事件_进入模式后(self):
		self.f登录自动刷新()
		v输出 = self.m设备.f输出()
		if "commit" in v输出:
			self.m设备.f执行命令("n")
	def f模式_全局配置(self):
		from . import 全局配置
		if self.m设备.m自动提交 == 操作.E自动提交.e不提交:
			self.fs自动提交(操作.E自动提交.e立即)
		return 全局配置.C系统视图ne(self)
	def f模式_全局显示(self):
		from . import 全局显示
		return 全局显示.C全局显示ne(self)
	#动作
	def f登录(self, a用户名 = "", a密码 = ""):
		self.m设备.f切换到当前连接()
		time.sleep(0.2)
		self.f记住登录(a用户名, a密码)
		self.m设备.f输入_回车()
		time.sleep(0.5)
		v输出 = self.m设备.f输出()
		#Warning: Uncommitted configurations found, commit them before exiting? [Y(yes)/N(no)/C(cancel)]:
		#Error: Please choose 'YES', 'NO' or 'CANCEL' first before pressing 'Enter'. [Y/N/C]:
		if "Warning: Uncommitted" in v输出 or "Error: Please choose" in v输出:
			v输出 = self.m设备.f执行命令("n")
		#Username:
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
class C用户视图ce(C用户视图ne):
	def f模式_全局配置(self):
		from . import 全局配置
		if self.m设备.m自动提交 == 操作.E自动提交.e不提交:
			self.fs自动提交(操作.E自动提交.e立即)
		return 全局配置.C系统视图ce(self)
	def f模式_全局显示(self):
		from . import 全局显示
		return 全局显示.C全局显示ce(self)