from ..命令行接口 import 全局显示
from . import 基本表信息
class C全局显示(全局显示.I全局显示):
	"""适用于: s3956(v2.2.0B)"""
	#显示
	def f显示_版本(self):
		v输出 = self.m设备.f执行显示命令("show version")
		return 系统信息.C版本(v输出)
	def f显示_启动配置(self):
		v输出 = self.m设备.f执行显示命令("show configuration")
		return v输出
	def f显示_当前配置(self):
		v输出 = self.m设备.f执行显示命令("show running-config")
		return v输出
	def f显示_时间(self):
		v版本 = self.f显示_版本()
		return v版本.fg当前时间()
	def f显示_设备名(self):
		v命令 = "show running-config | include hostname"
		v输出 = self.m设备.f执行显示命令(v命令)
		v位置 = v输出.find("hostname")
		v行结束 = v输出.find("\n", v位置)
		return v输出[v位置 + 9 : v行结束]
	#显示具体
	def f显示_接口表(self):
		v命令 = "show interface brief"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 基本表信息.C接口表(v输出)
	def f显示_网络接口表4(self):
		v命令 = "show ip interface brief"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 基本表信息.C网络接口表4(v输出)
