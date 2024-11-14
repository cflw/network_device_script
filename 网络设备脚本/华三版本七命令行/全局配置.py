from ..基础接口 import 操作
from ..命令行接口 import 命令
from ..华三命令行 import 全局配置 as 旧全局配置
from . import 接口 as 实现接口
class C系统视图_v7(旧全局配置.C系统视图):
	"""system-view
	适用于: 华三s5820v2(v7.1.075)"""
	def __init__(self, a):
		旧全局配置.C系统视图.__init__(self, a)
	def fg进入命令(self):
		return "system-view"
	def f显示_当前模式配置(self):
		return self.m设备.f执行显示命令("display current-configuration configuration system")
	#模式
	def f模式_接口(self, a接口, a操作 = 操作.E操作.e设置):
		v接口 = 实现接口.f创建接口v7(a接口)
		return 实现接口.C接口v7(self, v接口)
	def f模式_用户(self, a用户名, a操作 = 操作.E操作.e设置):
		from . import 用户 as 用户
		v次版本 = self.m设备.m版本[1]
		if v次版本 < 1:	#版本 <= 7.0
			return 用户.C用户v7(self, a用户名)
		else:	#版本 >= 7.1
			return 用户.C用户v7_1(self, a用户名)
	def f模式_登录(self, a方式, a范围, a操作 = 操作.E操作.e设置):	#废弃
		from . import 登录
		return 登录.C登录v7(self, a方式, a范围)
	def f模式_远程登录(self, a协议, a范围, a操作 = 操作.E操作.e设置):
		from . import 登录
		v模式 = 登录.C远程登录配置_v7(self, a协议, a范围)
		return v模式
	def f模式_时间范围(self, a名称, a操作 = 操作.E操作.e设置):
		from ..华三命令行 import 时间范围
		return 时间范围.C时间范围(self, a名称)
	def f模式_访问控制列表(self, a名称, a类型 = None, a操作 = 操作.E操作.e设置):
		from ..基础接口 import 访问控制列表 as 北向列表
		from ..命令行接口 import 访问控制列表 as 南向列表
		from . import 访问控制列表 as 实现列表
		v名称, v类型 = 南向列表.f解析名称和类型(a名称, a类型, 实现列表.C助手)
		if v类型 == 北向列表.E类型.e标准4:
			return 实现列表.C基本4配置_v7(self, v名称)
		elif v类型 == 北向列表.E类型.e扩展4:
			return 实现列表.C高级4配置_v7(self, v名称)
		elif v类型 == 北向列表.E类型.e标准6:
			return 实现列表.C基本6配置_v7(self, v名称)
		elif v类型 == 北向列表.E类型.e扩展6:
			return 实现列表.C高级6配置_v7(self, v名称)
		else:
			raise ValueError("错误的类型")
	#服务
	def f模式_安全外壳(self):
		from . import 安全外壳
		return 安全外壳.C安全外壳配置_v7(self)
	def f模式_网络时间协议(self, a端, a操作 = 操作.E操作.e设置):
		from ..华三命令行 import 网络时间协议
		if a端 == 操作.E端.e服务器:
			return 网络时间协议.C服务器(self)
		elif a端 == 操作.E端.e客户端:
			return 网络时间协议.C客户端(self)
		else:
			raise ValueError("a端 必需是服务器或客户端")
	def f模式_简单网络管理协议(self, a端 = 操作.E端.e代理, a操作 = 操作.E操作.e设置):
		from . import 简单网络管理协议
		if a端 == 操作.E端.e代理:
			return 简单网络管理协议.C代理v7(self)
		elif a端 == 操作.E端.e陷阱:
			return 简单网络管理协议.C陷阱v7(self)
		else:
			raise ValueError("a端 必需是代理或陷阱")
	#链路层
	def f模式_链路层发现协议(self, a接口 = None, a操作 = 操作.E操作.e设置):
		from . import 链路层发现协议
		if a接口:
			v接口 = 实现接口.f创建接口v7(a接口)
			return 链路层发现协议.C接口配置_v7(self, v接口)
		return 链路层发现协议.C进程配置_v7(self)
	#操作
	def fs设备名(self, a名称, a操作 = 操作.E操作.e设置):
		v命令 = 命令.C命令("sysname")
		v命令 += a名称
		self.f执行当前模式命令(a名称)
