import enum
import cflw代码库py.cflw工具 as 工具
from .基础接口 import 连接层
#===============================================================================
# 工厂
#===============================================================================
class E型号(enum.IntEnum):
	c交换机 = 0x10000000
	c路由器 = 0x20000000
	c防火墙 = 0x40000000
	c无线控制器 = 0x00100000
	c无线接入点 = 0x00200000
	c云引擎 = 0x01000000	#适用于: ce系列交换机
	c网引擎 = 0x01000000	#适用于: ne系列路由器, cx系列路由器
	#交换机
	s3700 = c交换机 + 0x3700
	s3928 = c交换机 + 0x3928
	s5700 = c交换机 + 0x5700
	s7700 = c交换机 + 0x7700
	ce6800 = c交换机 + c云引擎 + 0x6800	#ce = cloud engine
	ce12800 = c交换机 + c云引擎 + 0x12800
	#路由器
	ar201 = c路由器 + 0x0201
	ar1220 = c路由器 + 0x1220
	ar2220 = c路由器 + 0x2220
	ar2240 = c路由器 + 0x2240
	ar3260 = c路由器 + 0x3260
	ne40e = c路由器 + c网引擎 + 0x4000	#ne = network engine
	ne5000e = c路由器 + c网引擎 + 0x5000
	ne9000 = c路由器 + c网引擎 + 0x9000
	#无线控制器
	ac6005 = c无线控制器 + 6005
	ac6605 = c无线控制器 + 6605
	#无线接入点
	ap2050 = c无线接入点 + 2050
	ap3030 = c无线接入点 + 3030
	ap4030 = c无线接入点 + 4030
	ap4050 = c无线接入点 + 4050
	ap5030 = c无线接入点 + 5030
	ap6050 = c无线接入点 + 6050
	ap7030 = c无线接入点 + 7030
	ap7050 = c无线接入点 + 7050
	ap8030 = c无线接入点 + 8030
	ap8130 = c无线接入点 + 8130
	ap9131 = c无线接入点 + 9131
	ad9430 = c无线接入点 + 9430
	r250d = c无线接入点 + 0x250d
	#防火墙
	usg6000 = c防火墙 + 6000
def f创建设备(a连接, a型号 = 0, a版本 = 0):
	v版本 = 工具.S版本号.fc自动(a版本)
	if 连接层.fi命令行(a连接):	#命令行
		if a型号 & E型号.c网引擎:
			from .华为引擎命令行 import 设备
			return 设备.C设备ne(a连接, a型号, v版本)
		elif a型号 & E型号.c云引擎:
			from .华为引擎命令行 import 设备
			return 设备.C设备ce(a连接, a型号, v版本)
		else:
			from .华为命令行 import 设备
			return 设备.C设备(a连接, a型号, v版本)
	elif 连接层.fi简单网管(a连接):	#简单网管
		from .华为简单网管 import 设备
		return 设备.C设备(a连接, a型号, v版本)
	raise ValueError("不支持的连接,型号")
