import enum
import cflw代码库py.cflw工具 as 工具
from .基础接口 import 连接层
#===============================================================================
# 工厂
#===============================================================================
class E型号(enum.IntEnum):
	c交换机 = 0x10000000
	c路由器 = 0x20000000
	c盒式 = 0x01000000
	c框式 = 0x02000000
	c版本三 = 0x00010000
	c版本五 = 0x00020000
	c版本七 = 0x00040000	#comware v7
	c版本九 = 0x00080000	#comware v9
	s2126 = c交换机 + c盒式 + 2126
	s3100 = c交换机 + c盒式 + c版本三 + 3100
	s3100v2 = c交换机 + c盒式 + c版本五 + 3102
	s3100v3 = c交换机 + c盒式 + c版本七 + 3103
	s3600 = c交换机 + c盒式 + c版本三 + 3600
	s3600v2 = c交换机 + c盒式 + c版本五 + 3602
	s3928p = c交换机 + c盒式 + c版本三 + 3928
	s5100 = c交换机 + c盒式 + 5100
	s5110 = c交换机 + c盒式 + c版本五 + 5100
	s5130 = c交换机 + c盒式 + c版本七 + 5130
	s5500 = c交换机 + c盒式 + c版本五 + 5500
	s5560x = c交换机 + c盒式 + c版本七 + 5560
	s5600 = c交换机 + c盒式 + c版本三 + 5500
	s5820v2 = c交换机 + c盒式 + c版本七 + 5822
	s6500 = c交换机 + c框式 + 6500
	s6503 = c交换机 + c框式 + c版本三 + 6503
	s6520x = c交换机 + c盒式 + c版本七 + 6520
	s6900 = c交换机 + c盒式 + c版本七 + 6900
	s7500 = c交换机 + c框式 + 7500
	s7503 = c交换机 + c框式 + 7503
	s7503e = c交换机 + c框式 + c版本五 + 7503
	s7506e = c交换机 + c框式 + c版本五 + 7506
	s7506r = c交换机 + c框式 + c版本三 + 7506
	s9800 = c交换机 + c框式 + c版本七 + 9800
	s9810 = c交换机 + c框式 + c版本七 + 9810
	s9820 = c交换机 + c框式 + c版本七 + 9820
	s9850 = c交换机 + c框式 + c版本七 + 9850
	msr3600 = c路由器 + c框式 + c版本七 + 3600
	msr3620 = c路由器 + c框式 + c版本七 + 3620
	msr3640 = c路由器 + c框式 + c版本七 + 3640
	sr8800 = c路由器 + c框式 + c版本五 + 8800
	sr8808 = c路由器 + c框式 + c版本七 + 8808
def f创建设备(a连接, a型号 = 0, a版本 = 0):
	#解析版本
	if not a版本:
		if a型号 & E型号.c版本七:
			v版本 = 工具.S版本号.fc自动(7)
		elif a型号 & E型号.c版本九:
			v版本 = 工具.S版本号.fc自动(9)
		else:
			v版本 = 工具.S版本号.fc自动(5)
	else:
		from .华三命令行 import 版本
		if type(a版本) == str:
			v版本 = 版本.f解析版本字符串(a版本)
		else:
			v版本 = 工具.S版本号.fc自动(a版本)
	#创建设备
	if 连接层.fi命令行(a连接):	#命令行
		v主版本 = v版本[0]
		if v主版本 <= 5:
			from .华三命令行 import 设备 as 设备
			return 设备.C设备(a连接, a型号, v版本)
		elif v主版本 <= 7:
			from .华三版本七命令行 import 设备 as 设备
			v发行号 = v版本[3]
			if a型号 in (E型号.msr3620, E型号.s5820v2):
				vt设备 = 设备.C设备_ev7
			elif a型号 in (E型号.s9810,):
				vt设备 = 设备.C设备_s9v7
			elif a型号 == E型号.s5560x:	#S5560X-54C-EI, S5560X-30F-EI
				if v发行号 < 6526:	#Version 7.1.070, Release 1119P20
					vt设备 = 设备.C设备_sv7_2019
				else:	#Version 7.1.070, Release 6526
					vt设备 = 设备.C设备_s5v7
			else:
				vt设备 = 设备.C设备_v7
			return vt设备(a连接, a型号, v版本)
		elif v主版本 <= 9:
			raise ValueError("不支持的版本")
		else:
			raise ValueError("不支持的版本")
	raise ValueError("不支持的连接,型号,版本")