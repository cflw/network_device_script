from ..基础接口 import 全局显示
from ..命令行接口 import 模式
from ..命令行接口 import 命令
from ..命令行接口 import 显示
from . import 基本表信息
from . import 路由表信息
c命令_接口状态表 = "show interface status"
c命令_网络接口表4 = "show ip interface brief"
c命令_网络接口表6 = "show ipv6 interface brief"
c命令_地址解析表 = "show ip arp"
c命令_物理地址表 = "show mac address-table"
c命令_路由表4 = "show ip route"
def f解析虚拟路由转发(a虚拟路由转发):
	vt虚拟路由转发 = type(a虚拟路由转发)
	if vt虚拟路由转发 == bool:
		if a虚拟路由转发:
			return "vrf all"
		else:
			return ""
	elif vt虚拟路由转发 == str:
		return "vrf " + a虚拟路由转发
	else:
		ValueError("无法识别的类型")
class C全局显示_nv7_0(全局显示.I全局显示, 模式.I显示模式):
	"""适用于: 思科n9k系列(v7.0.*), 
	浪潮cn61108pcv(v7.0)"""
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	#设备
	def f模式_设备(self):
		from . import 设备模式
		return 设备模式.C设备显示_nv7_0(self)
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间显示_nv7(self)
	#配置
	def f显示_启动配置(self):
		v输出 = self.m设备.f执行显示命令("show startup-config")
		return v输出
	def f显示_当前配置(self):
		v输出 = self.m设备.f执行显示命令("show running-config")
		return v输出
	#表格
	f显示_接口表 = 显示.F显示并解析(c命令_接口状态表, 基本表信息.f接口状态表_nv7)
	f显示_物理地址表 = 显示.F显示并解析(c命令_物理地址表, 基本表信息.f物理地址表_nv7)
	def f显示_网络接口表4(self, a虚拟路由转发 = True):
		v命令 = 命令.C命令(c命令_网络接口表4)
		v命令 += f解析虚拟路由转发(a虚拟路由转发)
		v输出 = self.m设备.f执行显示命令(v命令)
		v表 = 基本表信息.f网络接口表4全部_nv7(v输出)
		return v表
	def f显示_地址解析表(self, a虚拟路由转发 = True):
		v命令 = 命令.C命令(c命令_地址解析表)
		v命令 += f解析虚拟路由转发(a虚拟路由转发)
		v输出 = self.m设备.f执行显示命令(v命令)
		v表 = 基本表信息.f地址解析表_nv7(v输出)
		return v表
	def f显示_路由表4(self, a虚拟路由转发 = True):
		v命令 = 命令.C命令(c命令_路由表4)
		v命令 += f解析虚拟路由转发(a虚拟路由转发)
		v输出 = self.m设备.f执行显示命令(v命令)
		v表 = 路由表信息.f路由表4全部_nv7(v输出)
		return v表
	#数据结构
	def f显示_访问控制列表摘要(self, a名称 = None):
		from . import 访问控制列表 as 实现列表
		v命令 = "show access-lists summary | include ACL"
		if a名称:
			v命令 += f".{a名称}"
			v输出 = self.m设备.f执行显示命令(v命令)
			return 实现列表.f解析访问列表摘要开头(v输出)
		else:
			v输出 = self.m设备.f执行显示命令(v命令)
			return 实现列表.f解析访问列表摘要(v输出)
	def f模式_访问控制列表(self, a名称, a类型 = None):
		"""适用于: 浪潮cn8696q(v7.3)"""
		from ..基础接口 import 访问控制列表 as 北向列表
		from ..命令行接口 import 访问控制列表 as 南向列表
		from ..思科命令行 import 访问控制列表 as 旧列表
		from . import 访问控制列表 as 实现列表
		v名称, v类型 = 南向列表.f解析名称和类型(a名称, a类型, 旧列表.C助手)
		v输出 = None	#显示缓存
		if v类型 == None:
			v输出 = self.m设备.f执行显示命令(f"show access-lists {a名称}")	#不存在显示空
			if not v输出:
				return None
			v类型 = 实现列表.f解析访问控制列表类型_nv7(v输出)
		#创建访问控制列表对象
		if v类型 in (北向列表.E类型.e标准4, 北向列表.E类型.e扩展4):
			v模式 = 实现列表.C四显示(self, v名称, a列表缓存 = v输出)
		elif v类型 in (北向列表.E类型.e标准6, 北向列表.E类型.e扩展6):
			v模式 = 旧列表.C六显示(self, v名称, a列表缓存 = v输出)	#未实现,先用旧的
		else:
			raise ValueError("未知的访问控制列表类型")
		return v模式
	#服务
	def f模式_安全外壳(self):
		from . import 安全外壳
		return 安全外壳.C安全外壳显示(self)
class C全局显示_nv7_3(C全局显示_nv7_0):
	"""适用于: 思科n7k(v7.3.*), 
	浪潮cn8672up(v7.3), 浪潮cn8696q(v7.3)"""
	def __init__(self, a):
		C全局显示_nv7_0.__init__(self, a)
class C全局显示_nv9_2(C全局显示_nv7_3):
	"""适用于: 浪潮cn61108pcv(v9.2.3)"""
	def __init__(self, a):
		C全局显示_nv7_3.__init__(self, a)
	#设备
	def f模式_设备(self):
		from . import 设备模式
		return 设备模式.C设备显示nv9_2(self)
	#表格
	f显示_物理地址表 = 显示.F显示并解析(c命令_物理地址表, 基本表信息.f物理地址表_nv9)
	#数据结构
	def f模式_访问控制列表(self, a名称, a类型 = None):
		"""适用于: 浪潮cv61108pcv(v9.2.3)"""
		from ..基础接口 import 访问控制列表 as 北向列表
		from ..命令行接口 import 访问控制列表 as 南向列表
		from ..思科命令行 import 访问控制列表 as 旧列表
		from . import 访问控制列表 as 实现列表
		v名称, v类型 = 南向列表.f解析名称和类型(a名称, a类型, 旧列表.C助手)
		v输出 = None	#显示缓存
		if v类型 == None:
			v输出 = self.m设备.f执行显示命令(f"show access-lists {a名称}")	#不存在显示空
			if not v输出:
				return None
			v类型 = 实现列表.f解析访问控制列表类型_nv9(v输出)
		#创建访问控制列表对象
		if v类型 in (北向列表.E类型.e标准4, 北向列表.E类型.e扩展4):
			v模式 = 实现列表.C四显示(self, v名称, a列表缓存 = v输出)
		elif v类型 in (北向列表.E类型.e标准6, 北向列表.E类型.e扩展6):
			v模式 = 旧列表.C六显示(self, v名称, a列表缓存 = v输出)	#未实现,先用旧的
		else:
			raise ValueError("未知的访问控制列表类型")
		return v模式
