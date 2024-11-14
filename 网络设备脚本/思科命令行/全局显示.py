from ..基础接口 import 全局显示
from ..命令行接口 import 模式
from . import 基本表信息
from . import 路由表信息
class C全局显示(全局显示.I全局显示, 模式.I显示模式):
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	#模式
	def f模式_设备(self):
		from . import 设备模式
		return 设备模式.C设备显示(self)
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间显示(self)
	#配置
	def f显示_启动配置(self):
		v输出 = self.m设备.f执行显示命令("show startup-config")
		return v输出
	def f显示_当前配置(self):
		v输出 = self.m设备.f执行显示命令("show running-config")
		return v输出
	#表
	def f显示_接口详细(self):
		v输出 = self.m设备.f执行显示命令("show interface")
		return 基本表信息.f接口详细(v输出)
	def f显示_接口表(self):	#部分型号没有show interface status命令, 需修改
		v输出 = self.m设备.f执行显示命令("show interface status")
		return 基本表信息.f接口状态表_v11(v输出)
	def f显示_网络接口表4(self):
		v输出 = self.m设备.f执行显示命令("show ip interface brief")
		return 基本表信息.f网络接口表4(v输出)
	def f显示_网络接口表6(self):
		v输出 = self.m设备.f执行显示命令("show ipv6 interface brief")
		return 基本表信息.f网络接口表6(v输出)
	def f显示_地址解析表(self):
		v输出 = self.m设备.f执行显示命令("show ip arp")
		return 基本表信息.f地址解析表(v输出)
	def f显示_物理地址表(self):
		v输出 = self.m设备.f执行显示命令("show mac address-table")
		return 基本表信息.f物理地址表(v输出)
	def f显示_路由表4(self):
		v输出 = self.m设备.f执行显示命令("show ip route")
		return 路由表信息.f路由表4(v输出)
	def f显示_路由表6(self):
		v输出 = self.m设备.f执行显示命令("show ipv6 route")
		return 路由表信息.f路由表6(v输出)
	#数据结构
	def f显示_访问控制列表摘要(self, a名称 = None):
		from . import 访问控制列表 as 实现列表
		v命令 = "show access-lists | include access list"
		if a名称:
			v命令 += f" {a名称}"
			v输出 = self.m设备.f执行显示命令(v命令)	#不存在则输出空
			return 实现列表.f解析访问列表摘要开头(v输出)
		else:
			v输出 = self.m设备.f执行显示命令(v命令)
			return 实现列表.f解析访问列表摘要(v输出)
	def f模式_访问控制列表(self, a名称, a类型 = None):
		from ..基础接口 import 访问控制列表 as 北向列表
		from ..命令行接口 import 访问控制列表 as 南向列表
		from . import 访问控制列表 as 实现列表
		v名称, v类型 = 南向列表.f解析名称和类型(a名称, a类型, 实现列表.C助手)
		v输出 = None	#显示缓存
		if v类型 == None:
			v输出 = self.m设备.f执行显示命令(f"show access-lists {a名称}")
			if not v输出:
				return None
			v类型 = 实现列表.f解析访问控制列表类型(v输出)
		#创建访问控制列表对象
		if v类型 == 北向列表.E类型.e标准4:
			实现列表.fi标准范围(v名称)
			v模式 = 实现列表.C标准4显示(self, v名称, a列表缓存 = v输出)
		elif v类型 == 北向列表.E类型.e扩展4:
			实现列表.fi扩展范围(v名称)
			v模式 = 实现列表.C扩展4显示(self, v名称, a列表缓存 = v输出)
		elif v类型 in (北向列表.E类型.e标准6, 北向列表.E类型.e扩展6):
			v模式 = 实现列表.C六显示(self, v名称)
		else:
			raise ValueError("未知的访问控制列表类型")
		return v模式
	#服务
	def f模式_安全外壳(self):
		from . import 安全外壳
		return 安全外壳.C安全外壳显示(self)
class C全局显示_v11(C全局显示):
	"""适用于: 浪潮s6550(v11.12)"""
	def __init__(self, a):
		C全局显示.__init__(self, a)
	def f显示_接口表(self):
		v输出 = self.m设备.f执行显示命令("show interface status")
		return 基本表信息.f接口状态表_v11(v输出)	
class C全局显示_v12(C全局显示):
	"""适用于: 浪潮s5960(v12.2)"""
	def __init__(self, a):
		C全局显示.__init__(self, a)
	def f显示_接口表(self):
		v输出 = self.m设备.f执行显示命令("show interface status")
		return 基本表信息.f接口状态表_v12(v输出)