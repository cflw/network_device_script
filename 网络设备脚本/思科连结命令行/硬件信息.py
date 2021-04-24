import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 数据表
from ..基础接口 import 硬件
#===============================================================================
# 通用
#===============================================================================
def f解析状态(a: str):
	return "ok" in a.lower()
#===============================================================================
# 资产
#===============================================================================
class F资产信息(数据表.I解析列表管线):
	"""show inventory
	适用于: 浪潮cn8672up(v7.3.0), 浪潮cn8696q(v7.3.0), 浪潮cn61108pcv(v9.2.3)"""
	c名称 = r"""^NAME: "(.+?)","""
	c描述 = r"""DESCR: "(.+?)"\s"""
	c型号 = r"""PID: (.+?),"""	#PID
	cVID = r"""VID: (.+?),"""	#VID
	c序列号 = r"""SN: (.+?)\s"""	#SN
	def __init__(self):
		数据表.I解析列表管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端名称, 数据表.F正则字段(F资产信息.c名称, 1), str)
		self.f添加字段(数据表.E字段.e本端描述, 数据表.F正则字段(F资产信息.c描述, 1), str)
		self.f添加字段(数据表.E字段.e本端型号, 数据表.F正则字段(F资产信息.c型号, 1), str)
		self.f添加字段("VID", 数据表.F正则字段(F资产信息.cVID, 1), str)
		self.f添加字段(数据表.E字段.e本端序列号, 数据表.F正则字段(F资产信息.c序列号, 1), str)
	f下一记录 = staticmethod(数据表.F下一记录("NAME:"))
f资产信息 = F资产信息()
#===============================================================================
# 电源
#===============================================================================
def f解析功率(a文本: str):
	return int(a文本[:-2])
class F电源v7_电源(数据表.I解析表格管线):
	"""show environment power, 第1个表
	适用于: 浪潮cn8672up(v7.3.0), 浪潮cn8696q(v7.3.0)"""
	c序号 = 0
	c型号 = 4
	c类型 = 25
	c功率 = 31
	c电流 = 43
	c状态 = 53
	ca列 = 数据表.C切割列(c序号, c型号, c类型, c功率, c电流, c状态)
	c标题行0 = "PS  Model                Input Power       Current   Status"
	c标题行1 = "                         Type  (Watts)     (Amps)          "
	c标题行2 = "-----------------------------------------------------------"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端索引, self.ca列[0], int)
		self.f添加字段(数据表.E字段.e本端型号, self.ca列[1], str)
		self.f添加字段(数据表.E字段.e本端电源类型, self.ca列[2], 硬件.ca电源类型.get)
		self.f添加字段(数据表.E字段.e本端额定功率, self.ca列[3], float)
		self.f添加字段(数据表.E字段.e本端电源电流, self.ca列[4], float)
		self.f添加字段(数据表.E字段.e本端电源状态, self.ca列[5], f解析状态)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1, c标题行2))
	fi有效行 = staticmethod(数据表.F有效长度(c状态))
	fi结束 = staticmethod(数据表.fi空行)
f电源v7_电源 = F电源v7_电源()
class F电源v7_板卡(数据表.I解析表格管线):
	"""show environment power, 第2个表
	适用于: 浪潮cn8672up(v7.3.0), 浪潮cn8696q(v7.3.0)"""
	c序号 = 0
	c型号 = 4
	c取功率 = 28
	c取电流 = 38
	c分配功率 = 50
	c分配电流 = 60
	c状态 = 72
	ca列 = 数据表.C切割列(c序号, c型号, c取功率, c取电流, c分配功率, c分配电流, c状态)
	c标题行0 = "Mod Model                   Power     Current     Power     Current     Status"
	c标题行1 = "                            Requested Requested   Allocated Allocated         "
	c标题行2 = "                            (Watts)   (Amps)      (Watts)   (Amps)              "
	c标题行3 = "--- ----------------------  -------   ----------  --------- ----------  ----------"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端索引, self.ca列[0], int)
		self.f添加字段(数据表.E字段.e本端型号, self.ca列[1], str)
		self.f添加字段(数据表.E字段.e本端输出功率, self.ca列[4], float)
		self.f添加字段(数据表.E字段.e本端电源电流, self.ca列[5], float)
		self.f添加字段(数据表.E字段.e本端电源状态, self.ca列[6], lambda x: "up" in x)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行1, c标题行2, c标题行3))
	fi有效行 = staticmethod(数据表.F有效长度(c状态))
	fi结束 = staticmethod(数据表.fi空行)
f电源v7_板卡 = F电源v7_板卡()
class F电源v9(数据表.I解析表格管线):
	"""show environment power
	适用于: 浪潮cn61108pcv(v9.2.3)"""
	c序号 = 0
	c型号 = 9
	c输出 = 27
	c输入 = 46
	c额定 = 59
	c状态 = 70
	ca列 = 数据表.C切割列(c序号, c型号, c输出, c输入, c额定, c状态)
	c标题行0 = "Power                      Actual             Actual        Total"
	c标题行1 = "Supply    Model            Output             Input      Capacity       Status"
	c标题行2 = "-------  ----------  ---------------  ------  ----------  --------------------"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端索引, self.ca列[0], int)
		self.f添加字段(数据表.E字段.e本端型号, self.ca列[1], str)
		self.f添加字段(数据表.E字段.e本端输出功率, self.ca列[2], f解析功率)
		self.f添加字段(数据表.E字段.e本端输入功率, self.ca列[3], f解析功率)
		self.f添加字段(数据表.E字段.e本端额定功率, self.ca列[4], f解析功率)
		self.f添加字段(数据表.E字段.e本端电源状态, self.ca列[5], f解析状态)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1, c标题行2))
	fi有效行 = staticmethod(数据表.F有效长度(c状态))
	fi结束 = staticmethod(数据表.fi空行)
