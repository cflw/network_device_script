from ..基础接口 import 操作
from ..基础接口 import 虚拟路由转发 as 北向转发
from ..命令行接口 import 虚拟路由转发 as 南向转发
class C资源配置nv7(南向转发.I资源配置):
	"""适用于: 浪潮cn8000系列(v7.3)"""
	def __init__(self, a, a名称):
		南向转发.I资源配置.__init__(self, a, a名称)
	def fg进入命令(self):
		"""命令: vrf context 名称"""
		return f"vrf context {self.fg名称()}"
class C接口配置nv7(南向转发.I接口配置):
	"""适用于: 浪潮cn8000系列(v7.3)"""
	def __init__(self, a, a接口):
		南向转发.I接口配置.__init__(self, a, a接口)
	def fs虚拟路由转发(self, a名称, a保留地址 = True, a操作 = 操作.E操作.e设置):
		"""命令: vrf member 名称"""
		v命令 = f"vrf member {a名称}"
		self.f执行当前模式命令(v命令)