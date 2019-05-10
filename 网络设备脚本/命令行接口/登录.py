from ..基础接口 import 登录
from . import 模式
class I登录配置(模式.I模式, 登录.I登录配置):
	def __init__(self, a):
		模式.I模式.__init__(self, a)
def f生成范围(a登录, a范围):
	return " ".join(f生成范围元组(a登录, a范围))
def f生成范围元组(a登录, a范围):
	if a登录 == 登录.E登录方式.e控制台:
		return (0,)
	elif a登录 == 登录.E登录方式.e虚拟终端:
		v范围类型 = type(a范围)
		if v范围类型 == int:
			return (a范围,)
		elif v范围类型 == range:
			return (a范围.start, a范围.stop - 1)
		else:
			return (0, 4)
	else:
		return (0,)
