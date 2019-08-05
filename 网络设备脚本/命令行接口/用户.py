from ..基础接口 import 用户
from . import 模式 as 模式
def f生成服务类型(a字典, a值):
	v列表 = []
	v类型 = type(a值)
	if v类型 in (list, tuple):
		for v in a值:
			v列表.append(a字典[v])
	elif v类型 == int:
		for v in range(10):
			n = 2 ** v
			if a值 & n:
				v列表.append(a字典[n])
	else:
		raise TypeError("无法解析的类型")
	return " ".join(v列表)
class I用户配置(模式.I模式, 用户.I用户配置):
	def __init__(self, a, a用户名):
		模式.I模式.__init__(self, a)
		self.m用户名 = str(a用户名)