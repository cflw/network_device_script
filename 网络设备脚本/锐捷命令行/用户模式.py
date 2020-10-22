import time
import cflw代码库py.cflw字符串 as 字符串
from ..命令行接口 import 用户模式
from ..命令行接口 import 命令
class C用户模式(用户模式.I用户模式):
	"""适用于: s5750(v11.4)"""
	def __init__(self, a):
		用户模式.I用户模式.__init__(self, a)
	#模式
	def f事件_进入模式后(self):
		self.m设备.f刷新()
		self.m设备.f输入_结束符()
		self.m设备.f输入_回车(-1, 5)
	def f模式_全局配置(self):
		from . import 全局配置
		return 全局配置.C全局配置(self)
	def f模式_全局显示(self):
		from . import 全局显示
		return 全局显示.C全局显示(self)
	#动作
	def f登录(self, a用户名 = "", a密码 = ""):
		time.sleep(1)
		v输出 = self.m设备.f输出()
		if "Username:" in v输出:
			v输出 = self.m设备.f执行命令(a用户名)
		if "Password:" in v输出:
			self.m设备.f执行命令(a密码)
	def f提升权限(self, a密码 = "", a级别 = None):
		v命令 = 命令.C命令("enable")
		if a级别:
			v命令 += a级别
		self.f执行当前模式命令(v命令)
		self.m设备.f执行命令(a密码)
	def f保存配置(self):
		self.f执行当前模式命令("write")
	def f清除配置(self):
		self.f执行当前模式命令("delete config.txt")
		self.m设备.f执行命令("y")
	def f重新启动(self):
		self.f执行当前模式命令("reload")
		self.m设备.f执行命令("y")
