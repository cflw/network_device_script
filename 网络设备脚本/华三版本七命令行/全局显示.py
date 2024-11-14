from ..基础接口 import 全局显示
from ..命令行接口 import 模式
from ..命令行接口 import 显示
from . import 基本表信息
from . import 路由表信息
c命令_接口表 = "display interface brief"
c命令_网络接口表4 = "display ip interface brief"
c命令_网络接口表6 = "display ipv6 interface brief"
c命令_地址解析表 = "display arp"
c命令_物理地址表 = "display mac-address"
c命令_路由表4 = "display ip routing-table"
class C全局显示_v7(全局显示.I全局显示, 模式.I显示模式):
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	#模式
	def f模式_设备(self):
		from . import 设备模式
		return 设备模式.C设备显示_v7(self)
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间显示_v7(self)
	#配置
	def f显示_当前配置(self):
		v命令 = "display current-configuration"
		v输出 = self.m设备.f执行显示命令(v命令, a自动换页 = True)
		return v输出
	def 显示_启动配置(self):
		v命令 = "display saved-configuration"
		v输出 = self.m设备.f执行显示命令(v命令, a自动换页 = True)
		return v输出
	def f显示_诊断信息(self):
		"""一次性获取所有信息"""
		v命令 = "display diagnostic-information"
		v输出 = self.m设备.f执行显示命令(v命令)
		#Save or display diagnostic information (Y=save, N=display)? [Y/N]:
		if "[Y/N]" in v输出:
			v输出 = self.m设备.f执行显示命令("N", a自动换页 = True)
		return v输出
	#表格
	f显示_物理地址表 = 显示.F显示并解析(c命令_物理地址表, 基本表信息.f物理地址表_v7)
	f显示_网络接口表4 = 显示.F显示并解析(c命令_网络接口表4, 基本表信息.f网络接口表4_v7)
	f显示_路由表4 = 显示.F显示并解析(c命令_路由表4, 路由表信息.f路由表4_v7)
	#数据结构
	def f模式_访问控制列表(self, a名称, a类型 = None):
		from ..基础接口 import 访问控制列表 as 北向列表
		from ..命令行接口 import 访问控制列表 as 南向列表
		from . import 访问控制列表 as 实现列表
		v名称, v类型 = 南向列表.f解析名称和类型(a名称, a类型, 实现列表.C助手)
		if v类型 == 北向列表.E类型.e标准4:
			return 实现列表.C基本4显示_v7(self, v名称)
		elif v类型 == 北向列表.E类型.e扩展4:
			return 实现列表.C高级4显示_v7(self, v名称)
		elif v类型 == 北向列表.E类型.e标准6:
			return 实现列表.C基本6显示_v7(self, v名称)
		elif v类型 == 北向列表.E类型.e扩展6:
			return 实现列表.C高级6显示_v7(self, v名称)
		else:
			raise ValueError("错误的类型")
	#服务
	def f模式_安全外壳(self):
		from . import 安全外壳
		return 安全外壳.C安全外壳显示_v7(self)
class C全局显示_ev7(C全局显示_v7):
	"""适用于: (模拟器)华三msr3620(v7.1.*), (模拟器)华三s5820v2(v7.1.*)"""
	def f模式_设备(self):
		from . import 设备模式
		return 设备模式.C设备显示_ev7_1(self)
class C全局显示_s5v7(C全局显示_v7):
	"""适用于: 华三s5560x(v7.1.070 r6526), 华三s5820v2(v7.1.075)"""
	#设备
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间显示_s7v7(self)
	#表格
	f显示_接口表 = 显示.F显示并解析(c命令_接口表, 基本表信息.f接口表_s5v7)
	f显示_网络接口表4 = 显示.F显示并解析(c命令_网络接口表4, 基本表信息.f网络接口表4_v7)
	f显示_物理地址表 = 显示.F显示并解析(c命令_物理地址表, 基本表信息.f物理地址表_v7)
	f显示_地址解析表 = 显示.F显示并解析(c命令_地址解析表, 基本表信息.f地址解析表_s7v7)
	f显示_路由表4 = 显示.F显示并解析(c命令_路由表4, 路由表信息.f路由表4_v7)
class C全局显示_s7v7(C全局显示_v7):
	"""适用于: 紫光s8600x(v7.1.070), 紫光s7800xp(v7.1.*), 紫光s5600(v7.1.070 r7748p01)"""
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间显示_s7v7(self)
	#显示表格
	f显示_接口表 = 显示.F显示并解析(c命令_接口表, 基本表信息.f接口表_s7v7)
	f显示_网络接口表4 = 显示.F显示并解析(c命令_网络接口表4, 基本表信息.f网络接口表4_s7v7)
	f显示_地址解析表 = 显示.F显示并解析(c命令_地址解析表, 基本表信息.f地址解析表_s7v7)
class C全局显示_us5v7(C全局显示_s7v7):
	"""适用于: 紫光s5200(v7.1.*)"""
	f显示_接口表 = 显示.F显示并解析(c命令_接口表, 基本表信息.f接口表_s7v7)
	f显示_网络接口表4 = 显示.F显示并解析(c命令_网络接口表4, 基本表信息.f网络接口表4_us5v7)
	f显示_地址解析表 = 显示.F显示并解析(c命令_地址解析表, 基本表信息.f地址解析表_s7v7)
class C全局显示_s9v7(C全局显示_v7):
	"""适用于: 华三s9810(v7.1.045)"""
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间显示_s9v7(self)
	#显示表格
	f显示_接口表 = 显示.F显示并解析(c命令_接口表, 基本表信息.f接口表_s9v7)
	f显示_网络接口表4 = 显示.F显示并解析(c命令_网络接口表4, 基本表信息.f网络接口表4_s9v7)
	f显示_网络接口表6 = 显示.F显示并解析(c命令_网络接口表6, 基本表信息.f网络接口表6_s9v7)
	f显示_地址解析表 = 显示.F显示并解析(c命令_地址解析表, 基本表信息.f地址解析表_s9v7)
	f显示_物理地址表 = 显示.F显示并解析(c命令_物理地址表, 基本表信息.f物理地址表_s9v7)
	f显示_路由表4 = 显示.F显示并解析(c命令_路由表4, 路由表信息.f路由表4_s9v7)
class C全局显示_sv7_2019(C全局显示_v7):
	"""适用于: 华三s5560x(v7.1.070 r1119p20), 紫光s5600(v7.1.070 r7734p05)"""
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间显示_s7v7(self)
	f显示_接口表 = 显示.F显示并解析(c命令_接口表, 基本表信息.f接口表_s5v7)
	f显示_网络接口表4 = 显示.F显示并解析(c命令_网络接口表4, 基本表信息.f网络接口表4_v7)
	f显示_地址解析表 = 显示.F显示并解析(c命令_地址解析表, 基本表信息.f地址解析表_sv7_2019)
	f显示_物理地址表 = 显示.F显示并解析(c命令_物理地址表, 基本表信息.f物理地址表_v7)
	f显示_路由表4 = 显示.F显示并解析(c命令_路由表4, 路由表信息.f路由表4_v7)
