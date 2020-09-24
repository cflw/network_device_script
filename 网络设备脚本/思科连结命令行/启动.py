import time
from ..基础接口 import 启动模式
from ..命令行接口 import 模式
c启动字符 = '\x03'	#ctrl+c
class C启动(启动模式.I启动模式, 模式.I模式):
	"""nexus系列的启动模式
	适用于: 什么都不适用"""
	def __init__(self, a):
		模式.I模式.__init__(self, a)
		self.m配置 = None
	def f登录(self, a密码 = "", a超时 = 60, a镜像 = "nxos.7.0.3.I5.2.bin"):
		v秒表 = 时间.C秒表()
		while True:
			self.m设备.f输入(c启动字符)
			time.sleep(1)
			v输出 = self.m设备.f输出(a等待 = False)
			#继续判断
			if "loader >" in v输出:
				time.sleep(1)
				break
			#超时判断
			if v秒表.f滴答() >= a超时:
				raise TimeoutError()
		self.m设备.f执行命令("cmdline recoverymode=1")
		self.m设备.f执行命令(f"boot {a镜像}")
		time.sleep(1)
	def f模式_配置(self):
		if not self.m配置:
			self.m配置 = C配置(self)
		return self.m配置
	def f更新系统(self, a文件):
		raise NotImplementedError()
	def f重置密码(self, a密码):
		v配置模式 = self.f模式_配置()
		v配置模式.f重置密码(a密码)
	def f清除配置(self):
		self.f执行当前模式命令("write erase")
	def f重新启动(self):
		self.f执行当前模式命令("load-nxos")
class C配置(模式.I模式):
	def __init__(self, a):
		模式.I模式.__init__(self, a)
	def fg进入命令(self):
		return "configure terminal"
	def fg退出命令(self):
		return "exit"
	def f重置密码(self, a密码):
		self.f执行当前模式命令(f"admin-password {a密码}")