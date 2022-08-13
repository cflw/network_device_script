from ..命令行接口 import 全局显示
from ..命令行接口 import 模式
from . import 基本表信息
#===============================================================================
# 全局显示
#===============================================================================
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
	#显示配置
	def f显示_启动配置(self):
		v命令 = "display saved-configuration"
		v输出 = self.m设备.f执行显示命令(v命令, a自动换页 = True)
		return C配置内容(v输出)
	def f显示_当前配置(self):
		v命令 = "display current-configuration"
		v输出 = self.m设备.f执行显示命令(v命令, a自动换页 = True)
		return C配置内容(v输出)
	#显示 基本表信息
	def f显示_物理地址表(self):
		v命令 = "display mac-address"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 基本表信息.f物理地址表(v输出)
	def f显示_地址解析表(self):
		v命令 = "display arp"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 基本表信息.f地址解析表(v输出)
	def f显示_接口表(self):
		v命令 = "display interface brief"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 基本表信息.f接口表(v输出)
	def f显示_网络接口表4(self):
		v命令 = "display ip interface brief"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 基本表信息.f网络接口表4(v输出)
#===============================================================================
# 工具
#===============================================================================
class C配置内容:
	def __init__(self, a配置):
		self.m配置 = a配置.replace('\r', '')
	def __str__(self):
		return self.m配置
	def fg设备名称(self):
		return C输出分析.f从配置取设备名称(self.m配置)
class C输出分析:
	@staticmethod
	def f从配置取设备名称(a配置):
		if not a配置:
			return ""
		v指定行 = a配置.find(' sysname ')
		v结束 = a配置.find('\n', v指定行)
		if v结束 == -1:
			return a配置[v指定行 + 8 :]
		else:
			return a配置[v指定行 + 8 : v结束]