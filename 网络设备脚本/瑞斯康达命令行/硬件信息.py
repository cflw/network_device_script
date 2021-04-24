import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 数据表
from ..基础接口 import 硬件
#===============================================================================
# 风扇
#===============================================================================
class F风扇状态表(数据表.I解析表格管线):
	"""show fan-monitor status unit all		其中的表格部分
	适用于: 浪潮s6550(v3.60.398)"""
	c索引 = 0
	c速度 = 14
	c状态 = 32
	ca列 = 数据表.C切割列(c索引, c速度, c状态)
	c标题行0 = "FanIndex      FanSpeed(r/min)   FanWorkState    "
	c标题行1 = "------------------------------------------------"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端索引, self.ca列[0], int)
		self.f添加字段(数据表.E字段.e本端风扇转速, self.ca列[1], int)
		self.f添加字段(数据表.E字段.e本端风扇状态, self.ca列[2], lambda x: x == "normal")
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
	fi结束 = staticmethod(数据表.fi空行)
f风扇状态表 = F风扇状态表()
class F风扇状态(数据表.I解析表格列表管线):
	"""show fan-monitor status unit all		全部
	适用于: 浪潮s6550(v3.60.398)"""
	c单元 = r"unit (\d+):"
	def __init__(self):
		数据表.I解析表格列表管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端单元, 数据表.F正则字段(self.c单元, 1), int)
		self.f添加表格(f风扇状态表)
	f下一记录 = staticmethod(数据表.F下一记录("Fan status information of unit"))
f风扇状态 = F风扇状态()
#===============================================================================
# 电源
#===============================================================================
class F电源信息(数据表.I解析表格管线):
	"""show environment power unit all
	适用于: 浪潮s6550(v3.60.398)"""
	c索引 = 0
	c电压 = 10
	c类型 = 23
	c序列号 = 34
	c状态 = 64
	ca列 = 数据表.C切割列(c索引, c电压, c类型, c序列号, c状态)
	c标题行0 = "Index     Volt(mv)     Type       Serial Num                    status"
	c标题行1 = "--------------------------------------------------------------------------"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端索引, self.ca列[0], int)
		self.f添加字段(数据表.E字段.e本端电源电压, self.ca列[1], lambda x: float(x) * 0.001)
		self.f添加字段(数据表.E字段.e本端电源类型, self.ca列[2], 硬件.ca电源类型.get)
		self.f添加字段(数据表.E字段.e本端序列号, self.ca列[3], str)
		self.f添加字段(数据表.E字段.e本端电源状态, self.ca列[4], lambda x: "on" in x)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
	fi结束 = staticmethod(数据表.fi空行)
f电源信息 = F电源信息()
class F电源全部(数据表.I解析表格列表管线):
	"""show environment power unit all
	适用于: 浪潮s6550(v3.60.398)"""
	c单元 = r"unit (\d+):"
	def __init__(self):
		数据表.I解析表格列表管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端单元, 数据表.F正则字段(self.c单元, 1), int)
		self.f添加表格(f电源信息)
	f下一记录 = staticmethod(数据表.F下一记录("The power information of unit"))
f电源全部 = F电源全部()
#===============================================================================
# 温度
#===============================================================================
class F温度信息(数据表.I解析列表管线):
	"""show environment temperature unit all
	适用于: 浪潮s6550(v3.60.398)"""
	c当前 = "Current"
	c最小 = "Min"
	c最大 = "Max"
	c单元 = 0
	c摄氏度 = 17
	c华氏度 = 28
	ca列 = 数据表.C切割列(c单元, c摄氏度, c华氏度)
	c标题行0 = "    Units        Celsius    Fahrenheit"
	c标题行1 = "    -----------------------------------"
	def __init__(self):
		数据表.I解析列表管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端温度, 数据表.F指定行列(字符串.F提取包含行(self.c当前), self.ca列[1]), int)
		self.f添加字段(数据表.E字段.e本端低温阈值, 数据表.F指定行列(字符串.F提取包含行(self.c最小), self.ca列[1]), int)
		self.f添加字段(数据表.E字段.e本端高温阈值, 数据表.F指定行列(字符串.F提取包含行(self.c最大), self.ca列[1]), int)
	f下一记录 = staticmethod(数据表.f下一记录_直接结束)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
f温度信息 = F温度信息()
class F温度全部(数据表.I解析表格列表管线):
	"""show environment temperature unit all
	适用于: 浪潮s6550(v3.60.398)"""
	c单元 = r"unit (\d+):"
	def __init__(self):
		数据表.I解析表格列表管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端单元, 数据表.F正则字段(self.c单元, 1), int)
		self.f添加表格(f温度信息)
	f下一记录 = staticmethod(数据表.F下一记录("The temperature information of unit "))
f温度全部 = F温度全部()