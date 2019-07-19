from .. import 浪潮
from ..命令行接口 import 设备 as 南向设备
from ..命令行接口 import 命令
from ..命令行接口 import 用户模式
class C设备cnv7(南向设备.I设备):
	"""适用于: cn8000系列(v7.3), cn61108(v7.x)"""
	def __init__(self, a连接, a型号, a版本):
		南向设备.I设备.__init__(self, a连接)
		self.m型号 = a型号
		self.m版本 = a版本
	#输入输出
	def f输入_结束符(self):
		self.f输入('\x1a')	#ctrl+z
	#模式
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户模式cnv7(self)
	#命令
	def f执行显示命令(self, a命令, a自动换页 = True):
		v命令 = str(a命令)
		v输出 = 南向设备.I设备.f执行显示命令(self, v命令, a自动换页)
		v输出 = v输出.replace("\r\n", "\n")
		v输出 = 南向设备.f去头尾行(v输出)
		# if v输出.count("\n") < 10:
		# 	self.f检测命令异常(self, v输出)
		return v输出
	def f退出(self, a关闭 = False):
		self.f执行命令("exit")
class C设备cnv6(南向设备.I设备):
	"""适用于: cn61108(v6.x)"""
	def __init__(self, a连接, a型号, a版本):
		南向设备.I设备.__init__(self, a连接)
		self.m型号 = a型号
		self.m版本 = a版本
	#输入输出
	def f输入_结束符(self):
		self.f输入('\x1a')	#ctrl+z
	#模式
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户模式cnv6(self)
	#命令
	def f执行命令(self, a命令):
		v输出 = 南向设备.I设备.f执行命令(self, a命令)
		# self.f检测命令异常(v输出)
		return v输出
	def f执行用户命令(self, a命令):
		v命令 = 命令.C命令(a命令)
		if not isinstance(self.fg当前模式(), 用户模式.I用户模式):	#在配置模式，命令前要加个do
			v命令.f前面添加(c做)
		v输出 = self.f执行命令(v命令)
		v输出 = v输出.replace("\r\n", "\n")
		return v输出
	def f执行显示命令(self, a命令, a自动换页 = True):
		v命令 = 命令.C命令(a命令)
		if not isinstance(self.fg当前模式(), 用户模式.I用户模式):	#在配置模式，命令前要加个do
			v命令.f前面添加(c做)
		v输出 = 南向设备.I设备.f执行显示命令(self, a命令 = v命令, a自动换页 = a自动换页)
		v输出 = v输出.replace("\r\n", "\n")
		v输出 = 南向设备.f去头尾行(v输出)
		# if v输出.count("\n") < 10:	#输出行数太少,检测是否有异常
		# 	self.f检测命令异常(v输出)
		return v输出
	def f退出(self, a关闭 = False):
		self.f执行命令("exit")
class C设备sv3(南向设备.I设备):
	"""适用于: s6550(v3.50)"""
	def __init__(self, a连接, a型号, a版本):
		南向设备.I设备.__init__(self, a连接)
		self.m型号 = a型号
		self.m版本 = a版本
	#输入输出
	def f输入_结束符(self):
		self.f输入('\x1a')	#ctrl+z
	#模式
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户模式sv3(self)
	#命令
	def f执行命令(self, a命令):
		v输出 = 南向设备.I设备.f执行命令(self, a命令)
		return v输出
	def f执行用户命令(self, a命令):
		#退到用户模式执行
		self.ma模式[0].f切换到当前模式()
		return self.f执行命令(a命令)
	def f执行显示命令(self, a命令, a自动换页 = True):
		#退到用户模式执行
		self.ma模式[0].f切换到当前模式()
		v输出 = 南向设备.I设备.f执行显示命令(self, a命令, a自动换页)
		v输出 = v输出.replace("\r\n", "\n")
		v输出 = 南向设备.f去头尾行(v输出)
		return v输出
	def f退出(self, a关闭 = False):
		self.f执行命令("exit")
