class I动态主机配置协议地址池(I模式):
	def __init__(self, a, a名称):
		I模式.__init__(self, a)
		self.m名称 = a名称
	def fs网络范围(self, a网络号, a掩码):
		raise NotImplementedError()
	def fs默认网关(self, a网关):
		raise NotImplementedError()
	def fs租期(self, a时间):
		raise NotImplementedError()
	def fs域名服务器(self, a地址):
		raise NotImplementedError()
class I动态主机配置协议(I模式):
	def __init__(self, a):
		I模式.__init__(self, a)
	def f显示_已分配地址(self):
		raise NotImplementedError()
	def f模式_地址池(self, a名称):
		raise NotImplementedError()
	def fs开关(self, a操作 = E操作.e设置):
		raise NotImplementedError()
