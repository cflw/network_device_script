from ..基础接口 import 操作
from ..基础接口 import 虚拟路由转发 as 北向虚拟路由转发
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 虚拟路由转发 as 南向虚拟路由转发
from .常量 import *
ca方向 = {
	操作.E方向.e入: "import",
	操作.E方向.e出: "export",
	操作.E方向.e双: "both"
}
class C资源配置(南向虚拟路由转发.I资源配置):
	def __init__(self, a, a名称):
		南向虚拟路由转发.I资源配置.__init__(self, a, a名称)
	def fg进入命令(self):
		return f"ip vrf {self.fg名称()}"
	def fs路由区分符(self, a路由区分符, a操作 = 操作.E操作.e设置):
		v命令 = 命令.C命令("rd")
		v命令 += a路由区分符
		self.f执行当前模式命令(v命令)
	def fs路由目标(self, a路由区分符, a方向 = 操作.E方向.e双, a操作 = 操作.E操作.e设置):
		v命令 = 命令.C命令("route-target")
		v命令 += ca方向[a方向]
		v命令 += a路由区分符
		self.f执行当前模式命令(v命令)
class C接口配置(南向虚拟路由转发.I接口配置):
	def __init__(self, a, a接口):
		南向虚拟路由转发.I接口配置.__init__(self, a, a接口)
	def fs虚拟路由转发(self, a名称, a保留地址 = True, a操作 = 操作.E操作.e设置):
		v命令 = f"ip vrf forwarding {a名称}"
		self.f执行当前模式命令(v命令)