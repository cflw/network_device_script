from ..基础接口 import 操作
from ..基础接口 import 协议
from ..命令行接口 import 全局配置
from . import 接口 as 实现接口
#===============================================================================
# s系列(v3.x)
#===============================================================================
class C全局配置sv3(全局配置.I全局配置):
	"""适用于: s6550(v3.x)"""
	def __init__(self, a):
		全局配置.I全局配置.__init__(self, a)
	def fg进入命令(self):
		return "config terminal"
	#模式
	def f模式_用户(self, a用户名, a操作 = 操作.E操作.e设置):
		from . import 用户
		return 用户.C用户sv3(self.fg上级模式(), a用户名)
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间sv3(self.fg上级模式())
	def f模式_日志(self):
		from . import 日志
		return 日志.C日志sv3(self)
	#服务
	def f模式_网络时间协议(self, a端, a操作 = 操作.E操作.e设置):
		from . import 网络时间协议 as 实现协议
		return 实现协议.f模式(self, a端, 实现协议.C客户端sv3, None, a操作)
	def f模式_简单网络管理协议(self, a端, a操作 = 操作.E操作.e设置):
		from . import 简单网络管理协议
		if a端 == 操作.E端.e代理:
			return 简单网络管理协议.C代理配置sv3(self)
		elif a端 == 操作.E端.e陷阱:
			return 简单网络管理协议.C陷阱配置sv3(self)
		else:
			raise ValueError("a端 必需是代理或陷阱")
