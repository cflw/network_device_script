import functools
import cflw代码库py.cflw网络地址 as 地址
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 数据表
from ..基础接口 import 访问控制列表 as 北向列表
from ..基础接口 import 操作
from ..命令行接口 import 命令
from ..命令行接口 import 访问控制列表 as 南向列表
from ..思科命令行.常量 import *
#===============================================================================
# 显示
#===============================================================================
class F访问列表表(数据表.I解析表格管线):
	"""show access-list
	适用于: 浪潮s6550(v3.60.10)"""
	c列表编号 = 0
	c规则数 = 6
	c使用 = 17
	c类型 = 23
	c名称 = 36
	ca列 = 数据表.C切割列(c列表编号, c规则数, c使用, c类型, c名称)
	c标题行0 = "Acl   RuleCount  InUse Type         Name    "
	c标题行1 = "-------------------------------------------------------------------------------"
	def __init__(self):	#字段名后续再改成枚举
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(北向列表.E字段.e列表编号, self.ca列[0], int)
		self.f添加字段(北向列表.E字段.e规则数量, self.ca列[1], int)
		self.f添加字段(北向列表.E字段.e是否使用, self.ca列[2], lambda x: x == "Yes")
		self.f添加字段(北向列表.E字段.e列表类型, self.ca列[3], str)
		self.f添加字段(北向列表.E字段.e列表名称, self.ca列[4], str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
f访问列表表 = F访问列表表()
def f访问列表扩展4(a文本: str):
	"""show access-list 2000
	适用于: 浪潮s6550(v3.60.10)"""
	#初始处理
	v文本 = 字符串.f提取字符串之间(a文本, "rule ", None, True)
	#返回
	ve规则 = (C扩展4.f解析规则(v行) for v行 in v文本.split("\n"))
	return ve规则
#===============================================================================
# 生成
#===============================================================================
f生成允许 = 南向列表.f生成允许
def f生成地址4(a地址)->str:
	if not a地址:
		return "any"
	v地址 = 地址.S网络地址4.fc自动(a地址)
	if v地址.fi空():
		return "any"
	else:
		return "%s %s" % (v地址.fg网络号s(), v地址.fg掩码s())
#端口号
class F生成端口(北向列表.I生成端口):
	def f等于(self, a序列):
		return " ".join(字符串.ft字符串序列(a序列))
	def f范围(self, a值: range):
		return "range %d %d" % (a值.start, a值.stop - 1)
f生成端口 = F生成端口()
#===============================================================================
# 配置
#===============================================================================
class I列表配置(南向列表.I列表配置):
	def __init__(self, a, a列表编号: int, a名称: str = ""):
		南向列表.I列表配置.__init__(self, a)
		self.m列表编号 = a列表编号
		self.m名称 = a名称
	def fg进入命令(self):
		"""命令: access-list 列表编号 [name 名称]"""
		v命令 = 命令.C命令("access-list")
		v命令 += self.m列表编号
		if self.m名称:
			v命令 += "name", self.m名称
		return v命令
	def fg删除命令(self):
		"""命令: no access-list 列表编号 [name 名称]"""
		return self.fg进入命令().f前面添加(c不)
	def f删除规则(self, a规则序号):
		"""命令: no rule 序号"""
		v命令 = 命令.C命令("no rule")
		v命令 += a规则序号
		self.f执行当前模式命令(v命令)
	def fs规则(self, a序号 = 北向列表.c空序号, a规则 = 北向列表.c空规则, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		if 操作.fi加操作(v操作):
			self.f添加规则(a序号, a规则)
		elif 操作.fi减操作(v操作):
			self.f删除规则(a序号)
		else:
			raise ValueError("不支持的操作")
class C标准4(I列表配置):
	def f添加规则(self, a规则序号, a规则):
		raise NotImplementedError()
class C扩展4(I列表配置):
	def f添加规则(self, a规则序号, a规则):
		"""命令: rule 序号 允许 协议 源地址 目的地址 目的端口"""
		v命令 = 命令.C命令("rule")
		v命令 += a规则序号
		v命令 += f生成允许(a规则.m允许)
		v命令 += f生成地址4(a规则.m源地址)
		v命令 += f生成端口(a规则.m源端口)
		v命令 += f生成地址4(a规则.m目的地址)
		v命令 += f生成端口(a规则.m目的端口)
		self.f执行当前模式命令(v命令)
	@staticmethod
	def f解析规则(a规则: str):
		v解析器 = C规则解析器(a规则)
		v规则 = 北向列表.S规则()
		v规则.m序号 = v解析器.fg规则序号()
		v规则.m允许 = v解析器.fg动作()
		v规则.m协议 = v解析器.fg协议()
		v规则.m源地址 = v解析器.fg地址4()
		v规则.m源端口 = v解析器.fg端口号()
		v规则.m目的地址 = v解析器.fg地址4()
		v规则.m目的端口 = v解析器.fg端口号()
		return v规则
#===============================================================================
# 解析
#===============================================================================
class C规则解析器:
	def __init__(self, a文本):
		self.m取词 = 字符串.C推进取词(a文本)
	def fg规则序号(self):
		if not self.m取词.f取词推进() == "rule":
			return None	#开头没有rule,检查文本是否正确
		return int(self.m取词.f取词推进())
	def fg动作(self):
		return self.m取词.f取词推进() == "permit"
	def fg协议(self):
		return 南向列表.ca字符串到协议[self.m取词.f取词推进()]
	def fg地址4(self):
		v词0 = self.m取词.f取词推进()
		if v词0 == "any":
			return None
		elif v词0.count(".") == 3:	#地址格式
			v词1 = self.m取词.f取词推进()
			return 地址.S网络地址4.fc地址掩码(v词0, v词1)
		else:
			return None
	def fg端口号(self):
		v词0 = self.m取词.f取词()
		if v词0 == None:	#结束
			return None
		elif v词0.isdigit():	#一个端口
			self.m取词.f推进()
			return int(v词0)
		elif v词0 == "range":	#端口范围
			self.m取词.f推进()
			v词1 = self.m取词.f取词推进()
			v词2 = self.m取词.f取词推进()
			return range(int(v词1), int(v词2))
		else:
			return None	#不是端口号