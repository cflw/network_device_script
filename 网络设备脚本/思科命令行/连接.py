from ..命令行接口 import 命令
from ..基础接口 import 连接
class C网络终端(连接.I命令行连接):
	def __init__(self, a模式, a地址, **a参数):
		连接.I命令行连接.__init__(self, a模式)
		v命令 = 命令.C命令("telnet")
		v命令 += a地址
		a模式.m设备.f执行用户命令(v命令)