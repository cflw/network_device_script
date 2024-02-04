import enum
import cflw代码库py.cflw工具 as 工具
from .基础接口 import 连接层
class E型号(enum.IntEnum):
	c防火墙 = 0x10000000
	sg6000p1412 = c防火墙 + 6412	#灰色界面
	sg6000a5100 = c防火墙 + 5100	#蓝色界面
def f创建设备(a连接, a型号, a版本 = 0):
	v版本 = 工具.S版本号.fc自动(a版本)
	if 连接层.fi网页(a连接):	#网页
		if a型号 & E型号.c防火墙:
			from .山石防火墙网页 import 设备
			if a型号 == E型号.sg6000p1412:
				t设备 = 设备.C设备_p
			elif a型号 == E型号.sg6000a5100:
				t设备 = 设备.C设备_a
			else:
				raise ValueError("不支持的型号")
			return t设备(a连接, a型号, v版本)
	raise ValueError("不支持的连接,型号,版本")