import cflw代码库py.cflw网络地址 as 地址
import cflw代码库py.cflw字符串 as 字符串
from .. import 华为
from ..基础接口 import 操作
from ..基础接口 import 协议
from ..基础接口 import 访问控制列表 as 北向列表
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 访问控制列表 as 南向列表
from .常量 import *
#===============================================================================
# 声明
#===============================================================================
c源地址 = "source"
c源端口 = "source-port"
c目的地址 = "destination"
c目的端口 = "destination-port"
#生成
def f生成名称(a名称):
	v类型 = type(a名称)
	if v类型 == int:
		return "%s" % (a名称,)
	v名称 = str(a名称)
	if v名称.isdigit():
		return "%s" % (v名称,)
	return "name %s" % (v名称,)
def f生成规则序号(a序号):
	v命令 = 命令.C命令("rule")
	if a序号:
		v命令 += a序号
	return v命令
f生成协议4 = 南向列表.f生成协议4
f生成协议6 = 南向列表.f生成协议6
f生成动作 = 南向列表.f生成动作
def f生成端口(a前置: str, a端口):
	return a前置 + " " + 南向列表.f生成端口(g到字符串, a端口)
def f生成地址4(a前置: str, a地址):
	if not a地址:
		return ""
	v地址 = 地址.S网络地址4.fc自动(a地址)
	if v地址.fi空():
		return "any"
	elif v地址.fi主机():
		return "%s %s %s" % (a前置, v地址.fg地址s(), 0)
	else:
		return "%s %s %s" % (a前置, v地址.fg地址s(), v地址.fg反掩码s())
def f生成地址6(a前置: str, a地址):
	if not a地址:
		return ""
	v地址 = 地址.S网络地址6.fc自动(a地址)
	if v地址.fi空():
		return "any"
	else:
		return "%s %s" % (a前置, v地址)
#到字符串
class C到字符串(北向列表.I生成端口):
	def f大于(self, a值):
		return "gt " + str(a值)
	def f小于(self, a值):
		return "lt " + str(a值)
	def f等于(self, a序列):
		return "eq %d" % (a序列[0], )
	def f范围(self, a值: range):
		return "range %d %d" % (a值.start, a值.stop - 1)
g到字符串 = C到字符串()
#规则
def fe规则行(a文本):
	v规则s = ""
	for v行 in a文本.split("\n"):
		if v行[:5] == " rule":	#新规则
			if v规则s[:5] == " rule":
				yield v规则s
			#重新开始
			v规则s = v行
		else:	#继续
			v规则s += v行
	#结束
	yield v规则s
#===============================================================================
# 显示
#===============================================================================
class I列表显示(北向列表.I列表显示, 模式.I显示模式):
	def __init__(self, a, a名称, a协议 = ""):
		模式.I显示模式.__init__(self, a)
		self.m名称 = a名称
		self.m协议 = a协议
	def fg显示命令(self, a序号 = None):
		v命令 = 命令.C命令("display acl")
		v命令 += self.m协议
		v命令 += f生成名称(self.m名称)
		if a序号 != None:
			if self.m设备.m型号 & 华为.E型号.c云:
				v命令 += "| include rule\\s%d\\s" % (a序号,)
			else:
				v命令 += "| include rule_%d_" % (a序号,)
		return v命令
	def fe规则(self):
		v命令 = self.fg显示命令()
		v输出 = self.m设备.f执行显示命令(v命令)
		for v行 in fe规则行(v输出):
			yield self.f解析规则(v行)
	def fg规则(self, a序号):
		v命令 = self.fg显示命令(a序号)
		v输出 = self.m设备.f执行显示命令(v命令)
		for v行 in fe规则行(v输出):
			return self.f解析规则(v行)
	def f解析规则(self, a规则):
		raise NotImplementedError()
class C基本4显示(I列表显示):
	@staticmethod
	def f解析规则(a规则: str):
		v解析器 = C规则解析器(a规则)
		v规则 = 北向列表.S规则()
		v规则.m序号 = v解析器.f序号()
		v规则.m动作 = v解析器.f动作()
		v规则.m源地址 = v解析器.f地址4()
		return v规则
class C高级4显示(I列表显示):
	@staticmethod
	def f解析规则(a规则: str):
		v解析器 = C规则解析器(a规则)
		v规则 = 北向列表.S规则()
		v规则.m序号 = v解析器.f序号()
		v规则.m动作 = v解析器.f动作()
		v规则.m协议 = v解析器.f协议()
		v规则.m源地址 = v解析器.f地址4()
		v规则.m源端口 = v解析器.f端口号()
		v规则.m目的地址 = v解析器.f地址4()
		v规则.m目的端口 = v解析器.f端口号()
		return v规则
