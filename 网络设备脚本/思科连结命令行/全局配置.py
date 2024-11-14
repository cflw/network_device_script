from ..命令行接口 import 全局配置
from ..基础接口 import 操作
from ..基础接口 import 协议
from ..命令行接口 import 路由 as 南向路由
from ..思科命令行 import 实用 as 思科实用
from ..思科命令行.常量 import *
from . import 接口 as 实现接口
class C全局配置nv7_0(全局配置.I全局配置):
	"""适用于: 思科nexus9000(v7.0), 浪潮cn61108pcv(v7.0)"""
	def __init__(self, a):
		全局配置.I全局配置.__init__(self, a)
	def fg进入命令(self):
		return "configure terminal"
	#模式
	def f模式_用户(self, a用户名, a操作 = 操作.E操作.e设置):
		from . import 用户
		v操作 = 操作.f解析操作(a操作)
		v模式 = 用户.C用户nv7(self, a用户名)
		if 操作.fi减操作(v操作):
			self.f执行当前模式命令(v模式.fg删除命令())
		return v模式
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间_nv7(self)
	def f模式_日志(self):
		from . import 日志
		return 日志.C日志nv7(self)
	def f模式_接口(self, a接口, a操作 = 操作.E操作.e设置):
		from ..思科命令行 import 接口 as 旧实现接口
		from ..命令行接口 import 接口 as 南向接口
		if isinstance(a接口, 南向接口.I接口配置):
			if not a接口.m设备 is self.m设备:
				raise ValueError("设备不匹配")
			v模式 = a接口
		else:
			v接口 = 实现接口.f创建接口_nv7(a接口)
			v模式 = 旧实现接口.C接口配置(self, v接口)
		思科实用.f执行模式操作命令(self, v模式, a操作)
		return v模式
	#数据结构
	def f模式_访问控制列表(self, a名称, a类型 = None, a操作 = 操作.E操作.e设置):
		from ..基础接口 import 访问控制列表 as 北向列表
		from ..命令行接口 import 访问控制列表 as 南向列表
		from ..思科命令行 import 访问控制列表 as 旧列表
		from . import 访问控制列表 as 实现列表
		v名称, v类型 = 南向列表.f解析名称和类型(a名称, a类型, 旧列表.C助手)
		#创建访问控制列表对象
		if v类型 in (北向列表.E类型.e标准4, 北向列表.E类型.e扩展4):
			v模式 = 实现列表.C四配置(self, v名称)
		elif v类型 in (北向列表.E类型.e标准6, 北向列表.E类型.e扩展6):
			v模式 = 旧列表.C六配置(self, v名称)
		else:	#没有类型,默认ipv4
			v模式 = 实现列表.C四配置(self, v名称)
		if a操作 == 操作.E操作.e删除:
			v命令 = c不 + v模式.fg进入命令()
			self.f执行当前模式命令(v命令)
		elif a操作 == 操作.E操作.e重置:
			v命令 = c默认 + v模式.fg进入命令()
			self.f执行当前模式命令(v命令)
		return v模式
	#路由
	def f模式_静态路由(self, a版本 = 协议.E协议.e网络协议4, a虚拟路由转发 = None):
		from . import 静态路由
		if a版本 == 协议.E协议.e网络协议4:
			if a虚拟路由转发:
				v模式 = 静态路由.C虚拟路由静态路由nv7(self, a虚拟路由转发)
			else:
				v模式 = 静态路由.C静态路由nv7(self)
		elif a版本 == 协议.E协议.e网络协议6:
			raise NotImplementedError()
		else:
			raise ValueError("未知的版本")
		return v模式
	def f模式_热备份路由协议(self, a接口, a组号, a操作 = 操作.E操作.e设置):
		from . import 热备份路由协议 as 实现协议
		v接口 = 实现接口.f创建接口_nv7(a接口)
		return 实现协议.C接口配置nv7(self, v接口, a组号)
	def f模式_虚拟路由器冗余协议(self, a接口, a组号, a操作 = 操作.E操作.e设置):
		from . import 虚拟路由器冗余协议 as 实现协议
		v接口 = 实现接口.f创建接口_nv7(a接口)
		v模式 = 实现协议.C接口(self, v接口, a组号)
		return v模式
	#服务
	def f模式_网络终端(self):
		from ..思科命令行 import 网络终端
		return 网络终端.C网络终端配置(self)
	def f模式_安全外壳(self):
		from .import 安全外壳
		return 安全外壳.C安全外壳配置(self)
	def f模式_网络时间协议(self, a端, a操作 = 操作.E操作.e设置):
		from . import 网络时间协议 as 实现协议
		return 实现协议.f模式(self, a端, 实现协议.C客户端nv7_0, None, a操作)
	def f模式_简单网络管理协议(self, a端, a操作 = 操作.E操作.e设置):
		from ..思科命令行 import 简单网络管理协议
		if a端 == 操作.E端.e代理:
			return 简单网络管理协议.C代理配置(self)
		elif a端 == 操作.E端.e陷阱:
			return 简单网络管理协议.C陷阱配置(self)
		else:
			raise ValueError("a端 必需是代理或陷阱")
class C全局配置nv7_3(C全局配置nv7_0):
	"""适用于: 浪潮cn8672(v7.3), 浪潮cn8696(v7.3)"""
	def __init__(self, a):
		C全局配置nv7_0.__init__(self, a)
	def f模式_网络时间协议(self, a端, a操作 = 操作.E操作.e设置):
		from . import 网络时间协议 as 实现协议
		return 实现协议.f模式(self, a端, 实现协议.C客户端nv7_3, None, a操作)
class C全局配置nv9_2(C全局配置nv7_3):
	"""适用于: 浪潮cn61108pcv(v9.2.3)"""