class E服务类型(enum.IntEnum):
	e无 = 0x00
	e控制台 = 0x01
	e远程连接 = 0x02
	e安全外壳 = 0x04
	e全部 = 0xff
class I用户配置模式(I模式):
	c模式名 = "用户配置模式"
	def __init__(self, a设备, a用户名):
		I模式.__init__(self, a设备)
		self.m用户名 = str(a用户名)
	def fs密码(self, a密码):
		raise NotImplementedError()
	def fs权限(self, a权限):
		raise NotImplementedError()
	def fs服务类型(self, a服务类型):
		raise NotImplementedError()
