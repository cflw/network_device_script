import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 操作
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 静态路由 as 南向静态路由
from ..思科命令行.常量 import *
def f生成静态路由命令4(a网络号, a下一跳):
	"""命令: ip route 网络号/前缀长度 下一跳"""
	v网络号 = 地址.S网络地址4.fc自动(a网络号)
	v下一跳 = 地址.S网络地址4.fc自动(a下一跳)
	v命令 = 命令.C命令("ip route")
	v命令 += v网络号.ft字符串()
	v命令 += v下一跳.fg地址s()
	return v命令
class C静态路由nv7(模式.C同级模式, 南向静态路由.I静态路由配置):
	"""适用于: 浪潮cn8000系列(v7.3)"""
	def __init__(self, a):
		南向静态路由.I静态路由配置.__init__(self, a)
	def fs路由(self, a网络号, a下一跳, a操作 = 操作.E操作.e添加):
		"""命令: ip route 网络号/前缀长度 下一跳 [优先级]"""
		v命令 = f生成静态路由命令4(a网络号, a下一跳)
		if a操作 == 操作.E操作.e删除:
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)
	def fs默认路由(self, a下一跳, a操作 = 操作.E操作.e添加):
		self.fs路由("0.0.0.0/0", a下一跳, a操作)
class C虚拟路由静态路由nv7(南向静态路由.I静态路由配置):
	"""适用于: 浪潮cn8000系列(v7.3)"""
	def __init__(self, a, a名称):
		南向静态路由.I静态路由配置.__init__(self, a)
		self.m名称 = a名称
	def fg进入命令(self):
		"""命令: vrf context 名称"""
		return f"vrf context {self.m名称}"
	def fs路由(self, a网络号, a下一跳, a操作 = 操作.E操作.e添加):
		"""命令: ip route 网络号/前缀长度 下一跳"""
		v命令 = f生成静态路由命令4(a网络号, a下一跳)
		if a操作 == 操作.E操作.e删除:
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)
	def fs默认路由(self, a下一跳, a操作 = 操作.E操作.e添加):
		self.fs路由("0.0.0.0/0", a下一跳, a操作)