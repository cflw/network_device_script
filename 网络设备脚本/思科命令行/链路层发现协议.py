import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 操作
from ..基础接口 import 链路层发现协议 as 北向协议
from ..基础接口 import 数据表
from ..基础接口 import 信息
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 链路层发现协议 as 南向协议
from .常量 import *
class C邻居表:
	c设备 = 0
	c本端接口 = 20
	c持续时间 = 35
	c能力 = 46
	c对端接口 = 62
	c标题行 = "Device ID           Local Intf     Hold-time  Capability      Port ID"
	c列开始 = (c设备, c本端端口, c持续时间, c能力, c对端端口)
	def __init__(self, a文本):
		v位置 = 字符串.f连续找最后(a, C邻居表.c标题行, "\n")
		self.m文本 = a[v位置+1:]
	def __iter__(self):
		return self.fe处理数据表(self.m文本)
	fe处理数据表 = 数据表.Fe一行记录数据表(
		数据表.F去标题行(c标题行0, c标题行1),
		运算.f总是真,
		[
			数据表.F处理列(数据表.E字段.e本端名称, 序列.F切片(c设备, c本端接口), 运算.f原值),
			数据表.F处理列(数据表.E字段.e本端接口, 序列.F切片(c接口, c状态), 实现接口.f创建接口),
			数据表.F处理列(数据表.E字段.e本端链路状态, 序列.F切片(c状态, c双工), 信息.f解析起宕状态),
			数据表.F处理列(数据表.E字段.e本端双工模式, 序列.F切片(c双工, c速率), 信息.f解析双工模式),
			数据表.F处理列(数据表.E字段.e本端速率, 序列.F切片(c速率, c模式), f解析速率),
			数据表.F处理列(数据表.E字段.e本端描述, 序列.F切片(c描述, None), 运算.f原值)
		],
		运算.f总是假
	)
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