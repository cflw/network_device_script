import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 连接
from ..基础接口 import 异常
from ..命令行接口 import 命令
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
		self.m地址 = a地址
		self.m端口号 = a参数.get("a端口号")
	def fg进入命令(self):
		v命令 = 命令.C命令("telnet")
		v命令 += self.m地址
		v命令 |= self.m端口号
		return v命令
	def f连接(self):
		v命令 = self.fg进入命令()
		self.m模式.f执行当前模式命令(v命令)
class C安全外壳(连接.I命令行连接):
	"""适用于: ne40e(v8.180)"""
	def __init__(self, a模式, a地址, **a参数):
		连接.I命令行连接.__init__(self, a模式)
		self.m地址 = a地址
		self.m用户名 = a参数.get("a用户名")
		if not self.m用户名:
			raise ValueError("必需指定 a用户名")
		self.m密码 = a参数.get("a密码")
		if not self.m密码:
			raise ValueError("必需指定 a密码")
		self.m源接口 = a参数.get("a源接口")
		self.m源地址 = a参数.get("a源地址")
		self.m端口号 = a参数.get("a端口号")
	def fg进入命令(self):
		v命令 = 命令.C命令("stelnet")
		v命令 |= "-a", self.m源地址
		v命令 |= "-i", self.m源接口
		v命令 += "-force-receive-pubkey"
		v命令 += self.m地址
		v命令 |= self.m端口号
		return v命令
	def f连接(self):
		v命令 = self.fg进入命令()
		v输出 = self.m模式.f执行当前模式命令(v命令)
		# Trying 1.1.1.1 ...
		# Press CTRL + K to abort
		# Connected to 1.1.1.1 ...
		# The server is not authenticated. Continue to access it? [Y/N]: y
		if "The server is not authenticated. Continue to access it? [Y/N]:" in v输出:
			v输出 = self.m设备.f执行命令("y")
		# Save the server's public key? [Y/N]: n
		if "Save the server's public key? [Y/N]:" in v输出:
			v输出 = self.m设备.f执行命令("n")
		# Please input the username: asdf
		if "Please input the username:" in v输出:
			v输出 = self.m设备.f执行命令(self.m用户名)
		# Enter password: 
		if "Enter password:" in v输出:
			v输出 = self.m设备.f执行命令(self.m密码)
		# The IP has been blocked and you cannot log on it.
		# Info: The connection was closed by the remote host.
		if "The connection was closed" in v输出:
			raise 异常.X连接()