from ..命令行接口 import 全局配置
from ..基础接口 import 操作
from ..思科命令行.常量 import *
class C全局配置(全局配置.I全局配置):
	"""适用于: sm4120(v6.6.4.1.3)"""
	def __init__(self, a):
		全局配置.I全局配置.__init__(self, a)
	#命令
	def fg进入命令(self):
		return "configure terminal"
	#模式
	def f模式_接口(self, a接口, a操作 = 操作.E操作.e设置):
		from ..思科命令行 import 接口
		v接口 = 接口.f创建接口(a接口)
		return 接口.C接口配置(self, v接口)
class C全局配置_v9(C全局配置):
	"""适用于: 迈普t6100(v9.3.4.45)"""
	def f模式_访问控制列表(self, a名称, a类型 = None, a操作 = 操作.E操作.e设置):
		from ..基础接口 import 访问控制列表 as 北向列表
		from ..命令行接口 import 访问控制列表 as 南向列表
		from . import 访问控制列表 as 实现列表
		v名称, v类型 = 南向列表.f解析名称和类型(a名称, a类型, 实现列表.C助手)
		if v类型 == 北向列表.E类型.e标准4:
			return 实现列表.C标准4配置(self, v名称)
		elif v类型 == 北向列表.E类型.e扩展4:
			return 实现列表.C扩展4配置(self, v名称)
		elif v类型 == 北向列表.E类型.e标准6:
			raise NotImplementedError()
		elif v类型 == 北向列表.E类型.e扩展6:
			raise NotImplementedError()
		else:
			raise ValueError("错误的类型")
