import enum
import cflw代码库py.cflw工具 as 工具
class E型号(enum.IntEnum):
	c防火墙 = 0x10000000
	af = c防火墙
	af2000 = c防火墙 + 2000
def f创建设备(a连接, a型号, a版本 = 0):
	v版本 = 工具.S版本号.fc自动(a版本)
	if "selenium" in str(a连接.__class__):	#网页
		if a型号 & E型号.c防火墙:
			from .深信服防火墙网页 import 设备
			return 设备.C设备(a连接, a型号, v版本)
	raise ValueError("不支持的连接,型号,版本")