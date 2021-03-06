from ..基础接口 import 操作
from ..基础接口 import 协议
from ..命令行接口 import 全局配置
from .. import 华三
from . import 接口 as 实现接口
class C系统视图(全局配置.I全局配置):
	"""system-view
	适用于: v5之前"""
	def __init__(self, a):
		全局配置.I全局配置.__init__(self, a)
	def fg进入命令(self):
		return "system-view"
	#模式
	def f模式_时间(self):
		raise NotImplementedError()
	def f模式_接口(self, a接口, a操作 = 操作.E操作.e设置):
		v接口 = 实现接口.f创建接口(a接口)
		return 实现接口.C接口(self, v接口)
	def f模式_用户(self, a用户名, a操作 = 操作.E操作.e设置):
		from . import 用户 as 用户
		if self.m设备.m型号 == 华三.E型号.s2126:
			return 用户.C用户s2126(self, a用户名)
		return 用户.C用户v5(self, a用户名)
	def f模式_登录(self, a方式, a范围 = 0, a操作 = 操作.E操作.e设置):	#console,vty之类的
		from . import 登录
		return 登录.C登录(self, a方式, a范围)
	def f模式_时间范围(self, a名称, a操作 = 操作.E操作.e设置):
		from . import 时间范围
		return 时间范围.C时间范围(self, a名称)
	def f模式_虚拟局域网(self, a序号):	#vlan
		raise NotImplementedError()
	#其它
	def f模式_访问控制列表(self, a名称, a类型 = None, a操作 = 操作.E操作.e设置):
		from ..基础接口 import 访问控制列表 as 北向列表
		from ..命令行接口 import 访问控制列表 as 南向列表
		from . import 访问控制列表 as 实现列表
		v名称, v类型 = 南向列表.f解析名称和类型(a名称, a类型, 实现列表.C助手)
		if v类型 == 北向列表.E类型.e标准4:
			return 实现列表.C基本4v5(self, v名称)
		elif v类型 == 北向列表.E类型.e扩展4:
			return 实现列表.C高级4v5(self, v名称)
		elif v类型 == 北向列表.E类型.e标准6:
			return 实现列表.C基本6v5(self, v名称)
		elif v类型 == 北向列表.E类型.e扩展6:
			return 实现列表.C高级6v5(self, v名称)
		else:
			raise ValueError("错误的类型")
	#设备配置
	def fs设备名(self, a名称, a操作 = 操作.E操作.e设置):
		v命令 = 命令.C命令("sysname")
		v命令 += a名称
		self.f执行当前模式命令(a名称)