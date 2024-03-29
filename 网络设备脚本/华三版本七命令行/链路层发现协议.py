import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw函数 as 函数
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 操作
from ..基础接口 import 数据表
from ..基础接口 import 链路层发现协议 as 北向协议
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 链路层发现协议 as 南向协议
from ..华三命令行.常量 import *
from . import 接口 as 实现接口
#===============================================================================
# 配置模式
#===============================================================================
class C进程配置_v7(模式.C同级模式, 南向协议.I进程配置):
	def __init__(self, a):
		南向协议.I进程配置.__init__(self, a)
	def f模式_接口(self, a接口):
		v接口 = 实现接口.f创建接口(a接口)
		return C接口配置_v7(self.fg上级模式(), v接口)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("lldp global enable")
		v命令.f前置肯定(操作.fi关操作(v操作), c不)
		self.f执行当前模式命令(v命令)
class C接口配置_v7(南向协议.I接口配置):
	def __init__(self, a, a接口):
		南向协议.I接口配置.__init__(self, a, a接口)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("lldp enable")
		v命令.f前置肯定(操作.fi关操作(v操作), c不)
		self.f执行当前模式命令(v命令)
#===============================================================================
# 数据表
#===============================================================================
def F列表字段_斜杠前(a字段: str):
	def f提取(a记录: str)->str:
		v行 = 字符串.f提取字符串之间(a记录, a字段, "\n")
		v结束 = v行.rfind("/")
		return v行[:v结束]
	return f提取
class F邻居表信息_v7(数据表.I解析列表管线):
	"""display lldp neighbor-information 
	适用于: 华三s6900(v7.1.*), 紫光s7800xp(v7.1.*)"""
	c值 = 23
	c本端接口 = "LLDP neighbor-information of port"
	c邻居索引 = " LLDP neighbor index :"
	c底层标识 = " ChassisID/subtype   :"
	c对端接口 = " PortID/subtype      :"
	c对端属性 = " Capabilities        :"
	def __init__(self):
		数据表.I解析列表管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, lambda x: 字符串.f提取字符串之间(x, "[", "]"), 实现接口.f创建接口v7)
		self.f添加字段(数据表.E字段.e对端物理地址, F列表字段_斜杠前(self.c底层标识), 函数.A忽略异常(地址.S物理地址.fc字符串))
		self.f添加字段(数据表.E字段.e对端接口, F列表字段_斜杠前(self.c对端接口), str)
	f下一记录 = staticmethod(数据表.F下一记录(c本端接口))
	fi有效字段 = staticmethod(数据表.F有效行数(5))
f邻居表信息_v7 = F邻居表信息_v7()
class F邻居表列表_s6v7(数据表.I解析表格管线):
	"""display lldp neighbor-information list
	适用于: 华三s6900(v7.1.*)"""
	c标题行 = "Local Interface Chassis ID      Port ID                    System Name          "
	c本端接口 = 0
	c底层标识 = 16
	c对端接口 = 32
	c系统名 = 59
	ca列 = 数据表.C切割列(c本端接口, c底层标识, c对端接口, c系统名)
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[0], 实现接口.f创建接口缩写v7)
		self.f添加字段(数据表.E字段.e对端物理地址, self.ca列[1], 函数.A忽略异常(地址.S物理地址.fc字符串))
		self.f添加字段(数据表.E字段.e对端接口, self.ca列[2], str)
		self.f添加字段(数据表.E字段.e对端名称, self.ca列[3], str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
	fi有效行 = staticmethod(数据表.F有效长度(c系统名))
f邻居表列表_s6v7 = F邻居表列表_s6v7()
class F邻居表列表_s7v7(数据表.I解析表格管线):
	"""display lldp neighbor-information list
	适用于: 紫光s7800xp(v7.1.*)"""
	c标题行 = "Local Interface Chassis ID      Port ID                         System Name     "
	c本端接口 = 0
	c底层标识 = 16
	c对端接口 = 32
	c系统名 = 64
	ca列 = 数据表.C切割列(c本端接口, c底层标识, c对端接口, c系统名)
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[0], 实现接口.f创建接口缩写v7)
		self.f添加字段(数据表.E字段.e对端物理地址, self.ca列[1], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e对端接口, self.ca列[2], str)
		self.f添加字段(数据表.E字段.e对端名称, self.ca列[3], str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
	fi有效行 = staticmethod(数据表.F有效长度(c系统名))
f邻居表列表_s7v7 = F邻居表列表_s7v7()
class F邻居表列表_s9v7(数据表.I解析列表管线):
	"""display lldp neighbor-information list
	适用于: 华三s9810(v7.1.*)"""
	c系统名 = 0
	c本端接口 = 21
	c底层标识 = 37
	c对端接口 = 53
	c行尾 = 80
	c标题行 = "System Name          Local Interface Chassis ID      Port ID"
	ca列 = 数据表.C切割列(c系统名, c本端接口, c底层标识, c对端接口, c行尾)
	def __init__(self):
		数据表.I解析列表管线.__init__(self)
		self.f添加字段(数据表.E字段.e对端名称, self.ca列.F跨行切片(0), str)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[1], 实现接口.f创建接口缩写v7)
		self.f添加字段(数据表.E字段.e对端物理地址, self.ca列[2], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e对端接口, self.ca列[3], str)
	def f下一记录(self, a文本: str, a开始位置: int) -> int:
		v下一行切片 = 字符串.f找下一行切片(a文本, a开始位置)
		if not v下一行切片:
			return -1
		v下一行s = a文本[v下一行切片]
		if v下一行s[self.c本端接口] != ' ':
			return v下一行切片.start
		else:
			return v下一行切片.stop + 1
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
f邻居表列表_s9v7 = F邻居表列表_s9v7()