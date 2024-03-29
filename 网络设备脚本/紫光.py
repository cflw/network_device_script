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
	c版本七 = 0x00040000	#uniware v7
	c版本九 = 0x00080000	#uniware v9
	s5200 = c交换机 + c盒式 + c版本七 + 5200
	s5200s = c交换机 + c盒式 + c版本七 + 5201
	s5600 = c交换机 + c盒式 + c版本七 + 5600
	s5600x = c交换机 + c盒式 + c版本七 + 5601
	s6600x = c交换机 + c盒式 + c版本七 + 6601
	s7800xp = c交换机 + c盒式 + c版本七 + 7801
	s8600x = c交换机 + c盒式 + c版本七 + 8601
def f创建设备(a连接, a型号 = 0, a版本 = 0):
	#解析版本
	if not a版本:
		if a型号 & E型号.c版本七:
			v版本 = 工具.S版本号.fc自动(7)
		elif a型号 & E型号.c版本九:
			v版本 = 工具.S版本号.fc自动(9)
		else:
			v版本 = 工具.S版本号.fc自动(7)
	else:
		from .华三命令行 import 版本
		if type(a版本) == str:
			v版本 = 版本.f解析版本字符串(a版本)
		else:
			v版本 = 工具.S版本号.fc自动(a版本)
	#创建设备
	if 连接层.fi命令行(a连接):	#命令行
		v主版本 = v版本[0]
		if v主版本 <= 7:
			from .华三版本七命令行 import 设备 as 设备
			v发行号 = v版本[3]
			if a型号 in (E型号.s5200, E型号.s5200s):
				vt设备 = 设备.C设备_us5v7
			elif a型号 == E型号.s5600:	#S5600-54C-EI-G
				if v发行号 < 7748:	#Version 7.1.070, Release 7734P05
					vt设备 = 设备.C设备_sv7_2019
				else:	#Version 7.1.070, Release 7748P01
					vt设备 = 设备.C设备_s7v7
			elif a型号 in (E型号.s7800xp, E型号.s8600x):
				vt设备 = 设备.C设备_s7v7
			else:
				vt设备 = 设备.C设备_v7
			return vt设备(a连接, a型号, v版本)
		else:
			raise ValueError("不支持的版本")
	raise ValueError("不支持的连接,型号,版本")