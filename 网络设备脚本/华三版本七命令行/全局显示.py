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
	#显示配置
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
	#显示表格
	f显示_物理地址表 = 显示.F显示并解析(c命令_物理地址表, 基本表信息.f物理地址表_v7)
	f显示_路由表4 = 显示.F显示并解析(c命令_路由表4, 路由表信息.f路由表4_v7)
class C全局显示_ev7(C全局显示_v7):
	"""适用于: (模拟器)华三msr3620(v7.1.*), (模拟器)华三s5820v2(v7.1.*)"""
	def __init__(self, a):
		C全局显示_v7.__init__(self, a)
	def f模式_设备(self):
		from . import 设备模式
		return 设备模式.C设备显示_ev7_1(self)
class C全局显示_s5v7(C全局显示_v7):
	"""适用于: 华三s5820v2(v7.1.075)"""
	def __init__(self, a):
		C全局显示_v7.__init__(self, a)
	def f显示_接口表(self):	#所有物理接口和逻辑接口
		v输出 = self.m设备.f执行显示命令(c命令_接口表)
		v表 = 基本表信息.f接口表_s5v7(v输出)
		return v表
class C全局显示_s7v7(C全局显示_v7):
	"""适用于: 紫光s8600x(v7.1.070), 紫光s7800xp(v7.1.*)"""
	def __init__(self, a):
		C全局显示_v7.__init__(self, a)
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间显示_s7v7(self)
	#显示表格
	f显示_接口表 = 显示.F显示并解析(c命令_接口表, 基本表信息.f接口表_s7v7)
	f显示_网络接口表4 = 显示.F显示并解析(c命令_网络接口表4, 基本表信息.f网络接口表4_s7v7)
	f显示_地址解析表 = 显示.F显示并解析(c命令_地址解析表, 基本表信息.f地址解析表_s7v7)
class C全局显示_us5v7(C全局显示_s7v7):
	"""适用于: 紫光s5200(v7.1.*)"""
	def __init__(self, a):
		C全局显示_s7v7.__init__(self, a)
	f显示_网络接口表4 = 显示.F显示并解析(c命令_网络接口表4, 基本表信息.f网络接口表4_us5v7)
class C全局显示_s9v7(C全局显示_v7):
	"""适用于: 华三s9810(v7.1.045)"""
	def __init__(self, a):
		C全局显示_v7.__init__(self, a)
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