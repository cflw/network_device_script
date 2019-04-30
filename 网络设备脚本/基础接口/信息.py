import enum
class I版本信息:
	def fg版本s(self)->str:
		"完整的版本字符串"
		raise NotImplementedError()
	def fg版本号(self)->str:
		raise NotImplementedError()
	def fg编译日期(self)->time.struct_time:
		"如果找不到,返回None"
		raise NotImplementedError()
	def fg运行时间(self)->datetime.timedelta:
		raise NotImplementedError()
	def fg开机日期(self)->time.struct_time:
		raise NotImplementedError()
class E物理地址类型(enum.IntEnum):
	e动态 = 0
	e静态 = 1
	e安全 = 2
class S物理地址表项:
	def __init__(self, a地址 = None, a接口 = None, a虚拟局域网 = None, a类型 = None):
		self.m地址 = a地址
		self.m接口 = a接口
		self.m虚拟局域网 = a虚拟局域网
		self.m类型 = a类型
	def __str__(self):
		return 字符串.ft字符串(self.m地址, self.m接口, self.m虚拟局域网, self.m类型)
class S网络接口表项:
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
class S接口表项:
	def __init__(self, a接口 = None, a状态 = None, a速率 = None, a双工 = None, a虚拟局域网 = 0, a描述 = ""):
		self.m接口 = a接口
		self.m状态 = a状态
		self.m速率 = a速率
		self.m双工 = a双工
		self.m虚拟局域网 = a虚拟局域网
		self.m描述 = a描述
	def __str__(self):
		return 字符串.ft字符串(self.m接口, self.m状态, self.m速率, self.m双工, self.m虚拟局域网, self.m描述)
class S地址解析表项:
	def __init__(self, a网络地址 = None, a物理地址 = None, a接口 = None, a寿命 = None):
		self.m网络地址 = a网络地址
		self.m物理地址 = a物理地址
		self.m接口 = a接口
		self.m寿命 = a寿命
	def __str__(self):
		return 字符串.ft字符串(self.m网络地址, self.m物理地址, self.m接口, self.m寿命)
