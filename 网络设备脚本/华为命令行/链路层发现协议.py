import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 操作
from ..基础接口 import 数据表
from ..基础接口 import 链路层发现协议 as 北向协议
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 链路层发现协议 as 南向协议
from ..华为命令行.常量 import *
from . import 接口 as 实现接口
#===============================================================================
# 数据表
#===============================================================================
class F邻居详细(数据表.I解析列表管线):
	"""display lldp neighbor 
	适用于: 华为s5700(模拟器), 华为ar201(模拟器)"""
	c本端接口正则 = r"(.+?) has (\d+) neighbors:"
	c邻居索引 = "Neighbor index"
	c底层标识 = "Chassis ID"
	c对端接口 = "Port ID"
	c对端接口描述 = "Port description"
	c对端系统名 = "System name"
	c对端系统描述 = "System description"
	def __init__(self):
		数据表.I解析列表管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, 数据表.F正则字段(self.c本端接口正则, 1), 实现接口.f创建接口)
		self.f添加字段(数据表.E字段.e对端物理地址, 数据表.F列表字段(self.c底层标识), 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e对端接口, 数据表.F列表字段(self.c对端接口), str)
		self.f添加字段(数据表.E字段.e对端名称, 数据表.F列表字段(self.c对端系统名), str)
		self.f添加字段(数据表.E字段.e对端描述, 数据表.F列表字段(self.c对端系统描述), str)
	f下一记录 = staticmethod(数据表.F下一记录行("neighbors"))
	fi有效字段 = staticmethod(数据表.F有效行数(5))
f邻居详细 = F邻居详细()
class F邻居摘要(数据表.I解析表格管线):
	"""display lldp neighbor brief
	适用于: 华为s5700(模拟器), 华为ar201(模拟器)"""
	c标题行 = "Local Intf   Neighbor Dev             Neighbor Intf             Exptime"
	c本端接口 = 0
	c对端名称 = 13
	c对端接口 = 38
	c有效期 = 64
	ca列 = 数据表.C切割列(c本端接口, c对端名称, c对端接口, c有效期)
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[0], 实现接口.f创建接口缩写)
		self.f添加字段(数据表.E字段.e对端名称, self.ca列[1], str)
		self.f添加字段(数据表.E字段.e对端接口, self.ca列[2], str)
		self.f添加字段(数据表.E字段.e本端寿命, self.ca列[3], int)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
	fi有效行 = staticmethod(数据表.F有效长度(c有效期))
f邻居摘要 = F邻居摘要()


