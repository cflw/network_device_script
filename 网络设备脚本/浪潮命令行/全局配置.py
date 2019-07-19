from ..基础接口 import 操作
from ..命令行接口 import 全局配置
from . import 接口 as 实现接口
class C全局配置cnv7(全局配置.I全局配置):
	"""适用于: cn8672(v7.x), cn8696(v7.x), cn61108(v7.x)"""
	def __init__(self, a):
		全局配置.I全局配置.__init__(self, a)
	def fg进入命令(self):
		return "configure terminal"
	#模式
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间cnv7(self)
	def f模式_日志(self):
		from . import 日志
		return 日志.C日志cnv7(self)
	#路由
	def f模式_热备份路由协议(self, a接口, a组号, a操作 = 操作.E操作.e设置):
		from . import 热备份路由协议 as 实现协议
		v接口 = 实现接口.f创建接口(a接口)
		return 实现协议.C接口配置cnv7(self, v接口, a组号)
class C全局配置cnv6(全局配置.I全局配置):
	"""适用于: cn61108(v6.x)"""
	def __init__(self, a):
		全局配置.I全局配置.__init__(self, a)
	def fg进入命令(self):
		return "configure terminal"
	#模式
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间cnv6(self)
	def f模式_日志(self):
		from . import 日志
		return 日志.C日志cnv6(self)
class C全局配置sv3(全局配置.I全局配置):
	"""适用于: s6550(v3.x)"""
	def __init__(self, a):
		全局配置.I全局配置.__init__(self, a)
	def fg进入命令(self):
		return "config terminal"
	#模式
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间sv3(self.fg上级模式())
	def f模式_日志(self):
		from . import 日志
		return 日志.C日志sv3(self)
