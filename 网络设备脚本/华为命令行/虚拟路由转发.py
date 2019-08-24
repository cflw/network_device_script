from ..基础接口 import 操作
from ..命令行接口 import 命令
from ..命令行接口 import 虚拟路由转发 as 南向转发
class C资源配置(南向转发.I资源配置):
	def __init__(self, a, a名称):
		南向转发.I资源配置.__init__(self, a, a名称)
	def fg进入命令(self):
		"""命令: ip vpn-instance 实例名"""
		return f"ip vpn-instance {self.fg名称()}"
	def fs路由区分符(self, a路由区分符, a操作 = 操作.E操作.e设置):
		"""命令: route-distinguisher ASN:nn"""
		v命令 = 命令.C命令("route-distinguisher")
		v命令 += a路由区分符
		self.f执行当前模式命令(v命令)
	def fs路由目标(self, a路由区分符, a方向 = 操作.E方向.e双, a操作 = 操作.E操作.e设置):
		"""命令: vpn-target ASN:nn(多个) 方向"""
		v命令 = 命令.C命令("vpn-target")
		v命令 += a路由区分符
		v命令 += {
			操作.E方向.e入: "import-extcommunity",
			操作.E方向.e出: "export-extcommunity",
			操作.E方向.e双: "both"
		}[a方向]
		self.f执行当前模式命令(v命令)
class C接口配置(南向转发.I接口配置):
	def __init__(self, a, a接口):
		南向转发.I接口配置.__init__(self, a接口)
	def fs虚拟路由转发(self, a名称, a保留地址 = True, a操作 = 操作.E操作.e设置):
		"""命令: ip binding vpn-instance 实例"""
		v命令 = f"ip binding vpn-instance {a名称}"
		self.f执行当前模式命令(v命令)