import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 操作
from ..基础接口 import 协议
from ..基础接口 import 接口 as 北向接口
from ..基础接口 import 路由 as 北向路由
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 路由 as 南向路由
from ..命令行接口 import 静态路由 as 南向静态路由
from .常量 import *
from . import 接口 as 实现接口
from . import 路由表信息
def f生成静态路由命令4(a网络号, a下一跳, a虚拟路由转发):
	"""命令: ip route-static [vpn-instance 实例] 网络号 长度|掩码 下一跳"""
	v网络号 = 地址.S网络地址4.fc自动(a网络号)
	v下一跳 = 南向路由.f生成下一跳4(a下一跳, 实现接口.f创建接口)
	v命令 = 命令.C命令("ip route-static")
	if a虚拟路由转发:
		v命令 += "vpn-instance", a虚拟路由转发
	v命令 += v网络号.fg地址s(), v网络号.fg前缀长度()
	v命令 += v下一跳
	return v命令
class C静态路由4(模式.C同级模式, 南向静态路由.I静态路由配置):
	def __init__(self, a, a虚拟路由转发 = None):
		南向静态路由.I静态路由配置.__init__(self, a)
		self.m虚拟路由转发 = a虚拟路由转发
	def f显示_路由表(self):
		v命令 = 路由表信息.f生成显示路由表命令(协议.E协议.e网络协议4, 北向路由.E路由类型.e静态)
		v输出 = self.m设备.f执行显示命令(v命令)
		return 路由表信息.C路由表4(v输出)
	def fs路由(self, a网络号, a下一跳, a操作 = 操作.E操作.e添加):
		v命令 = f生成静态路由命令4(a网络号, a下一跳, self.m虚拟路由转发)
		if a操作 == 操作.E操作.e删除:
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)
	def fs默认路由(self, a下一跳, a操作 = 操作.E操作.e添加):
		self.fs路由("0.0.0.0/0", a下一跳, a操作)