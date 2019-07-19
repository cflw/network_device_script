import enum
class E模式(enum.IntEnum):
	e生成树 = 0	#stp
	e每虚拟局域网生成树 = 1	#pvst
	e快速生成树 = 2	#rstp
	e每虚拟局域网快速生成树 = 3	#rpvst
	e多生成树 = 4	#mstp
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
class E优先级(enum.IntEnum):
	e主 = 0
	e次 = 1
c桥优先级倍数 = 4096
c端口优先级倍数 = 16
def f计算桥优先级(a优先级: int):
	return a优先级 * c桥优先级倍数
def f反算桥优先级(a优先级: int):
	return a优先级 // c桥优先级倍数
def f计算端口优先级(a优先级: int):
	return a优先级 * c端口优先级倍数
def f反算端口优先级(a优先级: int):
	return a优先级 // c端口优先级倍数
class I多生成树配置:
	c模式名 = "多生成树配置模式"
	def fs开关(self, a操作):
		raise NotImplementedError()
	def fs实例映射(self, a实例, a虚拟局域网, a操作):
		raise NotImplementedError()
	def fs实例优先级(self, a实例, a优先级, a操作):
		raise NotImplementedError()
	def fs域名(self, a名称, a操作):
		raise NotImplementedError()
	def fs版本(self, a版本, a操作):
		raise NotImplementedError()
class I接口配置:
	c模式名 = "生成树接口配置模式"
	def fs开关(self, a操作):
		raise NotImplementedError()
	def fs根保护(self, a开关, a操作):
		raise NotImplementedError()
	def fs环路保护(self, a开关, a操作):
		raise NotImplementedError()
	def fs开销(self, a树, a开销, a操作):
		raise NotImplementedError()
	def fs优先级(self, a树, a优先级, a操作):
		raise NotImplementedError()