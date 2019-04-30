import enum
class E登录方式(enum.IntEnum):
	e控制台 = 0	#console
	e辅助接口 = 1	#aux
	e虚拟终端 = 3	#vty
class E登录认证方式(enum.IntEnum):
	e无 = 0,
	e密码 = 1,
	e账号 = 2
	e认证授权记账 = 3
	aaa = 3
class E登录协议(enum.IntEnum):
	e无 = 0
	e远程登录 = 0x0001
	e安全外壳 = 0x0002
	e全部 = 0xffffffff
class I登录配置模式(I模式):
	def __init__(self, a):
		I模式.__init__(self, a)
	def fs认证方式(self, a认证方式, a操作 = E操作.e设置):
		raise NotImplementedError()
	def fs登录协议(self, a登录协议, a操作 = E操作.e设置):
		raise NotImplementedError()
	def fs访问控制列表(self, a访问列表, a操作 = E操作.e设置):
		raise NotImplementedError()
	def fs登录超时(self, a秒, a操作 = E操作.e设置):
		"登录中在规定时间内输完用户名密码"
		raise NotImplementedError()
	def fs操作超时(self, a秒, a操作 = E操作.e设置):
		"登录后在规定时间内没有任何操作则断开连接"
		raise NotImplementedError()
	def fg认证方式(self):
		raise NotImplementedError()
	def fg登录协议(self):
		raise NotImplementedError()
	def fg访问控制列表(self):
		"返回名称"
		raise NotImplementedError()
	def fg登录超时(self):
		raise NotImplementedError()
	def fg操作超时(self):
		raise NotImplementedError()
