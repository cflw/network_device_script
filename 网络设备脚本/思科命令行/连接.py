from ..基础接口 import 异常
from ..命令行接口 import 命令
from ..命令行接口 import 连接
class C网络终端(连接.I命令行连接):
	def __init__(self, a模式, a地址, **a参数):
		连接.I命令行连接.__init__(self, a模式)
		self.m地址 = a地址
	def fg进入命令(self):
		v命令 = 命令.C命令("telnet")
		v命令 += self.m地址
		return v命令
	def f连接(self):
		v命令 = self.fg进入命令()
		v输出 = self.m模式.f执行当前模式命令(v命令)
		# % Destination unreachable; gateway or host down
		if "Destination unreachable" in v输出:
			raise 异常.X连接()
class C安全外壳(连接.I命令行连接):
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
		self.m虚拟专用网 = a参数.get("a虚拟专用网")
		self.m版本 = a参数.get("a版本")
	def fg进入命令(self):
		"""命令: ssh [参数] 地址"""
		v命令 = 命令.C命令("ssh")
		v命令 += "-l", self.m用户名
		v命令 |= "-p", self.m端口号
		v命令 |= "-v", self.m版本
		v命令 |= "-vrf", self.m虚拟专用网
		v命令 += self.m地址
		return v命令
	def f连接(self):
		v命令 = self.fg进入命令()
		v输出 = self.m模式.f执行当前模式命令(v命令)
		#Password: 
		if "Password:" in v输出:
			v输出 = self.m设备.f执行命令(self.m密码)
		