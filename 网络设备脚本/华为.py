import enum
#===============================================================================
# 工厂
#===============================================================================
class E型号(enum.IntEnum):
	c交换机 = 0x10000000
	c路由器 = 0x20000000
	c云 = 0x01000000	#适用于: ne系列路由器, cx系列路由器, ce系列交换机
	s3700 = c交换机 + 0x3700
	s3928 = c交换机 + 0x3928
	s5700 = c交换机 + 0x5700
	s7700 = c交换机 + 0x7700
	ce6800 = c交换机 + c云 + 0x6800
	ce12800 = c交换机 + c云 + 0x12800
	ar201 = c路由器 + 0x0201
	ar1220 = c路由器 + 0x1220
	ar2220 = c路由器 + 0x2220
	ar2240 = c路由器 + 0x2240
	ar3260 = c路由器 + 0x3260
	ne40e = c路由器 + c云 + 0x4000
	ne5000e = c路由器 + c云 + 0x5000
	ne9000 = c路由器 + c云 + 0x9000
def f创建设备(a连接, a型号 = 0, a版本 = 0):
	if a连接.c连接特性 & 0x0001:	#命令行
		from .华为命令行 import 设备 as 设备
		return 设备.C设备(a连接, a型号, a版本)
#===============================================================================
# 工具
#===============================================================================
class C实用工具:
	@staticmethod
	def f加密等级(a):
		if type(a) == str:
			v补全 = 设备.C实用工具.f命令补全(a, 'cipher', 'simple')
			if v补全:
				return v补全
		if 设备.C实用工具.f参数等级(a加密等级, 1):
			return 'cipher'
		else:
			return 'simple'
class C配置内容:
	def __init__(self, a配置):
		self.m配置 = a配置.replace('\r', '')
	def __str__(self):
		return self.m配置
	def fg设备名称(self):
		return C输出分析.f从配置取设备名称(self.m配置)
class C输出分析:
	@staticmethod
	def f从配置取设备名称(a配置):
		if not a配置:
			return ""
		v指定行 = a配置.find(' sysname ')
		v结束 = a配置.find('\n', v指定行)
		if v结束 == -1:
			return a配置[v指定行 + 8 :]
		else:
			return a配置[v指定行 + 8 : v结束]