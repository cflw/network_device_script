import enum
class E端口角色(enum.IntEnum):
	e根 = 0		#stp
	e指定 = 1	#stp
	e非指定 = 2	#stp
	e替代 = 3	#mstp
	e备份 = 4	#mstp
	e主 = 5		#mstp
	e边缘 = 6	#mstp
class E端口状态(enum.IntEnum):
	e禁用 = 0	#stp
	e阻塞 = 1	#stp
	e监听 = 2	#stp
	e学习 = 3	#stp
	e转发 = 4	#stp
	e丢弃 = 5	#rstp
class I多生成树配置:
	def fs开关(self, a操作):
		raise NotImplementedError()
	def fs实例映射(self, a实例, a虚拟局域网):
		raise NotImplementedError()
	def fs实例优先级(self, a实例, a优先级):
		raise NotImplementedError()
	def fs实例开销(self, a接口, a实例, a开销):
		raise NotImplementedError()
	def fs域名(self, a名称):
		raise NotImplementedError()
	def fs版本(self, a版本):
		raise NotImplementedError()
class I生成树接口配置:
	def fs根保护(self, a):
		raise NotImplementedError()
	def fs环路保护(self, a):
		raise NotImplementedError()
	def fs开销(self, a树, a开销):
		raise NotImplementedError()