class C基本6显示(I列表显示):
	@staticmethod
	def f解析规则(a规则: str):
		v解析器 = C规则解析器(a规则)
		v规则 = 北向列表.S规则()
		v规则.m序号 = v解析器.f序号()
		v规则.m动作 = v解析器.f动作()
		v规则.m源地址 = v解析器.f地址6()
		return v规则
class C高级6显示(I列表显示):
	@staticmethod
	def f解析规则(a规则: str):
		v解析器 = C规则解析器(a规则)
		v规则 = 北向列表.S规则()
		v规则.m序号 = v解析器.f序号()
		v规则.m动作 = v解析器.f动作()
		v规则.m协议 = v解析器.f协议()
		v规则.m源地址 = v解析器.f地址6()
		v规则.m源端口 = v解析器.f端口号()
		v规则.m目的地址 = v解析器.f地址6()
		v规则.m目的端口 = v解析器.f端口号()
		return v规则
#===============================================================================
# 配置
#===============================================================================
class I列表配置(南向列表.I列表配置):
	def __init__(self, a, a名称, a协议 = ""):
		南向列表.I列表配置.__init__(self, a)
		self.m名称 = a名称
		self.m协议 = a协议
	def fg模式参数(self):
		return (self.m类型, self.m名称)
	def fg进入命令(self):
		v命令 = 命令.C命令("acl")
		v命令 += self.m协议
		v命令 += f生成名称(self.m名称)
		return v命令
	def f删除规则(self, a序号: int):
		v命令 = f生成规则序号(a序号)
		v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)
	def fs规则(self, a序号 = None, a规则 = None, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		if v操作 == 操作.E操作.e设置:
			self.f添加规则(a序号, a规则)
		elif v操作 == 操作.E操作.e新建:
			self.f添加规则(a序号, a规则)
		elif v操作 == 操作.E操作.e修改:
			v序号 = a序号 if a序号 >= 0 else a规则.m序号
			v规则 = self.fg规则(v序号)
			v规则.f更新_规则(a规则)
			if not self.m设备.m型号 & 华为.E型号.c云:
				self.f删除规则(v序号)
			self.f添加规则(v序号, v规则)
		elif v操作 == 操作.E操作.e删除:
			self.f删除规则(a序号)
class C基本4配置(I列表配置, C基本4显示):
	def __init__(self, a, a名称):
		I列表配置.__init__(self, a, a名称)
	def f添加规则(self, a序号 = None, a规则 = None):
		v命令 = f生成规则序号(a序号)
		v命令 += f生成动作(a规则.m动作)
		v命令 += f生成地址4(c源地址, a规则.m源地址)
		self.f执行当前模式命令(v命令)
class C高级4配置(I列表配置, C高级4显示):
	def __init__(self, a, a名称):
		I列表配置.__init__(self, a, a名称)
	def f添加规则(self, a序号 = None, a规则 = None):
		v命令 = f生成规则序号(a序号)
		v命令 += f生成动作(a规则.m动作)
		v命令 += f生成协议4(a规则.m协议)
		v命令 += f生成地址4(c源地址, a规则.m源地址)
		v命令 += f生成端口(c源端口, a规则.m源端口)
		v命令 += f生成地址4(c目的地址, a规则.m目的地址)
		v命令 += f生成端口(c目的端口, a规则.m目的端口)
		self.f执行当前模式命令(v命令)
class C基本6配置(I列表配置, C基本6显示):
	def __init__(self, a, a名称):
		I列表配置.__init__(self, a, a名称, "ipv6")
	def f添加规则(self, a序号 = None, a规则 = None):
		v命令 = f生成规则序号(a序号)
		v命令 += f生成动作(a规则.m动作)
		v命令 += f生成地址6(c源地址, a规则.m源地址)
		self.f执行当前模式命令(v命令)
class C高级6配置(I列表配置, C高级6显示):
	def __init__(self, a, a名称):
		I列表配置.__init__(self, a, a名称, "ipv6")
	def f添加规则(self, a序号 = None, a规则 = None):
		v命令 = f生成规则序号(a序号)
		v命令 += f生成动作(a规则.m动作)
		v命令 += f生成协议6(a规则.m协议)
		v命令 += f生成地址6(c源地址, a规则.m源地址)
		v命令 += f生成端口(c源端口, a规则.m源端口)
		v命令 += f生成地址6(c目的地址, a规则.m目的地址)
		v命令 += f生成端口(c目的端口, a规则.m目的端口)
		self.f执行当前模式命令(v命令)
#===============================================================================
# 其它
#===============================================================================
class C助手(北向列表.I助手):
	c基本 = range(2000, 3000)
	c高级 = range(3000, 4000)
	def F计算(a起始):
		@staticmethod
		def f(n):
			return n + a起始
		return f
	def F反算(a起始):
		@staticmethod
		def f(n):
			return n - a起始
		return f
	f计算标准4 = F计算(2000)
	f计算扩展4 = F计算(3000)
	f反算标准4 = F反算(2000)
	f反算扩展4 = F反算(3000)
	@staticmethod
	def ft特定编号(n, a类型):
		if a类型 == 北向列表.E类型.e标准4:
			return C助手.f计算标准4(n)
		elif a类型 == 北向列表.E类型.e扩展4:
			return C助手.f计算扩展4(n)
		return n
	@staticmethod
	def ft统一编号(n, a类型):
		if a类型 == 北向列表.E类型.e标准4:
			return C助手.f反算标准4(n)
		elif a类型 == 北向列表.E类型.e扩展4:
			return C助手.f反算扩展4(n)
		return n
	@staticmethod
	def f判断类型(n):
		try:
			v = int(n)
			if v in C助手.c基本:
				return 北向列表.E类型.e标准4
			elif v in C助手.c高级:
				return 北向列表.E类型.e扩展4
			else:
				return None
		except:
			return None
#===============================================================================
class C规则解析器:
	ca地址关键字 = (c源地址, c目的地址)
	ca端口号关键字 = (c源端口, c目的端口)
	def __init__(self, a文本):
		self.m取词 = 字符串.C推进取词(a文本)
	def f动作(self):
		return self.m取词.f取词推进() == "permit"
	def f协议(self):
		return 南向列表.ca字符串到协议[self.m取词.f取词推进()]
	def f序号(self):
		self.m取词.f推进()
		v词 = self.m取词.f取词推进()
		return int(v词)
	def f地址4(self):
		v关键字 = self.m取词.f取词()
		if not v关键字 in C规则解析器.ca地址关键字:
			return
		self.m取词.f推进()
		v词0 = self.m取词.f取词推进()
		if v词0 == "any":
			return None
		v词1 = self.m取词.f取词推进()
		if v词1.isdigit():
			v前缀长度 = int(v词1)
			if v前缀长度 == 0:	#主机地址
				return 地址.S网络地址4.fc主机地址字符串(v词0)
			else:	#真前缀长度
				return 地址.S网络地址4.fc地址前缀长度(v词0, v前缀长度)
		elif v词1.count(".") == 3:	#通配符
			v掩码 = 地址.S网络地址4.c全f - 地址.S网络地址4.f地址字符串转整数(v词1)
			return 地址.S网络地址4.fc地址掩码(v词0, v掩码)
		else:	#不存在的情况
			raise RuntimeError("无法解析的配置")
	def f地址6(self):	#六
		v关键字 = self.m取词.f取词()
		if not v关键字 in C规则解析器.ca地址关键字:
			return
		self.m取词.f推进()
		v词0 = self.m取词.f取词推进()
		if v词0 == "any":
			return None
		return 地址.S网络地址6.fc自动(v词0)
	def f端口号(self):
		v关键字 = self.m取词.f取词()
		if not v关键字 in C规则解析器.ca端口号关键字:
			return
		self.m取词.f推进()
		v词 = self.m取词.f取词推进()
		vf端口号 = C规则解析器.ca端口号运算函数[v词]
		return vf端口号(self)
	def f端口号_大于(self):
		return 北向列表.S端口号.fc大于(协议.f解析端口号(self.m取词.f取词推进()))
	def f端口号_小于(self):
		return 北向列表.S端口号.fc小于(协议.f解析端口号(self.m取词.f取词推进()))
	def f端口号_等于(self):
		return 北向列表.S端口号.fc等于(协议.f解析端口号(self.m取词.f取词推进()))
	def f端口号_不等于(self):
		return 北向列表.S端口号.fc不等于(协议.f解析端口号(self.m取词.f取词推进()))
	def f端口号_范围(self):
		v词1 = self.m取词.f取词推进()
		v词2 = self.m取词.f取词推进()
		return 北向列表.S端口号.fc范围(range(int(v词1), int(v词2) + 1))
	ca端口号运算函数 = {
		"eq": f端口号_等于,
		"neq": f端口号_不等于,
		"gt": f端口号_大于,
		"lt": f端口号_小于,
		"range": f端口号_范围,
	}