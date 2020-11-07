import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
import cflw代码库py.cflw工具_序列 as 序列
from ..基础接口 import 操作
from ..基础接口 import 数据表
from ..基础接口 import 接口 as 北向接口
from ..基础接口 import 链路层发现协议 as 北向协议
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 链路层发现协议 as 南向协议
from .常量 import *
from . import 接口 as 实现接口
#===============================================================================
# 配置模式
#===============================================================================
class C进程配置v7(模式.C同级模式, 南向协议.I进程配置):
	def __init__(self, a):
		南向协议.I进程配置.__init__(self, a)
	def f模式_接口(self, a接口):
		v接口 = 实现接口.f创建接口(a接口)
		return C接口配置v7(self.fg上级模式(), v接口)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("lldp global enable")
		v命令.f前置肯定(操作.fi关操作(v操作), c不)
		self.f执行当前模式命令(v命令)
class C接口配置v7(南向协议.I接口配置):
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
class F邻居表信息v7(数据表.I解析列表管线):
	"""display lldp neighbor-information 
	适用于: 华三s6900(v7.1.*)"""
	c值 = 23
	c本端接口 = "LLDP neighbor-information of port"
	c邻居索引 = " LLDP neighbor index :"
	c底层标识 = " ChassisID/subtype   :"
	c对端接口 = " PortID/subtype      :"
	c对端属性 = " Capabilities        :"
	def __init__(self):
		数据表.I解析列表管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, lambda x: 字符串.f提取字符串之间(x, "[", "]"), 实现接口.f创建接口)
		self.f添加字段(数据表.E字段.e对端物理地址, F列表字段_斜杠前(F邻居表信息v7.c底层标识), 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e对端接口, F列表字段_斜杠前(F邻居表信息v7.c对端接口), str)
	f下一记录 = staticmethod(数据表.F下一记录(c本端接口))
	fi有效字段 = staticmethod(数据表.F有效行数(5))
f邻居表信息v7 = F邻居表信息v7()
class F邻居表列表v7(数据表.I解析表格管线):
	"""display lldp neighbor-information list
	适用于: 华三s6900(v7.1.*)"""
	c标题行 = "Local Interface Chassis ID      Port ID                    System Name          "
	c本端接口 = 0
	c底层标识 = 16
	c对端接口 = 32
	c系统名 = 59
	ca列 = 序列.C切片组(c本端接口, c底层标识, c对端接口, c系统名)
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, F邻居表列表v7.ca列.F切片(0), 实现接口.f创建接口缩写)
		self.f添加字段(数据表.E字段.e对端物理地址, F邻居表列表v7.ca列.F切片(1), 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e对端接口, F邻居表列表v7.ca列.F切片(2), str)
		self.f添加字段(数据表.E字段.e对端名称, F邻居表列表v7.ca列.F切片(3), str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
	fi有效行 = staticmethod(数据表.F有效长度(c系统名))
f邻居表列表v7 = F邻居表列表v7()