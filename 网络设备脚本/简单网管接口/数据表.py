import pandas	#pandas
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 数据表
E字段 = 数据表.E字段
class C字段:
	"""通用的简单网管字段"""
	def __init__(self, a字段, a标识, af解析):
		self.m字段 = a字段
		self.m标识 = a标识	#对象标识符
		self.mf解析 = af解析
	def f遍历(self, a设备):
		return a设备.f遍历(self.m标识, None, self.mf解析)
class C整数字段:
	def __init__(self, a字段, a标识):
		self.m字段 = a字段
		self.m标识 = a标识
	def f遍历(self, a设备):
		return a设备.f遍历(self.m标识, None, int)
class C网络地址字段:
	"""处理地址掩码"""
	def __init__(self, a字段, a地址标识, a掩码标识):
		self.m字段 = a字段
		self.m地址标识 = a地址标识
		self.m掩码标识 = a掩码标识
	def f遍历(self, a设备):
		for v地址, v掩码 in zip(a设备.f遍历(self.m地址标识, None, bytes), a设备.f遍历(self.m掩码标识, None, bytes)):
			yield 地址.S网络地址4.fc地址掩码(v地址, v掩码)
class C物理地址字段:
	"""处理物理地址"""
	def __init__(self, a字段, a地址标识):
		self.m字段 = a字段
		self.m地址标识 = a地址标识
	def f遍历(self, a设备):
		for v地址 in a设备.f遍历(self.m地址标识, None, bytes):
			yield 地址.S物理地址.fc字节(v地址)
class I解析竖表管线:
	"""控制点: 无\n
	ma字段, 包含(字段, 标识, 解析函数)"""
	def __init__(self):
		self.ma字段 = []
	def __call__(self, a设备):
		va数据 = self.f生成(a设备)
		return self.f解析(va数据)
	def f添加字段(self, a字段, a标识, af解析):
		self.ma字段.append(C字段(a字段, a标识, af解析))
	def f生成(self, a设备):
		return dict((v字段.m字段, v字段.f遍历(a设备)) for v字段 in self.ma字段)
	def f解析(self, a数据: dict):
		return pandas.DataFrame(a数据)
class F解析竖表管线(I解析竖表管线):
	def __init__(self, *aa字段):
		I解析竖表管线.__init__(self)
		for v字段 in aa字段:
			self.ma字段.append(v字段)