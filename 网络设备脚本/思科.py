import enum
from .基础接口 import 连接层
#===============================================================================
# 工厂
#===============================================================================
class E型号(enum.IntEnum):
	c路由器 = 0x10000000
	c交换机 = 0x20000000
	c模拟器0 = 0x00010000	#Dynamips支持的型号
	c模拟器1 = 0x00020000	#IOS on Unix
	c枢纽 = 0x01000000
	l2iou = c模拟器1 + 2
	l3iou = c模拟器1 + 3
	c2950 = c交换机 + c模拟器0 + 2950
	c2960 = c交换机 + c模拟器0 + 2960
	c3560 = c交换机 + c模拟器0 + 3560
	c7200 = c路由器 + c模拟器0 + 7200	#cisco 7200
	n3000 = c路由器 + c枢纽 + 3000	#nexus 3000
	n9000 = c路由器 + c枢纽 + 9000	#nexus 9000
def f创建设备(a连接, a型号: int = 0, a版本 = 0):
	if 连接层.fi命令行(a连接):	#命令行
		if a型号 & E型号.c枢纽:
			from .思科枢纽命令行 import 设备
			if a版本 < 7:
				raise ValueError("不支持的版本")
			elif a版本 < 9:
				return 设备.C设备nv7(a连接, a型号, a版本)
			elif a版本 < 10:
				return 设备.C设备nv9(a连接, a型号, a版本)
			raise ValueError("不支持的版本")
		else:
			from .思科命令行 import 设备
			return 设备.C设备(a连接, a型号, a版本)
	elif 连接层.fi网页(a连接):	#网页
		if a型号 & E型号.c模拟器0:
			from .思科网页 import 命令行设备
			return 命令行设备.C设备(a连接, a型号, a版本)
	elif 连接层.fi简单网管(a连接):	#简单网管
		from .思科简单网管 import 设备
		return 设备.C设备(a连接, a型号, a版本)
	raise ValueError("不支持的连接,型号,版本")