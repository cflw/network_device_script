import functools
import cflw代码库py.cflw工具_运算 as 运算
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 数据表
from . import 接口 as 实现接口
class F邻居简介ev6(数据表.I解析列表管线):
	"""show lldp neighbor brief
	适用于: 浪潮s5350(v6.2.27.R5.*)"""
	c本端端口 = "Local Port"
	c对端端口 = "Remote Port"
	c保持时间 = "Hold Time"
	c过期时间 = "Expire Time"
	c系统名称 = "System Name"
	c分割线 = "------------------------------------------------------------"
	c值开始 = 14
	def __init__(self):
		数据表.I解析列表管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, 数据表.F列表字段(self.c本端端口), 实现接口.f创建接口_ev6)
		self.f添加字段(数据表.E字段.e对端接口, 数据表.F列表字段(self.c对端端口), str)
		self.f添加字段(数据表.E字段.e本端保持时间, 数据表.F列表字段(self.c保持时间), int)
		self.f添加字段(数据表.E字段.e本端寿命, 数据表.F列表字段(self.c过期时间), int)
		self.f添加字段(数据表.E字段.e对端名称, 数据表.F列表字段(self.c系统名称), str)
	f下一记录 = staticmethod(数据表.F下一记录(c分割线))
	fi有效记录 = staticmethod(数据表.F有效行数(5))
f邻居简介ev6 = F邻居简介ev6()