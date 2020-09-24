import enum
import cflw代码库py.cflw工具 as 工具
from .基础接口 import 连接层
class E型号(enum.IntEnum):
	c防火墙 = 0x10000000
	c应用交付 = 0x20000000
	af = c防火墙
	ad = c应用交付
	af2000 = c防火墙 + 2000
	ad1000 = c应用交付 + 1000
def f创建设备(a连接, a型号, a版本 = 0):
	v版本 = 工具.S版本号.fc自动(a版本)
	if 连接层.fi网页(a连接):	#网页
		if a型号 & E型号.c防火墙:
			from .深信服防火墙网页 import 设备
			return 设备.C设备(a连接, a型号, v版本)
		elif a型号 & E型号.c应用交付:
			if v版本 < "7.0.5":	#界面1
				from .深信服应用交付网页 import 设备
				return 设备.C设备ad70(a连接, a型号, v版本)
			else:	# v版本 >= "7.0.5"	#界面2
				from .深信服应用交付网页 import 设备
				return 设备.C设备ad705(a连接, a型号, v版本)
	raise ValueError("不支持的连接,型号")