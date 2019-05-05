from ..命令行接口 import 全局配置
from ..基础接口 import 操作
from ..基础接口 import 协议
from . import 实用 as 华为实用
# from . import 接口 as 接口
class C系统视图(全局配置.I全局配置模式):
	def __init__(self, a):
		全局配置.I全局配置模式.__init__(self, a)
	def fg进入命令(self):
		return "system-view"
	def f事件_退出模式(self):
		self.m设备.f自动提交(操作.E自动提交.e退出配置模式时)
	#模式
	def f模式_接口(self, a接口):
		v接口 = 接口.f创建接口(a接口)
		#检查值
		if v接口.fi属于分类(接口.E接口分类.e以太网):
			if v接口.fg主序号数() != 3:
				raise ValueError("在华为设备,接口序号有3段")
			elif v接口.fi范围():
				return C端口组(self, v接口)
		if v接口.fi属于分类(接口.E接口分类.e环回):
			if v接口.fg主序号数() != 1:
				raise ValueError("环回口的序号只有1段")
		return 接口.C接口视图(self, v接口)
	def f模式_登录(self, a方式, a范围 = 0, a操作 = 操作.E操作.e设置):
		return 登录.C登录(self, a方式, a范围)
	def f模式_虚拟局域网(self, a序号, a操作 = 操作.E操作.e设置):	#vlan
		v类型 = type(a序号)
		if v类型 == int:
			return 虚拟局域网.C配置(self, a序号)
		elif v类型 == 接口.S接口:
			return 接口.C虚拟局域网(self, a序号)
		elif isinstance(a序号, 接口配置.I接口配置模式基础):
			return 接口.C虚拟局域网(self, a序号.m接口)
		else:
			raise ValueError()
	#路由
	def f模式_静态路由(self, a版本 = 协议.E协议.e网络协议4, a虚拟路由转发 = None):
		v版本 = 通用路由.f解析网络协议版本(a版本)
		if v版本 == 协议.E协议.e网络协议4:
			return 静态路由.C静态路由4(self)
		elif v版本 == 协议.E协议.e网络协议6:
			raise NotImplementedError()
		else:
			raise ValueError("未知的版本")
	def f模式_开放最短路径优先(self, a进程号 = 1, a版本 = 协议.E协议.e开放最短路径优先, a接口 = None, a操作 = 操作.E操作.e设置):
		if a接口:	#有接口
			v接口 = 接口.f创建接口(a接口)
			if a版本 == 协议.E协议.e开放最短路径优先2:
				return 开放最短路径优先.C接口4(self, a进程号, a接口)
			elif a版本 == 协议.E协议.e开放最短路径优先3:
				raise NotImplementedError()
			else:
				raise ValueError()
		#没有接口
		if a版本 == 协议.E协议.e开放最短路径优先2:
			return 开放最短路径优先.C路由4(self, a进程号)
		elif a版本 == 协议.E协议.e开放最短路径优先3:
			raise NotImplementedError()
		else:
			raise ValueError()
	#其它
	def f模式_访问控制列表(self, a名称, a类型 = None, a操作 = 操作.E操作.e设置):
		v名称, v类型 = 通用访问列表.f解析名称和类型(a名称, a类型, 访问控制列表.C助手)
		if v类型 == 设备.E访问控制列表类型.e标准4:
			return 访问控制列表.C基本4(self, v名称)
		elif v类型 == 设备.E访问控制列表类型.e扩展4:
			return 访问控制列表.C高级4(self, v名称)
		elif v类型 == 设备.E访问控制列表类型.e标准6:
			return 访问控制列表.C基本6(self, v名称)
		elif v类型 == 设备.E访问控制列表类型.e扩展6:
			return 访问控制列表.C高级6(self, v名称)
		else:
			raise ValueError("错误的类型")
	def f模式_前缀列表(self, a名称, a类型 = 协议.E协议.e网络协议4):
		if a类型 == 协议.E协议.e网络协议4:
			return 前缀列表.C前缀列表(self, a名称, 前缀列表.c版本4, 地址.S网络地址4)
		elif a类型 == 协议.E协议.e网络协议6:
			return 前缀列表.C前缀列表(self, a名称, 前缀列表.c版本6, 地址.S网络地址6)
		else:
			raise ValueError("错误的类型")
	#配置
	def fs设备名(self, a名称):
		self.f执行当前模式命令("sysname " + str(a名称))
