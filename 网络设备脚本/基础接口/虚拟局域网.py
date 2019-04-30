class E链路类型(enum.IntEnum):
	e接入 = 0
	e中继 = 1
	e混合 = 2
class I虚拟局域网(I模式):
	def __init__(self, a, a编号):
		I模式.__init__(self, a)
		self.m编号 = a编号
	#命令
	def fg模式参数(self):
		return (self.m编号,)
	def fg进入命令(self):
		return C命令("vlan") + self.fg模式参数()
	#模式
	def f模式_接口(self, a接口, a操作 = E操作.e设置):
		raise NotImplementedError()
	#动作
	def fs描述(self, a描述, a操作 = E操作.e设置):
		raise NotImplementedError()
	def fs端口(self, a接口, a操作 = E操作.e添加):
		raise NotImplementedError()
class I虚拟局域网接口(I接口配置模式基础):
	def __init__(self, a, a接口):
		I接口配置模式基础.__init__(self, a, a接口)
	def fs链路类型(self, a类型):
		raise NotImplementedError()
	#中继(trunk)
	def f中继_s通过(self, a虚拟局域网, a操作 = E操作.e设置):
		raise NotImplementedError()
	def f中继_s封装协议(self, a协议):
		raise NotImplementedError()
	def f中继_s本征(self, a虚拟局域网):
		raise NotImplementedError()
	#接入(access)
	def f接入_s绑定(self, a虚拟局域网, a操作 = E操作.e设置):
		raise NotImplementedError()
	#混合(hybrid)
	def f混合_s无标记(self, a虚拟局域网, a操作 = E操作.e添加):
		raise NotImplementedError()
	def f混合_s有标记(self, a虚拟局域网, a操作 = E操作.e添加):
		raise NotImplementedError()
