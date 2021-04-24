from ..基础接口 import 信息
from ..基础接口 import 数据表
from ..基础接口 import 硬件
#===============================================================================
# 简单
#===============================================================================
class F简单信息v7(数据表.I解析表格管线):
	"""display fan, display power
	适用于: (模拟器)华三s5820v2(v7.1.075)"""
	c标识 = 0
	c状态 = 12
	ca列 = 数据表.C切割列(c标识, c状态)
	c标题行0 = "Device ID.  Status"
	def __init__(self, a状态字段):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端索引, self.ca列[0], int)
		self.f添加字段(a状态字段, self.ca列[1], lambda x: x == "Normal")
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
f简单风扇信息v7 = F简单信息v7(数据表.E字段.e本端风扇状态)
f简单电源信息v7 = F简单信息v7(数据表.E字段.e本端电源状态)
#===============================================================================
# 风扇
#===============================================================================
ca风扇方向 = {
	"Port-to-power": 硬件.E风扇方向.e从前到后,
}
class F风扇信息v7(数据表.I解析列表管线):
	"""display fan
	适用于: 华三s6900(v7.1.070)"""
	c风扇 = "Fan"
	c状态 = "State"
	c风向 = "Airflow Direction"
	def __init__(self):
		数据表.I解析列表管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端风扇, 数据表.F正则字段(r"Fan (\d+):", 1), int)
		self.f添加字段(数据表.E字段.e本端风扇状态, 数据表.F列表字段("State"), lambda x: x == "Normal")
		self.f添加字段(数据表.E字段.e本端风扇方向, 数据表.F列表字段("Airflow Direction"), ca风扇方向.get)
	f下一记录 = staticmethod(数据表.F下一记录("Fan"))
f风扇信息v7 = F风扇信息v7()
#===============================================================================
# 电源
#===============================================================================
ca电源风扇方向 = {
	"PortToPower": 硬件.E风扇方向.e从前到后,
}
class F电源信息v7(数据表.I解析表格管线):
	"""display power
	适用于: 华三s6900(v7.1.070)"""
	c标识 = 0
	c状态 = 9
	c模式 = 23
	c电流 = 30
	c电压 = 42
	c功率 = 54
	c风扇方向 = 64
	ca列 = 数据表.C切割列(c标识, c状态, c模式, c电流, c电压, c功率, c风扇方向)
	c标题行0 = " PowerID State         Mode   Current(A)  Voltage(V)  Power(W)  FanDirection"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端索引, self.ca列[0], int)
		self.f添加字段(数据表.E字段.e本端电源状态, self.ca列[1], lambda x: "Normal" in x)
		self.f添加字段(数据表.E字段.e本端电源类型, self.ca列[2], 硬件.ca电源类型.get)
		self.f添加字段(数据表.E字段.e本端电源电流, self.ca列[3], float)
		self.f添加字段(数据表.E字段.e本端电源电压, self.ca列[4], float)
		self.f添加字段(数据表.E字段.e本端输出功率, self.ca列[5], int)
		self.f添加字段(数据表.E字段.e本端风扇方向, self.ca列[6], ca电源风扇方向.get)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(c风扇方向))
	fi结束 = staticmethod(数据表.fi空行)
f电源信息v7 = F电源信息v7()
#===============================================================================
# 温度
#===============================================================================
class F温度信息v7(数据表.I解析表格管线):
	"""display enviroment
	适用于: 华三s6900(v7.1.070)"""
	c槽位 = 0
	c传感器 = 7
	c温度 = 17
	c低 = 30
	c警告 = 37
	c警报 = 46
	c关闭 = 53
	ca列 = 数据表.C切割列(c槽位, c传感器, c温度, c低, c警告, c警报, c关闭)
	c标题行0 = " Slot  Sensor    Temperature  Lower  Warning  Alarm  Shutdown"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端单元, self.ca列[0], int)
		self.f添加字段(数据表.E字段.e本端传感器, self.ca列[1], str)
		self.f添加字段(数据表.E字段.e本端温度, self.ca列[2], int)
		self.f添加字段(数据表.E字段.e本端低温阈值, self.ca列[3], int)
		self.f添加字段(数据表.E字段.e本端高温阈值, self.ca列[4], int)
		self.f添加字段(数据表.E字段.e本端严重高温阈值, self.ca列[5], int)
		# self.f添加字段(数据表.E字段.e本端关闭, self.ca列[6], lambda x: x == "NA")
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(c关闭))
	fi结束 = staticmethod(数据表.fi空行)
f温度信息v7 = F温度信息v7()
class F温度信息模拟v7(数据表.I解析表格管线):
	"""display enviroment
	适用于: """
	c槽位 = 0
	c传感器 = 6
	c温度 = 16
	c低 = 28
	c警告 = 39
	c警报 = 52
	ca列 = 数据表.C切割列(c槽位, c传感器, c温度, c低, c警告, c警报)
	c标题行0 = "Slot  Sensor    Temperature LowerLimit WarningLimit AlarmLimit"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		f切割列0 = self.ca列[0]
		def F切割列0分割(x):
			def f提取(a行: str):
				return f切割列0(a行).split("/")[x]
			return f提取
		self.f添加字段(数据表.E字段.e本端单元, F切割列0分割(0), int)
		self.f添加字段(数据表.E字段.e本端索引, F切割列0分割(1), int)
		self.f添加字段(数据表.E字段.e本端传感器, self.ca列[1], str)
		self.f添加字段(数据表.E字段.e本端温度, self.ca列[2], int)
		self.f添加字段(数据表.E字段.e本端低温阈值, self.ca列[3], int)
		self.f添加字段(数据表.E字段.e本端高温阈值, self.ca列[4], int)
		self.f添加字段(数据表.E字段.e本端严重高温阈值, self.ca列[5], int)
		# self.f添加字段(数据表.E字段.e本端关闭, self.ca列[6], lambda x: x == "NA")
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(c警报))
	fi结束 = staticmethod(数据表.fi空行)
f温度信息模拟v7 = F温度信息模拟v7()
