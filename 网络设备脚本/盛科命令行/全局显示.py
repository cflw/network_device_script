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
	#配置
	def f显示_当前配置(self):
		v输出 = self.m设备.f执行显示命令("show running-config")
		return v输出
	def f显示_启动配置(self):
		v输出 = self.m设备.f执行显示命令("show startup-config")
		return v输出
	#网络接口
	f显示_接口表 = 显示.F显示并解析(c命令_接口状态表, 基本表信息.f接口状态_ev6)
	f显示_网络接口表4 = 显示.F显示并解析(c命令_网络接口表4, 基本表信息.f网络接口表4_ev6)
	f显示_地址解析表 = 显示.F显示并解析(c命令_地址解析表, 基本表信息.f地址解析协议_ev6)
	f显示_物理地址表 = 显示.F显示并解析(c命令_物理地址表, 基本表信息.f物理地址表_ev6)
	f显示_路由表4 = 显示.F显示并解析(c命令_路由表4, 路由表信息.f路由表4_ev6)
	#数据结构
	def f显示_访问控制列表(self):
		from . import 访问控制列表 as 实现列表
		v命令 = "show running-config | include access-list"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 实现列表.f解析访问列表摘要(v输出)
	def f模式_访问控制列表(self, a名称, a类型 = None):
		from ..基础接口 import 访问控制列表 as 北向列表
		from ..命令行接口 import 访问控制列表 as 南向列表
		from . import 访问控制列表 as 实现列表
		v类型 = a类型
		v输出 = None	#显示缓存
		if v类型 == None:
			v命令 = f"show running-config | include access-list {a名称}"
			v输出 = self.m设备.f执行显示命令(v命令)	#不存在显示空
			if not v输出:
				return None
			v类型 = 实现列表.f解析访问控制列表类型(v输出)
		#创建访问控制列表对象
		if v类型 == 北向列表.E类型.e标准4:
			v模式 = 实现列表.C标准4显示(self, a名称)
		elif v类型 == 北向列表.E类型.e扩展4:
			v模式 = 实现列表.C扩展4显示(self, a名称)
		elif v类型 in (北向列表.E类型.e标准6, 北向列表.E类型.e扩展6):
			raise NotImplementedError()
		else:
			raise ValueError("未知的访问控制列表类型")
		return v模式
	#服务
	def f模式_安全外壳(self):
		from . import 安全外壳
		return 安全外壳.C安全外壳显示(self)
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
