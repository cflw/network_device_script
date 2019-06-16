import enum
class E地址族(enum.IntEnum):
	e单播4 = 0
	e虚拟路由4 = 1	#vrf
	e虚专网4 = 2	#vpn
	e单播6 = 10
	e虚拟路由6 = 11
	e虚专网6 = 12
class I进程配置:
	c模式名 = "边界网关协议进程配置模式"
	#模式
	def f模式_对等体(self, a对等体, a操作):
		raise NotImplementedError()
	def f模式_对等体组(self, a名称, a操作):
		raise NotImplementedError()
	def f模式_地址族(self, *a地址族, a操作):
		raise NotImplementedError()
	#显示
	def f显示_路由表(self):
		raise NotImplementedError()
	def f显示_邻居表(self):
		raise NotImplementedError()
	#操作
	def fs路由器号(self, a):
		raise NotImplementedError()
class I地址族配置:
	c模式名 = "边界网关协议地址族配置模式"
	def f模式_对等体(self, a名称):
		raise NotImplementedError()
	def f模式_对等体组(self, a名称, a操作):
		raise NotImplementedError()
	def f显示_路由表(self):
		raise NotImplementedError()
	def fs通告网络(self, a网络号, a操作):
		raise NotImplementedError()
	def fs通告接口(self, a接口, a操作):
		raise NotImplementedError()
class I对等体配置:
	c模式名 = "边界网关协议对等体(组)配置模式"
	#操作
	def fs激活(self, a操作):
		raise NotImplementedError()
	def fs远端自治系统号(self, a自治系统号, a操作):
		raise NotImplementedError()
	def fs本端自治系统号(self, a自治系统号, a操作):
		raise NotImplementedError()
	def fs更新源地址(self, a源, a操作):
		raise NotImplementedError()
	def fs对等体组(self, a对等体组, a操作):
		raise NotImplementedError()
