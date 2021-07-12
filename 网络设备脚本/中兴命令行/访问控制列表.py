import functools
import cflw代码库py.cflw网络地址 as 地址
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 操作
from ..基础接口 import 协议
from ..基础接口 import 异常
from ..基础接口 import 数据表
from ..基础接口 import 访问控制列表 as 北向列表
from ..命令行接口 import 命令
from ..命令行接口 import 访问控制列表 as 南向列表
from .常量 import *
#===============================================================================
# 显示
#===============================================================================
class F摘要表(数据表.I解析表格管线):
	"""show ipv4-access-lists brief
	适用于: 中兴m6000"""
	c编号 = 0
	c名称 = 9
	c规则数 = 31
	ca列 = 数据表.C切割列(c编号, c名称, c规则数)
	c标题行0 = "No.      ACL                   RuleSum"
	c标题行1 = "------------------------------------------------"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(北向列表.E字段.e列表编号, self.ca列[0], int)
		self.f添加字段(北向列表.E字段.e列表名称, self.ca列[1], str)
		self.f添加字段(北向列表.E字段.e规则数量, self.ca列[2], int)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
f摘要表 = F摘要表()
#===============================================================================
# 生成
#===============================================================================
def f生成地址4(a地址):
	if not a地址:
		return "any"
	v地址 = 地址.S网络地址4.fc自动(a地址)
	if v地址.fi主机():
		return v地址.fg地址s()
	elif v地址.fi空():
		return "any"
	else:
		return "%s %s" % (v地址.fg网络号s(), v地址.fg反掩码s())
class F生成端口(北向列表.I生成端口):
	def f等于(self, a序列):
		return "eq " + " ".join(字符串.ft字符串序列(a序列))
	def f大于等于(self, a值: int):
		return "ge %d" % (a值,)
	def f小于等于(self, a值: int):
		return "le %d" % (a值,)
	def f范围(self, a值: range):
		return "range %d %d" % (a值.start, a值.stop - 1)
f生成端口 = F生成端口()
#允许
f生成允许 = 南向列表.f生成允许
#===============================================================================
# 模式
#===============================================================================
class C扩展4_m6000(南向列表.I列表配置):
	"""适用于: 中兴m6000"""
	def __init__(self, a, a名称):
		南向列表.I列表配置.__init__(self, a)
		self.m名称 = a名称
	def fg进入命令(self):
		"""命令: ipv4-access-list 名称"""
		v命令 = 命令.C命令("ipv4-access-list")
		v命令 += self.m名称
		return v命令
	def fs规则(self, a序号 = None, a规则 = None, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		if 操作.fi加操作(v操作):
			self.f添加规则(a序号, a规则)
		elif 操作.fi减操作(v操作):
			self.f删除规则(a序号)
	def f添加规则(self, a序号, a规则):
		v命令 = 命令.C命令("rule")
		v命令 += a序号
		v命令 += f生成允许(a规则.m允许)
		#确定
		v命令 += 南向列表.ca协议到字符串4[a规则.m协议]
		v层 = 协议.f取协议层(a规则.m协议)
		#按层
		if v层 == 3:
			v命令 += f生成地址4(a规则.m源地址)
			v命令 += f生成地址4(a规则.m目的地址)
		elif v层 == 4:
			v命令 += f生成地址4(a规则.m源地址)
			v命令 += f生成端口(a规则.m源端口)
			v命令 += f生成地址4(a规则.m目的地址)
			v命令 += f生成端口(a规则.m目的端口)
		else:
			raise NotImplementedError("迷之逻辑")
		#执行命令
		self.f执行当前模式命令(v命令)
	def f删除规则(self, a序号):
		"""命令: no rule 序号"""
		v命令 = f"no rule {a序号}"
		self.f执行当前模式命令(v命令)
	def f移动规则(self, a旧序号, a新序号):
		"""命令: move 旧序号 新序号"""
		v命令 = f"move {a旧序号} {a新序号}"
		self.f执行当前模式命令(v命令)