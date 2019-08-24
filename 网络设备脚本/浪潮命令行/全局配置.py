from ..基础接口 import 操作
from ..基础接口 import 协议
from ..命令行接口 import 全局配置
from . import 接口 as 实现接口
#===============================================================================
# cn系列(v7.x)
#===============================================================================
class C全局配置cnv7_0(全局配置.I全局配置):
	"""适用于: cn61108(v7.0)"""
	def __init__(self, a):
		全局配置.I全局配置.__init__(self, a)
	def fg进入命令(self):
		return "configure terminal"
	#模式
	def f模式_用户(self, a用户名, a操作 = 操作.E操作.e设置):
		from . import 用户
		return 用户.C用户cnv7(self, a用户名)
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间cnv7(self)
	def f模式_日志(self):
		from . import 日志
		return 日志.C日志cnv7(self)
	#路由
	def f模式_静态路由(self, a版本 = 协议.E协议.e网络协议4, a虚拟路由转发 = None):
		from . import 静态路由
		if a版本 == 协议.E协议.e网络协议4:
			if a虚拟路由转发:
				v模式 = 静态路由.C虚拟路由静态路由cnv7(self, a虚拟路由转发)
			else:
				v模式 = 静态路由.C静态路由cnv7(self)
		elif a版本 == 协议.E协议.e网络协议6:
			raise NotImplementedError()
		else:
			raise ValueError("未知的版本")
		return v模式
	def f模式_热备份路由协议(self, a接口, a组号, a操作 = 操作.E操作.e设置):
		from . import 热备份路由协议 as 实现协议
		v接口 = 实现接口.f创建接口(a接口)
		return 实现协议.C接口配置cnv7(self, v接口, a组号)
	#服务
	def f模式_网络时间协议(self, a端, a操作 = 操作.E操作.e设置):
		from . import 网络时间协议 as 实现协议
		return 实现协议.f模式(self, a端, 实现协议.C客户端cnv7_0, None, a操作)
	def f模式_简单网络管理协议(self, a端, a操作 = 操作.E操作.e设置):
		from ..思科命令行 import 简单网络管理协议
		if a端 == 操作.E端.e代理:
			return 简单网络管理协议.C代理配置(self)
		elif a端 == 操作.E端.e陷阱:
			return 简单网络管理协议.C陷阱配置(self)
		else:
			raise ValueError("a端 必需是代理或陷阱")
class C全局配置cnv7_3(C全局配置cnv7_0):
	"""适用于: cn8672(v7.3), cn8696(v7.3)"""
	def __init__(self, a):
		C全局配置cnv7_0.__init__(self, a)
	def f模式_网络时间协议(self, a端, a操作 = 操作.E操作.e设置):
		from . import 网络时间协议 as 实现协议
		return 实现协议.f模式(self, a端, 实现协议.C客户端cnv7_3, None, a操作)
#===============================================================================
# cn系列(v6.x)
#===============================================================================
class C全局配置cnv6(全局配置.I全局配置):
	"""适用于: cn61108(v6.x)"""
	def __init__(self, a):
		全局配置.I全局配置.__init__(self, a)
	def fg进入命令(self):
		return "configure terminal"
	#模式
	def f模式_用户(self, a用户名, a操作 = 操作.E操作.e设置):
		from . import 用户
		return 用户.C用户cnv6(self, a用户名)
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间cnv6(self)
	def f模式_日志(self):
		from . import 日志
		return 日志.C日志cnv6(self)
	#服务
	def f模式_网络时间协议(self, a端, a操作 = 操作.E操作.e设置):
		from . import 网络时间协议 as 实现协议
		return 实现协议.f模式(self, a端, 实现协议.C客户端cnv6, None, a操作)
	def f模式_简单网络管理协议(self, a端, a操作 = 操作.E操作.e设置):
		from . import 简单网络管理协议
		if a端 == 操作.E端.e代理:
			return 简单网络管理协议.C代理配置cnv6(self)
		elif a端 == 操作.E端.e陷阱:
			return 简单网络管理协议.C陷阱配置cnv6(self)
		else:
			raise ValueError("a端 必需是代理或陷阱")
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
