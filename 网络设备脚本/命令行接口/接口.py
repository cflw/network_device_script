import copy
from . import 模式
from ..基础接口 import 接口 as 北向接口
from ..命令行接口 import 命令
#===============================================================================
# 实用
#===============================================================================
def fe接口模式展开(a接口模式):
	for v接口 in a接口模式.m接口.fe接口():
		v接口模式 = copy.copy(a接口模式)
		v接口模式.m模式栈 = a接口模式.m模式栈[:-1] + (v接口模式,)
		v接口模式.m接口 = v接口
		yield v接口模式
def A接口自动展开(af):
	def fi展开(self):
		if not self.m接口.fi范围():
			return False
		elif hasattr(self, "mi接口自动展开"):
			return bool(self.mi接口自动展开)
		else:
			return True
	def f包装(self, *a元组, **a字典):
		if fi展开(self):
			for v接口模式 in fe接口模式展开(self):
				af(v接口模式, *a元组, **a字典)
		else:
			return af(self, *a元组, **a字典)
	return f包装
#===============================================================================
# 接口模式
#===============================================================================
class I接口配置基础(模式.I模式):	#所有接口配置模式接口的基类
	c模式名 = "接口配置模式"
	def __init__(self, a设备, a接口):
		模式.I模式.__init__(self, a设备)
		if not isinstance(a接口, 北向接口.C接口):
			raise TypeError("a接口 必须是一个 C接口 对象")
		self.m接口 = a接口
	def __eq__(self, a):
		if not isinstance(a, I接口配置基础):
			return False
		return self.m接口 == a.m接口
	#通用方法
	def fg模式参数(self):	#在这里确定不同厂商的接口名称
		return (self.m接口,)
	def fg进入命令(self):
		return 命令.C命令("interface") + self.fg模式参数()
	def fg接口(self):
		return self.m接口
class I接口配置(I接口配置基础, 北向接口.I接口配置):
	def __init__(self, a, a接口):
		I接口配置基础.__init__(self, a, a接口)
