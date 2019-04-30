class I路由策略组(I模式):
	def __init__(self, a, a名称):
		I模式.__init__(self, a)
		self.m名称 = a名称
	def f模式_策略(self, a动作, a策略号):
		raise NotImplementedError()
class I路由策略节点(I模式):
	def __init__(self, a, a节点号):
		I模式.__init__(self, a)
		self.m节点号 = a节点号
	#匹配
	def f匹配_访问列表(self, a访问列表, a操作 = E操作.e添加):
		raise NotImplementedError()
	def f匹配_前缀列表(self, a前缀列表, a操作 = E操作.e添加):
		raise NotImplementedError()
	#应用
	def f应用_下一跳4(self, a地址, a操作 = E操作.e添加):
		raise NotImplementedError()
	def f应用_默认下一跳4(self, a地址, a操作 = E操作.e添加):
		raise NotImplementedError()
	def f应用_出接口(self, a接口, a操作 = E操作.e添加):
		raise NotImplementedError()
	def f应用_默认出接口(self, a接口, a操作 = E操作.e添加):
		raise NotImplementedError()
	#应用 路由
	def f应用_度量值(self, a值, a操作 = E操作.e设置):
		raise NotImplementedError()
	def f应用_区域类型(self, a区域类型, a操作 = E操作.e设置):
		"用于: ospf, isis"
		raise NotImplementedError()
	def f应用_路由类型(self, a路由类型, a操作 = E操作.e设置):
		"用于: ospf, eigrp, isis"
		raise NotImplementedError()
