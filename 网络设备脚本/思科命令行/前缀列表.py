import cflw代码库py.cflw网络地址 as 地址
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 操作
from ..基础接口 import 协议
from ..基础接口 import 接口 as 北向接口
from ..基础接口 import 前缀列表 as 北向列表
from ..命令行接口 import 模式
from ..命令行接口 import 命令
from ..命令行接口 import 前缀列表 as 南向列表
from .常量 import *
#===============================================================================
# 基础
#===============================================================================
c版本4 = "ip"
c版本6 = "ipv6"
c序号不存在 = "Sequence number does not exist"
#===============================================================================
# 模式
#===============================================================================
class I前缀列表(模式.C同级模式, 南向列表.I前缀列表配置):
	def __init__(self, a, a名称, a版本, t地址):
		南向列表.I前缀列表配置.__init__(self, a)
		self.m名称 = a名称
		self.m版本 = a版本
		if not t地址 in (地址.S网络地址4, 地址.S网络地址6):
			raise TypeError()
		self.t地址 = t地址
		self.c最大前缀长度 = t地址.c最大前缀长度
	def fg显示命令(self, a序号 = None):
		v命令 = 命令.C命令("show ip prefix-list")
		v命令 += self.m名称
		if a序号:
			v命令 += "seq", a序号
		return v命令
	def f生成命令(self, a序号 = None, a规则 = None):
		v命令 = 命令.C命令()
		v命令 += "%s prefix-list %s" % (self.m版本, self.m名称)
		if a序号:
			v命令 += "seq %d" % (a序号,)
		if a规则:
			if not a序号 and a规则.m序号:
				v命令 += "seq %d" % (a规则.m序号,)
			v命令 += "permit %s/%d" % (a规则.m网络号.fg网络号s(), a规则.m网络号.fg前缀长度())
			if a规则.m最小长度:
				v命令 += "ge %d" % (a规则.m最小长度,)
			if a规则.m最大长度:
				v命令 += "le %d" % (a规则.m最大长度,)
		return v命令
	def f添加规则(self, a序号, a规则):
		v命令 = self.f生成命令(a序号, a规则)
		self.f执行当前模式命令(v命令)
	def f删除规则(self, a序号, a规则):
		v命令 = self.f生成命令(a序号, a规则)
		v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)
	def fs规则(self, a序号 = None, a规则 = None, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		if a操作 == 操作.E操作.e是:
			self.f添加规则(a序号, a规则)
		elif a操作 == 操作.E操作.e否:
			self.f删除规则(a序号, a规则)
		elif 操作.fi加操作(v操作):
			self.f添加规则(a序号, a规则)
		elif 操作.fi减操作(v操作):
			v规则 = a规则 if a规则 else self.fg规则(a序号)
			if v规则:
				self.f删除规则(a序号, v规则)
	def fe规则(self):
		v命令 = self.fg显示命令()
		v输出 = self.m设备.f执行显示命令(v命令)
		for v行 in v输出.split("\n"):
			if not "seq" in v行:
				continue
			yield self.f解析规则(v行)
	def fg规则(self, a序号):
		v命令 = self.fg显示命令(a序号)
		v输出 = self.m设备.f执行显示命令(v命令)
		if c序号不存在 in v输出:
			return
		return self.f解析规则(v输出)
class C四(I前缀列表):
	def __init__(self, a, a名称):
		I前缀列表.__init__(self, a, a名称, c版本4, 地址.S网络地址4)
	@staticmethod
	def f解析规则(a规则):
		v规则 = 北向列表.S规则()
		v解析器 = C规则解析器(a规则)
		v规则.m序号 = v解析器.f序号()
		v规则.m允许 = v解析器.f允许()
		v规则.m网络号 = v解析器.f地址4()
		v规则.m最小长度 = v解析器.f大于()
		v规则.m最大长度 = v解析器.f小于()
		return v规则
class C六(I前缀列表):
	def __init__(self, a, a名称):
		I前缀列表.__init__(self, a, a名称, c版本6, 地址.S网络地址6)
	@staticmethod
	def f解析规则(a规则):
		v规则 = 北向列表.S规则()
		v解析器 = C规则解析器(a规则)
		v规则.m序号 = v解析器.f序号()
		v规则.m允许 = v解析器.f允许()
		v规则.m网络号 = v解析器.f地址6()
		v规则.m最小长度 = v解析器.f大于()
		v规则.m最大长度 = v解析器.f小于()
		return v规则
#===============================================================================
# 规则解析器
#===============================================================================
class C规则解析器:
	def __init__(self, a文本):
		self.m取词 = 字符串.C推进取词(a文本)
	def f序号(self):
		self.m取词.f推进()
		v词 = self.m取词.f取词推进()
		return int(v词)
	def f允许(self):
		return self.m取词.f取词推进() == "permit"
	def f地址4(self):
		return 地址.S网络地址4.fc自动(self.m取词.f取词推进())
	def f地址6(self):
		return 地址.S网络地址6.fc自动(self.m取词.f取词推进())
	def f大于(self):
		v词 = self.m取词.f取词()
		if v词 != "ge":
			return
		self.m取词.f推进()
		v词 = self.m取词.f取词推进()
		return int(v词)
	def f小于(self):
		v词 = self.m取词.f取词()
		if v词 != "le":
			return
		self.m取词.f推进()
		v词 = self.m取词.f取词推进()
		return int(v词)