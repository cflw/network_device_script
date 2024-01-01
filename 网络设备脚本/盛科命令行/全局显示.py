from ..基础接口 import 全局显示
from ..命令行接口 import 模式
from ..命令行接口 import 显示
from . import 系统信息
from . import 基本表信息
from . import 路由表信息
c命令_接口状态表 = "show interface status"
c命令_网络接口表4 = "show ip interface brief"
c命令_地址解析表 = "show ip arp"
c命令_物理地址表 = "show mac address-table"
c命令_路由表4 = "show ip route"
#===============================================================================
# 全局显示
#===============================================================================
class C全局显示_ev6(全局显示.I全局显示, 模式.I显示模式):
	"""适用于: 浪潮cn61108pcvh(v6.x)"""
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	#模式
	def f模式_设备(self):
		from . import 设备模式
		return 设备模式.C设备显示_ev6(self)
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间显示_ev6(self)
	#显示配置
	def f显示_当前配置(self):
		v输出 = self.m设备.f执行显示命令("show running-config")
		return v输出
	def f显示_启动配置(self):
		v输出 = self.m设备.f执行显示命令("show startup-config")
		return v输出
	#显示接口
	f显示_接口表 = 显示.F显示并解析(c命令_接口状态表, 基本表信息.f接口状态_ev6)
	f显示_网络接口表4 = 显示.F显示并解析(c命令_网络接口表4, 基本表信息.f网络接口表4_ev6)
	f显示_地址解析表 = 显示.F显示并解析(c命令_地址解析表, 基本表信息.f地址解析协议_ev6)
	f显示_物理地址表 = 显示.F显示并解析(c命令_物理地址表, 基本表信息.f物理地址表_ev6)
	f显示_路由表4 = 显示.F显示并解析(c命令_路由表4, 路由表信息.f路由表4_ev6)
class C全局显示_e580v6(C全局显示_ev6):
	"""适用于: 浪潮cn61108pcvh(v6.2.27)"""
	#模式
	def f模式_设备(self):
		from . import 设备模式
		return 设备模式.C设备显示_e580v6(self)
class C全局显示_e530v6(C全局显示_ev6):
	"""适用于: 浪潮s5350(v6.2.27)"""
	#模式
	def f模式_设备(self):
		from . import 设备模式
		return 设备模式.C设备显示_e530v6(self)
