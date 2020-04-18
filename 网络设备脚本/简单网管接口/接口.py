import enum
import numpy
import pandas	#pandas
import cflw代码库py.cflw工具_序列 as 序列
from ..基础接口 import 数据表
from ..基础接口 import 接口
from . import 模式
class E类型(enum.IntEnum):
	e其他 = 1	#other(1)
	e以太网 = 6	#ethernetCsmacd(6)
	e虚拟 = 53	#propVirtual(53)
#===============================================================================
# 基础
#===============================================================================
class I接口配置基础(模式.I模式):
	def __init__(self, a, a索引):
		模式.I模式.__init__(self, a)
		self.m索引 = a索引
#===============================================================================
# 显示
#===============================================================================
class I全局接口显示(模式.I模式):
	def f获取_接口数量(self):
		return self.m设备.f获取(c标识_接口数量0, at类型 = int)
	def f遍历_接口索引(self):
		return self.m设备.f遍历(c标识_接口索引, at类型 = int)
class I接口显示(I接口配置基础):
	def f获取_接口描述(self):
		return self.m设备.f获取(f"{c标识_接口描述}.{self.m索引}", at类型 = str)
	def f获取_接口类型(self):
		return self.m设备.f获取(f"{c标识_接口类型}.{self.m索引}", at类型 = int)
#===============================================================================
# 配置
#===============================================================================
class I接口配置(I接口配置基础):
	def f设置_网络地址4(self, a值):
		raise NotImplementedError()
	def f设置_开关(self, a值):
		return self.m设备.f设置(f"{c标识_接口管理状态}.{self.m索引}", a值)
	def fs网络地址4(self, a地址, a操作 = None):
		raise NotImplementedError()
	def fs开关(self, a操作 = None):
		self.f设置_开关(bool(a操作))