from ..命令行接口 import 全局配置
from ..基础接口 import 操作
from ..基础接口 import 协议
from ..命令行接口 import 路由 as 南向路由
from . import 实用 as 思科实用
from . import 接口 as 实现接口
class C全局配置(全局配置.I全局配置):
	c进入命令 = "configure terminal"
	def __init__(self, a):
		全局配置.I全局配置.__init__(self, a)
	#模式
	def fg进入命令(self):
		return C全局配置.c进入命令
	#基本模式
	def f模式_接口(self, a接口, a操作 = 操作.E操作.e设置):
		from ..命令行接口 import 接口 as 南向接口
		if isinstance(a接口, 南向接口.I接口配置):
			if not a接口.m设备 is self.m设备:
				raise ValueError("设备不匹配")
			v模式 = a接口
		else:
			v接口 = 实现接口.f创建接口(a接口)
			v模式 = 实现接口.C接口配置(self, v接口)
		思科实用.f执行模式操作命令(self, v模式, a操作)
		return v模式
	def f模式_用户(self, a, a操作 = 操作.E操作.e设置):
		from . import 用户 as 实现用户
		from ..基础接口 import 用户 as 北向用户
		if isinstance(a, 北向用户.I用户配置):
			if not a.m设备 is self.m设备:
				raise ValueError("设备不匹配")
			v模式 = a
		else:
			v模式 = 实现用户.C用户配置(self, a)
		if a操作 == 操作.E操作.e删除:
			v命令 = v模式.fg删除命令()
			self.f执行当前模式命令(v命令)
		return v模式
	def f模式_登录(self, a方式, a范围 = 0, a操作 = 操作.E操作.e设置):
		from . import 登录 as 登录
		return 登录.C登录(self, a方式, a范围)
	def f模式_时间范围(self, a, a操作 = 操作.E操作.e设置):
		from . import 时间范围 as 时间范围
		return 时间范围.C时间范围(self, a)
	def f模式_访问控制列表(self, a名称, a类型 = None, a操作 = 操作.E操作.e设置):
		from ..基础接口 import 访问控制列表 as 北向列表
		from ..命令行接口 import 访问控制列表 as 南向列表
		from . import 访问控制列表 as 实现列表
		v名称, v类型 = 南向列表.f解析名称和类型(a名称, a类型, 实现列表.C助手)
		#创建访问控制列表对象
		if v类型 == 北向列表.E类型.e标准4:
			实现列表.fi标准范围(v名称)
			v模式 = 实现列表.C标准4(self, v名称)
		elif v类型 == 北向列表.E类型.e扩展4:
			实现列表.fi扩展范围(v名称)
			v模式 = 实现列表.C扩展4(self, v名称)
		elif v类型 in (北向列表.E类型.e标准6, 北向列表.E类型.e扩展6):
			v模式 = 实现列表.C六(self, v名称)
		else:
			raise ValueError("未知的访问控制列表类型")
		if a操作 == 操作.E操作.e删除:
			v命令 = c不 + v模式.fg进入命令()
			self.f执行当前模式命令(v命令)
		elif a操作 == 操作.E操作.e重置:
			v命令 = c默认 + v模式.fg进入命令()
			self.f执行当前模式命令(v命令)
		return v模式
	def f模式_前缀列表(self, a名称, a类型 = 协议.E协议.e网络协议4, a操作 = 操作.E操作.e设置):
		from . import 前缀列表 as 实现列表
		if a类型 == 协议.E协议.e网络协议4:
			return 实现列表.C四(self, a名称)
		elif a类型 == 协议.E协议.e网络协议6:
			return 实现列表.C六(self, a名称)
		else:
			raise ValueError("错误的 a类型")
	def f模式_钥匙链(self, a名称, a操作 = 操作.E操作.e设置):
		from . import 钥匙链
		return 钥匙链.C钥匙链(self, a名称)
	#路由
	def f模式_静态路由(self, a版本 = 协议.E协议.e网络协议4, a虚拟路由转发 = None):
		from . import 静态路由
		v版本 = 南向路由.f解析网络协议版本(a版本)
		if v版本 == 协议.E协议.e网络协议4:
			return 静态路由.C静态路由4(self)
		elif v版本 == 协议.E协议.e网络协议6:
			raise NotImplementedError()
		else:
			raise ValueError("未知的版本")
	def f模式_路由信息协议(self, a进程号 = 0, a版本 = 协议.E协议.e路由信息协议, a接口 = None, a操作 = 操作.E操作.e设置):	#rip
		from . import 路由信息协议
		v版本 = 南向路由.f解析路由信息协议版本(a版本)
		if v版本 == 协议.E协议.e路由信息协议:	#rip
			return 路由信息协议.C当代(self)
		elif v版本 == 协议.E协议.e下一代路由信息协议:	#ripng
			v进程号 = str(a进程号)
			if not v进程号:
				raise ValueError("当版本为ripng时,必须指定进程号")
			return 路由信息协议.C下代(self, a进程号)
		else:
			raise ValueError("未知的版本")
	def f模式_开放最短路径优先(self, a进程号 = 1, a版本 = 协议.E协议.e开放最短路径优先, a接口 = None, a操作 = 操作.E操作.e设置):
		from . import 开放最短路径优先
		v版本 = 南向路由.f解析开放最短路径优先版本(a版本)
		if a接口:	#有接口
			v接口 = 实现接口.f创建接口(a接口)
			if a版本 == 协议.E协议.e开放最短路径优先2:
				return 开放最短路径优先.C接口4(self, a进程号, v接口)
			elif a版本 == 协议.E协议.e开放最短路径优先3:
				raise NotImplementedError()
			else:
				raise ValueError("未知的版本")
		#没有接口
		if a版本 == 协议.E协议.e开放最短路径优先2:
			return 开放最短路径优先.C路由配置(self, a进程号)
		elif a版本 == 协议.E协议.e开放最短路径优先3:
			raise NotImplementedError()
		else:
			raise ValueError("未知的版本")
	def f模式_增强内部网关路由协议(self, a, a版本 = 协议.E协议.e网络协议4, a接口 = None, a操作 = 操作.E操作.e设置):	#eigrp
		from . import 增强内部网关路由协议
		v版本 = 南向路由.f解析网络协议版本(a版本)
		if v版本 == 协议.E协议.e网络协议4:
			return 增强内部网关路由协议.C经典(self, a)
		elif v版本 == 协议.E协议.e网络协议6:
			raise NotImplementedError()
		else:
			raise ValueError("未知的版本")
	def f模式_边界网关协议(self, a自治系统号, a操作 = 操作.E操作.e设置):
		from . import 边界网关协议
		return 边界网关协议.C路由(self, a自治系统号)
	#服务
	def f模式_动态主机配置协议地址池(self, a名称):
		from . import 动态主机配置协议
		return 动态主机配置协议.C地址池4(self, a名称)
	def f模式_动态主机配置协议(self):
		from . import 动态主机配置协议
		return 动态主机配置协议.C服务4(self)
	#全局配置
	def fs设备名(self, a名称):
		v命令 = "hostname " + str(a名称)
		self.f执行当前模式命令(v命令)
	#其它
	def fs域名(self, a名称 = "a"):
		v命令 = "ip domain-name" + str(a名称)
		self.f执行当前模式命令(v命令)
