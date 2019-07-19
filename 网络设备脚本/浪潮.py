import enum
class E型号(enum.IntEnum):
	c路由器 = 0x10000000
	c交换机 = 0x20000000
	c思科 = 0x40000000
	c云 = 0x80000000
	cn8000 = c交换机 + c云 + 8000
	cn8672 = c交换机 + c云 + 8672
	cn8696 = c交换机 + c云 + 8696
	cn6000 = c交换机 + c云 + 6000
	cn61108 = c交换机 + c云 + 6118
	s5960 = c交换机 + c思科 + 5960
	s5960l = c交换机 + c思科 + 5961
	s6550 = c交换机 + 6550
	s6650 = c交换机 + c思科 + 6650
	s6650l = c交换机 + c思科 + 6651
	s6850 = c交换机 + 6850
def f创建设备(a连接, a型号, a版本):
	if a型号 & E型号.c思科:
		from .思科命令行 import 设备
		return 设备.C设备(a连接, a型号, a版本)
	if a型号 & E型号.c云:
		from .浪潮命令行 import 设备
		if a版本 >= 7:
			return 设备.C设备cnv7(a连接, a型号, a版本)
		if a版本 >= 6:
			return 设备.C设备cnv6(a连接, a型号, a版本)
		raise ValueError("不支持的版本")
	if a型号 == E型号.s6550:
		from .浪潮命令行 import 设备
		return 设备.C设备sv3(a连接, a型号, a版本)
	raise ValueError("不支持的型号")
