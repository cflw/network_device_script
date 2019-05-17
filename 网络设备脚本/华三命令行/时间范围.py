from ..基础接口 import 操作
from ..基础接口 import 异常
from ..基础接口 import 时间范围 as 北向时间范围
from ..基础接口 import 接口 as 北向接口
from ..命令行接口 import 模式
from ..命令行接口 import 命令
from ..命令行接口 import 时间范围 as 南向时间范围
from .常量 import *
ca日子 = {
	北向时间范围.E日子.e一: "mon",
	北向时间范围.E日子.e二: "tue",
	北向时间范围.E日子.e三: "wed",
	北向时间范围.E日子.e四: "thu",
	北向时间范围.E日子.e五: "fri",
	北向时间范围.E日子.e六: "sat",
	北向时间范围.E日子.e日: "sun",
	北向时间范围.E日子.e工作日: "working-day",
	北向时间范围.E日子.e周末: "off-day",
	北向时间范围.E日子.e每天: "daily",
}
def f生成绝对时间(a元组: tuple):
	"(年,月,日,时,分)"
	return "%s:%s %s/%s/%s" % (a元组[3], a元组[4], a元组[0], a元组[1], a元组[2])
def f生成相对时间(a元组: tuple):
	"(时,分)"
	return "%s:%s" % a元组
def f生成命令(a名称: str, a时间范围: 北向时间范围.S时间范围):
	#前置
	v命令 = 命令.C命令("time-range")
	v命令 += a名称
	#参数
	if a时间范围.m绝对:
		if a时间范围.m开始时间:
			v命令 += "from", f生成绝对时间(a时间范围.m开始时间)
		v命令 += "to", f生成绝对时间(a时间范围.m结束时间)
	else:
		v命令 += f生成相对时间(a时间范围.m开始时间)
		v命令 += "to", f生成相对时间(a时间范围.m结束时间)
		v命令 += ca日子[a时间范围.m日子]
	return v命令
class C时间范围(模式.C同级模式, 南向时间范围.I时间范围配置):
	def __init__(self, a, a名称: str):
		南向时间范围.I时间范围配置.__init__(self, a)
		self.m名称 = a名称
	def f执行时间范围命令(self, ai: bool, a时间范围: 北向时间范围.S时间范围):
		v命令 = f生成命令(self.m名称, a时间范围)
		v命令.f前置否定(ai, c不)
		self.f执行当前模式命令(v命令)
	def f添加(self, a时间范围: 北向时间范围.S时间范围):
		self.f执行时间范围命令(True, a时间范围)
	def f删除(self, a时间范围: 北向时间范围.S时间范围):
		self.f执行时间范围命令(False, a时间范围)
	def fs值(self, a时间范围, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		if 操作.fi加操作(v操作):
			self.f添加(a时间范围)
		elif 操作.fi减操作(v操作):
			self.f删除(a时间范围)
		else:
			raise 异常.X操作(a操作)
