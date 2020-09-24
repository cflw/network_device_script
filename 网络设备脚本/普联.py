import enum
from .基础接口 import 连接层
class E型号(enum.IntEnum):
	wdr5620 = 5620
def f创建设备(a连接, a型号, a版本 = 0):
	if 连接层.fi网页(a连接):
		from .普联网页 import 设备
		return 设备.C设备(a连接, a型号, a版本)
	raise ValueError("不支持的连接,型号")