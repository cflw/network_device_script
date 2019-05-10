from ..命令行接口 import 全局配置
from ..基础接口 import 操作
from ..基础接口 import 协议
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
	def f模式_接口(self, a接口):
		v接口 = 接口.f创建接口(a接口)
		return 接口.C接口(self, v接口)
	def f模式_用户(self, a用户名):
		if self.m设备.m型号 == E型号.s2126:
			return 用户.C用户s2126(self, a用户名)
		return 用户.C用户v5(self, a用户名)
	def f模式_登录(self, a方式, a范围 = 0, a操作 = 操作.E操作.e设置):	#console,vty之类的
		return 登陆.C登录(self, a方式, a范围)
	def f模式_时间范围(self, a名称):
		return 时间范围.C时间范围(self, a名称)
	def f模式_虚拟局域网(self, a序号):	#vlan
		raise NotImplementedError()
	#其它
	def f模式_访问控制列表(self, a名称, a类型 = None, a操作 = 操作.E操作.e设置):
		v名称, v类型 = 通用访问列表.f解析名称和类型(a名称, a类型, 访问控制列表.C助手)
		if v类型 == 北向列表.E类型.e标准4:
			return 访问控制列表.C基本4v5(self, v名称)
		elif v类型 == 北向列表.E类型.e扩展4:
			return 访问控制列表.C高级4v5(self, v名称)
		elif v类型 == 北向列表.E类型.e标准6:
			return 访问控制列表.C基本6v5(self, v名称)
		elif v类型 == 北向列表.E类型.e扩展6:
			return 访问控制列表.C高级6v5(self, v名称)
		else:
			raise ValueError("错误的类型")
	#设备配置
	def fs设备名(self, a名称):
		v命令 = 命令.C命令("sysname")
		v命令 += a名称
		self.f执行当前模式命令(a名称)
class C系统视图v7(全局配置.I全局配置):
	"""system-view
	适用于: v7"""
	def __init__(self, a):
		全局配置.I全局配置.__init__(self, a)
	def fg进入命令(self):
		return "system-view"
	def f显示_当前模式配置(self):
		return self.m设备.f执行显示命令("display current-configuration configuration system")
	#模式
	def f模式_接口(self, a接口):
		v接口 = 接口.f创建接口(a接口)
		return 接口.C接口(self, v接口)
	def f模式_用户(self, a用户名):
		if self.m设备.m版本 < 7.1:
			return 用户.C用户v7(self, a用户名)
		else:
			return 用户.C用户v7_1(self, a用户名)
	def f模式_登录(self, a方式, a范围, a操作 = 操作.E操作.e设置):
		return 登录.C登录v7(self, a方式, a范围)
	def f模式_访问控制列表(self, a名称, a类型 = None, a操作 = 操作.E操作.e设置):
		v名称, v类型 = 通用访问列表.f解析名称和类型(a名称, a类型, 访问控制列表.C助手)
		if v类型 == 北向列表.E类型.e标准4:
			return 访问控制列表.C基本4v7(self, v名称)
		elif v类型 == 北向列表.E类型.e扩展4:
			return 访问控制列表.C高级4v7(self, v名称)
		elif v类型 == 北向列表.E类型.e标准6:
			return 访问控制列表.C基本6v7(self, v名称)
		elif v类型 == 北向列表.E类型.e扩展6:
			return 访问控制列表.C高级6v7(self, v名称)
		else:
			raise ValueError("错误的类型")
	#操作
	def fs设备名(self, a名称):
		v命令 = 命令.C命令("sysname")
		v命令 += a名称
		self.f执行当前模式命令(a名称)
