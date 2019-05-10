from ..基础接口 import 虚拟局域网
from . import 命令
from . import 模式
from . import 接口
#===============================================================================
# 基础
#===============================================================================
c虚拟局域网范围 = range(1, 4095)	#可用范围
def f生成一个(a虚拟局域网):
	v类型 = type(a虚拟局域网)
	if v类型 == str:
		if not a虚拟局域网.isdigit():
			raise ValueError("a虚拟局域网 必须是数字")
		v数字 = int(a虚拟局域网)
		if not fi范围内(v数字):
			raise ValueError("a虚拟局域网 超出范围")
		return str(v数字)
	elif v类型 == int:
		if not fi范围内(a虚拟局域网):
			raise ValueError("a虚拟局域网 超出范围")
		return str(a虚拟局域网)
	else:
		raise TypeError("无法识别的类型")
def fi范围内(a虚拟局域网: int):
	return a虚拟局域网 in c虚拟局域网范围
#===============================================================================
# 模式
#===============================================================================
class I虚拟局域网配置(模式.I模式):
	def __init__(self, a, a编号):
		模式.I模式.__init__(self, a)
		self.m编号 = a编号
	def fg模式参数(self):
		return (self.m编号,)
	def fg进入命令(self):
		return 命令.C命令("vlan") + self.fg模式参数()
class I接口配置(接口.I接口配置基础):
	def __init__(self, a, a接口):
		接口.I接口配置基础.__init__(self, a, a接口)
