from ..基础接口 import 操作
from ..命令行接口 import 命令
from ..基础接口 import 时间范围 as 北向时间范围
from ..命令行接口 import 时间范围 as 南向时间范围
import cflw代码库py.cflw英语 as 英语
from .常量 import *
ca日子 = {
	北向时间范围.E日子.e一: "monday",
	北向时间范围.E日子.e二: "tuesday",
	北向时间范围.E日子.e三: "wednesday",
	北向时间范围.E日子.e四: "thursday",
	北向时间范围.E日子.e五: "friday",
	北向时间范围.E日子.e六: "saturday",
	北向时间范围.E日子.e日: "sunday",
	北向时间范围.E日子.e工作日: "weekdays",
	北向时间范围.E日子.e周末: "weekend",
	北向时间范围.E日子.e每天: "daily",
}
def f生成绝对时间(a时间元组):
	"""参数: (年,月,日,时,分)
	返回: "时:分 日 月 年" """
	return "%s:%s %s %s %s" % (a时间元组[3], a时间元组[4], a时间元组[2], 英语.f月份(a时间元组[1])[:3], a时间元组[0])	#时:分 日 月 年
def f生成定期时间(a时间元组):
	"(时,分)"
	return "%s:%s" % (a时间元组[0], a时间元组[1])	#时:分
def f生成时间范围命令(a时间范围):
	if a时间范围.m绝对:
		v命令 = 命令.C命令("absolute")
		v命令 += "start " + f生成绝对时间(a时间范围.m开始时间)
		v命令 += "end " + f生成绝对时间(a时间范围.m结束时间)
	else:	#定期
		v命令 = 命令.C命令("periodic")
		v命令 += ca日子[a时间范围.m日子]
		v命令 += f生成定期时间(a时间范围.m开始时间)
		v命令 += "to"
		v命令 += f生成定期时间(a时间范围.m结束时间)
	return v命令
class C时间范围(南向时间范围.I时间范围配置):
	def __init__(self, a, a名称):
		南向时间范围.I时间范围配置.__init__(self, a)
		self.m名称 = a名称
	def fg进入命令(self):
		return "time-range " + self.m名称
	def f执行时间范围命令(self, ai: bool, a时间范围):
		v命令 = f生成时间范围命令(a时间范围)
		v命令.f前置否定(ai, c不)
		self.f执行当前模式命令(v命令)
	def fs值(self, a时间范围, a操作 = 操作.E操作.e添加):
		v操作 = 操作.f解析操作(a操作)
		if 操作.fi加操作(v操作):
			self.f添加(a时间范围)
		elif 操作.fi减操作(v操作):
			self.f添加(a时间范围)
	def f添加(self, a时间范围):
		self.f执行时间范围命令(True, a时间范围)
	def f删除(self, a时间范围):
		self.f执行时间范围命令(False, a时间范围)
