import cflw代码库py.cflw网络地址 as 地址
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 操作
from ..基础接口 import 协议
from ..基础接口 import 访问控制列表 as 北向列表
from ..命令行接口 import 命令
from ..命令行接口 import 访问控制列表 as 南向列表
from ..华三命令行.常量 import *
from ..华三命令行.访问控制列表 import *
#===============================================================================
# 生成
#===============================================================================
def f生成名称_v7(a名称):	#序号不带"number"
	v类型 = type(a名称)
	if v类型 == int:
		return "%s" % (a名称,)
	v名称 = str(a名称)
	if v名称.isdigit():
		return "%s" % (v名称,)
	return "name %s" % (v名称,)
#===============================================================================
# 模式
#===============================================================================
class I访问控制列表_v7(I访问控制列表):
	"""acl 类型 访问列表号
	适用于: v7.1"""
	def fg进入命令(self):
		v命令 = 命令.C命令("acl")
		v命令 += self.m协议
		v命令 += self.m类型
		v命令 += f生成名称_v7(self.m名称)
		return v命令
	def fg显示命令(self, a序号 = None):
		v命令 = 命令.C命令("display acl")
		v命令 += self.m协议
		v命令 += f生成名称_v7(self.m名称)
		if a序号 != None:
			v命令 += "| include rule.%d.[dp]" % (a序号,)
		return v命令
class C基本4_v7(I访问控制列表_v7, C基本4):
	def __init__(self, a, a名称):
		I访问控制列表_v7.__init__(self, a, a名称, c基本, c网络协议4)
class C高级4_v7(I访问控制列表_v7, C高级4):
	def __init__(self, a, a名称):
		I访问控制列表_v7.__init__(self, a, a名称, c高级, c网络协议4)
class C基本6_v7(I访问控制列表_v7, C基本6):
	def __init__(self, a, a名称):
		I访问控制列表_v7.__init__(self, a, a名称, c基本, c网络协议6)
class C高级6_v7(I访问控制列表_v7, C高级6):
	def __init__(self, a, a名称):
		I访问控制列表_v7.__init__(self, a, a名称, c高级, c网络协议6)