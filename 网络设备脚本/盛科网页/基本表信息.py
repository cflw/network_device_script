from ..基础接口 import 数据表
from ..基础接口 import 信息
from . import 模式
from ..盛科命令行 import 接口 as 实现接口
from ..盛科命令行 import 基本表信息 as 命令行信息
class C接口表ev6:
	"""端口->端口状态
	适用于: 浪潮s5350(v6.x)"""
	c表格路径 = "/html/body/div/form/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody"
	def __init__(self, a设备):
		self.m设备 = a设备
	def __iter__(self):
		return self.fe行()
	def fe行(self):
		self.m设备.f切换模式(模式.C模式ev6.c端口_端口状态)
		w表格 = self.m设备.f网页_查找(C接口表ev6.c表格路径)
		for w行 in w表格.fe查找("tr"):
			if w行.fg属性("class") == "tableheader":	#标题行
				continue
			w选择, w端口, w状态, w双工, w速率, w模式, w类型, w描述 = w行.fe查找("td")
			yield 数据表.C记录({
				数据表.E字段.e本端接口: 实现接口.f创建接口ev6(w端口.fg文本()),
				数据表.E字段.e本端链路状态: 信息.f解析起宕状态(w状态.fg文本()),
				数据表.E字段.e本端双工模式: 信息.f解析双工模式(w双工.fg文本()),
				数据表.E字段.e本端速率: 命令行信息.f解析速率(w速率.fg文本()),
				数据表.E字段.e本端描述: w描述.fg文本()
			})