import cflw代码库py.cflw简单网管_派 as 连接
from ..基础接口 import 设备
class I设备(设备.I设备):
	def __init__(self, a连接):
		self.m连接 = a连接
		self.m接口索引表 = None
	#SNMP
	def f获取(self, a标识, at类型 = None):
		return self.m连接.f获取(a标识, at类型)
	def f设置(self, a标识, a值, at类型 = None):
		return self.m连接.f设置(a标识, a值, at类型)
	def f遍历(self, a开始, a结束 = None, at类型 = None):
		return self.m连接.f遍历(a开始, a结束, at类型)
	def f陷阱(self, a标识, a值, at类型 = None):
		return self.m连接.f陷阱(a标识, a值, at类型)
	#缓存
	def fg接口索引表(self):
		from . import 接口
		if not self.m接口索引表:
			self.m接口索引表 = 接口.C接口索引表()
			self.m接口索引表.f更新(self)
		return self.m接口索引表