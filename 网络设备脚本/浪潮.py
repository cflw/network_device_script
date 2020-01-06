import enum
import cflw代码库py.cflw网络连接 as 连接
import cflw代码库py.cflw工具 as 工具
class E型号(enum.IntEnum):
	c路由器 = 0x10000000
	c交换机 = 0x20000000
	c思科 = 0x01000000
	c盛科 = 0x02000000
	c瑞斯康达 = 0x04000000
	c思科枢纽 = 0x00100000
	cn8000 = c交换机 + c思科枢纽 + 8000
	cn8672 = c交换机 + c思科枢纽 + 8672
	cn8696 = c交换机 + c思科枢纽 + 8696
	cn61108pcv = c交换机 + c思科枢纽 + 6118
	cn61108pcvh = c交换机 + c盛科 + 6118
	s5350 = c交换机 + c盛科 + 5350
	s5960 = c交换机 + c思科 + 5960
	s5960l = c交换机 + c思科 + 5961
	s6550 = c交换机 + c瑞斯康达 + 6550
	s6650 = c交换机 + c思科 + 6650
	s6650l = c交换机 + c思科 + 6651
	s6850 = c交换机 + 6850
def f创建设备(a连接, a型号, a版本):
	v版本 = 工具.S版本号.fc自动(a版本)
	if hasattr(a连接, "c连接特性") and a连接.c连接特性 & 连接.E连接特性.e命令行:	#命令行
		if a型号 & E型号.c思科:
			from .思科命令行 import 设备
			return 设备.C设备(a连接, a型号, v版本)
		if a型号 & E型号.c思科枢纽:
			from .思科枢纽命令行 import 设备
			if v版本 >= 7:
				return 设备.C设备nv7(a连接, a型号, v版本)
			raise ValueError("不支持的版本")
		if a型号 & E型号.c盛科:
			from .盛科命令行 import 设备
			if v版本 >= 6:
				return 设备.C设备ev6(a连接, a型号, v版本)
			raise ValueError("不支持的版本")
		if a型号 == E型号.s6550:
			from .瑞斯康达命令行 import 设备
			if v版本 < (3,60):
				return 设备.C设备sv3_50(a连接, a型号, v版本)
			else:
				return 设备.C设备sv3_60(a连接, a型号, v版本)
	elif "selenium" in str(a连接.__class__):	#网页
		if a型号 & E型号.c盛科:
			from .盛科网页 import 设备
			return 设备.C设备ev6(a连接, a型号, a版本)
	raise ValueError("不支持的型号")
