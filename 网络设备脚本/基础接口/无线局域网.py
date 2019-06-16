import enum
import cflw代码库py.cflw字符串 as 字符串
class E模式(enum.IntEnum):
	"""802.11标准"""
	#单模式
	a = 0x0001
	b = 0x0002
	g = 0x0004
	n = 0x0008
	ac = 0x0010
	ax = 0x0020
	#混合
	bg = b | g
	bgn = b | g | n
class S主机表项:
	def __init__(self, a名称, a物理地址, a接口 = None):
		self.m名称 = a名称
		self.m物理地址 = a物理地址
		self.m接口 = a接口
	def __str__(self):
		return 字符串.ft字符串(self.m名称, self.m物理地址, self.m接口)
class I接口配置:
	c模式名 = "无线局域网无线电接口配置模式"
	def f显示_主机表(self):
		raise NotImplementedError()
	def fs开关(self, a操作):
		"是否发射信号"
		raise NotImplementedError()
	def fs服务集标识广播(self, a操作):
		"是否广播ssid"
		raise NotImplementedError()
	def fs服务集标识号(self, a号, a操作):
		"ssid名称"
		raise NotImplementedError()
class I接入点配置:
	c模式名 = "无线局域网接入点配置模式"
	def f显示_主机表(self):
		raise NotImplementedError()
class I控制器配置:
	c模式名 = "无线局域网接入控制器配置模式"
	def f显示_支持型号表(self):
		raise NotImplementedError()
