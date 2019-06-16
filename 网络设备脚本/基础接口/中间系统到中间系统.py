import enum
import re
import cflw代码库py.cflw字符串 as 字符串
class E级别(enum.IntEnum):
	e级别1 = 1	#区域内
	e级别2 = 2	#骨干区域
	e级别1和2 = 3	#区域边界
class S网络标识:
	def __init__(self, a字节):
		self.m字节 = a字节
	def __str__(self):
		return self.ft字符串()
	@staticmethod
	def fc自动(a):
		v类型 = type(a)
		if v类型 == str:
			return S网络标识.fc字符串(a)
		elif v类型 in (tuple, list):
			return S网络标识.fc三段(*a)
		elif v类型 == S网络标识:
			return a
		else:
			raise TypeError("无法识别的类型")
	@staticmethod
	def fc字符串(a):
		"""xx.xxxx.xxxx.xxxx.xxxx.xx"""
		v标识s = 字符串.f去非十六进制数字(a)
		return S网络标识(bytes.fromhex(v标识s))
	@staticmethod
	def fc三段(a区域号, a系统号, a序列号 = 0):
		"""a区域号: xx.xxxx
		a系统号: xxxx.xxxx.xxxx
		a序列号: xx"""
		def f处理(a, a长度):
			v类型 = type(a)
			if v类型 == int:
				v字符串 = hex(a)[2:]
			else:
				v字符串 = str(a)
				v字符串 = 字符串.f去非十六进制数字(a)
			if len(v字符串) > a长度:
				raise ValueError("太长")
			v字符串 = 字符串.f前面填充(v字符串, "0", a长度)
			return bytes.fromhex(v字符串)
		v区域号b = f处理(a区域号, 6)
		v系统号b = f处理(a系统号, 12)
		v序列号b = f处理(a序列号, 2)
		return S网络标识(v区域号b + v系统号b + v序列号b)
	def ft字符串(self):
		"""xx.xxxx.xxxx.xxxx.xxxx.xx"""
		v字符串 = self.m字节.hex()
		v字符串 = 字符串.f隔段插入字符串(v字符串, ".", range(2, 20, 4))
		return v字符串
class I进程配置:
	c模式名 = "中间系统到中间系统进程配置模式"
	def f显示_路由表(self):
		raise NotImplementedError()
	def f显示_邻居表(self):
		raise NotImplementedError()
	def f模式_接口(self, a接口, a操作):
		raise NotImplementedError()
	def fs网络标识(self, a标识, a操作):
		raise NotImplementedError()
	def fs通告接口(self, a接口, a操作):
		raise NotImplementedError()
	def fs级别(self, a级别, a操作):
		raise NotImplementedError()
class I接口配置:
	c模式名 = "中间系统到中间系统接口配置模式"
	def fs通告接口(self, a操作):
		raise NotImplementedError()
	def fs被动接口(self, a操作):
		raise NotImplementedError()