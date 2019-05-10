import enum
class E链路类型(enum.IntEnum):
	e接入 = 0
	e中继 = 1
	e混合 = 2
class I虚拟局域网配置:
	#模式
	def f模式_接口(self, a接口, a操作):
		raise NotImplementedError()
	#动作
	def fs描述(self, a描述, a操作):
		raise NotImplementedError()
	def fs端口(self, a接口, a操作):
		raise NotImplementedError()
class I接口配置:
	def fs链路类型(self, a类型, a操作):
		raise NotImplementedError()
	def fg链路类型(self):
		raise NotImplementedError()
	#中继(trunk)
	def f中继_s通过(self, a虚拟局域网, a操作):
		raise NotImplementedError()
	def f中继_s封装协议(self, a协议, a操作):
		raise NotImplementedError()
	def f中继_s本征(self, a虚拟局域网, a操作):
		raise NotImplementedError()
	#接入(access)
	def f接入_s绑定(self, a虚拟局域网, a操作):
		raise NotImplementedError()
	#混合(hybrid)
	def f混合_s无标记(self, a虚拟局域网, a操作):
		raise NotImplementedError()
	def f混合_s有标记(self, a虚拟局域网, a操作):
		raise NotImplementedError()
