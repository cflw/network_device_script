import enum
import cflw代码库py.cflw字符串 as 字符串
class I版本信息:
	def fg版本s(self)->str:
		"完整的版本字符串"
		raise NotImplementedError()
	def fg版本号(self)->str:
		raise NotImplementedError()
	def fg编译日期(self):
		"""返回time.struct_time对象
		如果找不到,返回None"""
		raise NotImplementedError()
	def fg运行时间(self):
		"""返回datetime.timedelta对象"""
		raise NotImplementedError()
	def fg开机日期(self):
		"""返回time.struct_time对象"""
		raise NotImplementedError()
class E物理地址类型(enum.Enum):
	e动态 = 0
	e静态 = 1
	e安全 = 2
#===============================================================================
# 解析
#===============================================================================
def f解析起宕状态(a状态: str):
	"up为真"
	return "up" in a状态.lower()
def f解析双工模式(a双工: str):
	"full为真"
	v双工 = a双工.lower()
	if "full" in v双工:
		return True
	elif "half" in v双工:
		return False
	return None	#未知
def f解析速率(a速率: str):
	"解析带单位的速率"
	v单位 = a速率[-1]
	if v单位 == "G":
		return int(a速率[:-1]) * 10 ** 9
	elif v单位 == "M":
		return int(a速率[:-1]) * 10 ** 6
	elif v单位 == "k":
		return int(a速率[:-1]) * 10 ** 3
	else:
		return int(a速率)
def f解析链路类型(a类型: str):
	from . import 虚拟局域网
	v类型 = a类型.lower()
	if "access" in v类型:
		return 虚拟局域网.E链路类型.e接入
	elif "trunk" in v类型:
		return 虚拟局域网.E链路类型.e中继
	elif "hybrid" in v类型:
		return 虚拟局域网.E链路类型.e混合
	raise ValueError()
ca物理地址类型 = {
	"STATIC": E物理地址类型.e静态,
	"DYNAMIC": E物理地址类型.e动态,
	"SECURITY": E物理地址类型.e安全,
}
def f解析物理地址类型(a类型: str):
	return ca物理地址类型.get(a类型, None)
#===============================================================================
# 表项(废弃)
#===============================================================================
class S物理地址表项:	#废弃
	def __init__(self, a地址 = None, a接口 = None, a虚拟局域网 = None, a类型 = None):
		self.m地址 = a地址
		self.m接口 = a接口
		self.m虚拟局域网 = a虚拟局域网
		self.m类型 = a类型
	def __str__(self):
		return 字符串.ft字符串(self.m地址, self.m接口, self.m虚拟局域网, self.m类型)
class S网络接口表项:	#废弃
	def __init__(self, a接口 = None, a地址 = None, a状态 = None, a描述 = ""):
		self.m接口 = a接口
		self.m地址 = a地址
		self.m状态 = a状态
		self.m描述 = a描述
	def __str__(self):
		if type(self.m地址) in (tuple, list):
			return 字符串.ft字符串(self.m接口, 字符串.ft字符串(*self.m地址), self.m状态, self.m描述)
		else:
			return 字符串.ft字符串(self.m接口, self.m地址, self.m状态, self.m描述)
class S接口表项:	#废弃
	def __init__(self, a接口 = None, a状态 = None, a速率 = None, a双工 = None, a虚拟局域网 = 0, a描述 = ""):
		self.m接口 = a接口
		self.m状态 = a状态
		self.m速率 = a速率
		self.m双工 = a双工
		self.m虚拟局域网 = a虚拟局域网
		self.m描述 = a描述
	def __str__(self):
		return 字符串.ft字符串(self.m接口, self.m状态, self.m速率, self.m双工, self.m虚拟局域网, self.m描述)
class S地址解析表项:	#废弃
	def __init__(self, a网络地址 = None, a物理地址 = None, a接口 = None, a寿命 = None):
		self.m网络地址 = a网络地址
		self.m物理地址 = a物理地址
		self.m接口 = a接口
		self.m寿命 = a寿命
	def __str__(self):
		return 字符串.ft字符串(self.m网络地址, self.m物理地址, self.m接口, self.m寿命)