f电源v9 = F电源v9()
#===============================================================================
# 风扇
#===============================================================================
ca风扇方向 = {
	"front-to-back": 硬件.E风扇方向.e从前到后,
	"back-to-front": 硬件.E风扇方向.e从后到前,
}
class F风扇v7(数据表.I解析表格管线):
	"""show environment fan
	适用于: 浪潮cn8672up(v7.3.0), 浪潮cn8696q(v7.3.0)"""
	c风扇 = 0
	c型号 = 16
	c硬件 = 37
	c状态 = 48
	ca列 = 数据表.C切割列(c风扇, c型号, c硬件, c状态)
	c标题行0 = "Fan             Model                Hw         Status"
	c标题行1 = "------------------------------------------------------"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端风扇, self.ca列[0], str)
		self.f添加字段(数据表.E字段.e本端型号, self.ca列[1], str)
		# self.f添加字段(数据表.E字段.e本端硬件, self.ca列[2], str)
		self.f添加字段(数据表.E字段.e本端风扇状态, self.ca列[3], f解析状态)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
	fi有效行 = staticmethod(数据表.F有效长度(c状态))
	fi结束 = staticmethod(数据表.fi空行)
f风扇v7 = F风扇v7()
class F风扇v9(数据表.I解析表格管线):
	"""show environment fan
	适用于: 浪潮cn61108pcv(v9.2.3)"""
	c风扇 = 0
	c型号 = 16
	c硬件 = 37
	c方向 = 44
	c状态 = 60
	ca列 = 数据表.C切割列(c风扇, c型号, c硬件, c方向, c状态)
	c标题行0 = "Fan             Model                Hw     Direction       Status"
	c标题行1 = "---------------------------------------------------------------------------"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端风扇, self.ca列[0], str)
		self.f添加字段(数据表.E字段.e本端型号, self.ca列[1], str)
		# self.f添加字段(数据表.E字段.e本端硬件, self.ca列[2], str)
		self.f添加字段(数据表.E字段.e本端风扇方向, self.ca列[3], ca风扇方向.get)
		self.f添加字段(数据表.E字段.e本端风扇状态, self.ca列[4], f解析状态)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
	fi有效行 = staticmethod(数据表.F有效长度(c状态))
	fi结束 = staticmethod(数据表.fi空行)
f风扇v9 = F风扇v9()
#===============================================================================
# 温度
#===============================================================================
class F温度v7(数据表.I解析表格管线):
	"""show environment temperature
	适用于: 浪潮cn8672up(v7.3.0), 浪潮cn8696q(v7.3.0)"""
	c模块 = 0
	c传感器 = 9
	c主要阈值 = 20
	c次要阈值 = 34
	c当前温度 = 47
	c状态 = 59
	ca列 = 数据表.C切割列(c模块, c传感器, c主要阈值, c次要阈值, c当前温度, c状态)
	c标题行0 = "Module   Sensor     MajorThresh   MinorThres   CurTemp     Status"
	c标题行1 = "                    (Celsius)     (Celsius)    (Celsius)         "
	c标题行2 = "-----------------------------------------------------------------"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端索引, self.ca列[0], int)
		self.f添加字段(数据表.E字段.e本端传感器, self.ca列[1], str)
		self.f添加字段(数据表.E字段.e本端严重高温阈值, self.ca列[2], int)
		self.f添加字段(数据表.E字段.e本端高温阈值, self.ca列[3], int)
		self.f添加字段(数据表.E字段.e本端温度, self.ca列[4], int)
		self.f添加字段(数据表.E字段.e本端温度状态, self.ca列[5], f解析状态)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1, c标题行2))
	fi有效行 = staticmethod(数据表.F有效长度(c状态))
	fi结束 = staticmethod(数据表.fi空行)
f温度v7 = F温度v7()
class F温度v9(数据表.I解析表格管线):
	"""show environment temperature
	适用于: 浪潮cn61108pcv(v9.2.3)"""
	c模块 = 0
	c传感器 = 9
	c主要阈值 = 23
	c次要阈值 = 37
	c当前温度 = 50
	c状态 = 62
	ca列 = 数据表.C切割列(c模块, c传感器, c主要阈值, c次要阈值, c当前温度, c状态)
	c标题行0 = "Module   Sensor        MajorThresh   MinorThres   CurTemp     Status"
	c标题行1 = "                       (Celsius)     (Celsius)    (Celsius)         "
	c标题行2 = "--------------------------------------------------------------------"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端索引, self.ca列[0], int)
		self.f添加字段(数据表.E字段.e本端传感器, self.ca列[1], str)
		self.f添加字段(数据表.E字段.e本端严重高温阈值, self.ca列[2], int)
		self.f添加字段(数据表.E字段.e本端高温阈值, self.ca列[3], int)
		self.f添加字段(数据表.E字段.e本端温度, self.ca列[4], int)
		self.f添加字段(数据表.E字段.e本端温度状态, self.ca列[5], f解析状态)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1, c标题行2))
	fi有效行 = staticmethod(数据表.F有效长度(c状态))
	fi结束 = staticmethod(数据表.fi空行)
f温度v9 = F温度v9()
