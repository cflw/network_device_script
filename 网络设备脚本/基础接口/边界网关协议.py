class E边界网关协议地址族(enum.IntEnum):
	e单播4 = 0
	e虚拟路由4 = 1	#vrf
	e虚专网4 = 2	#vpn
	e单播6 = 10
	e虚拟路由6 = 11
	e虚专网6 = 12
class I边界网关协议(I模式):
	c模式名 = "边界网关协议配置模式"
	def __init__(self, a, a自治系统号):
		I模式.__init__(self, a)
		self.m自治系统号 = int(a自治系统号)
	#命令
	def fg模式参数(self):
		"返回自治系统号"
		return (self.m自治系统号,)
	#模式
	def f模式_对等体(self, a对等体, a操作 = E操作.e设置):
		raise NotImplementedError()
	def f模式_地址族(self, *a地址族, a操作 = E操作.e设置):
		raise NotImplementedError()
	#显示
	def f显示_路由表(self):
		raise NotImplementedError()
	def f显示_邻居(self):
		raise NotImplementedError()
	#操作
	def fs路由器号(self, a):
		raise NotImplementedError()
class I边界网关协议地址族(I模式):
	c模式名 = "边界网关协议地址族配置模式"
	def __init__(self, a, a参数):
		I模式.__init__(self, a)
		self.m参数 = a参数
	def f模式_对等体(self, a名称):
		raise NotImplementedError()
	def f显示_路由表(self):
		raise NotImplementedError()
	def fs通告网络(self, a网络号, a操作 = E操作.e设置):
		raise NotImplementedError()
	def fs通告接口(self, a接口, a操作 = E操作.e设置):
		raise NotImplementedError()
class I边界网关协议对等体(I模式):
	c模式名 = "边界网关协议对等体配置模式"
	def __init__(self, a, a对等体):
		I模式.__init__(self, a)
		self.m对等体 = a对等体
	def __str__(self):
		return str(self.m对等体)
	#操作
	def fs激活(self, a操作 = E操作.e设置):
		raise NotImplementedError()
	def fs远端自治系统号(self, a):
		raise NotImplementedError()
	def fs本端自治系统号(self, a):
		raise NotImplementedError()
	def fs更新源地址(self, a):
		raise NotImplementedError()
