class I网络时间协议服务器(I模式):
	def __init__(self, a):
		I模式.__init__(self, a)
	def fs开关(self, a操作 = E操作.e设置):
		raise NotImplementedError()
	def fs版本(self, a版本):
		raise NotImplementedError()
	def fs源地址(self, a地址):
		raise NotImplementedError()
	def fs广播更新(self, a):
		raise NotImplementedError()
class I网络时间协议客户端(I模式):
	def __init__(self, a):
		I模式.__init__(self, a)
	def fs服务器地址(self, a地址, a操作 = E操作.e添加):
		raise NotImplementedError()
	def f显示_同步信息(self):
		raise NotImplementedError()
