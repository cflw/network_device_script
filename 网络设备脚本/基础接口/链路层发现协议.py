import enum
class E邻居信息(enum.IntEnum):
	"用于：链路层发现协议"
	e邻居名称 = 1
	e邻居描述 = 2
	e更新时间 = 3
	e本端接口 = 10
	e本端接口描述 = 11
	e对端接口 = 20
	e对端接口描述 = 21
	e管理地址类型 = 30
	e管理地址 = 31
class I进程配置:
	def f模式_接口(self, a接口):
		raise NotImplementedError()
	def f显示_邻居表(self):
		raise NotImplementedError()
	def fs开关(self, a操作):
		raise NotImplementedError()
class I接口配置:
	def fs开关(self, a操作):
		raise NotImplementedError()