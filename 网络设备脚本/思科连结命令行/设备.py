from ..基础接口 import 操作
from ..命令行接口 import 设备 as 南向设备
from ..命令行接口 import 命令
#===============================================================================
# nexus(v7.*)
#===============================================================================
class C设备_nv7(南向设备.I设备):
	"""适用于: 思科n7k系列, 思科n9k系列(v7.0), 浪潮cn61108pcv(v7.0)"""
	def __init__(self, a连接, a型号, a版本):
		南向设备.I设备.__init__(self, a连接)
		self.m连接.fs编码("utf-8")
		self.fs自动换页("--More--")
		self.m型号 = a型号
		self.m版本 = a版本
	#输入输出
	def f输入_结束符(self):
		self.f输入('\x1a')	#ctrl+z
	#模式
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户模式_nv7_0(self)
	#命令
	def f处理显示结果(self, a命令):
		v输出 = a命令.replace("\r\n", "\n")
		v输出 = 南向设备.f去头尾行(v输出)
		# if v输出.count("\n") < 10:
		# 	self.f检测命令异常(self, v输出)
		return v输出
	def f退出(self, a关闭 = False):
		self.f执行命令("exit")
class C设备_nv7_3(C设备_nv7):
	"""适用于: 浪潮cn8672up(v7.3), 浪潮cn8696q(v7.3)"""
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户模式_nv7_3(self)	
class C设备_nv9(C设备_nv7):
	"""适用于: 思科n9k系列(v9.x), 浪潮cn61108pcv(v9.2.3)"""
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户模式_nv9_2(self)