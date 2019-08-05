import enum
class E服务类型(enum.IntEnum):
	e无 = 0x00
	e终端 = 0x01
	e网络终端 = 0x02
	e安全外壳 = 0x04
	e网页 = 0x08
	e全部 = 0xff
class E用户权限(enum.IntEnum):
	e最低 = 0
	e最高 = 1
class I用户配置:
	c模式名 = "用户配置模式"
	def fs密码(self, a密码, a操作):
		raise NotImplementedError()
	def fs权限(self, a权限, a操作):
		raise NotImplementedError()
	def fs服务类型(self, a服务类型, a操作):
		raise NotImplementedError()
