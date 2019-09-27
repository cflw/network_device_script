class I设备:
	def __init__(self):
		self.m回显 = False
		self.m等待回显 = False
		self.m检测异常 = False
	def fs回显(self, a回显 = True, a等待回显 = True):
		self.m回显 = a回显
		self.m等待回显 = a等待回显
	def fs检测异常(self, a异常 = True):
		self.m检测异常 = a异常
	def f模式_用户(self):	#要求：ma模式[0]总是用户模式，没有则创建。不能创建多个用户模式对象。
		"用户模式只能查看信息,做一些基本操作,不能配置"
		raise NotImplementedError()
	def f模式_启动(self):
		"在交换机开机阶段执行操作的模式,需要串口连接"
		raise NotImplementedError()
	def f模式_配置(self):
		"直接进入配置模式, 用于不需要用户名密码登录, 没有状态的连接方式"
		raise NotImplementedError()
	def f模式_显示(self):
		"直接进入显示模式"
		raise NotImplementedError()
	def f助手_访问控制列表(self):
		raise NotImplementedError()
	def f助手_密码(self):
		raise NotImplementedError()
