from ..基础接口 import 用户
from . import 模式 as 模式
class I用户配置(模式.I模式, 用户.I用户配置):
	def __init__(self, a, a用户名):
		模式.I模式.__init__(self, a)
		self.m用户名 = str(a用户名)