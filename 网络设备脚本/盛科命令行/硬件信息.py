from ..基础接口 import 信息
from ..基础接口 import 数据表
from ..基础接口 import 硬件
#===============================================================================
# 信息
#===============================================================================
def f解析状态(a文本: str):
	return "OK" in a文本
#===============================================================================
# 风扇
#===============================================================================
class F风扇信息e580(数据表.I解析表格管线):
	"""show environment
	适用于: 浪潮cn61108pcvh(v6.2.27.13, v6.6.6.R1.23)"""
	c索引 = 0
	c状态 = 11
	c速率 = 18
	c模式 = 28
	ca列 = 数据表.C切割列(c索引, c状态, c速率, c模式)
	c标题行0 = "FanIndex   Status SpeedRate Mode"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端索引, self.ca列[0], lambda x: tuple(int(v) for v in x.split("-")))
		self.f添加字段(数据表.E字段.e本端风扇状态, self.ca列[1], f解析状态)
		self.f添加字段("风扇速率", self.ca列[2], 信息.f解析数字)
		self.f添加字段("风扇模式", self.ca列[3], str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(c模式))
	fi结束 = staticmethod(lambda a行: "--" in a行)
f风扇信息e580 = F风扇信息e580()
class F风扇信息e530(数据表.I解析表格管线):
	"""show environment
	适用于: 浪潮s5350(v6.2.27.R5.66T3)"""
	c索引 = 0
	c状态 = 10
	c速率 = 20
	c模式 = 30
	ca列 = 数据表.C切割列(c索引, c状态, c速率, c模式)
	c标题行0 = "Index     Status    SpeedRate Mode"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端索引, self.ca列[0], int)
		self.f添加字段(数据表.E字段.e本端风扇状态, self.ca列[1], f解析状态)
		self.f添加字段("风扇速率", self.ca列[2], 信息.f解析数字)
		self.f添加字段("风扇模式", self.ca列[3], str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(c模式))
	fi结束 = staticmethod(lambda a行: "--" in a行)
f风扇信息e530 = F风扇信息e530()
#===============================================================================
# 电源
#===============================================================================
class F电源信息(数据表.I解析表格管线):
	"""show environment
	适用于: 浪潮cn61108pcvh(v6.2.27.13)"""
	c索引 = 0
	c状态 = 10
	c电源 = 20
	c类型 = 30
	c报警 = 40
	ca列 = 数据表.C切割列(c索引, c状态, c电源, c类型, c报警)
	c标题行0 = "Index     Status    Power     Type      Alert"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端索引, self.ca列[0], int)
		self.f添加字段(数据表.E字段.e本端电源状态, self.ca列[2], f解析状态)
		self.f添加字段(数据表.E字段.e本端电源类型, self.ca列[3], 硬件.ca电源类型.get)
		self.f添加字段("电源报警", self.ca列[4], lambda x: "YES" in x)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(c报警))
	fi结束 = staticmethod(lambda a行: "--" in a行)
f电源信息 = F电源信息()
#===============================================================================
# 温度
#===============================================================================
class F温度信息(数据表.I解析表格管线):
	"""show environment
	适用于: 浪潮cn61108pcvh(v6.2.27.13)"""
	c索引 = 0
	c温度 = 6
	c低温 = 18
	c高温 = 30
	c严重 = 42
	c位置 = 57
	ca列 = 数据表.C切割列(c索引, c温度, c低温, c高温, c严重, c位置)
	c标题行0 = "Index Temperature Lower_alarm Upper_alarm Critical_limit Position"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端索引, self.ca列[0], int)
		self.f添加字段(数据表.E字段.e本端温度, self.ca列[1], int)
		self.f添加字段(数据表.E字段.e本端低温阈值, self.ca列[2], int)
		self.f添加字段(数据表.E字段.e本端高温阈值, self.ca列[3], int)
		self.f添加字段(数据表.E字段.e本端严重高温阈值, self.ca列[4], int)
		self.f添加字段(数据表.E字段.e本端传感器, self.ca列[5], str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(c位置))
f温度信息 = F温度信息()