import enum
import cflw代码库py.cflw工具 as 工具
from .基础接口 import 连接层
class E型号(enum.IntEnum):
	c路由器 = 0x10000000
	c交换机 = 0x20000000
	c思科 = 0x01000000
	c盛科 = 0x02000000
	c瑞斯康达 = 0x04000000
	c博科 = 0x08000000
	c思科连结 = 0x00100000
	cn8000 = c交换机 + c思科连结 + 8000
	cn8672 = c交换机 + c思科连结 + 8672
	cn8696 = c交换机 + c思科连结 + 8696
	cn12710 = c交换机 + c思科连结 + 12710
	cn61108pcv = c交换机 + c思科连结 + 6118
	cn61108pcvh = c交换机 + c盛科 + 6118
	fs5900 = c交换机 + c博科 + 5900
	fs6500 = c交换机 + c博科 + 6500
	fs6600 = c交换机 + c博科 + 6600
	s5350 = c交换机 + c盛科 + 5350
	s5960 = c交换机 + c思科 + 5960
	s5960l = c交换机 + c思科 + 5961
	s6550 = c交换机 + c瑞斯康达 + 6550
	s6650 = c交换机 + c思科 + 6650
	s6650l = c交换机 + c思科 + 6651
	s6850 = c交换机 + c思科 + 6850
def f创建设备(a连接, a型号, a版本):
	v版本 = 工具.S版本号.fc自动(a版本)
	if 连接层.fi命令行(a连接):	#命令行
		if a型号 & E型号.c思科:
			from .思科命令行 import 设备
			return 设备.C设备(a连接, a型号, v版本)
		if a型号 & E型号.c思科连结:
			from .思科连结命令行 import 设备
			if v版本 >= 9:
				return 设备.C设备nv9(a连接, a型号, v版本)
			elif v版本 >= 7:
				return 设备.C设备nv7(a连接, a型号, v版本)
			raise ValueError("不支持的版本")
		if a型号 & E型号.c盛科:
			from .盛科命令行 import 设备
			if v版本 >= 6:
				return 设备.C设备ev6(a连接, a型号, v版本)
			raise ValueError("不支持的版本")
		if a型号 & E型号.c瑞斯康达:
			from .瑞斯康达命令行 import 设备
			if v版本 < (3,60):
				return 设备.C设备sv3_50(a连接, a型号, v版本)
			else:
				return 设备.C设备sv3_60(a连接, a型号, v版本)
		if a型号 & E型号.c博科:
			raise ValueError("不支持的型号")
	elif 连接层.fi网页(a连接):	#网页
		if a型号 & E型号.c盛科:
			from .盛科网页 import 设备
			return 设备.C设备ev6(a连接, a型号, a版本)
	elif 连接层.fi简单网管(a连接):	#简单网络管理协议
		if a型号 & E型号.c思科:
			from .思科简单网管 import 设备
			return 设备.C设备(a连接, a型号, a版本)
	raise ValueError("不支持的连接,型号")
