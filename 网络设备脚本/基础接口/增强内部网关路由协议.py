class I增强内部网关路由协议(I模式):
	def __init__(self, a, a自制系统号):
		I模式.__init__(self, a)
		self.m自制系统号 = a自制系统号
	#显示
	def f显示_路由表(self):
		raise NotImplementedError()
	def f显示_邻居表(self):
		raise NotImplementedError()
	#操作
	def fs开关(self, a操作 = E操作.e设置):
		raise NotImplementedError()
	def fs路由器号(self, a路由器号):
		raise NotImplementedError()
	def fs通告网络(self, a网络号, a操作 = E操作.e设置):
		raise NotImplementedError()
	def fs通告接口(self, a接口, a操作 = E操作.e设置):
		raise NotImplementedError()
	def fs自动汇总(self, a操作 = E操作.e设置):
		raise NotImplementedError()
	#度量值
	def fs带宽(self, a带宽, a操作 = E操作.e设置):
		raise NotImplementedError()
	def fs延迟(self, a延迟, a操作 = E操作.e设置):
		raise NotImplementedError()
class I增强内部网关路由协议接口(I接口配置基础):
	def __init__(self, a, a接口, a自制系统号):
		I接口配置基础.__init__(self, a, a接口)
		self.m自制系统号 = a自制系统号
	def fs通告接口(self, a操作 = E操作.e设置):
		raise NotImplementedError()
	def fs被动(self, a操作 = E操作.e设置):
		raise NotImplementedError()
	def fs水平分割(self, a操作 = E操作.e设置):
		raise NotImplementedError()
	def fs汇总(self, a网络号, a操作 = E操作.e设置):
		raise NotImplementedError()
