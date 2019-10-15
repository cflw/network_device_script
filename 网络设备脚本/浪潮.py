import enum
import cflw代码库py.cflw工具 as 工具
class E型号(enum.IntEnum):
	c路由器 = 0x10000000
	c交换机 = 0x20000000
	c思科 = 0x40000000
	c盛科 = 0x80000000
	c枢纽 = 0x01000000
	cn8000 = c交换机 + c枢纽 + 8000
	cn8672 = c交换机 + c枢纽 + 8672
	cn8696 = c交换机 + c枢纽 + 8696
	cn61108pcv = c交换机 + c枢纽 + 6118
	cn61108pcvh = c交换机 + c盛科 + 6118
	s5350 = c交换机 + c盛科 + 5350
	s5960 = c交换机 + c思科 + 5960
	s5960l = c交换机 + c思科 + 5961
	s6550 = c交换机 + 6550
	s6650 = c交换机 + c思科 + 6650
	s6650l = c交换机 + c思科 + 6651
	s6850 = c交换机 + 6850
def f创建设备(a连接, a型号, a版本):
	v版本 = 工具.S版本号.fc自动(a版本)
	if a型号 & E型号.c思科:
		from .思科命令行 import 设备
		return 设备.C设备(a连接, a型号, v版本)
	if a型号 & E型号.c枢纽:
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
		from .浪潮命令行 import 设备
		if v版本 < (3,60):
			return 设备.C设备sv3_50(a连接, a型号, v版本)
		else:
			return 设备.C设备sv3_60(a连接, a型号, v版本)
	raise ValueError("不支持的型号")
