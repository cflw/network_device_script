from ..命令行接口 import 命令
from ..基础接口 import 连接
class C安全外壳(连接.I命令行连接):
	"""适用于: msr3620(v7.1)"""
	def __init__(self, a模式, a地址, **a参数):
		连接.I命令行连接.__init__(self, a模式)
		self.m地址 = a地址
		self.m用户名 = a参数.get("a用户名")
		if not self.m用户名:
			raise ValueError("必需指定 a用户名")
		self.m密码 = a参数.get("a密码")
		if not self.m密码:
			raise ValueError("必需指定 a密码")
		self.m端口号 = a参数.get("a端口号")
		self.m源地址 = a参数.get("a源地址")
		self.m虚拟专用网 = a参数.get("a虚拟专用网")
	def fg进入命令(self):
		v命令 = 命令.C命令("ssh")
		v命令 += self.m地址
		v命令 |= self.m端口号
		v命令 |= "source", self.m源地址
		v命令 |= "vpn-instance", self.m虚拟专用网
		return v命令
	def f连接(self):
		v命令 = self.fg进入命令()
		v输出 = self.m模式.f执行当前模式命令(v命令)
		# Username: asdf
		if "Username:" in v输出:
			self.m设备.f执行命令(self.m用户名)
		# Press CTRL+C to abort.
		# Connecting to 12.0.0.2 port 22.
		# The server is not authenticated. Continue? [Y/N]:y
		if "[Y/N]" in v输出:
			self.m设备.f执行命令("y")
		# Do you want to save the server public key? [Y/N]:n
		if "[Y/N]" in v输出:
			self.m设备.f执行命令("n")
		# asdf@12.0.0.2's password: 
		if "password:" in v输出:
			self.m设备.f执行命令(self.m密码)
