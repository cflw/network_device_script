import enum
#===============================================================================
# 工厂
#===============================================================================
class E型号(enum.IntEnum):
	s3956 = 3956
def f创建设备(a连接, a型号, a版本 = 0):
	from .博达命令行 import 设备
	return 设备.C设备(a连接, a型号, a版本)
