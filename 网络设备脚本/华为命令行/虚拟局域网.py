import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw工具_序列 as 序列
from ..基础接口 import 操作
from ..基础接口 import 接口 as 北向接口
from ..基础接口 import 虚拟局域网 as 北向虚网
from ..命令行接口 import 命令
from ..命令行接口 import 接口 as 南向接口
from ..命令行接口 import 虚拟局域网 as 南向虚网
from .常量 import *
from . import 实用 as 华为实用
from . import 接口 as 实现接口
#===============================================================================
# 路由
#===============================================================================
ca链路类型 = {
	北向虚网.E链路类型.e接入: "access",
	北向虚网.E链路类型.e中继: "trunk",
	北向虚网.E链路类型.e混合: "hybrid",
}
ca链路类型反 = 序列.f字典键值反转(ca链路类型)
def f提取链路类型(a文本):
	v文本 = 字符串.f提取字符串之间(a文本, "link-type ", "\n")
	if v文本:
		return ca链路类型反[v文本]
	else:
		return 北向虚网.E链路类型.e混合
#===============================================================================
# 配置模式
#===============================================================================
class C虚网配置(南向虚网.I虚拟局域网配置):
	def __init__(self, a, a编号):
		南向虚网.I虚拟局域网配置.__init__(self, a, a编号)
	#动作
	def fs描述(self, a描述 = "", a操作 = 操作.E操作.e设置):
		v命令 = 命令.f生成描述命令(a命令 = c命令_描述, a不 = c不, a描述 = a描述, a操作 = a操作)
		self.f执行当前模式命令(v命令)
	def fs端口(self, a接口, a操作 = 操作.E操作.e添加):
		v接口 = 实现接口.f创建接口(a接口)
		v命令 = 命令.C命令("port")
		if not v接口.fi范围():
			v命令 += v接口
		elif v接口.fi只有末尾序号是范围():
			v命令 += 华为实用.f生成接口范围(v接口)
		else:	#展开
			for v接口 in a接口.fe接口():
				v命令 = "port %s" % (v接口,)
				self.f执行当前模式命令(v命令)
			return
		self.f执行当前模式命令(v命令)
class C接口配置(南向虚网.I接口配置):
	def __init__(self, a, a接口):
		南向虚网.I接口配置.__init__(self, a, a接口)
	@南向接口.A接口自动展开
	def fs链路类型(self, a类型 = 北向虚网.E链路类型.e混合, a操作 = 操作.E操作.e设置):
		v链路类型 = self.fg链路类型()
		if v链路类型 != a类型:
			self.f重置链路类型()
		v命令 = 命令.C命令("port link-type")
		v命令 += ca链路类型[a类型]
		self.f执行当前模式命令(v命令)
	def fg链路类型(self):
		v输出 = self.f显示_当前模式配置()
		return f提取链路类型(v输出)
	@南向接口.A接口自动展开
	def f重置链路类型(self):
		v输出 = self.f显示_当前模式配置()
		v链路类型 = f提取链路类型(v输出)
		if v链路类型 == 北向虚网.E链路类型.e中继:
			self.f执行当前模式命令("port trunk allow-pass vlan 1")
			self.f执行当前模式命令("undo port trunk allow-pass vlan 2 to 4094")
			self.f执行当前模式命令("undo port trunk pvid vlan")
		elif v链路类型 == 北向虚网.E链路类型.e接入:
			self.f执行当前模式命令("undo port default vlan")
		elif v链路类型 == 北向虚网.E链路类型.e混合:
			self.f执行当前模式命令("port hybrid pvid vlan 1")
			self.f执行当前模式命令("port hybrid vlan 1")
			self.f执行当前模式命令("undo port hybrid untagged vlan 2 to 4094")
			self.f执行当前模式命令("undo port hybrid tagged vlan all")
	@南向接口.A接口自动展开
	def f中继_s通过(self, a虚拟局域网, a操作 = 操作.E操作.e设置):
		v命令 = 命令.C命令("port trunk allow-pass vlan")
		v命令 += 南向虚网.f生成一个(a虚拟局域网)
		self.m设备.f执行命令(v命令)
	@南向接口.A接口自动展开
	def f接入_s绑定(self, a虚拟局域网, a操作 = 操作.E操作.e设置):
		v命令 = 命令.C命令("port default vlan")
		v命令 += 南向虚网.f生成一个(a虚拟局域网)
		self.f执行当前模式命令(v命令)
class C接口配置s5700(C接口配置):
	@南向接口.A接口自动展开
	def f重置链路类型(self):
		v输出 = self.f显示_当前模式配置()
		v链路类型 = f提取链路类型(v输出)
		if v链路类型 == 北向虚网.E链路类型.e中继:
			#s5700(v5.110)不能直接删除2~4094,只能一个个删或全删. 现在先全部删,以后改进
			self.f执行当前模式命令("undo port trunk allow-pass vlan all")
			self.f执行当前模式命令("port trunk allow-pass vlan 1")
			self.f执行当前模式命令("undo port trunk pvid vlan")
		elif v链路类型 == 北向虚网.E链路类型.e接入:
			self.f执行当前模式命令("undo port default vlan")
		elif v链路类型 == 北向虚网.E链路类型.e混合:
			#同上, s5700只能全删再添加
			self.f执行当前模式命令("undo port hybrid untagged vlan all")
			self.f执行当前模式命令("undo port hybrid tagged vlan all")
			self.f执行当前模式命令("port hybrid pvid vlan 1")
			self.f执行当前模式命令("port hybrid vlan 1")
