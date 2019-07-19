import time
import cflw代码库py.cflw字符串 as 字符串
from ..命令行接口 import 用户模式
from ..命令行接口 import 命令
class C用户模式cnv7(用户模式.I用户模式):
	"""适用于: cn8000系列(v7.3)"""
	def __init__(self, a):
		用户模式.I用户模式.__init__(self, a)
	#模式
	def f事件_进入模式(self):
		self.m设备.f刷新()
		self.m设备.f输入_结束符()
		self.m设备.f输入_回车(-1, 5)
	#显示
	def f显示_时间(self):
		v输出 = self.m设备.f执行显示命令("show clock")
		from . import 时间
		return 时间.f解析时间cnv7(v输出)
	#模式
	def f模式_全局配置(self):
		from . import 全局配置
		return 全局配置.C全局配置cnv7(self)
	#动作
	def f登录(self, a用户名 = "", a密码 = ""):
		time.sleep(0.5)
		v输出 = self.m设备.f输出()[-100:]
		if "Username:" in v输出:
			v输出 = self.m设备.f执行命令(a用户名)
		if "Password:" in v输出:
			self.m设备.f执行命令(a密码)
		self.f切换到当前模式()
		time.sleep(0.5)
	def f保存配置(self):
		self.f执行当前模式命令("copy running-config startup-config")
class C用户模式cnv6(用户模式.I用户模式):
	"""适用于: cn61108(v6.x)"""
	def __init__(self, a):
		用户模式.I用户模式.__init__(self, a)
	#事件
	def f事件_进入模式(self):
		self.m设备.f刷新()
		self.m设备.f输入_结束符()
		self.m设备.f输入_回车(-1, 5)
	#显示
	def f显示_时间(self):
		v输出 = self.m设备.f执行显示命令("show clock")
		from . import 时间
		return 时间.f解析时间cnv6(v输出)
	#模式
	def f模式_全局配置(self):
		from . import 全局配置
		return 全局配置.C全局配置cnv6(self)
	#动作
	def f登录(self, a用户名 = "", a密码 = ""):
		time.sleep(0.5)
		v输出 = self.m设备.f输出()[-100:]
		if "Username:" in v输出:
			v输出 = self.m设备.f执行命令(a用户名)
		if "Password:" in v输出:
			self.m设备.f执行命令(a密码)
		self.f切换到当前模式()
		time.sleep(0.5)
	def f保存配置(self):
		self.f执行当前模式命令("write")
class C用户模式sv3(用户模式.I用户模式):
	"""适用于: s6550(v3)"""
	def __init__(self, a):
		用户模式.I用户模式.__init__(self, a)
	#显示
	def f显示_时间(self):
		v输出 = self.m设备.f执行显示命令("show clock")
		from . import 时间
		return 时间.f解析时间sv3(v输出)
	#模式
	def f模式_全局配置(self):
		from . import 全局配置
		return 全局配置.C全局配置sv3(self)
	#操作
	def f登录(self, a用户名 = "", a密码 = ""):
		time.sleep(0.5)
		v输出 = self.m设备.f输出()[-100:]
		if "Username:" in v输出:
			v输出 = self.m设备.f执行命令(a用户名)
		if "Password:" in v输出:
			self.m设备.f执行命令(a密码)
		self.f切换到当前模式()
		time.sleep(0.5)
	def f保存配置(self):
		self.f执行当前模式命令("write")