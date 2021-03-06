import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw工具_运算 as 运算
from ..基础接口 import 操作
from ..基础接口 import 链路层发现协议 as 北向协议
from ..基础接口 import 数据表
from ..基础接口 import 信息
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 链路层发现协议 as 南向协议
from .常量 import *
from . import 接口 as 实现接口
#===============================================================================
# 表
#===============================================================================
class F邻居表(数据表.I解析表格管线):
	"""show lldp neighbors
	适用于: 浪潮s5960(v12.2.*), 浪潮s6650(v11.12.*)"""
	c设备 = 0	#Device ID
	c本端接口 = 20	#Local Intf
	c保持时间 = 35	#Hold-time
	c能力 = 46	#Capability
	c对端接口 = 62	#Port ID
	c标题行0 = "Device ID           Local Intf     Hold-time  Capability      Port ID"
	ca列 = 数据表.C切割列(c设备, c本端接口, c保持时间, c能力, c对端接口)
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e对端名称, F邻居表.ca列[0], 运算.f原值)
		self.f添加字段(数据表.E字段.e本端接口, F邻居表.ca列[1], 实现接口.f创建接口缩写)
		self.f添加字段(数据表.E字段.e本端保持时间, F邻居表.ca列[2], int)
		self.f添加字段(数据表.E字段.e对端接口, F邻居表.ca列[4], 运算.f原值)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	@staticmethod
	def fi有效行(a行: str):
		if a行[F邻居表.c保持时间 : F邻居表.c能力].strip().isdigit():	#保持时间
			return True
		return False
	@staticmethod
	def fi结束(a行: str):
		return "Total entries displayed:" in a行
f邻居表 = F邻居表()
#===============================================================================
# 配置
#===============================================================================
class C进程配置(模式.C同级模式, 南向协议.I进程配置):
	def __init__(self, a):
		南向协议.I进程配置.__init__(self, a)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("lldp run")
		v命令.f前置肯定(操作.fi关操作(v操作), c不)
		self.f执行当前模式命令(v命令)
	def f显示_邻居表(self):
		raise NotImplementedError()