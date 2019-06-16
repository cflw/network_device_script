import cflw代码库py.cflw网络地址 as 地址
from ..命令行接口 import 命令
from ..基础接口 import 连接
def f生成源地址4(a地址):
	if not a地址:
		return
	v地址 = 地址.S网络地址4.fc自动(a地址)
	return f"-a {v地址.fg地址s()}"
def f生成源接口4(a接口):
	if not a接口:
		return
	raise NotImplementedError()
def f生成虚专网实例(a实例):
	if not a实例:
		return
	return str(a实例)
class C网络终端(连接.I命令行连接):
	def __init__(self, a模式, a地址, **a参数):
		连接.I命令行连接.__init__(self, a模式)
		v命令 = 命令.C命令("telnet")
		v命令 += a地址
		v命令 += a参数.get("a端口号")
		a模式.f执行当前模式命令(v命令)
class C安全外壳(连接.I命令行连接):
	def __init__(self, a模式, a地址, **a参数):
		连接.I命令行连接.__init__(self, a模式)
		v命令 = 命令.C命令("ssh")
		v命令 += a地址
		a模式.m设备.f执行用户命令(v命令)
