import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw工具_序列 as 序列
import cflw代码库py.cflw工具_运算 as 运算
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 数据表
from ..基础接口 import 信息
from . import 接口 as 实现接口
class C接口表sv3:
	"""show interface brief
	适用于: s6550"""
	c接口 = 0
	c管理 = 16
	c操作 = 26
	c速率双工 = 40
	c输入 = 52
	c输出 = 62
	c入错 = 72
	c出错 = 85
	c描述 = 101
	ca列开始 = (c接口, c管理, c操作, c速率双工, c输入, c输出, c入错, c出错, c描述)
	c标题行0 = "Interface       Admin    Operate        Speed/Duplex     InUti    OutUti     InErrors    OutErrors   Description"
	c标题行1 = "-------------------------------------------------------------------------------------------------------------------------"
	def __init__(self, a文本):
		self.m文本 = a文本
	def __iter__(self):
		return self.fe处理数据表(self.m文本)
	fe处理数据表 = 数据表.Fe一行记录数据表(
		数据表.F去标题行(c标题行0, c标题行1),
		运算.f总是真,
		[
			数据表.F处理列(数据表.E字段.e本端接口, 序列.F切片(c接口, c管理), 实现接口.f创建接口缩写sv3),
			数据表.F处理列(数据表.E字段.e本端管理状态, 序列.F切片(c管理, c操作), 信息.f解析起宕状态),
			数据表.F处理列(数据表.E字段.e本端链路状态, 序列.F切片(c操作, c速率双工), 信息.f解析起宕状态),
			数据表.F处理列(数据表.E字段.e本端描述, 序列.F切片(c描述, None), 运算.f原值)
		],
		运算.f总是假
	)